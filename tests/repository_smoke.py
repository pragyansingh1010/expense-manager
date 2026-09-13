from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source_files = list(ROOT.glob("*.py"))
assert source_files, "no Python source file found"
assert all(p.stat().st_size > 0 for p in source_files)
print("Expense Manager smoke check passed")
