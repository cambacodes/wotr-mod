# Explicit-slot rebuild report

Base: `remote/claude/trickster-expansion` @ `ef49eeaa`, branch `claude/slot-rebuild`.
Export: `development/Story.json` at that head. The checked-in export is not rebuilt here;
the coordinator rebuilds on the remote.

The work ran in two passes. Pass 1 was briefs only. Pass 2 applied the coordinator
rulings and touched briefs, the lint, `storylines/chivarro_setpieces.py`,
`storylines/minachiv_voice.py`, the minachiv slot index and directly affected tests.

## Lint counts

| Run | Briefs | Hard | Known rebuild | Warnings |
|---|---|---|---|---|
| Start, `--strict` | 352 | 213 | 0 | 189 |
| Start, `--known-rebuilds` | 352 | 0 | 213 | 189 |
| Pass 1 (briefs only), `--strict` | 352 | 105 | 0 | 189 |
| **Pass 2 (rulings), `--strict`** | **315** | **5** | 0 | **177** |
| **Pass 2, `--strict --known-rebuilds`** | 315 | **0** | **5** | 177 |

Pass 2 removes the 37 `chivarro/` mirror briefs, so the brief count drops from 352 to 315.
The 177 warnings break down as follows:

- 125 background male mentions
- 50 terminal boundaries (`last_line` needs editorial review)
- 2 new `narration_tense` notes. These are third-person *present* hosts, and Gemory only writes third-person past:
  - `eritrice.trickster.epilogue.commit.explicit.1`
  - `minagho_chivarro.trickster.epilogue.commit.explicit.1`

The 5 remaining hard findings are the 4 reserved harem slots listed below.

### Classification of the 213 starting hard findings and their resolution

| Class | Start | Resolution |
|---|---|---|
| `facts` given as a list (schema) | 63 | Joined into text (pass 1). |
| Stale boundary (`last_line` is not the next node's first beat) | 71 | 44 rebound in pass 1. 8 areelu rebound in pass 2, with the test updated (ruling 3). 19 were `chivarro/` mirrors, now deleted. |
| Divergent duplicate slot ID | 56 | `minagho/` is the single source; `chivarro/` deleted (ruling 1). |
| Epilogue narration | 18 | The lint now follows the host's person (ruling 2). Briefs were set to match their hosts. |
| Host missing or moved | 4 | `camellia_vellexia` is now addressed but gated off by design. 3 have no host scene. All 4 remain (ruling 4). |
| Missing required field | 1 | `nocticula_shamira` has no `example` (ruling 4). |
| Participant / pronoun | 0 | Warnings only. |
| Stale export digests | 0 | No brief records a digest. Receipts bind at generation time. |

## Changes

### Pass 1 (briefs only)

- **facts to text:** 63 briefs.
- **Boundaries:** 44 boundaries set to the next node's first beat. The old closing line is kept as `prior_stop_line`, which Gemory and the lint ignore.
- **Host address:** `camellia_vellexia` now names `host_scene: household.pair.camellia_vellexia.choice` and `host_node: explicit.1`.

### Ruling 1: `minagho/` is the single source

- **Deleted** all 37 `chivarro/` briefs:
  - the 28 divergent `minagho_chivarro.*` mirrors
  - the 9 identical `minachiv.*` copies
- **`storylines/chivarro_setpieces.py`** now reads `explicit_slots/minagho/`.
  - The source node list is now `brief.get("source_nodes") or [brief["source"]["node"]]`. `minagho/` briefs carry `source`, and the minachiv ones also carry `source_nodes`.
  - It skips briefs whose `source.scene` is a different page.
  - The cross-folder text replacement is gone, because the brief that installed the slot is now the same brief.
  - The `speakers`, `slot_id` and `default_text` reads are unchanged.
  - Run against the current export's 98 Minagho/Chivarro pages, `_slots` changes nothing: it is idempotent.
- **`storylines/minachiv_voice.py`:** the two `SLOT_TEXT` entries that read `chivarro/` now read `minagho/`. Their content is byte-identical.
- **Export text stays the same.** In the current export, 18 slot nodes carry text that the old builder copied in from a `chivarro/` brief, matched by source node. I set each of those `minagho/` briefs' `default_text` to that live text, so the single-source rebuild should reproduce the current export unchanged (not verified by a build).
  - 10 slots got text from their own same-ID mirror:
    - `after.before_the_last_road.1`, `before_the_last_road_letter.1`, `when_it_scars.1`
    - `alone.chivarro.1`, `chivarro_letter.1`/`.2`, `chivarro_when_it_scars.1`/`.2`
    - `epilogue.commit.1`/`.2`
  - 8 slots are the ones that previously matched neither copy. They were filled by a sibling mirror whose source node matched:
    - `after.before_the_last_road.3` came from `.2`
    - `before_the_last_road_letter.3` came from `.2`
    - `when_it_scars.3` came from `.2`
    - `alone.chivarro.2` came from `alone.chivarro.1`
    - `alone.chivarro.3` and `.4` came from `alone.chivarro.2`
    - `epilogue.commit.3` came from `.4`
    - `epilogue.commit.5` came from `.3`
  - Every other field of the `minagho/` briefs is kept: scene, voice, facts, speakers and source.
  - The other 16 Minagho/Chivarro slots already carried their `minagho/` text.
- **Index:** `plans/minachiv-slot-index.json` now lists only the `minagho/` file for each of the 9 minachiv entries.
- **Test:** `tests/test_minagho_round2.py` asserts the `chivarro/` folder is empty and that each brief's own `default_text` is in its slot.

### Ruling 2: narration follows the host prose

- **`tools/slot_brief_lint.py`.** The epilogue-ownership rule is removed. `host_narration()` reads the host's narration (`{n}` text or Narrator text, without quoted dialogue) and decides person and tense:
  - Person comes from "you" against "the Commander". When neither appears, two or more of "them/their" count as third person.
  - The evidence is checked in order: the slot's own node or paragraph (for inline slots, the text before the anchor), then the beats it flows into, then the build-up nodes.
  - Second person requires `second-present` (or no field). Third person requires `third-past`. A third-person present host adds a `narration_tense` warning.
  - A host with no person marker, or `commander: absent`, sets no requirement.
- **The 16 ruled briefs:**
  - Areelu finale/report (8): `second-present`, matching their hosts.
  - Minagho/Chivarro `epilogue.commit.explicit.1`/`.2`: `third-past` (third-person hosts). `.1` carries the tense warning.
  - Minagho/Chivarro `.3`/`.4`/`.5`: `second-present`.
- **Seven more briefs** had `third-past` on second-person hosts, which the new rule exposed. They are now `second-present`:
  - `delamere.trickster.epilogue.late.explicit.1`
  - `eliandra.trickster.epilogue.{late,together,unasked}.explicit.1`
  - `herrax.trickster.epilogue.after_hours.explicit.1`
  - `iomedae.trickster.epilogue.platform.explicit.1`
  - `shamira.trickster.epilogue.late.explicit.1`
- **`tests/test_iomedae_round3.py`** pinned `third-past` for both Iomedae briefs. It now expects `after` to be `third-past` and `platform` to be `second-present`.
- **`tests/test_slot_brief_lint.py`.** The new test `test_narration_follows_host_prose_not_epilogue_ownership` checks:
  - A second-person present epilogue host accepts `second-present` and rejects `third-past`.
  - A third-person host requires `third-past`.
  - A neutral host and an absent Commander set no requirement.

  The CLI known-rebuild test now uses the `nocticula` route.

### Ruling 3: stop line is the next node's first line

- **Areelu (8 briefs):** `last_line` rebound to the next beat. `tests/test_areelu_round2.py` now asserts `last_line == first_beat(next node)`. It keeps the old protection through `prior_stop_line == "N: " + default_text`, and the existing `default_text == slot Text` check stays.
- **`camellia_vellexia`:** `last_line` rebound to the first beat of `after`. `tests/test_harem_row_s25.py` asserts the new stop line, `prior_stop_line == "V: That display was hideous anyway."` and the host address.

### Known-rebuild allowlist

`REBUILDING` is now `nocticula, jerribeth, arueshalae, camellia`: just the owners of the 4 reserved harem pairs. Areelu, minagho and chivarro are clean and were removed.

## Needs host scene (structure owner)

These stay blocked (ruling 4). Each brief already says it is blocked in its own `status`.

| Slot | Brief | Lint | What is missing |
|---|---|---|---|
| `household.pair.camellia_vellexia.choice.explicit.1` | `harem/household.pair.camellia_vellexia.choice.explicit.1.json` | retired | The host scene exists, but its gate both requires and forbids `household.pair.camellia_vellexia.ready`, so it can never be reached. The structure owner must open the reserved window (152-hour bodily venue). |
| `household.pair.jerribeth_vellexia.choice.explicit.1` | `harem/household.pair.jerribeth_vellexia.choice.explicit.1.json` | host | There is no `household.pair.jerribeth_vellexia.choice` scene and no successor. Per the `build_contract`, the owner must confirm the overlapping body/venue window. |
| `household.pair.shamira_arueshalae.choice.explicit.1` | `harem/household.pair.shamira_arueshalae.choice.explicit.1.json` | host | There is no `household.pair.shamira_arueshalae.choice` scene and no successor. It is blocked until the corrupted-only F-to-R ceiling and arc allocation are integrated. |
| `household.pair.nocticula_shamira.return.explicit.1` | `harem/blocked/nocticula_shamira/household.pair.nocticula_shamira.return.explicit.1.json` | host; required | There is no `return` scene (only `precedence` and `precedence.live`), and the brief has no `example`. |

## After the remote rebuild

- Re-run `python tools/slot_brief_lint.py --strict` against the rebuilt export. The narration rule reads the host prose. Ruling 1 should leave the slot text unchanged, but confirm that.
- `tests/test_minagho_round2` already passes on the current export with the synced `default_text`. It should also pass after the rebuild.

## Ready vs blocked per woman

Unique slots. "Dropped" means an evidenced drop in `plans/slot-brief-index.json`. Ready means
no hard lint finding against the current export. It is not editorial approval: every
candidate still needs voice and continuity review.

| Woman / unit | Ready | Blocked | Dropped |
|---|---|---|---|
| anevia | 20 | 0 | 0 |
| aranka | 11 | 0 | 0 |
| areelu | 9 | 0 | 0 |
| arsinoe | 5 | 0 | 0 |
| arueshalae | 5 | 0 | 0 |
| camellia | 23 | 0 | 0 |
| chadali | 3 | 0 | 0 |
| delamere | 5 | 0 | 0 |
| devarra | 5 | 0 | 0 |
| dorgelinda | 1 | 0 | 0 |
| eliandra | 5 | 0 | 0 |
| elyanka | 4 | 0 | 0 |
| eritrice | 3 | 0 | 0 |
| galfrey | 4 | 0 | 0 |
| gesmerha | 6 | 0 | 1 |
| harem: camellia_arueshalae | 1 | 0 | 0 |
| harem: camellia_vellexia | 0 | 1 | 0 |
| harem: jerribeth_vellexia | 0 | 1 | 0 |
| harem: nocticula_shamira | 0 | 1 | 0 |
| harem: seelah_arueshalae | 1 | 0 | 0 |
| harem: seelah_wenduag | 1 | 0 | 0 |
| harem: shamira_arueshalae | 0 | 1 | 0 |
| harem: wenduag_arueshalae | 1 | 0 | 0 |
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
| minachiv | 2 | 0 | 0 |
| minagho | 46 | 0 | 0 |
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
| **Total** | **307** | **4** | **4** |

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
| `areelu.trickster.finale.ascended.explicit.1` | `areelu.trickster.finale.ascended` | slot node `areelu.trickster.finale.ascended.explicit.1` | `asc_night` | `asc_morning` |
| `areelu.trickster.finale.company.explicit.1` | `areelu.trickster.finale.company` | slot node `areelu.trickster.finale.company.explicit.1` | `welcome_mortal` | `morning_mortal` |
| `areelu.trickster.finale.company.explicit.2` | `areelu.trickster.finale.company` | slot node `areelu.trickster.finale.company.explicit.2` | `welcome_witch` | `morning_witch` |
| `areelu.trickster.finale.lien_bottled.explicit.1` | `areelu.trickster.finale.lien_bottled` | slot node `areelu.trickster.finale.lien_bottled.explicit.1` | `across` | `morning` |
| `areelu.trickster.finale.not_burned.explicit.1` | `areelu.trickster.finale.not_burned` | slot node `areelu.trickster.finale.not_burned.explicit.1` | `nb_across` | `nb_morning` |
| `areelu.trickster.report.inn.explicit.1` | `areelu.trickster.report.inn` | slot node `areelu.trickster.report.inn.explicit.1` | `welcome` | `morning` |
| `areelu.trickster.report.participation.explicit.1` | `areelu.trickster.report.participation` | slot node `areelu.trickster.report.participation.explicit.1` | `in_mortal_2`, `notebook` | `morning` |
| `areelu.trickster.report.participation.explicit.2` | `areelu.trickster.report.participation` | slot node `areelu.trickster.report.participation.explicit.2` | `in_witch_2`, `notebook` | `morning` |
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

### delamere

| Slot | Host scene | Slot / host node | Build-up node(s) to extend to the act start | Exits / notes |
|---|---|---|---|---|
| `delamere.trickster.epilogue.late.explicit.1` | `delamere.trickster.epilogue.late` | `page` paragraph `delamere.trickster.epilogue.late.explicit.1` (#0) | (scene start) | `next paragraph` ; male mention (background) |
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
| `eliandra.trickster.epilogue.late.explicit.1` | `eliandra.trickster.epilogue.late` | `late_accepted` paragraph `eliandra.trickster.epilogue.late.explicit.1` (#0) | `page` | `next paragraph` |
| `eliandra.trickster.epilogue.together.explicit.1` | `eliandra.trickster.epilogue.together` | `page` paragraph `eliandra.trickster.epilogue.together.explicit.1` (#2) | `page` paragraphs 0..1 | `next paragraph` |
| `eliandra.trickster.epilogue.unasked.explicit.1` | `eliandra.trickster.epilogue.unasked` | `late_accepted` paragraph `eliandra.trickster.epilogue.unasked.explicit.1` (#1) | `late_accepted` paragraphs 0..0 | `next paragraph` ; male mention (background) |
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
| `herrax.trickster.epilogue.after_hours.explicit.1` | `herrax.trickster.epilogue.after_hours.invitation` | slot node `herrax.trickster.epilogue.after_hours.explicit.1` | `desire` | `morning` ; male mention (background) |
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
| `iomedae.trickster.epilogue.platform.explicit.1` | `iomedae.trickster.epilogue.platform` | slot node `iomedae.trickster.epilogue.platform.explicit.1` | `down` | `morning_dead`, `morning_kept`, `morning_open` |

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
| `minachiv.a_room_she_likes.explicit.1` | `minachiv.a_room_she_likes` | slot node `minachiv.a_room_she_likes.explicit.1` | `later` | `END` ; terminal: review last_line |
| `minachiv.after_the_last_lamp.explicit.1` | `minachiv.after_the_last_lamp` | slot node `minachiv.after_the_last_lamp.explicit.1` | `night` | `END` ; terminal: review last_line |
| `minachiv.before_the_last_road.explicit.1` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.1` | `stance_0_night_minagho` | `stance_discovery_0_minagho` |
| `minachiv.before_the_last_road.explicit.2` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.2` | `stance_0_night_chivarro` | `stance_discovery_0_chivarro` |
| `minachiv.before_the_last_road.explicit.3` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.3` | `stance_1_night_minagho` | `stance_discovery_1_minagho` |
| `minachiv.before_the_last_road.explicit.4` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.4` | `stance_2_night_minagho` | `stance_discovery_2_minagho` |
| `minachiv.before_the_last_road.explicit.5` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.5` | `stance_2_night_chivarro` | `stance_discovery_2_chivarro` |
| `minachiv.before_the_last_road.explicit.6` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.6` | `stance_3_night_chivarro` | `stance_discovery_3_chivarro` |
| `minachiv.before_the_last_road.explicit.7` | `minachiv.before_the_last_road` | slot node `minachiv.before_the_last_road.explicit.7` | `stance_7_night_chivarro` | `stance_discovery_7_chivarro` |
| `minachiv.the_unhired_evening.explicit.1` | `minachiv.the_unhired_evening` | slot node `minachiv.the_unhired_evening.explicit.1` | `minagho_kiss` | `END` ; terminal: review last_line |
| `minachiv.the_unhired_evening.explicit.2` | `minachiv.the_unhired_evening` | slot node `minachiv.the_unhired_evening.explicit.2` | `chivarro_kiss` | `END` ; terminal: review last_line |
| `minachiv.the_unhired_evening.explicit.3` | `minachiv.the_unhired_evening` | slot node `minachiv.the_unhired_evening.explicit.3` | `together_kiss` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.1` | `minagho_chivarro.trickster.after.before_the_last_road` | slot node `minagho_chivarro.trickster.after.before_the_last_road.explicit.1` | `threshold` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.2` | `minagho_chivarro.trickster.after.before_the_last_road` | slot node `minagho_chivarro.trickster.after.before_the_last_road.explicit.2` | `stance_0_night_minagho` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.after.before_the_last_road.explicit.3` | `minagho_chivarro.trickster.after.before_the_last_road` | slot node `minagho_chivarro.trickster.after.before_the_last_road.explicit.3` | `stance_0_night_chivarro` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.1` | `minagho_chivarro.trickster.after.before_the_last_road_letter` | slot node `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.1` | `came` | `morning` |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.2` | `minagho_chivarro.trickster.after.before_the_last_road_letter` | slot node `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.2` | `stance_0_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.3` | `minagho_chivarro.trickster.after.before_the_last_road_letter` | slot node `minagho_chivarro.trickster.after.before_the_last_road_letter.explicit.3` | `stance_0_night_chivarro` | `stance_morning_route` |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.1` | `minagho_chivarro.trickster.after.when_it_scars` | slot node `minagho_chivarro.trickster.after.when_it_scars.explicit.1` | `night` | `morning` |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.2` | `minagho_chivarro.trickster.after.when_it_scars` | slot node `minagho_chivarro.trickster.after.when_it_scars.explicit.2` | `stance_0_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.after.when_it_scars.explicit.3` | `minagho_chivarro.trickster.after.when_it_scars` | slot node `minagho_chivarro.trickster.after.when_it_scars.explicit.3` | `stance_0_night_chivarro` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.chivarro.explicit.1` | `minagho_chivarro.trickster.alone.chivarro` | slot node `minagho_chivarro.trickster.alone.chivarro.explicit.1` | `threshold` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.chivarro.explicit.2` | `minagho_chivarro.trickster.alone.chivarro` | slot node `minagho_chivarro.trickster.alone.chivarro.explicit.2` | `threshold_clean` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.chivarro.explicit.3` | `minagho_chivarro.trickster.alone.chivarro` | slot node `minagho_chivarro.trickster.alone.chivarro.explicit.3` | `stance_0_night_chivarro` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.chivarro.explicit.4` | `minagho_chivarro.trickster.alone.chivarro` | slot node `minagho_chivarro.trickster.alone.chivarro.explicit.4` | `stance_1_night_chivarro` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.chivarro_letter.explicit.1` | `minagho_chivarro.trickster.alone.chivarro_letter` | slot node `minagho_chivarro.trickster.alone.chivarro_letter.explicit.1` | `came` | `morning` |
| `minagho_chivarro.trickster.alone.chivarro_letter.explicit.2` | `minagho_chivarro.trickster.alone.chivarro_letter` | slot node `minagho_chivarro.trickster.alone.chivarro_letter.explicit.2` | `stance_0_night_chivarro` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.1` | `minagho_chivarro.trickster.alone.chivarro_when_it_scars` | slot node `minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.1` | `night` | `morning` |
| `minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.2` | `minagho_chivarro.trickster.alone.chivarro_when_it_scars` | slot node `minagho_chivarro.trickster.alone.chivarro_when_it_scars.explicit.2` | `stance_0_night_chivarro` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho.explicit.1` | `minagho_chivarro.trickster.alone.minagho` | slot node `minagho_chivarro.trickster.alone.minagho.explicit.1` | `threshold` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.minagho.explicit.2` | `minagho_chivarro.trickster.alone.minagho` | slot node `minagho_chivarro.trickster.alone.minagho.explicit.2` | `stance_0_night_minagho` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.1` | `minagho_chivarro.trickster.alone.minagho_letter` | slot node `minagho_chivarro.trickster.alone.minagho_letter.explicit.1` | `came` | `morning` |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.2` | `minagho_chivarro.trickster.alone.minagho_letter` | slot node `minagho_chivarro.trickster.alone.minagho_letter.explicit.2` | `stance_0_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.3` | `minagho_chivarro.trickster.alone.minagho_letter` | slot node `minagho_chivarro.trickster.alone.minagho_letter.explicit.3` | `stance_1_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.4` | `minagho_chivarro.trickster.alone.minagho_letter` | slot node `minagho_chivarro.trickster.alone.minagho_letter.explicit.4` | `stance_2_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho_letter.explicit.5` | `minagho_chivarro.trickster.alone.minagho_letter` | slot node `minagho_chivarro.trickster.alone.minagho_letter.explicit.5` | `stance_3_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho_spared.explicit.1` | `minagho_chivarro.trickster.alone.minagho_spared` | slot node `minagho_chivarro.trickster.alone.minagho_spared.explicit.1` | `threshold` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.minagho_spared.explicit.2` | `minagho_chivarro.trickster.alone.minagho_spared` | slot node `minagho_chivarro.trickster.alone.minagho_spared.explicit.2` | `stance_0_night_minagho` | `END` ; terminal: review last_line |
| `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.1` | `minagho_chivarro.trickster.alone.minagho_when_it_scars` | slot node `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.1` | `night` | `morning` |
| `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.2` | `minagho_chivarro.trickster.alone.minagho_when_it_scars` | slot node `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.2` | `stance_0_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.3` | `minagho_chivarro.trickster.alone.minagho_when_it_scars` | slot node `minagho_chivarro.trickster.alone.minagho_when_it_scars.explicit.3` | `stance_1_night_minagho` | `stance_morning_route` |
| `minagho_chivarro.trickster.epilogue.commit.explicit.1` | `minagho_chivarro.trickster.epilogue.commit` | slot node `minagho_chivarro.trickster.epilogue.commit.explicit.1` | `pair` | `went` ; third-past |
| `minagho_chivarro.trickster.epilogue.commit.explicit.2` | `minagho_chivarro.trickster.epilogue.commit` | slot node `minagho_chivarro.trickster.epilogue.commit.explicit.2` | `waiting` | `END`, `went_alone` ; third-past |
| `minagho_chivarro.trickster.epilogue.commit.explicit.3` | `minagho_chivarro.trickster.epilogue.commit` | slot node `minagho_chivarro.trickster.epilogue.commit.explicit.3` | `waiting` | `END`, `late_waiting_secret` |
| `minagho_chivarro.trickster.epilogue.commit.explicit.4` | `minagho_chivarro.trickster.epilogue.commit` | slot node `minagho_chivarro.trickster.epilogue.commit.explicit.4` | `pair` | `late_secret_minagho` |
| `minagho_chivarro.trickster.epilogue.commit.explicit.5` | `minagho_chivarro.trickster.epilogue.commit` | slot node `minagho_chivarro.trickster.epilogue.commit.explicit.5` | `pair` | `late_secret_chivarro` |

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
| `shamira.trickster.epilogue.late.explicit.1` | `shamira.trickster.epilogue.late` | host node `explicit.1` | `explicit.1` itself (after `late_initiation`) | `partner_late_won` |
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
