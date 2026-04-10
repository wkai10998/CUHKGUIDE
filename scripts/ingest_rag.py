from __future__ import annotations

import argparse
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from utils.rag_pipeline import ingest_knowledge_base

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


def main() -> int:
    parser = argparse.ArgumentParser(description="将项目知识库切片并写入 Supabase pgvector。")
    parser.add_argument("--chunk-size", type=int, default=None, help="切片长度（按字符）。")
    parser.add_argument("--overlap", type=int, default=None, help="切片重叠长度。")
    parser.add_argument("--batch-size", type=int, default=32, help="embedding 批量大小（<=64）。")
    args = parser.parse_args()

    if load_dotenv is not None:
        load_dotenv()

    result = ingest_knowledge_base(
        chunk_size=args.chunk_size,
        overlap=args.overlap,
        batch_size=args.batch_size,
    )
    print(f"RAG ingest 完成：生成切片 {result['records']} 条，写入/更新 {result['upserted']} 条。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
