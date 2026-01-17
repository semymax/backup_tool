from pathlib import Path
import hashlib

def verify_sha256(archive: Path) -> bool:
    checksum_file = archive.with_name(archive.name + ".sha256")
    
    if not checksum_file.is_file():
        return False
    
    expected = checksum_file.read_text().split()[0]
    h = hashlib.sha256()
    
    with open(archive, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
            
    return h.hexdigest() == expected
