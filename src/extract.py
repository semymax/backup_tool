from pathlib import Path
import tarfile

def extract_tar(tar_path: Path, destination: Path) -> Path:
    with tarfile.open(tar_path, "r") as tar:
        tar.extractall(path=destination)
