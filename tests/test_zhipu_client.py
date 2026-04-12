import os
import unittest
from unittest.mock import patch

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


if __name__ == "__main__":
    unittest.main()
