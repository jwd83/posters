from pathlib import Path

raw_dir = Path("raw")
catalog_file = Path("catalog.txt")

image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"}

images = sorted([f.name for f in raw_dir.iterdir() if f.suffix.lower() in image_extensions])

with open(catalog_file, "w", newline="\n") as f:
    f.write("\n".join(images))

print(f"Generated catalog.txt with {len(images)} images from {raw_dir}/")
