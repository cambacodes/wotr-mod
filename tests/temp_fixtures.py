"""System-temp fixtures use ordinary inherited directory permissions."""
from contextlib import contextmanager
from pathlib import Path
import shutil
import tempfile
import uuid


@contextmanager
def temporary_directory():
    directory = Path(tempfile.gettempdir()) / ("rrt-fixture-" + uuid.uuid4().hex)
    directory.mkdir()
    try:
        yield directory
    finally:
        shutil.rmtree(directory)
