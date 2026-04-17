import unittest
from unittest.mock import patch

from utils import rag_pipeline


class RagPipelineTestCase(unittest.TestCase):
    def test_split_text_with_overlap(self):
        chunks = rag_pipeline.split_text("abcdefghij", chunk_size=4, overlap=1)
        self.assertEqual(chunks, ["abcd", "defg", "ghij"])

    def test_build_rag_records_generates_stable_uid(self):
        fake_chunks = [
            {
                "source_type": "faq",
                "source": "常见问题 · Q1",
                "link": "/faq/1",
                "content": "这是一段用于测试的文本内容。",
            }
        ]
        with patch.object(rag_pipeline, "build_knowledge_chunks", return_value=fake_chunks):
            rows1 = rag_pipeline.build_rag_records(chunk_size=8, overlap=2)
            rows2 = rag_pipeline.build_rag_records(chunk_size=8, overlap=2)

        self.assertGreaterEqual(len(rows1), 1)
        self.assertEqual([item["chunk_uid"] for item in rows1], [item["chunk_uid"] for item in rows2])
        self.assertEqual(rows1[0]["source_type"], "faq")

    def test_ask_with_rag_filters_legacy_faq_citations(self):
        fake_matches = [
            {
                "source_type": "faq",
                "source": "常见问题 · 旧问题",
                "link": "/faq/1",
                "content": "旧 FAQ 内容",
                "similarity": 0.99,
            },
            {
                "source_type": "guide",
                "source": "操作步骤 · 材料准备 / 推荐信",
                "link": "/guide/prep?step=2",
                "content": "推荐信通常需要提前 4-8 周联系老师。",
                "similarity": 0.88,
            },
            {
                "source_type": "program",
                "source": "专业速查 · 新媒体",
                "link": "/programs",
                "content": "该专业截止日期通常在 12 月。",
                "similarity": 0.81,
            },
        ]

        with (
            patch.object(rag_pipeline, "is_rag_runtime_ready", return_value=True),
            patch.object(rag_pipeline.zhipu_client, "create_embeddings", return_value=[[0.1, 0.2]]),
            patch.object(rag_pipeline.supabase_client, "match_rag_chunks", return_value=fake_matches),
            patch.object(rag_pipeline.zhipu_client, "generate_answer", return_value="这是回答"),
        ):
            answer, sources = rag_pipeline.ask_with_rag("推荐信要提前多久联系老师？")

        self.assertEqual(answer, "这是回答")
        self.assertEqual(
            sources,
            [
                {"source": "操作步骤 · 材料准备 / 推荐信", "link": "/guide/prep?step=2"},
                {"source": "专业速查 · 新媒体", "link": "/programs"},
            ],
        )

    def test_ask_with_rag_returns_empty_when_only_disallowed_sources(self):
        fake_matches = [
            {
                "source_type": "faq",
                "source": "常见问题 · 旧问题",
                "link": "/faq/1",
                "content": "旧 FAQ 内容",
                "similarity": 0.93,
            }
        ]

        with (
            patch.object(rag_pipeline, "is_rag_runtime_ready", return_value=True),
            patch.object(rag_pipeline.zhipu_client, "create_embeddings", return_value=[[0.1, 0.2]]),
            patch.object(rag_pipeline.supabase_client, "match_rag_chunks", return_value=fake_matches),
            patch.object(rag_pipeline.zhipu_client, "generate_answer", return_value="不应被调用") as answer_mock,
        ):
            answer, sources = rag_pipeline.ask_with_rag("推荐信要提前多久联系老师？")

        self.assertIn("我没有在当前知识库检索到直接证据", answer)
        self.assertEqual(sources, [])
        answer_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main()
