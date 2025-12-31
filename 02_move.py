import shutil
from pathlib import Path

# Define paths
raw_dir = Path("raw")
tmp_raw_dir = Path("tmp/raw")

# Delete ./raw/ if it exists
if raw_dir.exists():
    shutil.rmtree(raw_dir)
    print(f"Deleted {raw_dir}/")

# Replace ./raw/ with ./tmp/raw/
shutil.move(str(tmp_raw_dir), str(raw_dir))
print(f"Moved {tmp_raw_dir}/ to {raw_dir}/")
