import unittest
from unittest.mock import patch

import app as app_module


class AssistantRagTestCase(unittest.TestCase):
    def test_answer_assistant_question_prefers_rag(self):
        rag_sources = [{"source": "常见问题 · 推荐信", "link": "/faq/1"}]
        with patch.object(
            app_module,
            "ask_assistant_with_rag",
            return_value=("这是 RAG 回答", rag_sources),
        ):
            answer, sources = app_module.answer_assistant_question("推荐信要提前多久联系老师？")

        self.assertEqual(answer, "这是 RAG 回答")
        self.assertEqual(sources, rag_sources)

    def test_answer_assistant_question_falls_back_when_rag_fails(self):
        with (
            patch.object(
                app_module,
                "ask_assistant_with_rag",
                side_effect=RuntimeError("RAG 暂不可用"),
            ),
            patch.object(
                app_module,
                "ask_assistant_local",
                return_value=("这是本地回退回答", []),
            ),
        ):
            answer, sources = app_module.answer_assistant_question("语言成绩最晚何时提交？")

        self.assertEqual(answer, "这是本地回退回答")
        self.assertEqual(sources, [])


if __name__ == "__main__":
    unittest.main()
