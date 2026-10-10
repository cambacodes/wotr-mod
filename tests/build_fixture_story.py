"""Fixture build entry for tests/story_fixture.py: an inspectable script, because the gate runner refuses inline
`python -c` code (A114). Prints the assembled expansion as JSON; --no-harem builds the partial (harem-less) variant."""
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

if "--no-harem" in sys.argv:
    os.environ["RRT_PARTIAL_BUILD"] = "1"
    import storylines.harem_rows as rows
    rows.register_all = lambda *args: False
import expansion

from authoring import generation_errors

try:
    print(json.dumps(expansion.make_expansion()))
except generation_errors.GenerationErrors:
    print(json.dumps(generation_errors.errors), file=sys.stderr)
    raise
