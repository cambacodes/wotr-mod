"""Disposable fixtures inherit directory permissions, including the Windows sandbox identity."""
from contextlib import contextmanager
from pathlib import Path
import shutil
import tempfile
from uuid import uuid4


@contextmanager
def temporary_directory():
    directory = Path(tempfile.gettempdir()) / ("rrt-tests-" + uuid4().hex)
    directory.mkdir()
    try:
        yield str(directory)
    finally:
        shutil.rmtree(directory)
