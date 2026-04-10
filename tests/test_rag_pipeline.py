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


if __name__ == "__main__":
    unittest.main()
