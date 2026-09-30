"""Harness-only probe scenes. NEVER imported by expansion.py: they are not in development/Story.json and never ship.

tools/build-harness-probes.py appends PROBES to the built story and writes harness/probes/Story.json (gitignored), which
run-harness.ps1 -Probes installs in place of development/Story.json for that run only (the Mods folder is restored after).

pacing.e0.probe (handoff 13, E-new 0): a no-op inline attachment on a Prologue host, to read Player.Chapter there and prove
that a chapter 0 scene attaches and hands the conversation back. Host: MeetSeelahAnevia (Anevia's "My ankle's killin' me",
Cue_0003 ecc3bd72, via continue); entry list AnswersList a55fc20c; return cue 159c4442 (PP0 findings).
"""
from story_format import c, n, scene

E0_LIST = "a55fc20c6f0ff56439b40d6ba53cb8d7"
E0_RETURN = "159c4442a8672334c9394d9579cfd8f9"

PROBES = [
    scene("pacing.e0.probe", "Prologue probe", "Anevia", 0, "[RRT harness probe] Continue.", [
        n("start", "Narrator", "{n}RRT harness probe (E-new 0): a chapter 0 scene attached to a Prologue answer list.{/n}",
          c("Continue")),
    ], last=0, optional=True, Relationship="anevia", Chapters=[0], AnswerLists=[E0_LIST], NativeReturnCue=E0_RETURN),
]

PROBE_IDS = [s["Id"] for s in PROBES]
