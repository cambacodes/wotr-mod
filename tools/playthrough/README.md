# Playthrough walker and checkpoint dossiers

Deterministic simulated playthroughs of the export (`development/Story.json`) under named player
policies, turned into per-chapter dossiers for LLM continuity reviewers (Luna per chapter part,
Terra for findings marked uncertain). Walking/rendering needs no game install or provider.

```sh
python tools/playthrough/walker.py --all                          # 4 policies, one process each, ~4 min
python tools/playthrough/walker.py --policy trickster_villain     # one policy, ~1 min
python tools/playthrough/dossier.py --all                         # every runs/*/trace.json, ~10 s
python tools/playthrough/dossier.py --policy hostile --max-kb 120 --knowledge C:/Users/Z/Documents/Projects/Writer/knowledge
```

Both scripts re-run themselves with `PYTHONHASHSEED=0 PYTHONUTF8=1` so output is byte-stable.
`--knowledge` defaults to `$RRT_KNOWLEDGE` or the Writer repo path above; it is only read.

## Files

- `walker.py`: runs the repo's E9 campaign simulator (`tools/rrt_verify.simulate_rest_budget`,
  the `Rules.Available` / `sim_play` mirrors, unchanged) under a policy and writes
  `runs/<policy>/trace.json`.
- `policies.json`: the four policies, as data: path flag, which parts of the ideal-run kit to use,
  pursued relationships, objective tuples, choice-weight rules, scheduled natives.
- `dossier.py`: writes `runs/<policy>/chapter-<N>[-part-<k>].md` (each <= `--max-kb`, default 120
  KB), a whole-chapter timeline, `states.json`, `dossier-manifest.json`, and `runs/<policy>/index.md`.
- `reviewer-contract.md` + `reviewer-schema.json`: the reviewer checklist and strict JSON output.

Runs, state references, manifests and dossiers are generated and ignored (apart from the
legacy committed summaries). Regenerate them after an export change. Legacy summaries
are unpinned leads; the new aggregator requires admitted manifest-declared outputs.

Reviewing invokes providers and requires separate authorization for that run:

```sh
bash tools/playthrough/review.sh hostile 4 --knowledge /path/to/Writer/knowledge
python tools/playthrough/aggregate.py --manifest tools/playthrough/runs/review-manifest.json
```

The shell wrapper propagates the Python runner's exit. Each call hashes all supplied
inputs, export and contract/schema plus model/effort/prompt, validates strict output,
and atomically publishes an admitted output and receipt under its digest. Failed calls
retain diagnostics and usage; missing usage is `unknown`. The manifest declares parts
and one chapter synthesis per policy/chapter; aggregation ignores undeclared outputs,
keeps pending/dropped/artifact dispositions and raw scores, and fails on missing coverage
or unresolved verification. Chapter metrics use equal chapter weights within policy,
then equal policy weights, independent of dossier size. An incomplete metric is null.
Review receipts do not replace the integration runner's gate receipts.

Offline regressions (fake provider only):

```sh
python -m unittest tests.test_playthrough_loop
```

## How a run works

The scheduler is the simulator's: chapters 0-6 (days per chapter from `policies.json`
`chapter_days`, default profile 3:80, 5:30, 6:45 as in `run_guide_check.py`), one daily round of
physical visits per relationship, mailbag letters at rests, The Table at rests in chapters 3 and 5.
Then an **epilogue pass**: every epilogue scene whose gates hold on the final state, in export order.

The walker changes only what the player does:

- **Planner.** `planner: kit` is final_sim.py's (sim_plan, depth 80, closures widened by
  `avoid.txt`). `planner: policy` uses the identical traversal (Requires/Forbids on held flags,
  EnterSet, crusade payments, check -> success, abort) and picks the path with the lowest objective
  tuple; ties keep the first answer in story order (stable). Objective keys and the `wanted`
  rules (which scenes the player opens at all) are documented in `policies.json` `_doc`.
- **Weights.** `rules` add weight per answer by alignment shift (`Alignment.Direction` x value),
  answer-text regex, or regex over the flags the answer sets.
- **World.** Natives come from the ideal-run kit (`natives/`, `w6/`) when `kit.natives` is true
  (optionally filtered by `kit.natives_exclude`), else from the simulator's own progress rule;
  `natives_on` adds native keys (validated against the export) from a chapter. Bans, skips and
  avoid-text from the kit apply only where the policy enables them.
- **Path.** `mythic` replaces the `trickster` flag from chapter 1. With `enforce_mythic`, answers
  with a `Mythic` gate and scenes with `EntryMythic` for another path are unavailable (the E9
  mirror ignores both).

Parity: `trickster_all_romance` reproduces `tools/ideal-run-kit/final_sim.py` (with
`CHDAYS=3:80,5:30`) exactly: same 1090 scene visits, days and answer indices, plus 130 epilogue pages.

## Trace format (`rrt-playthrough-trace/1`)

`summary` (stats, scheduled natives, skipped scenes), `chapters` and `relationships` (simulator
results), `final_flags`, and ordered `events`:

- `{"type":"world", ch, day, hour, on:[...], off:[...]}`: natives, timed natives and derived
  composites that changed between scenes.
- `{"type":"scene", id, rel, owner, title, ch, day, hour, remote, table, epilogue, completed,
  steps:[{node, index, text, paragraphs:[visible indices], set, check, crusade, alignment,
  native_next}], end_node, set, unset}`: visible paragraphs are evaluated with the flags held on
  entering each node (`Rules.ParagraphVisible`).

## Dossier contents

Per part: state table at start and end (started / committed / closed / departed / dead per
relationship, harem eligibility, returns via overrides), native progress within 3 days of the part,
ordered scene list, then per scene: how it is reached (native dialogue answer, The Table, rest
letter, interaction hub, area, owner contact), gameplay touched (checks, crusade costs, alignment,
native hand-offs, items, etudes, native state, rest allowance, delays), placement between native
progress keys, entry answer, full visible text with chosen answer and the other answers shown, flags
set, word count. Appendix: per woman present (roster women in `knowledge/identities.json`, matched
by relationship, owner, speaker and participants), her knowledge file paths and 10 native lines
ranked by vocabulary shared with her scenes in the part.

## Limitations

- Simulation, not the game: native quests exist only as the native keys the export reads; their
  timing comes from the kit or the simulator's earliest-chapter rule. Checks always succeed;
  crusade resources are unlimited; the player is assumed in the right area with every contact.
- One scene per relationship per simulated day; the in-game answer lists that chain several pages
  at once are spread over days (as in final_sim).
- `hostile`'s deaths/departures are scheduled natives at plausible chapters, not derived from
  played native choices; combinations are not validated against the base game.
- `nontrickster_good` uses only path-neutral kit natives; Angel-specific native progress beyond
  what the export reads is not modelled, and `EntryAlignment` is not enforced (alignment unknown).
- The epilogue pass plays every satisfiable epilogue page in export order; the runtime's
  epilogue sequencing and suppression rules are not modelled.
- The policy planner is a per-scene greedy choice; it does not plan across scenes (a villain may
  still commit a non-villain route when every completing path commits).
- Relationship status is per relationship; a pair (`minagho_chivarro`, `tirabade`) shows one row.
