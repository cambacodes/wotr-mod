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

# Discovery imports both spellings; share the expensive isolated-build cache.
sys.modules.setdefault('story_fixture', sys.modules[__name__])
sys.modules.setdefault('tests.story_fixture', sys.modules[__name__])

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=2)
def _assembled(include_harem=True):
    path = os.environ.get('RRT_TEST_STORY' if include_harem else 'RRT_TEST_BASE_STORY')
    if path:
        return json.loads(Path(path).read_text(encoding='utf-8-sig'))
    # The harem-less variant is a partial build (A109); the entry is a named script, not inline -c code (A114).
    argv = [sys.executable, '-B', str(ROOT / 'tests/build_fixture_story.py'), *([] if include_harem else ['--no-harem'])]
    run = subprocess.run(argv, cwd=ROOT, env=dict(os.environ, PYTHONHASHSEED='0', PYTHONPATH=str(ROOT)),
                         capture_output=True, text=True)
    if run.returncode:
        raise RuntimeError(run.stderr)
    return json.loads(run.stdout)


def fresh_story(include_harem=True):
    return copy.deepcopy(_assembled(include_harem))
