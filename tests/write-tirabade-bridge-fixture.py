"""Stage the real bridge and Anevia source with a labeled Irabeth contract fixture.

This tests joins while Irabeth's independently owned manuscript is in progress.
The fixture cannot certify a played Irabeth romance or assembled release readiness.
"""
import json
from copy import deepcopy
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from expansion import make_expansion
from story_format import c, n, scene
from storylines import anevia_independent, tirabade_independent_bridge

payload = make_expansion()
payload["Relationships"]["anevia"] = deepcopy(anevia_independent.RELATIONSHIP)
payload["Scenes"].extend(deepcopy(anevia_independent.SCENES))
payload["Relationships"]["irabeth"] = dict(
    Title="Irabeth contract fixture, not a played route", StartedFlag="irabeth.started",
    ClosedFlag="irabeth.closed", CommittedFlag="irabeth.committed",
    UnavailableFlags=["irabeth_dead", "irabeth_gone", "swarm", "true_lich"], FailureFlags=[])
payload["Scenes"].append(scene("bridge_contract_fixture", "Unplayed contract declarations", "Memory", 3, "", [
    n("declaration", "Narrator", "Test-only marker producers. These are not a reviewed or played romance.",
      c(flags=("irabeth.courtship_requested", "irabeth.local_declined", "irabeth.lover", "irabeth.marital_terms_agreed")))
], Relationship="irabeth", Remote=True, ManualOnly=True, optional=True))
tirabade_independent_bridge.integrate(payload)
path = ROOT / "development/tirabade-bridge-fixture.json"
path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Wrote explicit bridge/Irabeth-contract fixture: {path}")
