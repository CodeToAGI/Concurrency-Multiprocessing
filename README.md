# CodeToAGI — Episode 42: Concurrency & Multiprocessing

**Learn how to use all your CPU cores — threading, multiprocessing, GIL, and concurrent.futures explained.**

## 📁 Files

- `manim_ep42.py` — Manim animation scenes
- `generate_ep42.py` — Full episode builder
- `parallel_file_processor.py` — **Challenge solution**

## 🎯 Challenge

Build a **parallel file processor** that:
1. Scans a folder recursively
2. Uses `ThreadPoolExecutor` or `ProcessPoolExecutor` to process files
3. Counts total lines + total size
4. Times it and compares with sequential processing
5. **Bonus**: Try both ThreadPool and ProcessPool

**Solution included**: `parallel_file_processor.py`

## 🛠️ Key Topics Covered

- The Global Interpreter Lock (GIL) explained
- `threading` vs `multiprocessing`
- `ThreadPoolExecutor` (I/O-bound)
- `ProcessPoolExecutor` (CPU-bound)
- `concurrent.futures` modern API
- `if __name__ == "__main__"` guard
- Real performance comparison

## Next Episode

**EP43 — Descriptors & Metaclasses**

---

Made with ❤️ for the CodeToAGI community
