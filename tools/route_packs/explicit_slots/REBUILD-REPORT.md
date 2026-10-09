# Explicit-slot rebuild report

Base: `remote/claude/trickster-expansion` @ `ef49eeaa`, branch `claude/slot-rebuild`.
Export: `development/Story.json` at that head. Only briefs changed, plus the
`REBUILDING` allowlist in `tools/slot_brief_lint.py`. No export, scene, node or
choice ID changed.

## Lint counts

| Run | Briefs | Hard | Known rebuild | Warnings |
|---|---|---|---|---|
| Before, `--strict` | 352 | 213 | 0 | 189 |
| Before, `--known-rebuilds` | 352 | 0 | 213 | 189 |
| After, `--strict` | 352 | 105 | 0 | 189 |
| After, `--strict --known-rebuilds` | 352 | 0 | 105 | 189 |

The 189 warnings are unchanged. They are 64 terminal boundaries (`last_line` needs
editorial review) and 125 background male-mention notes. No scope, variant or
pronoun failure was hard, before or after.

### Classification of the 213 hard findings at the start

| Class | Before | Fixed | After | Notes |
|---|---|---|---|---|
| `facts` given as a list (schema) | 63 | 63 | 0 | Joined into one text field. Gemory concatenates `facts`. |
| Stale boundary (`last_line` is not the next node's first beat) | 71 | 44 | 27 | Fixed for 21 camellia and 23 minagho briefs. 8 areelu briefs are pinned by a test; 19 are stale `chivarro/` mirrors. |
| Stale boundary exposed once the host was addressed | 0 | - | 1 | `camellia_vellexia`: pinned by a test. |
| Divergent duplicate slot ID | 56 | 0 | 56 | 28 `minagho_chivarro.*` slots each exist in both `minagho/` and `chivarro/`. |
| Epilogue narration (`third-past`) | 18 | 2 | 16 | Fixed where the host is third person. The rest have second-person hosts. |
| Host missing or moved | 4 | 1 address fixed | 3 (+1 `retired`) | `camellia_vellexia` is now addressed, but its reserved host is gated off by design. |
| Missing required field | 1 | 0 | 1 | `nocticula_shamira` has no `example`. The brief is already in `harem/blocked/`. |
| Participant / pronoun | 0 | - | 0 | Only warnings (background male mentions). |
| Stale export digests | 0 | - | 0 | No brief records a digest. Receipts bind at generation time (`--host-export`). |

### Fixes applied

- **facts to text** (63 briefs: `camellia/` 21, `minagho/minagho_chivarro.*` 34, `areelu-vorlesh/` 8).
- **Boundary set to the next node's first beat** (44 briefs). The beat is computed with the
  lint's own `first_beat`, and every host has exactly one next beat. The old closing line
  is kept in the new field `prior_stop_line`, which Gemory and the lint ignore, so the
  author's intended last spoken line survives for editorial use.
- **`narration: third-past`** on `minagho/minagho_chivarro.trickster.epilogue.commit.explicit.1`
  and `.2`. Both hosts are third person. Caveat: the `.1` boundary (`went`) is in the present tense.
- **Host address** for `harem/household.pair.camellia_vellexia.choice.explicit.1`:
  `host_scene: household.pair.camellia_vellexia.choice` and `host_node: explicit.1`.
  This is the short runtime ID in the export.
- **Allowlist shrink.** `REBUILDING` went from 10 to 7 routes: nocticula, jerribeth,
  minagho, chivarro, arueshalae, areelu and camellia. Removed: minachiv, hepzamirah and
  melazmera, which have no remaining debt. Each remaining route still has at least one
  hard finding. Harem pairs are attributed to camellia, jerribeth, arueshalae and nocticula.

Fields read by the builders were not touched: `default_text`, `slot_id`, `source`,
`source_nodes`, `insertion` and `speakers`. These are read by
`storylines/camellia_round2.py`, `minagho_round2.py`, `chivarro_setpieces.py` and
`minachiv_voice.py`, so the export does not change.

## Ready vs blocked per woman

Unique slot IDs. The 9 `minachiv.*` briefs that are identical copies in `minagho/` and
`chivarro/` are counted once, under chivarro. "Dropped" means an evidenced drop in
`plans/slot-brief-index.json`.

| Woman / unit | Ready | Blocked | Dropped |
|---|---|---|---|
| anevia | 20 | 0 | 0 |
| aranka | 11 | 0 | 0 |
| areelu (`areelu/` + `areelu-vorlesh/`) | 1 | 8 | 0 |
| arsinoe | 5 | 0 | 0 |
| arueshalae | 5 | 0 | 0 |
| camellia | 23 | 0 | 0 |
| chadali | 3 | 0 | 0 |
| chivarro (`chivarro/`, incl. 9 shared `minachiv.*`) | 9 | 28 (stale mirror copies) | 0 |
| delamere | 5 | 0 | 0 |
| devarra | 5 | 0 | 0 |
| dorgelinda | 1 | 0 | 0 |
| eliandra | 5 | 0 | 0 |
| elyanka | 4 | 0 | 0 |
| eritrice | 3 | 0 | 0 |
| galfrey | 4 | 0 | 0 |
| gesmerha | 6 | 0 | 1 |
| hepzamirah | 5 | 0 | 0 |
| herrax | 7 | 0 | 0 |
| horzalah | 7 | 0 | 0 |
| iomedae | 2 | 0 | 0 |
| irabeth | 10 | 0 | 0 |
| jannah | 2 | 0 | 0 |
| jerribeth | 8 | 0 | 1 |
| kaylessa | 2 | 0 | 0 |
| kiana | 4 | 0 | 1 |
| konomi | 8 | 0 | 0 |
| melazmera | 2 | 0 | 0 |
| mielarah | 4 | 0 | 0 |
| minachiv (`minachiv/`) | 2 | 0 | 0 |
| minagho (`minagho/`, excl. the 9 shared `minachiv.*`) | 9 | 28 (canonical copies, duplicate-blocked) | 0 |
| nenio | 4 | 0 | 1 |
| nidalynn | 1 | 0 | 0 |
| nocticula | 15 | 0 | 0 |
| nurah | 13 | 0 | 0 |
| seelah | 7 | 0 | 0 |
| shamira | 5 | 0 | 0 |
| soana | 23 | 0 | 0 |
| targona | 5 | 0 | 0 |
| terendelev | 2 | 0 | 0 |
| vellexia | 3 | 0 | 0 |
| wenduag | 6 | 0 | 0 |
| yaniel | 1 | 0 | 0 |
| harem pairs (camellia_arueshalae, seelah_arueshalae warded, seelah_wenduag, wenduag_arueshalae / camellia_vellexia, jerribeth_vellexia, shamira_arueshalae, nocticula_shamira) | 4 | 4 | 0 |
| **Total (unique slots)** | **271** | **40 slots / 68 brief files** | **4** |

The 28 blocked `minagho_chivarro.*` slots are the same slots in both folders, so they
count once in the total. Ready means no hard lint finding against the current export.
It is not editorial approval: every candidate still needs voice and continuity review.
Ready slots marked `terminal: review last_line` have no next-node boundary.

## Coordinator decisions needed

1. **`minagho_chivarro.*` duplicates (28 slots, 56 findings).** The canonical copy is
   `minagho/`. Each of its briefs names the exact predecessor node now in the export
   (`threshold`, `threshold_clean`, `stance_N_night_*`, `came`, `night`, `pair` or `waiting`).
   It also names the right woman for that night. Several `chivarro/` copies describe a
   swapped or stale host. For example, `after.*.explicit.2` is now Minagho's secret night,
   but the `chivarro/` brief describes Chivarro's. The same problem affects
   `after.*.explicit.3`, `alone.chivarro.explicit.2` and `epilogue.commit.explicit.3`-`.5`.
   The `chivarro/` copies cannot simply be deleted, because they are build inputs:
   `storylines/chivarro_setpieces.py` reads their `source_nodes`, `default_text` and `speakers`.
   The current slot text matches the `chivarro/` `default_text` in 8 of the 28 slots, the
   `minagho/` one in 11, and neither in 9. Resolving this needs a builder change and a
   rebuild, which is out of scope for a briefs-only job. Choose one of two options:
   - Make `minagho/` the single source. Repoint `chivarro_setpieces.py` and remove the mirrors.
   - Add a lint-recognised "build mirror" marker.
2. **Epilogue narration vs second-person hosts (16 findings).** These are
   `areelu.trickster.finale.*` / `report.*` (8, owner `Epilogue`) and
   `minagho_chivarro.trickster.epilogue.commit.explicit.3`-`.5`. Their host and boundary
   prose is second-person present ("She draws you onto the bed"). The lint requires
   `third-past`, which would make Gemory write third person into a second-person boundary.
   Options:
   - Re-tense the host prose.
   - Let the lint accept second-present when the host is second person.

   The existing precedent is inconsistent: `iomedae.trickster.epilogue.platform` passes with
   `third-past` on a second-person host.
3. **Test-pinned boundaries.** `tests/test_areelu_round2.py:42` requires areelu
   `last_line == "N: " + default_text`, which is the old "slot default" convention.
   `tests/test_harem_row_s25.py:233` pins the `camellia_vellexia` `last_line`. Both conflict
   with the lint's next-beat boundary. The tests need updating before these briefs can be fixed.
4. **Reserved harem slots.** `camellia_vellexia` has a host, but its gate requires and forbids
   `household.pair.camellia_vellexia.ready`. `jerribeth_vellexia`, `shamira_arueshalae` and
   `nocticula_shamira` have no host scene and no successor. All four say they are blocked in
   their own `status`. They stay as debt until their structure owners build the hosts.
5. **Tense caveat.** `minagho/...epilogue.commit.explicit.1` is now `third-past`, but its
   boundary `went` is third-person present ("At dawn Chivarro retrieves the sword belt").
   It is still duplicate-blocked, so decide this together with item 2.

## Blocked slots

| Slot | Brief | Hard codes | Reason |
|---|---|---|---|
| `areelu.trickster.finale.ascended.explicit.1` | `areelu-vorlesh/areelu.trickster.finale.ascended.explicit.1.json` | last_line; narration | Epilogue-owned host written in second-person present; lint requires `narration: third-past` (decision). `last_line` is pinned to the slot's own default text by `tests/test_areelu_round2.py:42`, not to the next beat the lint requires (decision/test change). |
| `areelu.trickster.finale.company.explicit.1` | `areelu-vorlesh/areelu.trickster.finale.company.explicit.1.json` | last_line; narration | Epilogue-owned host written in second-person present; lint requires `narration: third-past` (decision). `last_line` is pinned to the slot's own default text by `tests/test_areelu_round2.py:42`, not to the next beat the lint requires (decision/test change). |
| `areelu.trickster.finale.company.explicit.2` | `areelu-vorlesh/areelu.trickster.finale.company.explicit.2.json` | last_line; narration | Epilogue-owned host written in second-person present; lint requires `narration: third-past` (decision). `last_line` is pinned to the slot's own default text by `tests/test_areelu_round2.py:42`, not to the next beat the lint requires (decision/test change). |
| `areelu.trickster.finale.lien_bottled.explicit.1` | `areelu-vorlesh/areelu.trickster.finale.lien_bottled.explicit.1.json` | last_line; narration | Epilogue-owned host written in second-person present; lint requires `narration: third-past` (decision). `last_line` is pinned to the slot's own default text by `tests/test_areelu_round2.py:42`, not to the next beat the lint requires (decision/test change). |
| `areelu.trickster.finale.not_burned.explicit.1` | `areelu-vorlesh/areelu.trickster.finale.not_burned.explicit.1.json` | last_line; narration | Epilogue-owned host written in second-person present; lint requires `narration: third-past` (decision). `last_line` is pinned to the slot's own default text by `tests/test_areelu_round2.py:42`, not to the next beat the lint requires (decision/test change). |
| `areelu.trickster.report.inn.explicit.1` | `areelu-vorlesh/areelu.trickster.report.inn.explicit.1.json` | last_line; narration | Epilogue-owned host written in second-person present; lint requires `narration: third-past` (decision). `last_line` is pinned to the slot's own default text by `tests/test_areelu_round2.py:42`, not to the next beat the lint requires (decision/test change). |
| `areelu.trickster.report.participation.explicit.1` | `areelu-vorlesh/areelu.trickster.report.participation.explicit.1.json` | last_line; narration | Epilogue-owned host written in second-person present; lint requires `narration: third-past` (decision). `last_line` is pinned to the slot's own default text by `tests/test_areelu_round2.py:42`, not to the next beat the lint requires (decision/test change). |
| `areelu.trickster.report.participation.explicit.2` | `areelu-vorlesh/areelu.trickster.report.participation.explicit.2.json` | last_line; narration | Epilogue-owned host written in second-person present; lint requires `narration: third-past` (decision). `last_line` is pinned to the slot's own default text by `tests/test_areelu_round2.py:42`, not to the next beat the lint requires (decision/test change). |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.1` | `chivarro/minagho_chivarro.trickster.after.before_the_last_road.explicit.1.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.2` | `chivarro/minagho_chivarro.trickster.after.before_the_last_road.explicit.2.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.3` | `chivarro/minagho_chivarro.trickster.after.before_the_last_road.explicit.3.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.1` | `chivarro/minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.1.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.2` | `chivarro/minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.2.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.3` | `chivarro/minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.3.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.1` | `chivarro/minagho_chivarro.trickster.after.when_it_scars.explicit.1.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.2` | `chivarro/minagho_chivarro.trickster.after.when_it_scars.explicit.2.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.3` | `chivarro/minagho_chivarro.trickster.after.when_it_scars.explicit.3.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.chivarro.explicit.1` | `chivarro/minagho_chivarro.trickster.alone.chivarro.explicit.1.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.chivarro.explicit.2` | `chivarro/minagho_chivarro.trickster.alone.chivarro.explicit.2.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.chivarro_letter.explicit.1` | `chivarro/minagho_chivarro.trickster.alone.chivarro_letter.explicit.1.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.chivarro_letter.explicit.2` | `chivarro/minagho_chivarro.trickster.alone.chivarro_letter.explicit.2.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.1` | `chivarro/minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.1.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.2` | `chivarro/minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.2.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.minagho.explicit.1` | `chivarro/minagho_chivarro.trickster.alone.minagho.explicit.1.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.minagho.explicit.2` | `chivarro/minagho_chivarro.trickster.alone.minagho.explicit.2.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.1` | `chivarro/minagho_chivarro.trickster.alone.minagho_letter.explicit.1.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.2` | `chivarro/minagho_chivarro.trickster.alone.minagho_letter.explicit.2.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.minagho_spared.explicit.1` | `chivarro/minagho_chivarro.trickster.alone.minagho_spared.explicit.1.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.minagho_spared.explicit.2` | `chivarro/minagho_chivarro.trickster.alone.minagho_spared.explicit.2.json` | duplicate | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.1` | `chivarro/minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.1.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.2` | `chivarro/minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.2.json` | duplicate; last_line | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.epilogue.commit.explicit.1` | `chivarro/minagho_chivarro.trickster.epilogue.commit.explicit.1.json` | duplicate; last_line; narration | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line; narration). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.epilogue.commit.explicit.2` | `chivarro/minagho_chivarro.trickster.epilogue.commit.explicit.2.json` | duplicate; last_line; narration | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line; narration). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.epilogue.commit.explicit.3` | `chivarro/minagho_chivarro.trickster.epilogue.commit.explicit.3.json` | duplicate; last_line; narration | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line; narration). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.epilogue.commit.explicit.4` | `chivarro/minagho_chivarro.trickster.epilogue.commit.explicit.4.json` | duplicate; last_line; narration | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line; narration). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `minagho_chivarro.trickster.epilogue.commit.explicit.5` | `chivarro/minagho_chivarro.trickster.epilogue.commit.explicit.5.json` | duplicate; last_line; narration | Divergent duplicate of the `minagho/` copy; stale mapping (codes: duplicate; last_line; narration). Kept because `storylines/chivarro_setpieces.py` builds from it. |
| `household.pair.camellia_vellexia.choice.explicit.1` | `harem/household.pair.camellia_vellexia.choice.explicit.1.json` | last_line; retired | Host now addressed (`host_scene`/`host_node: explicit.1`), but the host scene requires and forbids `household.pair.camellia_vellexia.ready` (reserved, unreachable by design; brief `status: blocked`). `last_line` is pinned by `tests/test_harem_row_s25.py:233`. |
| `household.pair.jerribeth_vellexia.choice.explicit.1` | `harem/household.pair.jerribeth_vellexia.choice.explicit.1.json` | host | No `household.pair.jerribeth_vellexia.choice` scene in the export, and no successor. The brief's own `status`/`build_contract` say it is a blocked reservation. |
| `household.pair.nocticula_shamira.return.explicit.1` | `harem/blocked/nocticula_shamira/household.pair.nocticula_shamira.return.explicit.1.json` | host; required | No host scene (only `precedence`/`precedence.live`) and no `example`. The brief is already under `harem/blocked/`. |
| `household.pair.shamira_arueshalae.choice.explicit.1` | `harem/household.pair.shamira_arueshalae.choice.explicit.1.json` | host | No `household.pair.shamira_arueshalae.choice` scene in the export, and no successor. The brief is a self-declared reserved/blocked slot. |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.1` | `minagho/minagho_chivarro.trickster.after.before_the_last_road.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.2` | `minagho/minagho_chivarro.trickster.after.before_the_last_road.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.3` | `minagho/minagho_chivarro.trickster.after.before_the_last_road.explicit.3.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.1` | `minagho/minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.2` | `minagho/minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.3` | `minagho/minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.3.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.1` | `minagho/minagho_chivarro.trickster.after.when_it_scars.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.2` | `minagho/minagho_chivarro.trickster.after.when_it_scars.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.3` | `minagho/minagho_chivarro.trickster.after.when_it_scars.explicit.3.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.chivarro.explicit.1` | `minagho/minagho_chivarro.trickster.alone.chivarro.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.chivarro.explicit.2` | `minagho/minagho_chivarro.trickster.alone.chivarro.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.chivarro_letter.explicit.1` | `minagho/minagho_chivarro.trickster.alone.chivarro_letter.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.chivarro_letter.explicit.2` | `minagho/minagho_chivarro.trickster.alone.chivarro_letter.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.1` | `minagho/minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.2` | `minagho/minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.minagho.explicit.1` | `minagho/minagho_chivarro.trickster.alone.minagho.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.minagho.explicit.2` | `minagho/minagho_chivarro.trickster.alone.minagho.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.1` | `minagho/minagho_chivarro.trickster.alone.minagho_letter.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.2` | `minagho/minagho_chivarro.trickster.alone.minagho_letter.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.minagho_spared.explicit.1` | `minagho/minagho_chivarro.trickster.alone.minagho_spared.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.minagho_spared.explicit.2` | `minagho/minagho_chivarro.trickster.alone.minagho_spared.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.1` | `minagho/minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.2` | `minagho/minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.epilogue.commit.explicit.1` | `minagho/minagho_chivarro.trickster.epilogue.commit.explicit.1.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.epilogue.commit.explicit.2` | `minagho/minagho_chivarro.trickster.epilogue.commit.explicit.2.json` | duplicate | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. |
| `minagho_chivarro.trickster.epilogue.commit.explicit.3` | `minagho/minagho_chivarro.trickster.epilogue.commit.explicit.3.json` | duplicate; narration | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. Also: Epilogue host is second-person, so `third-past` would contradict the host and boundary (decision). |
| `minagho_chivarro.trickster.epilogue.commit.explicit.4` | `minagho/minagho_chivarro.trickster.epilogue.commit.explicit.4.json` | duplicate; narration | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. Also: Epilogue host is second-person, so `third-past` would contradict the host and boundary (decision). |
| `minagho_chivarro.trickster.epilogue.commit.explicit.5` | `minagho/minagho_chivarro.trickster.epilogue.commit.explicit.5.json` | duplicate; narration | Canonical copy (host mapping matches the current export); still blocked only by the divergent `chivarro/` duplicate. Also: Epilogue host is second-person, so `third-past` would contradict the host and boundary (decision). |

## Ready slots: exact hosts

For each ready slot: the host scene; the slot node, or the host node for inline briefs;
and the node(s) that must carry the heated build-up to the start of the act (HEAT,
Directive 12: graphic where it fits the character; the situation, build-up and aftermath
carry the drama). A prose writer extends the build-up node(s) up to the act boundary.
The slot node holds the act (Gemory fill); its exits are the retained continuation.
Inline briefs (`after_text`) put the act inside the host node, after the anchor.
"Paragraph" hosts put it after that paragraph of the host node.

### anevia

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `a_crossing.explicit.1` | `a_crossing` | slot node `a_crossing.explicit.1` | `round2.buildup.night` | `night` |
| `anevia.a_key_that_is_hers.explicit.1` | `anevia.a_key_that_is_hers` | slot node `anevia.a_key_that_is_hers.explicit.1` | `round2.buildup.night` | `night` |
| `anevia.a_key_that_is_hers.explicit.2` | `anevia.a_key_that_is_hers` | slot node `anevia.a_key_that_is_hers.explicit.2` | `round2.buildup.partner_secret_night` | `partner_secret_night` |
| `anevia.a_key_that_is_hers.explicit.3` | `anevia.a_key_that_is_hers` | slot node `anevia.a_key_that_is_hers.explicit.3` | `round2.buildup.partner_absent_night` | `partner_absent_night` |
| `anevia.the_evening_without_a_case.explicit.1` | `anevia.the_evening_without_a_case` | slot node `anevia.the_evening_without_a_case.explicit.1` | `round2.buildup.night` | `night` |
| `anevia.trickster.gone.commit.explicit.1` | `anevia.trickster.gone.commit` | slot node `anevia.trickster.gone.commit.explicit.1` | `round2.buildup.threshold` | `threshold` |
| `anevia.trickster.gone.commit.explicit.2` | `anevia.trickster.gone.commit` | slot node `anevia.trickster.gone.commit.explicit.2` | `round2.buildup.partner_answer_1_secret_night` | `partner_answer_1_secret_night` |
| `anevia.trickster.gone.commit.explicit.3` | `anevia.trickster.gone.commit` | slot node `anevia.trickster.gone.commit.explicit.3` | `round2.buildup.partner_answer_1_absent_night` | `partner_answer_1_absent_night` |
| `anevia.trickster.gone.fetched_commit.explicit.1` | `anevia.trickster.gone.fetched_commit` | slot node `anevia.trickster.gone.fetched_commit.explicit.1` | `round2.buildup.threshold` | `threshold` |
| `anevia.trickster.gone.fetched_commit.explicit.2` | `anevia.trickster.gone.fetched_commit` | slot node `anevia.trickster.gone.fetched_commit.explicit.2` | `round2.buildup.partner_answer_1_secret_night` | `partner_answer_1_secret_night` |
| `anevia.trickster.gone.fetched_commit.explicit.3` | `anevia.trickster.gone.fetched_commit` | slot node `anevia.trickster.gone.fetched_commit.explicit.3` | `round2.buildup.partner_answer_1_absent_night` | `partner_answer_1_absent_night` |
| `anevia.trickster.gone.fetched_second_ask.explicit.1` | `anevia.trickster.gone.fetched_second_ask` | slot node `anevia.trickster.gone.fetched_second_ask.explicit.1` | `round2.buildup.night` | `night` |
| `anevia.trickster.gone.fetched_second_ask.explicit.2` | `anevia.trickster.gone.fetched_second_ask` | slot node `anevia.trickster.gone.fetched_second_ask.explicit.2` | `round2.buildup.partner_price_0_secret_night` | `partner_price_0_secret_night` |
| `anevia.trickster.gone.fetched_second_ask.explicit.3` | `anevia.trickster.gone.fetched_second_ask` | slot node `anevia.trickster.gone.fetched_second_ask.explicit.3` | `round2.buildup.partner_price_0_absent_night` | `partner_price_0_absent_night` |
| `anevia.trickster.gone.muster.explicit.1` | `anevia.trickster.gone.muster` | slot node `anevia.trickster.gone.muster.explicit.1` | `round2.buildup.threshold` | `threshold` |
| `anevia.trickster.gone.second_ask.explicit.1` | `anevia.trickster.gone.second_ask` | slot node `anevia.trickster.gone.second_ask.explicit.1` | `round2.buildup.night` | `night` |
| `anevia.trickster.gone.second_ask.explicit.2` | `anevia.trickster.gone.second_ask` | slot node `anevia.trickster.gone.second_ask.explicit.2` | `round2.buildup.partner_price_0_secret_night` | `partner_price_0_secret_night` |
| `anevia.trickster.gone.second_ask.explicit.3` | `anevia.trickster.gone.second_ask` | slot node `anevia.trickster.gone.second_ask.explicit.3` | `round2.buildup.partner_price_0_absent_night` | `partner_price_0_absent_night` |
| `three_open_road.explicit.1` | `three_open_road` | `night` (inline, after anchor) | `night` up to the anchor | `END` |
| `three_rooms_unlocked.explicit.1` | `three_rooms_unlocked` | `night` (inline, after anchor) | `night` up to the anchor | `morning` |

### aranka

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `aranka.no_encore_needed.explicit.1` | `aranka.no_encore_needed` | slot node `aranka.no_encore_needed.explicit.1` | `night_initiation` | `night` |
| `aranka.the_story_that_follows.explicit.1` | `aranka.the_story_that_follows` | slot node `aranka.the_story_that_follows.explicit.1` | `private` | `hollow_morning` |
| `aranka.trickster.epilogue.commit.explicit.1` | `aranka.trickster.epilogue.commit` | `end` paragraph `aranka.trickster.epilogue.commit.explicit.1` (#3) | `end` paragraphs 0..2 | `next paragraph` ; third-past |
| `aranka.trickster.verse.encore.explicit.1` | `aranka.trickster.verse.encore` | slot node `aranka.trickster.verse.encore.explicit.1` | `threshold` | `morning` |
| `aranka.trickster.verse.encore_late.explicit.1` | `aranka.trickster.verse.encore_late` | slot node `aranka.trickster.verse.encore_late.explicit.1` | `threshold` | `morning` |
| `aranka.trickster.verse.encore_yard.explicit.1` | `aranka.trickster.verse.encore_yard` | slot node `aranka.trickster.verse.encore_yard.explicit.1` | `threshold` | `morning` |
| `aranka.trickster.verse.encore_yard_late.explicit.1` | `aranka.trickster.verse.encore_yard_late` | slot node `aranka.trickster.verse.encore_yard_late.explicit.1` | `threshold` | `morning` |
| `aranka.trickster.verse.third_verse.explicit.1` | `aranka.trickster.verse.third_verse` | slot node `aranka.trickster.verse.third_verse.explicit.1` | `threshold` | `morning` |
| `aranka.trickster.verse.third_verse_late.explicit.1` | `aranka.trickster.verse.third_verse_late` | slot node `aranka.trickster.verse.third_verse_late.explicit.1` | `threshold` | `morning` |
| `aranka.trickster.verse.third_verse_yard.explicit.1` | `aranka.trickster.verse.third_verse_yard` | slot node `aranka.trickster.verse.third_verse_yard.explicit.1` | `threshold` | `morning` |
| `aranka.trickster.verse.third_verse_yard_late.explicit.1` | `aranka.trickster.verse.third_verse_yard_late` | slot node `aranka.trickster.verse.third_verse_yard_late.explicit.1` | `threshold` | `morning` |

### areelu

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `areelu.trickster.report.rooms.explicit.1` | `areelu.trickster.report.rooms` | host node `pen` | `pen` itself (after `hands`) | `end` ; third-past |

### arsinoe

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `arsinoe.trickster.cauldron.collection.explicit.1` | `arsinoe.trickster.cauldron.collection` | slot node `arsinoe.trickster.cauldron.collection.explicit.1` | `threshold`, `threshold_return` | `morning` |
| `arsinoe.trickster.late.commit.explicit.1` | `arsinoe.trickster.late.commit` | slot node `arsinoe.trickster.late.commit.explicit.1` | `night`, `late_return` | `morning` ; third-past |
| `arsinoe.trickster.late.commit.explicit.2` | `arsinoe.trickster.late.commit` | slot node `arsinoe.trickster.late.commit.explicit.2` | `deferred_evening` | `table` ; third-past |
| `arsinoe_the_unprofitable_hour.explicit.1` | `arsinoe_the_unprofitable_hour` | slot node `arsinoe_the_unprofitable_hour.explicit.1` | `kiss` | `private_morning` |
| `arsinoe_the_window_opens.explicit.1` | `arsinoe_the_window_opens` | slot node `arsinoe_the_window_opens.explicit.1` | `window_invitation`, `window_return` | `night` |

### arueshalae

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `arueshalae.treatment.night.explicit.1` | `arueshalae.treatment.night` | slot node `arueshalae.treatment.night.explicit.1` | `undress` | `morning_after_paid` |
| `arueshalae.treatment.night.explicit.2` | `arueshalae.treatment.night` | slot node `arueshalae.treatment.night.explicit.2` | `undress` | `morning_after` |
| `arueshalae.trickster.evil.window.explicit.1` | `arueshalae.trickster.evil.window` | slot node `arueshalae.trickster.evil.window.explicit.1` | `cut` | `after` |
| `arueshalae.trickster.evil.window_yard.explicit.1` | `arueshalae.trickster.evil.window_yard` | slot node `arueshalae.trickster.evil.window_yard.explicit.1` | `cut` | `after` |
| `arueshalae.trickster.fallen.roof.explicit.1` | `arueshalae.trickster.fallen.roof` | slot node `arueshalae.trickster.fallen.roof.explicit.1` | `cut` | `after` |

### camellia

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `camellia.trickster.bond.not_today.explicit.1` | `camellia.trickster.bond.not_today` | slot node `camellia.trickster.bond.not_today.explicit.1` | `night` | `morning.not_today` ; male mention (background) |
| `camellia.trickster.bond.not_today_alive.explicit.1` | `camellia.trickster.bond.not_today_alive` | slot node `camellia.trickster.bond.not_today_alive.explicit.1` | `night` | `morning.not_today` ; male mention (background) |
| `camellia.trickster.bond.not_today_camp.explicit.1` | `camellia.trickster.bond.not_today_camp` | slot node `camellia.trickster.bond.not_today_camp.explicit.1` | `night` | `morning.not_today` ; male mention (background) |
| `camellia.trickster.bond.witness.explicit.1` | `camellia.trickster.bond.witness` | host node `hers` | `hers` itself (after `choice`) | `END` ; terminal: review last_line |
| `camellia.trickster.cards.the_deck_again.explicit.1` | `camellia.trickster.cards.the_deck_again` | slot node `camellia.trickster.cards.the_deck_again.explicit.1` | `silk` | `close` ; male mention (background) |
| `camellia.trickster.cards.the_deck_again_alive.explicit.1` | `camellia.trickster.cards.the_deck_again_alive` | slot node `camellia.trickster.cards.the_deck_again_alive.explicit.1` | `silk` | `close` ; male mention (background) |
| `camellia.trickster.cards.the_deck_again_camp.explicit.1` | `camellia.trickster.cards.the_deck_again_camp` | slot node `camellia.trickster.cards.the_deck_again_camp.explicit.1` | `silk` | `close` ; male mention (background) |
| `camellia.trickster.cards.two_lies_again.explicit.1` | `camellia.trickster.cards.two_lies_again` | slot node `camellia.trickster.cards.two_lies_again.explicit.1` | `all` | `morning.all` ; male mention (background) |
| `camellia.trickster.cards.two_lies_again.explicit.2` | `camellia.trickster.cards.two_lies_again` | slot node `camellia.trickster.cards.two_lies_again.explicit.2` | `mine` | `morning.mine` ; male mention (background) |
| `camellia.trickster.cards.two_lies_again_alive.explicit.1` | `camellia.trickster.cards.two_lies_again_alive` | slot node `camellia.trickster.cards.two_lies_again_alive.explicit.1` | `all` | `morning.all` ; male mention (background) |
| `camellia.trickster.cards.two_lies_again_alive.explicit.2` | `camellia.trickster.cards.two_lies_again_alive` | slot node `camellia.trickster.cards.two_lies_again_alive.explicit.2` | `mine` | `morning.mine` ; male mention (background) |
| `camellia.trickster.cards.two_lies_again_camp.explicit.1` | `camellia.trickster.cards.two_lies_again_camp` | slot node `camellia.trickster.cards.two_lies_again_camp.explicit.1` | `all` | `morning.all` ; male mention (background) |
| `camellia.trickster.cards.two_lies_again_camp.explicit.2` | `camellia.trickster.cards.two_lies_again_camp` | slot node `camellia.trickster.cards.two_lies_again_camp.explicit.2` | `mine` | `morning.mine` ; male mention (background) |
| `camellia.trickster.day.the_second_dance.explicit.1` | `camellia.trickster.day.the_second_dance` | slot node `camellia.trickster.day.the_second_dance.explicit.1` | `strap` | `end` ; male mention (background) |
| `camellia.trickster.day.the_second_dance.explicit.2` | `camellia.trickster.day.the_second_dance` | slot node `camellia.trickster.day.the_second_dance.explicit.2` | `leave` | `end` ; male mention (background) |
| `camellia.trickster.day.the_second_dance_alive.explicit.1` | `camellia.trickster.day.the_second_dance_alive` | slot node `camellia.trickster.day.the_second_dance_alive.explicit.1` | `strap` | `end` ; male mention (background) |
| `camellia.trickster.day.the_second_dance_alive.explicit.2` | `camellia.trickster.day.the_second_dance_alive` | slot node `camellia.trickster.day.the_second_dance_alive.explicit.2` | `leave` | `end` ; male mention (background) |
| `camellia.trickster.day.the_second_dance_camp.explicit.1` | `camellia.trickster.day.the_second_dance_camp` | slot node `camellia.trickster.day.the_second_dance_camp.explicit.1` | `strap` | `end` ; male mention (background) |
| `camellia.trickster.day.the_second_dance_camp.explicit.2` | `camellia.trickster.day.the_second_dance_camp` | slot node `camellia.trickster.day.the_second_dance_camp.explicit.2` | `leave` | `end` ; male mention (background) |
| `camellia.trickster.evening.the_prisoner.explicit.1` | `camellia.trickster.evening.the_prisoner` | host node `watch` | `watch` itself (after `ask`) | `END` ; terminal: review last_line |
| `camellia.trickster.returned.test.explicit.1` | `camellia.trickster.returned.test` | slot node `camellia.trickster.returned.test.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `camellia.trickster.returned.test_alive.explicit.1` | `camellia.trickster.returned.test_alive` | slot node `camellia.trickster.returned.test_alive.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `camellia.trickster.returned.test_camp.explicit.1` | `camellia.trickster.returned.test_camp` | slot node `camellia.trickster.returned.test_camp.explicit.1` | `threshold` | `morning` ; male mention (background) |

### chadali

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `chadali.fortunes.honey.explicit.1` | `chadali.fortunes.honey` | slot node `chadali.fortunes.honey.explicit.1` | `look` | `cut` |
| `chadali.sessions.what_chance_wishes.explicit.1` | `chadali.sessions.what_chance_wishes` | slot node `chadali.sessions.what_chance_wishes.explicit.1` | `stay` | `END` ; terminal: review last_line |
| `chadali.trickster.epilogue.commit.explicit.1` | `chadali.trickster.epilogue.commit` | slot node `chadali.trickster.epilogue.commit.explicit.1` | `page` | `stay` ; third-past |

### chivarro

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `minachiv.a_room_she_likes.explicit.1` (identical copy also in minagho/) | `minachiv.a_room_she_likes` | slot node `minachiv.a_room_she_likes.explicit.1` | `later` | `END` ; terminal: review last_line |
| `minachiv.after_the_last_lamp.explicit.1` (identical copy also in minagho/) | `minachiv.after_the_last_lamp` | slot node `minachiv.after_the_last_lamp.explicit.1` | `night` | `END` ; terminal: review last_line |
| `minachiv.before_the_last_road.explicit.1` (identical copy also in minagho/) | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.1` | `stance_0_night_minagho` | `stance_discovery_0_minagho` |
| `minachiv.before_the_last_road.explicit.2` (identical copy also in minagho/) | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.2` | `stance_0_night_chivarro` | `stance_discovery_0_chivarro` |
| `minachiv.before_the_last_road.explicit.3` (identical copy also in minagho/) | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.3` | `stance_1_night_minagho` | `stance_discovery_1_minagho` |
| `minachiv.before_the_last_road.explicit.4` (identical copy also in minagho/) | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.4` | `stance_2_night_minagho` | `stance_discovery_2_minagho` |
| `minachiv.the_unhired_evening.explicit.1` (identical copy also in minagho/) | `minachiv.the_unhired_evening` | slot node `minachiv.the_unhired_evening.explicit.1` | `minagho_kiss` | `END` ; terminal: review last_line |
| `minachiv.the_unhired_evening.explicit.2` (identical copy also in minagho/) | `minachiv.the_unhired_evening` | slot node `minachiv.the_unhired_evening.explicit.2` | `chivarro_kiss` | `END` ; terminal: review last_line |
| `minachiv.the_unhired_evening.explicit.3` (identical copy also in minagho/) | `minachiv.the_unhired_evening` | slot node `minachiv.the_unhired_evening.explicit.3` | `together_kiss` | `END` ; terminal: review last_line |

### delamere

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `delamere.trickster.epilogue.late.explicit.1` | `delamere.trickster.epilogue.late` | `page` paragraph `delamere.trickster.epilogue.late.explicit.1` (#0) | (scene start) | `next paragraph` ; third-past; male mention (background) |
| `delamere.trickster.woken.day_owed.explicit.1` | `delamere.trickster.woken.day_owed` | host node `again` | `again` itself (after `caught_again`, `caught_again_short`) | `cold` |
| `delamere.trickster.woods.second_hunt.explicit.1` | `delamere.trickster.woods.second_hunt` | slot node `delamere.trickster.woods.second_hunt.explicit.1` | `cut` | `morning` ; male mention (background) |
| `delamere.trickster.woods.second_hunt_late.explicit.1` | `delamere.trickster.woods.second_hunt_late` | slot node `delamere.trickster.woods.second_hunt_late.explicit.1` | `cut` | `morning` ; male mention (background) |
| `delamere.trickster.woods.second_hunt_page.explicit.1` | `delamere.trickster.woods.second_hunt_page` | slot node `delamere.trickster.woods.second_hunt_page.explicit.1` | `cut` | `morning` ; male mention (background) |

### devarra

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `devarra.tower.before_the_end.explicit.1` | `devarra.tower.before_the_end` | host node `owe_free` | `owe_free` itself (after `climb`) | `end_her` |
| `devarra.tower.first_bite.explicit.1` | `devarra.tower.first_bite` | slot node `devarra.tower.first_bite.explicit.1` | `bite`, `bite_free` | `morning` ; male mention (background) |
| `devarra.tower.under_the_wing.explicit.1` | `devarra.tower.under_the_wing` | host node `why` | `why` itself (after `her`) | `sleep` |
| `devarra.trickster.epilogue.commit.explicit.1` | `devarra.trickster.epilogue.commit` | `late_accepted` (inline, after anchor) | `late_accepted` up to the anchor | `page_exit` ; third-past |
| `devarra.trickster.epilogue.woken.explicit.1` | `devarra.trickster.epilogue.woken` | `page` paragraph `devarra.trickster.epilogue.woken.explicit.1` (#23) | `page` paragraphs 0..22 | `next paragraph` ; third-past; male mention (background) |

### dorgelinda

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `dorgelinda.ledger.after_hours.explicit.1` | `dorgelinda.ledger.after_hours` | slot node `dorgelinda.ledger.after_hours.explicit.1` | `threshold` | `END` ; terminal: review last_line |

### eliandra

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `eliandra.trickster.epilogue.late.explicit.1` | `eliandra.trickster.epilogue.late` | `late_accepted` paragraph `eliandra.trickster.epilogue.late.explicit.1` (#0) | `page` | `next paragraph` ; third-past |
| `eliandra.trickster.epilogue.together.explicit.1` | `eliandra.trickster.epilogue.together` | `page` paragraph `eliandra.trickster.epilogue.together.explicit.1` (#2) | `page` paragraphs 0..1 | `next paragraph` ; third-past |
| `eliandra.trickster.epilogue.unasked.explicit.1` | `eliandra.trickster.epilogue.unasked` | `late_accepted` paragraph `eliandra.trickster.epilogue.unasked.explicit.1` (#1) | `late_accepted` paragraphs 0..0 | `next paragraph` ; third-past; male mention (background) |
| `eliandra.trickster.visit.star_heart.explicit.1` | `eliandra.trickster.visit.star_heart` | slot node `eliandra.trickster.visit.star_heart.explicit.1` | `charts` | `morning` |
| `eliandra.trickster.visit.star_heart_mark.explicit.1` | `eliandra.trickster.visit.star_heart_mark` | slot node `eliandra.trickster.visit.star_heart_mark.explicit.1` | `charts` | `morning` |

### elyanka

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `elyanka.trickster.beat.table.explicit.1` | `elyanka.trickster.beat.table` | host node `door2` | `door2` itself (after `door`) | `END` ; terminal: review last_line |
| `elyanka.trickster.ch6.collateral.explicit.1` | `elyanka.trickster.ch6.collateral` | host node `rift2` | `rift2` itself (after `rift`) | `END` ; terminal: review last_line |
| `elyanka.trickster.epilogue.claim.explicit.1` | `elyanka.trickster.epilogue.claim` | `page` (inline, after anchor) | `page` up to the anchor | `END` ; third-past |
| `elyanka.trickster.visit.hearse.explicit.1` | `elyanka.trickster.visit.hearse` | slot node `elyanka.trickster.visit.hearse.explicit.1` | `threshold` | `morning` |

### eritrice

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `eritrice.council.twice_nightly.explicit.1` | `eritrice.council.twice_nightly` | slot node `eritrice.council.twice_nightly.explicit.1` | `carried` | `END` ; terminal: review last_line |
| `eritrice.minutes.adjourned.explicit.1` | `eritrice.minutes.adjourned` | slot node `eritrice.minutes.adjourned.explicit.1` | `cut` | `END` ; terminal: review last_line |
| `eritrice.trickster.epilogue.commit.explicit.1` | `eritrice.trickster.epilogue.commit` | `aye` paragraph `eritrice.trickster.epilogue.commit.explicit.1` (#0) | `page` | `next paragraph` ; third-past |

### galfrey

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `galfrey.trickster.alive.after_no.explicit.1` | `galfrey.trickster.alive.after_no` | slot node `galfrey.trickster.alive.after_no.explicit.1` | `threshold` | `morning` |
| `galfrey.trickster.alive.oath.explicit.1` | `galfrey.trickster.alive.oath` | slot node `galfrey.trickster.alive.oath.explicit.1` | `threshold` | `morning` |
| `galfrey.trickster.visit.tent.explicit.1` | `galfrey.trickster.visit.tent` | slot node `galfrey.trickster.visit.tent.explicit.1` | `cut` | `after` |
| `galfrey.trickster.visit.tent_stall.explicit.1` | `galfrey.trickster.visit.tent_stall` | slot node `galfrey.trickster.visit.tent_stall.explicit.1` | `cut` | `after` |

### gesmerha

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `gesmerha.the_room_she_chose.explicit.1` | `gesmerha.the_room_she_chose` | slot node `gesmerha.the_room_she_chose.explicit.1` | `lover` | `after_night`, `night` ; male mention (background) |
| `gesmerha.the_room_she_chose.explicit.2` | `gesmerha.the_room_she_chose` | slot node `gesmerha.the_room_she_chose.explicit.2` | `first_kiss` | `after_first_night`, `first_night` ; male mention (background) |
| `gesmerha.trickster.returned.bench.explicit.1` | `gesmerha.trickster.returned.bench` | slot node `gesmerha.trickster.returned.bench.explicit.1` | `terms` | `morning`, `night` ; male mention (background) |
| `gesmerha.trickster.returned.second_ask.explicit.1` | `gesmerha.trickster.returned.second_ask` | slot node `gesmerha.trickster.returned.second_ask.explicit.1` | `sat` | `morning`, `night` ; male mention (background) |
| `gesmerha.trickster.returned.second_ask.explicit.2` | `gesmerha.trickster.returned.second_ask` | slot node `gesmerha.trickster.returned.second_ask.explicit.2` | `sat` | `morning`, `night_flinched` ; male mention (background) |
| `gesmerha.what_she_asks.explicit.1` | `gesmerha.what_she_asks` | slot node `gesmerha.what_she_asks.explicit.1` | `touch` | `after_private`, `private` ; male mention (background) |

### harem: camellia_arueshalae

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `household.pair.camellia_arueshalae.choice.explicit.1` | `household.pair.camellia_arueshalae.choice` | slot node `household.pair.camellia_arueshalae.choice.explicit.1` | `cut` | `kept_warded` |

### harem: seelah_arueshalae

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `household.pair.seelah_arueshalae.choice.explicit.1.warded` | `household.pair.seelah_arueshalae.choice` | host node `explicit.1.warded` | `explicit.1.warded` itself (after `cut_warded`) | `kept_warded` |

### harem: seelah_wenduag

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `household.pair.seelah_wenduag.choice.explicit.1` | `household.pair.seelah_wenduag.choice` | slot node `household.pair.seelah_wenduag.choice.explicit.1` | `wenduag_yes` | `held` ; male mention (background) |

### harem: wenduag_arueshalae

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `household.pair.wenduag_arueshalae.choice.explicit.1` | `household.pair.wenduag_arueshalae.choice` | slot node `household.pair.wenduag_arueshalae.choice.explicit.1` | `threshold` | `after` |

### hepzamirah

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `hepzamirah.trickster.body.terms.explicit.1` | `hepzamirah.trickster.body.terms` | slot node `hepzamirah.trickster.body.terms.explicit.1` | `threshold` | `END` ; terminal: review last_line; male mention (background) |
| `hepzamirah.trickster.bond.crooked.explicit.1` | `hepzamirah.trickster.bond.crooked` | slot node `hepzamirah.trickster.bond.crooked.explicit.1` | `down` | `END` ; terminal: review last_line; male mention (background) |
| `hepzamirah.trickster.bond.eve.explicit.1` | `hepzamirah.trickster.bond.eve` | host node `face_say` | `face_say` itself (after `face`) | `last` |
| `hepzamirah.trickster.bond.gift.explicit.1` | `hepzamirah.trickster.bond.gift` | host node `kiss` | `kiss` itself (after `speech`) | `kiss_say` |
| `hepzamirah.trickster.bond.her_room.explicit.1` | `hepzamirah.trickster.bond.her_room` | host node `sit_say` | `sit_say` itself (after `sit`) | `END` ; terminal: review last_line |

### herrax

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `herrax.house.a_night_out.explicit.1` | `herrax.house.a_night_out` | host node `home` | `home` itself (after `small`, `big`) | `END` ; terminal: review last_line |
| `herrax.house.her_rooms.explicit.1` | `herrax.house.her_rooms` | host node `beside` | `beside` itself (after `expected`, `chest`) | `END` ; terminal: review last_line |
| `herrax.house.last_night.explicit.1` | `herrax.house.last_night` | host node `agreed` | `agreed` itself (after `say`, `dead`) | `END` ; terminal: review last_line |
| `herrax.house.the_stairs.explicit.1` | `herrax.house.the_stairs` | slot node `herrax.house.the_stairs.explicit.1` | `close`, `find` | `return_morning` |
| `herrax.trickster.epilogue.after_hours.explicit.1` | `herrax.trickster.epilogue.after_hours.invitation` | slot node `herrax.trickster.epilogue.after_hours.explicit.1` | `desire` | `morning` ; third-past; male mention (background) |
| `herrax.trickster.madam.reachable.explicit.1` | `herrax.trickster.madam.reachable` | slot node `herrax.trickster.madam.reachable.explicit.1` | `cut` | `morning` ; male mention (background) |
| `herrax.trickster.madam.reachable_restored.explicit.1` | `herrax.trickster.madam.reachable_restored` | slot node `herrax.trickster.madam.reachable_restored.explicit.1` | `cut` | `morning` |

### horzalah

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `horzalah.trickster.beat.ramparts.explicit.1` | `horzalah.trickster.beat.ramparts` | host node `hand` | `hand` itself (after `end`) | `END` ; terminal: review last_line |
| `horzalah.trickster.beat.ribbon.explicit.1` | `horzalah.trickster.beat.ribbon` | host node `tied` | `tied` itself (after `tie`) | `END` ; terminal: review last_line |
| `horzalah.trickster.beat.second_night.explicit.1` | `horzalah.trickster.beat.second_night` | slot node `horzalah.trickster.beat.second_night.explicit.1` | `cut` | `after` ; male mention (background) |
| `horzalah.trickster.epilogue.commit.explicit.1` | `horzalah.trickster.epilogue.commit` | `page` paragraph `horzalah.trickster.epilogue.commit.explicit.1` (#8) | `page` paragraphs 0..7 | `next paragraph` ; third-past; male mention (background) |
| `horzalah.trickster.epilogue.decided.explicit.1` | `horzalah.trickster.epilogue.decided` | host node `page` | `page` itself | `END` ; terminal: review last_line; third-past |
| `horzalah.trickster.epilogue.together.explicit.1` | `horzalah.trickster.epilogue.together` | `page` paragraph `horzalah.trickster.epilogue.together.explicit.1` (#14) | `page` paragraphs 0..13 | `next paragraph` ; third-past; male mention (background) |
| `horzalah.trickster.visit.chamber.explicit.1` | `horzalah.trickster.visit.chamber` | slot node `horzalah.trickster.visit.chamber.explicit.1` | `cut`, `cut_tonight` | `morning` ; male mention (background) |

### iomedae

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `iomedae.trickster.epilogue.after.explicit.1` | `iomedae.trickster.epilogue.after` | slot node `iomedae.trickster.epilogue.after.explicit.1` | `page` | `vigil_morning` ; third-past |
| `iomedae.trickster.epilogue.platform.explicit.1` | `iomedae.trickster.epilogue.platform` | slot node `iomedae.trickster.epilogue.platform.explicit.1` | `down` | `morning_dead`, `morning_kept`, `morning_open` ; third-past |

### irabeth

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `i_crossing.explicit.1` | `i_crossing` | slot node `i_crossing.explicit.1` | `night` | `i_crossing.after_explicit.1` ; male mention (background) |
| `irabeth.a_road_she_would_choose.explicit.1` | `irabeth.a_road_she_would_choose` | slot node `irabeth.a_road_she_would_choose.explicit.1` | `partner_lasting_0_night` | `partner_lasting_0_morning` ; male mention (background) |
| `irabeth.the_hour_before_battle.explicit.1` | `irabeth.the_hour_before_battle` | slot node `irabeth.the_hour_before_battle.explicit.1` | `night` | `irabeth.the_hour_before_battle.after_explicit.1` ; male mention (background) |
| `irabeth.trickster.commit.explicit.1` | `irabeth.trickster.commit` | slot node `irabeth.trickster.commit.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `irabeth.trickster.commit.explicit.2` | `irabeth.trickster.commit` | slot node `irabeth.trickster.commit.explicit.2` | `threshold_blow` | `morning` ; male mention (background) |
| `irabeth.trickster.nevi_reply.explicit.1` | `irabeth.trickster.nevi_reply` | slot node `irabeth.trickster.nevi_reply.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `irabeth.trickster.nevi_reply.explicit.2` | `irabeth.trickster.nevi_reply` | slot node `irabeth.trickster.nevi_reply.explicit.2` | `threshold_blow` | `morning` ; male mention (background) |
| `irabeth.trickster.second_ask.explicit.1` | `irabeth.trickster.second_ask` | slot node `irabeth.trickster.second_ask.explicit.1` | `threshold` | `morning`, `morning_home`, `morning_house` ; male mention (background) |
| `irabeth.trickster.second_ask.explicit.2` | `irabeth.trickster.second_ask` | slot node `irabeth.trickster.second_ask.explicit.2` | `threshold_blow` | `morning`, `morning_home`, `morning_house` ; male mention (background) |
| `irabeth.without_an_account.explicit.1` | `irabeth.without_an_account` | slot node `irabeth.without_an_account.explicit.1` | `private` | `irabeth.without_an_account.after_explicit.1` ; male mention (background) |

### jannah

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `jannah.circle.eyes_open.explicit.1` | `jannah.circle.eyes_open` | slot node `jannah.circle.eyes_open.explicit.1` | `still`, `moved` | `future` |
| `jannah.trickster.circle_night.explicit.1` | `jannah.trickster.circle_night` | slot node `jannah.trickster.circle_night.explicit.1` | `cut` | `END` ; terminal: review last_line |

### jerribeth

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `jerribeth.future.explicit.1` | `jerribeth.future` | slot node `jerribeth.future.explicit.1` | `tenant_pinned` | `tenant_morning` ; male mention (background) |
| `jerribeth.future.explicit.2` | `jerribeth.future` | slot node `jerribeth.future.explicit.2` | `tenant_free` | `tenant_morning_free` ; male mention (background) |
| `jerribeth.room_measure.explicit.1` | `jerribeth.room_measure` | slot node `jerribeth.room_measure.explicit.1` | `desire` | `end` ; male mention (background) |
| `jerribeth.trickster.epilogue.commit.explicit.1` | `jerribeth.trickster.epilogue.commit` | slot node `jerribeth.trickster.epilogue.commit.explicit.1` | `night` | `night_after` ; third-past; male mention (background) |
| `jerribeth.trickster.epilogue.commit.explicit.2` | `jerribeth.trickster.epilogue.commit` | slot node `jerribeth.trickster.epilogue.commit.explicit.2` | `night_mind` | `night_mind_after` ; third-past; male mention (background) |
| `jerribeth.trickster.visit.explicit.1` | `jerribeth.trickster.visit` | slot node `jerribeth.trickster.visit.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `jerribeth.trickster.visit.explicit.2` | `jerribeth.trickster.visit` | slot node `jerribeth.trickster.visit.explicit.2` | `threshold_free` | `morning_free` ; male mention (background) |
| `jerribeth.unsold_evening.explicit.1` | `jerribeth.unsold_evening` | slot node `jerribeth.unsold_evening.explicit.1` | `kiss` | `after`, `story` ; male mention (background) |

### kaylessa

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `kaylessa.clearing.where_i_was_meant_to_die.explicit.1` | `kaylessa.clearing.where_i_was_meant_to_die` | host node `explicit.1` | `explicit.1` itself (after `cut`) | `END` ; terminal: review last_line |
| `kaylessa.trickster.epilogue.commit.explicit.1` | `kaylessa.trickster.epilogue.commit` | `page` paragraph `kaylessa.trickster.epilogue.commit.explicit.1` (#2) | `page` paragraphs 0..1 | `next paragraph` ; third-past |

### kiana

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `kiana.date.explicit.1` | `kiana.date` | slot node `kiana.date.explicit.1` | `threshold` | `morning_after` ; male mention (background) |
| `kiana.date.explicit.2` | `kiana.date` | slot node `kiana.date.explicit.2` | `kiss` | `END` ; terminal: review last_line; male mention (background) |
| `kiana.ink_after.explicit.1` | `kiana.ink_after` | slot node `kiana.ink_after.explicit.1` | `kiss` | `round2_after` ; male mention (background) |
| `kiana.unborrowed_evening.explicit.1` | `kiana.unborrowed_evening` | slot node `kiana.unborrowed_evening.explicit.1` | `kiss` | `round2_after` ; male mention (background) |

### konomi

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `konomi.chosen_evening.explicit.1` | `konomi.chosen_evening` | slot node `konomi.chosen_evening.explicit.1` | `night` | `morning` |
| `konomi.evening.explicit.1` | `konomi.evening` | slot node `konomi.evening.explicit.1` | `stay` | `stay_after` |
| `konomi.private_last_visit.explicit.1` | `konomi.private_last_visit` | slot node `konomi.private_last_visit.explicit.1` | `night` | `night_after` |
| `konomi.the_evening_she_kept.explicit.1` | `konomi.the_evening_she_kept` | slot node `konomi.the_evening_she_kept.explicit.1` | `night` | `night_after` |
| `konomi.trickster.dismissed.a_season.explicit.1` | `konomi.trickster.dismissed.a_season` | slot node `konomi.trickster.dismissed.a_season.explicit.1` | `yes` | `a_season_morning` |
| `konomi.trickster.dismissed.private.explicit.1` | `konomi.trickster.dismissed.private` | slot node `konomi.trickster.dismissed.private.explicit.1` | `threshold` | `morning`, `morning_favour` |
| `konomi.trickster.never_arrived.rooms.explicit.1` | `konomi.trickster.never_arrived.rooms` | slot node `konomi.trickster.never_arrived.rooms.explicit.1` | `accept` | `morning` |
| `konomi.trickster.never_arrived.second_supper.explicit.1` | `konomi.trickster.never_arrived.second_supper` | slot node `konomi.trickster.never_arrived.second_supper.explicit.1` | `accept` | `morning` |

### melazmera

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `melazmera.trickster.beat.count.explicit.1` | `melazmera.trickster.beat.count` | host node `ate` | `ate` itself (after `count`) | `END` ; terminal: review last_line |
| `melazmera.trickster.visit.heap.explicit.1` | `melazmera.trickster.visit.heap` | slot node `melazmera.trickster.visit.heap.explicit.1` | `cut` | `morning` |

### mielarah

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `mielarah.deck.quarterdeck.arcade.explicit.1` | `mielarah.deck.quarterdeck.arcade` | host node `explicit.1` | `explicit.1` itself (after `threshold`) | `END` ; terminal: review last_line |
| `mielarah.deck.quarterdeck.explicit.1` | `mielarah.deck.quarterdeck` | host node `explicit.1` | `explicit.1` itself (after `threshold`) | `END` ; terminal: review last_line |
| `mielarah.deck.wheel.arcade.explicit.1` | `mielarah.deck.wheel.arcade` | host node `explicit.1` | `explicit.1` itself (after `threshold`) | `END` ; terminal: review last_line |
| `mielarah.deck.wheel.explicit.1` | `mielarah.deck.wheel` | host node `explicit.1` | `explicit.1` itself (after `threshold`) | `END` ; terminal: review last_line |

### minachiv

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `minachiv.before_the_last_road.explicit.8` | `minachiv.before_the_last_road` | `together` (inline, after anchor) | `together` up to the anchor | `END`, `stance_2_exclusive_chivarro`, `stance_2_exclusive_minagho`, `stance_2_secret_chivarro`, `stance_2_secret_minagho` |
| `minachiv.minaghos_unfinished_sentence.explicit.1` | `minachiv.minaghos_unfinished_sentence` | slot node `minachiv.minaghos_unfinished_sentence.explicit.1` | `hand` | `hand_after` ; male mention (background) |

### minagho

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `minachiv.before_the_last_road.explicit.5` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.5` | `stance_2_night_chivarro` | `stance_discovery_2_chivarro` |
| `minachiv.before_the_last_road.explicit.6` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.6` | `stance_3_night_chivarro` | `stance_discovery_3_chivarro` |
| `minachiv.before_the_last_road.explicit.7` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.7` | `stance_7_night_chivarro` | `stance_discovery_7_chivarro` |
| `minagho_chivarro.trickster.alone.chivarro.explicit.3` | `minagho_chivarro.trickster.alone.chivarro` | slot node `minagho_chivarro.trickster.alone.chivarro.explicit.3` | `stance_0_night_chivarro` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.chivarro.explicit.4` | `minagho_chivarro.trickster.alone.chivarro` | slot node `minagho_chivarro.trickster.alone.chivarro.explicit.4` | `stance_1_night_chivarro` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.3` | `minagho_chivarro.trickster.alone.minagho_letter` | slot node `minagho_chivarro.trickster.alone.minagho_letter.explicit.3` | `stance_1_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.4` | `minagho_chivarro.trickster.alone.minagho_letter` | slot node `minagho_chivarro.trickster.alone.minagho_letter.explicit.4` | `stance_2_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.5` | `minagho_chivarro.trickster.alone.minagho_letter` | slot node `minagho_chivarro.trickster.alone.minagho_letter.explicit.5` | `stance_3_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.3` | `minagho_chivarro.trickster.alone.minagho_when_it_scars` | slot node `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.3` | `stance_1_night_minagho` | `stance_morning_route` |

### nenio

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `nenio.trickster.epilogue.commit.explicit.1` | `nenio.trickster.epilogue.commit` | slot node `nenio.trickster.epilogue.commit.explicit.1` | `page` | `morning_after` ; third-past |
| `nenio.trickster.night.explicit.1` | `nenio.trickster.night` | slot node `nenio.trickster.night.explicit.1` | `watch` | `END` ; terminal: review last_line |
| `nenio.trickster.night_arcade.explicit.1` | `nenio.trickster.night_arcade` | slot node `nenio.trickster.night_arcade.explicit.1` | `watch` | `END` ; terminal: review last_line |
| `nenio.trickster.night_visitor.explicit.1` | `nenio.trickster.night_visitor` | slot node `nenio.trickster.night_visitor.explicit.1` | `watch` | `END` ; terminal: review last_line |

### nidalynn

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `nidalynn.trickster.ridge.snowfield.explicit.1` | `nidalynn.trickster.ridge.snowfield` | host node `explicit.1` | `explicit.1` itself (after `cut`) | `morning` |

### nocticula

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `noct.acq.an_answer_of_her_own.explicit.1` | `noct.acq.an_answer_of_her_own` | slot node `noct.acq.an_answer_of_her_own.explicit.1` | `accept` | `noct.acq.an_answer_of_her_own.aftermath.1` |
| `noct.acq.epilogue.correspondence.explicit.1` | `noct.acq.epilogue.correspondence` | slot node `noct.acq.epilogue.correspondence.explicit.1` | `admitted` | `morning` ; third-past |
| `noct.acq.the_paid_address.explicit.1` | `noct.acq.the_paid_address` | slot node `noct.acq.the_paid_address.explicit.1` | `an_answer_of_her_own.accept` | `noct.acq.the_paid_address.aftermath.1` |
| `noct.another_place.explicit.1` | `noct.another_place` | slot node `noct.another_place.explicit.1` | `laulieh`, `departure`, `courier` | `noct.another_place.aftermath.1` ; male mention (background) |
| `noct.empty_chair.explicit.1` | `noct.empty_chair` | slot node `noct.empty_chair.explicit.1` | `vow_guard` | `noct.empty_chair.aftermath.1` |
| `noct.her_own_face.explicit.1` | `noct.her_own_face` | slot node `noct.her_own_face.explicit.1` | `night` | `noct.her_own_face.aftermath.1` |
| `noct.last_buyer.explicit.1` | `noct.last_buyer` | slot node `noct.last_buyer.explicit.1` | `named` | `noct.last_buyer.aftermath.1` ; male mention (background) |
| `noct.second_door.explicit.1` | `noct.second_door` | slot node `noct.second_door.explicit.1` | `yes` | `noct.second_door.aftermath.1` |
| `noct.second_door.explicit.2` | `noct.second_door` | slot node `noct.second_door.explicit.2` | `power` | `noct.second_door.aftermath.2` ; male mention (background) |
| `noct.unborrowed_evening.explicit.1` | `noct.unborrowed_evening` | slot node `noct.unborrowed_evening.explicit.1` | `close` | `noct.unborrowed_evening.aftermath.1` |
| `noct.unlit_quay.explicit.1` | `noct.unlit_quay` | slot node `noct.unlit_quay.explicit.1` | `later` | `noct.unlit_quay.aftermath.1` ; male mention (background) |
| `nocticula.trickster.defeated.chair.explicit.1` | `nocticula.trickster.defeated.chair` | slot node `nocticula.trickster.defeated.chair.explicit.1` | `threshold` | `END`, `morning_late`, `morning_late_paid` |
| `nocticula.trickster.epilogue.commit.explicit.1` | `nocticula.trickster.epilogue.commit` | slot node `nocticula.trickster.epilogue.commit.explicit.1` | `kissed` | `after_paid`, `after_refused` ; third-past |
| `nocticula.trickster.epilogue.commit.explicit.2` | `nocticula.trickster.epilogue.commit` | slot node `nocticula.trickster.epilogue.commit.explicit.2` | `knelt` | `after_paid`, `after_refused` ; third-past |
| `nocticula.trickster.epilogue.commit.explicit.3` | `nocticula.trickster.epilogue.commit` | slot node `nocticula.trickster.epilogue.commit.explicit.3` | `walked` | `after_paid`, `after_refused` ; third-past |

### nurah

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `nurah.a_margin_for_you.explicit.1` | `nurah.a_margin_for_you` | slot node `nurah.a_margin_for_you.explicit.1` | `teasing` | `morning` ; male mention (background) |
| `nurah.a_margin_for_you.explicit.2` | `nurah.a_margin_for_you` | slot node `nurah.a_margin_for_you.explicit.2` | `kiss` | `morning` ; male mention (background) |
| `nurah.a_margin_for_you.explicit.3` | `nurah.a_margin_for_you` | slot node `nurah.a_margin_for_you.explicit.3` | `stay` | `morning` ; male mention (background) |
| `nurah.the_letter_she_wrote.explicit.1` | `nurah.the_letter_she_wrote` | slot node `nurah.the_letter_she_wrote.explicit.1` | `near.build_up` | `near` ; male mention (background) |
| `nurah.trickster.epilogue.commit.explicit.1` | `nurah.trickster.epilogue.commit` | slot node `nurah.trickster.epilogue.commit.explicit.1` | `read.build_up` | `read` ; third-past; male mention (background) |
| `nurah.trickster.epilogue.commit.explicit.2` | `nurah.trickster.epilogue.commit` | slot node `nurah.trickster.epilogue.commit.explicit.2` | `went.build_up` | `went` ; third-past; male mention (background) |
| `nurah.trickster.epilogue.the_margin.explicit.1` | `nurah.trickster.epilogue.the_margin` | host node `start` | `start` itself | `END` ; terminal: review last_line; third-past |
| `nurah.trickster.prison.terms.explicit.1` | `nurah.trickster.prison.terms` | slot node `nurah.trickster.prison.terms.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `nurah.trickster.prison.terms_late.explicit.1` | `nurah.trickster.prison.terms_late` | slot node `nurah.trickster.prison.terms_late.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `nurah.trickster.ran_off.terms.explicit.1` | `nurah.trickster.ran_off.terms` | slot node `nurah.trickster.ran_off.terms.explicit.1` | `threshold`, `threshold.wink`, `threshold.betrayal` | `morning` ; male mention (background) |
| `nurah.trickster.ran_off.terms_night.explicit.1` | `nurah.trickster.ran_off.terms_night` | slot node `nurah.trickster.ran_off.terms_night.explicit.1` | `threshold`, `threshold.wink`, `threshold.betrayal` | `morning` ; male mention (background) |
| `nurah.trickster.terms.explicit.1` | `nurah.trickster.terms` | slot node `nurah.trickster.terms.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `nurah.trickster.terms_night.explicit.1` | `nurah.trickster.terms_night` | slot node `nurah.trickster.terms_night.explicit.1` | `threshold` | `morning` ; male mention (background) |

### seelah

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `seelah.door.explicit.1` | `seelah.door` | slot node `seelah.door.explicit.1` | `seelah.door.explicit.1.approach` | `night` ; male mention (background) |
| `seelah.late_afterglow.explicit.1` | `seelah.late_afterglow` | slot node `seelah.late_afterglow.explicit.1` | `seelah.late_afterglow.explicit.1.approach` | `night` ; male mention (background) |
| `seelah.trickster.dismissed.commit.explicit.1` | `seelah.trickster.dismissed.commit` | slot node `seelah.trickster.dismissed.commit.explicit.1` | `seelah.trickster.dismissed.commit.explicit.1.approach` | `threshold` ; male mention (background) |
| `seelah.trickster.dismissed.commit_visit.explicit.1` | `seelah.trickster.dismissed.commit_visit` | slot node `seelah.trickster.dismissed.commit_visit.explicit.1` | `seelah.trickster.dismissed.commit_visit.explicit.1.approach` | `threshold` ; male mention (background) |
| `seelah.trickster.dismissed.second_ask.explicit.1` | `seelah.trickster.dismissed.second_ask` | slot node `seelah.trickster.dismissed.second_ask.explicit.1` | `seelah.trickster.dismissed.second_ask.explicit.1.approach` | `threshold` ; male mention (background) |
| `seelah.trickster.dismissed.second_ask_visit.explicit.1` | `seelah.trickster.dismissed.second_ask_visit` | slot node `seelah.trickster.dismissed.second_ask_visit.explicit.1` | `seelah.trickster.dismissed.second_ask_visit.explicit.1.approach` | `threshold` ; male mention (background) |
| `seelah.trickster.epilogue.commit.explicit.1` | `seelah.trickster.epilogue.commit` | `end` paragraph `seelah.trickster.epilogue.commit.explicit.1` (#0) | (scene start) | `next paragraph` ; third-past; male mention (background) |

### shamira

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `shamira.trickster.after.night_alone.explicit.1` | `shamira.trickster.after.night_alone` | host node `read` | `read` itself (after `morning`) | `END` ; terminal: review last_line |
| `shamira.trickster.after.night_alone.offered.explicit.1` | `shamira.trickster.after.night_alone` | host node `offered` | `offered` itself (after `private`) | `END` ; terminal: review last_line |
| `shamira.trickster.epilogue.late.explicit.1` | `shamira.trickster.epilogue.late` | host node `explicit.1` | `explicit.1` itself (after `late_initiation`) | `partner_late_won` ; third-past |
| `shamira.trickster.harem.explicit.1` | `shamira.trickster.harem` | host node `explicit.1` | `explicit.1` itself (after `cut`) | `morning` |
| `shamira.trickster.harem_awning.explicit.1` | `shamira.trickster.harem_awning` | host node `explicit.1` | `explicit.1` itself (after `cut`) | `morning` |

### soana

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `soana.after_the_last_visitor.explicit.1` | `soana.after_the_last_visitor` | slot node `soana.after_the_last_visitor.explicit.1` | `night` | `round2_morning` ; male mention (background) |
| `soana.after_the_last_visitor.explicit.2` | `soana.after_the_last_visitor` | slot node `soana.after_the_last_visitor.explicit.2` | `quiet_r3_night` | `quiet_r3_round2_morning` ; male mention (background) |
| `soana.before_the_far_road.explicit.1` | `soana.before_the_far_road` | slot node `soana.before_the_far_road.explicit.1` | `night` | `round2_morning` ; male mention (background) |
| `soana.before_the_far_road.explicit.2` | `soana.before_the_far_road` | slot node `soana.before_the_far_road.explicit.2` | `quiet_r3_night` | `quiet_r3_round2_morning` ; male mention (background) |
| `soana.trickster.epilogue.commit.explicit.1` | `soana.trickster.epilogue.commit` | slot node `soana.trickster.epilogue.commit.explicit.1` | `round2_vow` | `round2_morning` ; third-past; male mention (background) |
| `soana.trickster.epilogue.living_late.explicit.1` | `soana.trickster.epilogue.living_late` | slot node `soana.trickster.epilogue.living_late.explicit.1` | `start` | `round2_morning` ; third-past; male mention (background) |
| `soana.trickster.epilogue.luck_late.explicit.1` | `soana.trickster.epilogue.luck_late` | slot node `soana.trickster.epilogue.luck_late.explicit.1` | `start`, `partner_share_start`, `partner_secret_start` | `round2_morning` ; third-past; male mention (background) |
| `soana.trickster.missed.bowl.explicit.1` | `soana.trickster.missed.bowl` | slot node `soana.trickster.missed.bowl.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `soana.trickster.missed.bowl.explicit.2` | `soana.trickster.missed.bowl` | slot node `soana.trickster.missed.bowl.explicit.2` | `quiet_r3_threshold` | `quiet_r3_morning` ; male mention (background) |
| `soana.trickster.missed.second_ask.explicit.1` | `soana.trickster.missed.second_ask` | slot node `soana.trickster.missed.second_ask.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `soana.trickster.missed.second_ask.explicit.2` | `soana.trickster.missed.second_ask` | slot node `soana.trickster.missed.second_ask.explicit.2` | `quiet_r3_threshold` | `quiet_r3_morning` ; male mention (background) |
| `soana.trickster.returned.rebind.explicit.1` | `soana.trickster.returned.rebind` | slot node `soana.trickster.returned.rebind.explicit.1` | `night` | `morning` ; male mention (background) |
| `soana.trickster.returned.rebind.explicit.2` | `soana.trickster.returned.rebind` | slot node `soana.trickster.returned.rebind.explicit.2` | `night_clay` | `morning` ; male mention (background) |
| `soana.trickster.returned.rebind.explicit.3` | `soana.trickster.returned.rebind` | slot node `soana.trickster.returned.rebind.explicit.3` | `quiet_r3_night` | `quiet_r3_morning` ; male mention (background) |
| `soana.trickster.returned.rebind.explicit.4` | `soana.trickster.returned.rebind` | slot node `soana.trickster.returned.rebind.explicit.4` | `quiet_r3_night_clay` | `quiet_r3_morning` ; male mention (background) |
| `soana.trickster.returned.second_ask.explicit.1` | `soana.trickster.returned.second_ask` | slot node `soana.trickster.returned.second_ask.explicit.1` | `night` | `morning` ; male mention (background) |
| `soana.trickster.returned.second_ask.explicit.2` | `soana.trickster.returned.second_ask` | slot node `soana.trickster.returned.second_ask.explicit.2` | `night_clay` | `morning` ; male mention (background) |
| `soana.trickster.returned.second_ask.explicit.3` | `soana.trickster.returned.second_ask` | slot node `soana.trickster.returned.second_ask.explicit.3` | `quiet_r3_night` | `quiet_r3_morning` ; male mention (background) |
| `soana.trickster.returned.second_ask.explicit.4` | `soana.trickster.returned.second_ask` | slot node `soana.trickster.returned.second_ask.explicit.4` | `quiet_r3_night_clay` | `quiet_r3_morning` ; male mention (background) |
| `soana.trickster.returned.terms.explicit.1` | `soana.trickster.returned.terms` | slot node `soana.trickster.returned.terms.explicit.1` | `night` | `morning` ; male mention (background) |
| `soana.trickster.returned.terms.explicit.2` | `soana.trickster.returned.terms` | slot node `soana.trickster.returned.terms.explicit.2` | `night_clay` | `morning` ; male mention (background) |
| `soana.trickster.returned.terms.explicit.3` | `soana.trickster.returned.terms` | slot node `soana.trickster.returned.terms.explicit.3` | `quiet_r3_night` | `quiet_r3_morning` ; male mention (background) |
| `soana.trickster.returned.terms.explicit.4` | `soana.trickster.returned.terms` | slot node `soana.trickster.returned.terms.explicit.4` | `quiet_r3_night_clay` | `quiet_r3_morning` ; male mention (background) |

### targona

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `targona.the_open_threshold.explicit.1` | `targona.the_open_threshold` | `buckles` (inline, after anchor) | `buckles` up to the anchor | `END` ; male mention (background) |
| `targona.trickster.after.quiet_ward.explicit.1` | `targona.trickster.after.quiet_ward` | slot node `targona.trickster.after.quiet_ward.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `targona.trickster.after.ward.explicit.1` | `targona.trickster.after.ward` | slot node `targona.trickster.after.ward.explicit.1` | `threshold` | `morning` ; male mention (background) |
| `targona.trickster.epilogue.commit.explicit.1` | `targona.trickster.epilogue.commit` | `end` (inline, after anchor) | `end` up to the anchor | `END` ; third-past |
| `targona.ward_evening.explicit.1` | `targona.ward_evening` | slot node `targona.ward_evening.explicit.1` | `wall` | `bell` |

### terendelev

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `terendelev.trickster.night.watch.explicit.1` | `terendelev.trickster.night.watch` | slot node `terendelev.trickster.night.watch.explicit.1` | `cut` | `grey` |
| `terendelev.trickster.night.watch_awning.explicit.1` | `terendelev.trickster.night.watch_awning` | slot node `terendelev.trickster.night.watch_awning.explicit.1` | `cut` | `grey` |

### vellexia

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `vellexia.the_question_after_business.desire.explicit.1` | `vellexia.the_question_after_business` | host node `desire` | `desire` itself (after `near`) | `END` ; terminal: review last_line |
| `vellexia.trickster.after.night.explicit.1` | `vellexia.trickster.after.night` | slot node `vellexia.trickster.after.night.explicit.1` | `threshold` | `morning` |
| `vellexia.trickster.epilogue.commit.explicit.1` | `vellexia.trickster.epilogue.commit` | `start` after paragraph #2 | `start` paragraphs 0..2 | `next paragraph` ; third-past; male mention (background) |

### wenduag

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `wenduag.trickster.court.cairn.explicit.1` | `wenduag.trickster.court.cairn` | slot node `wenduag.trickster.court.cairn.explicit.1` | `decide`, `roll`, `knife_down` | `cut`, `cut_echo` ; male mention (background) |
| `wenduag.trickster.court.cairn.native_visit.explicit.1` | `wenduag.trickster.court.cairn.native_visit` | slot node `wenduag.trickster.court.cairn.native_visit.explicit.1` | `decide`, `roll`, `knife_down` | `cut`, `cut_echo` ; male mention (background) |
| `wenduag.trickster.court.gongs.explicit.1` | `wenduag.trickster.court.gongs` | slot node `wenduag.trickster.court.gongs.explicit.1` | `saw`, `stronger` | `END` ; terminal: review last_line; male mention (background) |
| `wenduag.trickster.court.gongs.native_visit.explicit.1` | `wenduag.trickster.court.gongs.native_visit` | slot node `wenduag.trickster.court.gongs.native_visit.explicit.1` | `saw`, `stronger` | `END` ; terminal: review last_line; male mention (background) |
| `wenduag.trickster.court.hunt.explicit.1` | `wenduag.trickster.court.hunt` | `ate` (inline, after anchor) | `ate` up to the anchor | `END` ; male mention (background) |
| `wenduag.trickster.epilogue.pack.explicit.1` | `wenduag.trickster.epilogue.pack` | `page` (inline, after anchor) | `page` up to the anchor | `next paragraph` ; third-past |

### yaniel

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `yaniel.trickster.visit.niche.explicit.1` | `yaniel.trickster.visit.niche` | slot node `yaniel.trickster.visit.niche.explicit.1` | `threshold2` | `morning`, `morning_worn` ; male mention (background) |
