import tempfile
import unittest
from pathlib import Path

from utils.knowledge_files import load_external_knowledge_documents


class KnowledgeFilesTestCase(unittest.TestCase):
    def test_load_external_documents_supports_txt_json_csv(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir)
            (base / "notice.txt").write_text("这是 txt 文本", encoding="utf-8")
            (base / "rules.json").write_text(
                '{"title":"申请说明","items":["语言成绩","推荐信"]}',
                encoding="utf-8",
            )
            (base / "deadlines.csv").write_text(
                "program,deadline\nMSc AI,2026-01-31\n",
                encoding="utf-8",
            )

            docs = load_external_knowledge_documents(base)

        self.assertEqual(len(docs), 3)
        for item in docs:
            self.assertEqual(item["source_type"], "external")
            self.assertTrue(str(item["source"]).startswith("外部知识库 · "))
            self.assertTrue(bool(item["content"]))
            self.assertIn("format", item["metadata"])


if __name__ == "__main__":
    unittest.main()
