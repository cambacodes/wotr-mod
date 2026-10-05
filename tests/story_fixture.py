"""One isolated authoring build per process; every caller gets its own data.

The gates supply a copy of their freshly generated export. Direct unittest runs
build in a fresh interpreter so mutations of authoring globals cannot leak in.
Tests of the generator itself continue calling make_expansion directly.
"""
import copy
from functools import lru_cache
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def _assembled():
    path = os.environ.get('RRT_TEST_STORY')
    if path:
        return json.loads(Path(path).read_text(encoding='utf-8-sig'))
    run = subprocess.run([sys.executable, '-B', '-c',
                          'import expansion,json; print(json.dumps(expansion.make_expansion()))'],
                         cwd=ROOT, env=dict(os.environ, PYTHONHASHSEED='0'),
                         capture_output=True, text=True)
    if run.returncode:
        raise RuntimeError(run.stderr)
    return json.loads(run.stdout)


def fresh_story():
    return copy.deepcopy(_assembled())
