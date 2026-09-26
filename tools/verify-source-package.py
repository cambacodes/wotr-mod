"""Rebuild the expansion from an extracted source archive and compare exact bytes."""
import argparse
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    parser.add_argument("expected_story", type=Path)
    args = parser.parse_args()
    expected = args.expected_story.read_bytes()
    with tempfile.TemporaryDirectory(prefix="rrt-source-rebuild-") as temporary:
        destination = Path(temporary)
        with ZipFile(args.archive) as archive:
            archive.extractall(destination)
        subprocess.run([sys.executable, str(destination / "expansion.py")], cwd=destination, check=True)
        rebuilt = (destination / "development/Story.json").read_bytes()
        if rebuilt != expected:
            raise SystemExit("FAIL: extracted source rebuild differs from the expected story")
    print("PASS: extracted source rebuild " + hashlib.sha256(rebuilt).hexdigest().upper())


if __name__ == "__main__":
    main()
