from pathlib import Path
import hashlib

def sha256(file_path: Path) -> Path:
    hash_path = file_path.with_suffix(file_path.suffix + ".sha256")
    h = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
            
    hash_path.write_text(f"{h.hexdigest()} {file_path.name}\n")
    return hash_path
