"""Kiana's native reconciliations (engine queue 8; Writer/handoffs/trickster/kiana.md, Polish pass residuals 1-2).

8a: VendorArsinoe/Answer_0025 ("Is there any news about the poor folk whose souls were stolen?" -> Cue_0026, her search
found nothing) stays offered after the Commander ransomed or bought back the guests. A reviewed E18 gate hides it in those
worlds (the list the game already shows once Seelah's Q3 has started). Read only; warning-only on refusal.
"""
from storylines import kiana_trickster as kt

NATIVE_GATES = {
    "arsinoe.souls_search_answer": dict(Target="41d9638f7d971164fab4efdbbbffbe70", Relationship="kiana",
                                        When=[["trickster.ever", kt.RANSOMED], ["trickster.ever", kt.BOUGHT]]),
}


def integrate(payload):
    """Register the gates (after kiana_trickster)."""
    gates = payload.setdefault("NativeGates", {})
    for key, gate in NATIVE_GATES.items():
        if key in gates:
            raise ValueError("kiana_native: conflicting native gate " + key)
        gates[key] = dict(gate, When=[list(g) for g in gate["When"]])
