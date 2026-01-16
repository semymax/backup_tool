from pathlib import Path
import tarfile
import tempfile

def create_tar(sources: list[Path]) -> Path:
    temp_dir = tempfile.mkdtemp()
    tar_path = Path(temp_dir) / "bkp.tar"

    with tarfile.open(tar_path, "w") as tar:
        for src in sources:
            tar.add(src, arcname=src.name)
        
    return tar_path
