#!/usr/bin/env python3
"""
CodeToAGI — EP42 Challenge Solution
Parallel File Processor with ThreadPool + ProcessPool
"""

import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime

def process_file(file_path: Path) -> dict:
    """Process one file: return line count and size."""
    try:
        size = file_path.stat().st_size
        lines = 0
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = sum(1 for _ in f)
        return {"path": str(file_path), "lines": lines, "size": size}
    except Exception:
        return {"path": str(file_path), "lines": 0, "size": 0}


def parallel_process_files(folder_path: str, max_workers: int = 8, use_processes: bool = False):
    root = Path(folder_path).resolve()
    if not root.exists():
        print(f"❌ Folder not found: {root}")
        return

    # Find all files recursively
    files = list(root.rglob("*.*"))  # or rglob("*") for all files
    print(f"🔍 Found {len(files)} files in {root}")
    print(f"⚙️  Using {'ProcessPool' if use_processes else 'ThreadPool'} with {max_workers} workers\n")

    start = time.time()

    Executor = ProcessPoolExecutor if use_processes else ThreadPoolExecutor

    with Executor(max_workers=max_workers) as executor:
        results = list(executor.map(process_file, files))

    total_time = time.time() - start

    # Summary
    total_lines = sum(r["lines"] for r in results)
    total_size_mb = sum(r["size"] for r in results) / (1024 * 1024)

    print("✅ Parallel Processing Complete!")
    print(f"   Total files : {len(files):,}")
    print(f"   Total lines : {total_lines:,}")
    print(f"   Total size  : {total_size_mb:.2f} MB")
    print(f"   Time taken  : {total_time:.2f} seconds\n")

    return results


if __name__ == "__main__":
    print("🚀 CodeToAGI EP42 - Parallel File Processor\n")

    # === CHANGE THIS PATH ===
    target_folder = "."   # or r"C:\your\dataset\folder"

    print("=== ThreadPoolExecutor (I/O bound) ===")
    parallel_process_files(target_folder, max_workers=8, use_processes=False)

    print("\n=== ProcessPoolExecutor (CPU bound) ===")
    parallel_process_files(target_folder, max_workers=8, use_processes=True)

    print(f"\n🎉 Challenge completed at {datetime.now().strftime('%H:%M:%S')}")
    print("Tip: Try a large folder of text/CSV files to see the real speedup!")
