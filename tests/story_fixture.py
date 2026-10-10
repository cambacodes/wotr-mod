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


def row_registration_fixture(module):
    """Keep assembled dependencies and exercise this row's authoring registrar.

    Final controllers decorate row choices and contacts. Registrar unit tests
    build their own row before those passes; full-export tests cover delivery.
    """
    story = fresh_story()
    prefix = getattr(module, 'PREFIX', None) or module.P
    story['Scenes'] = [s for s in story['Scenes'] if not s['Id'].startswith(prefix)]
    if module.__name__.endswith('.s42'):
        # S42 also appends this owned continuation to Kaylessa's clearing.
        clearing = next(s for s in story['Scenes'] if s['Id'] == 'kaylessa.clearing.where_i_was_meant_to_die')
        clearing['Nodes'] = [n for n in clearing['Nodes'] if n['Id'] != 's42_cover']
        opening = clearing['Nodes'][0]
        opening['Choices'] = [c for c in opening['Choices'] if c.get('Next') != 's42_cover']
    module.register(story, story['Scenes'], story['Etudes'])
    from storylines import scene_kinds
    scene_kinds.integrate(story)
    return story
