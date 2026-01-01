import shutil
from pathlib import Path

tmp_dir = Path("./tmp")

if tmp_dir.exists():
    shutil.rmtree(tmp_dir)
    print(f"Deleted {tmp_dir}/")
else:
    print(f"{tmp_dir}/ does not exist, nothing to clean")
