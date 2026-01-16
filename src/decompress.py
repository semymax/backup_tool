from pathlib import Path
import zstandard as zstd

def decompress_zstd(zst_path: Path) -> Path:
    tar_path = zst_path.with_suffix(".tar")

    dctx = zstd.ZstdDecompressor()
    with open(zst_path, "rb") as fin, open(tar_path, "wb") as fout:
        dctx.copy_stream(fin, fout)
        
    return tar_path
