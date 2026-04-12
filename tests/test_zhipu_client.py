import os
import unittest
from unittest.mock import MagicMock, patch

from utils import zhipu_client


class ZhipuClientTestCase(unittest.TestCase):
    def test_post_json_converts_timeout_to_runtime_error(self):
        with (
            patch.dict(
                os.environ,
                {
                    "ZHIPU_API_KEY": "test-key",
                    "ZHIPU_API_BASE": "https://example.com",
                },
                clear=False,
            ),
            patch("urllib.request.urlopen", side_effect=TimeoutError("read timed out")),
        ):
            with self.assertRaises(RuntimeError) as context:
                zhipu_client._post_json("chat/completions", {"model": "glm"})

        self.assertIn("超时", str(context.exception))

    def test_generate_answer_includes_configured_max_tokens(self):
        fake_response = {"choices": [{"message": {"content": "ok"}}]}
        with (
            patch.dict(
                os.environ,
                {
                    "ZHIPU_API_KEY": "test-key",
                    "ZHIPU_API_BASE": "https://example.com",
                    "ZHIPU_CHAT_MAX_TOKENS": "256",
                },
                clear=False,
            ),
            patch.object(zhipu_client, "_post_json", return_value=fake_response) as mock_post,
        ):
            answer = zhipu_client.generate_answer("sys", "user")

        self.assertEqual(answer, "ok")
        _, payload = mock_post.call_args.args
        self.assertEqual(payload.get("max_tokens"), 256)
        self.assertEqual(mock_post.call_args.kwargs.get("retries"), 1)

    def test_post_json_retries_once_on_timeout(self):
        response_obj = MagicMock()
        response_obj.read.return_value = b'{"ok": true}'
        context_manager = MagicMock()
        context_manager.__enter__.return_value = response_obj
        context_manager.__exit__.return_value = False

        with (
            patch.dict(
                os.environ,
                {
                    "ZHIPU_API_KEY": "test-key",
                    "ZHIPU_API_BASE": "https://example.com",
                },
                clear=False,
            ),
            patch(
                "urllib.request.urlopen",
                side_effect=[TimeoutError("read timed out"), context_manager],
            ) as mock_urlopen,
        ):
            data = zhipu_client._post_json("chat/completions", {"model": "glm"}, retries=1)

        self.assertEqual(data.get("ok"), True)
        self.assertEqual(mock_urlopen.call_count, 2)


if __name__ == "__main__":
    unittest.main()
