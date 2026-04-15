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
                patch.object(knowledge_base, "get_programs", return_value=[]),
                patch.object(knowledge_base, "get_guides", return_value={}),
            ):
                rows = knowledge_base.build_knowledge_chunks()

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source_type"], "external")
        self.assertEqual(rows[0]["source"], "官方知识库")
        self.assertIn("港中文", rows[0]["content"])

    def test_build_knowledge_chunks_empty_when_no_uploaded_kb_text(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            rag_path = Path(temp_dir) / "rag_kb.txt"
            rag_path.write_text("   ", encoding="utf-8")
            with (
                patch.object(knowledge_base, "RAG_TEXT_PATH", rag_path),
                patch.object(knowledge_base, "get_programs", return_value=[]),
                patch.object(knowledge_base, "get_guides", return_value={}),
            ):
                rows = knowledge_base.build_knowledge_chunks()

        self.assertEqual(rows, [])

    def test_build_knowledge_chunks_includes_programs_and_guides(self):
        fake_programs = [
            {
                "name": "MSc in Information Engineering",
                "school": "Faculty of Engineering",
                "focus": "数据与智能系统",
                "deadline": "2027-01-15",
                "language": "IELTS 6.5 / TOEFL 79",
            }
        ]
        fake_guides = {
            "prep": {
                "title": "申请前准备（2.1+2.2）",
                "steps": [
                    {
                        "id": 1,
                        "title": "注册与准备",
                        "tutorial": ["准备申请账号。"],
                        "notes": ["整理材料清单。"],
                    }
                ],
            }
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            rag_path = Path(temp_dir) / "rag_kb.txt"
            rag_path.write_text("", encoding="utf-8")
            with (
                patch.object(knowledge_base, "RAG_TEXT_PATH", rag_path),
                patch.object(knowledge_base, "get_programs", return_value=fake_programs),
                patch.object(knowledge_base, "get_guides", return_value=fake_guides),
            ):
                rows = knowledge_base.build_knowledge_chunks()

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["source_type"], "program")
        self.assertEqual(rows[0]["link"], "/programs")
        self.assertEqual(rows[1]["source_type"], "guide")
        self.assertEqual(rows[1]["link"], "/guide/prep?step=1")


if __name__ == "__main__":
    unittest.main()
