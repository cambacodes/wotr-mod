"""System-temp test fixtures with ordinary inherited permissions."""
from contextlib import contextmanager
from pathlib import Path
import shutil
import tempfile
from uuid import uuid4


@contextmanager
def writable_temp():
    directory = Path(tempfile.gettempdir()) / ("rrt-writable-" + uuid4().hex)
    # Python 3.14's mkdtemp uses 0700, which removes the sandbox's inherited access on Windows.
    directory.mkdir(mode=0o777)
    try:
        yield directory
    finally:
        shutil.rmtree(directory)
