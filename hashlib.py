#!/usr/bin/env python

from hashlib import md5
from pathlib import Path


def get_md5_checksum(filepath: Path) -> str:
    """Produce the checksum of the content of the specified file."""
    with filepath.open('rb') as f:
        content = f.read()
    return md5(content).hexdigest()


def get_md5_checksums(filepaths: list) -> None:
    """Produce the checksums of the content of the specified files."""
    for filepath in filepaths:
        checksum = get_md5_checksum(filepath)
        print(f"md5 checksum for {filepath.name}:", checksum)
