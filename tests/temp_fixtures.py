"""Fixture directories inherit the workspace ACL, including on managed Windows sandboxes."""
from contextlib import contextmanager
from pathlib import Path
import shutil
import uuid


@contextmanager
def temporary_directory():
    directory = Path(__file__).resolve().parent / ("fixture-" + uuid.uuid4().hex)
    directory.mkdir()
    try:
        yield directory
    finally:
        shutil.rmtree(directory)
