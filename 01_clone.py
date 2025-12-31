import subprocess
import os

repo_url = "https://github.com/jwd83/posterdb"
target_dir = "./tmp"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

subprocess.run(["git", "clone", repo_url, target_dir], check=True)
print(f"Cloned {repo_url} into {target_dir}")
