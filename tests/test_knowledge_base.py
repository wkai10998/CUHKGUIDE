import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from utils import knowledge_base


class KnowledgeBaseTestCase(unittest.TestCase):
    def test_build_knowledge_chunks_includes_rag_text_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            rag_path = Path(temp_dir) / "rag_kb.txt"
            rag_path.write_text("港中文 申请 材料 清单 示例", encoding="utf-8")

            with (
                patch.object(knowledge_base, "RAG_TEXT_PATH", rag_path),
                patch.object(knowledge_base, "get_faqs", return_value=[]),
                patch.object(knowledge_base, "get_programs", return_value=[]),
                patch.object(knowledge_base, "get_guides", return_value={}),
            ):
                rows = knowledge_base.build_knowledge_chunks()

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source_type"], "external")
        self.assertEqual(rows[0]["source"], "外部知识库 · rag_kb.txt")
        self.assertIn("港中文", rows[0]["content"])


if __name__ == "__main__":
    unittest.main()
