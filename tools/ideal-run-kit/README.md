# F8 combined Trickster run

This is the Writer ideal-run kit, versioned beside the worktree it exercises. The
runner resolves `tools/rrt_verify.py` and `development/Story.json` from its own
repository, including when launched from another directory. Regenerate first:

```sh
PYTHONHASHSEED=0 python expansion.py
PYTHONHASHSEED=0 python tools/ideal-run-kit/final_sim.py /tmp/rrt-default.json
PYTHONHASHSEED=0 CHDAYS=3:80,5:30 python tools/ideal-run-kit/final_sim.py /tmp/rrt-short.json
```

Optional relationship arguments after the output path print their choice traces.
Delete the output JSON files after inspection. See
[`../ideal-run-regression.md`](../ideal-run-regression.md) for the result table,
native evidence, gate results, and limitations.

The kit schedules native observations and steers player choices. It does not
change availability rules. A non-native scheduled flag is rejected, including in
the after-scene scripts. Authored costs, commitments and returns must come from
the choices actually played. Files beginning `_` in `natives/` are the original
alternative histories and are ignored by the combined run; `w6/combined.extra.txt`
duplicates the per-route extras retained from the Writer kit.

F8 corrections:

- Delamere: after entering the tomb, break the seal, leave the relics, close the
  lid, then choose the native **Close** answer. This earns the existing Book-lock
  gate before the living waking. Her remains stay in the temple.
- Dorgelinda: take the guide's rider/signing choice at Logistics 4. The former
  after-scene injection of `cost.carts_signed` is removed from both copies of the
  extras. The cost now appears in the executed `rider/0` choice's `Set`.

The all-romance policy also avoids Dorgelinda's `ledger.quarrel_cold` and
`ledger.quarrel_unmended` outcomes. The shortest unsteered path walks out of
**Hammer and tongs** and later lets **Cold counts** stand, which withholds current
eligibility despite the earlier commitment. The kit instead writes the existing
letter and earns `ledger.quarrel_mended`, including the allotment cuts and powder
restoration. If the Commander already walked out, the same policy steers the
later **Cold counts** apology and letter. No route gate or derived forbid changes.

The unchanged simulator policy uses successful checks, a deeper planner for
folded pages, daily physical visits, and 45 simulated Chapter 6 days to play the
consecutive entries on the Threshold answer list. Its default 30-day Chapter 3
is a scheduling stress case; the guide requires at least 75 days for native
Seelah progression, so the 80-day run is the relevant campaign-length check.
