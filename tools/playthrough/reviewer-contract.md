# Checkpoint reviewer contract

You review **one checkpoint dossier** (`runs/<policy>/chapter-<N>[-part-<k>].md`) produced by
`tools/playthrough/dossier.py`. Read only; do not edit the mod or the knowledge repo. Your output
is **one JSON object** matching the schema below and nothing else.

Default reviewer: Luna (medium), one part per call, then one whole-chapter synthesis.
Terra (medium) adjudicates only submitted `pending_verification` findings. The two
outputs are distinct strict variants of [reviewer-schema.json](reviewer-schema.json).
A missing or invalid adjudication stays pending and blocks complete coverage.

## What the dossier is

- A deterministic **simulated** playthrough under one policy (see the dossier header). Native
  quests are present only as the native state keys the export reads ("Native progress around
  this part"). Checks always succeed. Crusade resources are assumed sufficient.
- Scenes are in play order. For each scene: how it is reached, what gameplay it touches, where it
  sits among native progress, the player-visible text along the path taken (node text, the
  conditional paragraphs `[pN]` visible with the flags held there, the chosen answer, the other
  answers shown), the flags it set and its approximate word count.
- Start/end state applies both `set` and `unset`. `states.json` holds exact trace scene
  before/after states and addressed node replay before entry, at visible text, and after
  the chosen answer. Absent flags are negative evidence. Node replay does not claim
  runtime derived-state fidelity. Per-flag timestamps name the trace event/hour and
  preserve unknown earning/attribution. Scene entry, choice and paragraph gates,
  host/return GUIDs and presence definitions accompany the text.
- The whole-chapter timeline preserves every world and scene event, including events
  outside this part: delivery windows, visible words, uninterrupted node text, exported
  outcome distinctions, costs/checks, remote/physical mix, setup/payoff flag links,
  gaps and explicit unknown missed windows/required beats. Days and access are simulated.
  Exported alternative outcomes are uncovered. Scheduled native keys are not played
  native choices; authored mod scenes are not native transcripts.
- Appendix: for each woman present, the knowledge files to consult and 10 native lines.
  Open her `canon.md`, `voice.md`, `states.md`, `relationships.md` and `decisions.md` when they
  exist before writing any `character_truth` or `character_knowledge` finding.

## Addresses

Cite evidence by address: `scene_id/node_id` for node text, `scene_id/node_id/pN` for a
paragraph, `scene_id/node_id/choice[i]` for an answer, or a flag name. Quote at most 40 words.
A finding without an address and a quote (or flag) is invalid.

## Checklist

Work through every scene, then the chapter as a whole.

1. **fact**: the text contradicts canon or lore (knowledge `canon.md`, native lines), or the
   world state (a quest the native progress list shows as not yet done is treated as done, a
   place or title is wrong).
2. **chronology**: events referenced before they happen; scenes out of order relative to native
   progress or to each other; a later scene ignores an earlier one's outcome; days/delays that
   make no sense (a "next morning" letter after twenty days).
3. **character_knowledge**: a character knows something she could not know at this point
   (secret, offscreen event, the Commander's private deal) or forgets something she witnessed.
4. **continuity**: assess the actual role (body, projection, memory, historical
   reference, or earlier-sent message) against node state and the latest loss/return
   history. A closed romance is not physical absence, and a flag name is not its meaning.
   Verify producers, native variants, and gates before declaring an unearned body.
   Authored earned Trickster survival after native death goes to history/native-variant
   verification; deliberate player kill or later loss after a return does not earn a body.
   A committed/closed relationship is treated otherwise; a committed/closed relationship
   is treated otherwise; a canon partner is silently ignored; the same beat or device repeats
   across scenes; flags set do not match what the text says happened.
5. **game_feel**: the scene does not read like Owlcat's game: wrong register, menu-like prose,
   meta talk, broken formatting, a wall of text where the game would cut to a choice, answers that
   all say the same thing.
6. **character_truth**: a woman acts against her canon goals, appetite or cruelty; sanitized or
   flanderized; villains reduced to paperwork; her voice does not match `voice.md` and the native
   lines in the appendix.
7. **fun** (player's perspective): pacing (too many scenes in one rest or day; long dry stretches),
   agency (choices that change nothing, a single real answer, the obvious answer always right),
   payoff (set-ups with no return, commitments that land flat), repetition (same structure or
   joke again), tedium (filler, reading obligation without reward), reward (no mechanical or
   emotional reward for effort).
8. **gameplay_integration**: content disconnected from play: long text-only scenes; menu or
   Satchel-delivered content that should happen in the world; remote visits/letters that should be
   physical; events that should be an in-game sidequest, companion interaction, area encounter,
   camp event, quest-journal entry, crusade event, or an item/check/combat beat. Use the
   "Reached", "Gameplay touched" and "Placement" lines.

For `fun` and `gameplay_integration` findings, `recommended_form` is required. For every other
kind it is optional (use it when the fix is a change of form).

## Severity and certainty

- `hard`: breaks the game's truth for the player (dead woman speaking, impossible knowledge, a
  contradiction of a visible canon fact, a state the flags contradict). Must be fixed.
- `major`: a reviewer who knows the game would notice and lose trust: weak character truth,
  confusing chronology, a scene that clearly belongs in the world rather than a menu.
- `minor`: polish.
- `certain`: the quoted evidence alone proves the claim. `uncertain`: depends on canon or game
  state you could not confirm from the dossier and the listed knowledge files; Terra rechecks it.
  Simulator artifacts (always-succeeding checks, assumed resources, simulated days) are not
  findings unless the text itself is wrong under any reachable timing.

## Output and admission (strict)

[reviewer-schema.json](reviewer-schema.json) defines all required fields; extra keys,
prose, Markdown fences, or JSON fragments are rejected. IDs are unique within an output.
Reuse the supplied dossier/policy/chapter/part identity exactly. Finding IDs are observation
IDs, not coordinator defect-ledger IDs; do not invent cross-round closure.

Luna outputs `schema: "rrt-checkpoint-review/2"`, `reviewer: "luna"`,
`scope: "part"` or `"chapter"`, the identity, findings, characters, verdict,
`chapter_disposition: "reviewed"` or `"no_mod_content"`, and `chapter_metrics`.
Each finding has explicit `disposition`: `confirmed` iff certainty is `certain`,
otherwise `pending_verification`. Keep addressed raw evidence, including uncertain hard
items. Characters use `character_id`, not a display name as identity.

Terra outputs `schema: "rrt-checkpoint-adjudication/2"`, `reviewer: "terra"`,
the identity and `dispositions`, one for EACH submitted ID and no other IDs:

```json
{"id":"submitted-id", "disposition":"artifact", "reason":"trace simulator assumption, not a legal history", "finding":null}
```

Allowed dispositions: `confirmed`, `revised`, `dropped`, `artifact`,
`pending_verification`, `needs_live`, `design_required`. Confirmed/revised requires a
complete replacement finding with the SAME ID, certainty `certain`, disposition
`confirmed`, and addressed evidence. Other dispositions require `finding: null` and
retain the raw Luna observation with the reason. Unsupported physical delivery/history
stays `needs_live`; uncertainty is not permission to silently drop evidence.

Aggregation retains dropped/artifact/pending records and raw Luna verdicts. Active
severity counts exclude dropped/artifact; a confirmed hard item is `blocking`, otherwise
pending verification/live/design is `pending`, hard/major is `needs_fixes`, minor is
`pass_with_minor`, else `pass`. Missing/invalid outputs are missing coverage. Luna's
submitted verdict counts match its findings; its status uses the original four labels
(pending hard/major is `needs_fixes`, pending minor is `pass_with_minor`). Terra does not
change Luna's subjective scores or certify a second literary audit.

Keep Fun and Feels-like-part-of-the-game, integer 1-10 with addressed justification.
Part scores remain local observations. Overall diagnostics use one chapter synthesis
cell per declared policy/chapter (epilogue separately), equal chapter weights within
policy, then equal policy weights. Part count never contributes weight. Missing cells
and unmeasured scores stay null; policy means cannot silently drop them. A legitimately
empty chapter uses explicit `no_mod_content`, null metrics and no invented findings.
Never infer empty coverage from a missing output or an unvisited available route.

## Chapter metrics and anchors

`chapter_metrics` contains `flow_pacing`, `appetite_character_truth`, and
`gameplay_seam`. Each requires `score` (integer 0-10 or null), `justification`,
`evidence` (addressed strings), and `evidence_level` (`text`, `static_export`,
`simulated`, `managed_runtime`, `live_campaign`, or `unmeasured`). A null score uses
`unmeasured` and explains the missing evidence. Part calls use null chapter scores;
the whole-chapter synthesis scores the sequence from timeline, full excerpts and part
observations. Splitting the same chapter into more parts cannot improve its weight.

| Score | Flow/Pacing | Appetite/Character-truth | Gameplay-seam |
|---|---|---|---|
| 0 | Progress cannot deliver a coherent sequence. | Actions invert the character's central motives. | The promised playable beat has no reachable delivery. |
| 2 | Repeated stalls, collapsed journeys, or conflicting order dominate. | Generic behavior or sanitization dominates. | Delivery contradicts venue/state; promises have no implemented outcome. |
| 5 | Playable but concentrated, repetitive, or long without a meaningful decision/payoff. | Some recognizable voice, but wants rarely drive choices or counter-moves. | Hooks exist; important costs or consequences remain detached narration. |
| 7 | Clear sequence and payoffs; one material compression, gap, or repeated structure remains. | Her wants and methods shape most beats; one important passive/generic beat remains. | Most content enters through plausible play and records consequences; one substantial seam is weak. |
| 9 | Chapter pressure, discovery, build-up, choices, and payoffs work together with no major defect. | Distinct wants, temper, faith/trade, and agency remain consistent, including villainy where appropriate. | Native timing, entry, checks/costs, fail/decline branches, and later consumers agree at the declared evidence level. |
| 10 | Comparable to a supplied strong native chapter sequence, with no material improvement the judge can substantiate. | Comparable to supplied strong native characterization, throughout the covered branches. | Comparable to supplied native delivery; every load-bearing seam is supported. |

Intermediate integers require a reason between adjacent anchors. Scores only cover
observed branches at their declared evidence level. Appetite concerns wants and actions,
not sex frequency. Heat facets (desire, build-up, approach/cut, voice, aftermath, ceiling)
follow the binding task boundary. Ember/Aivu incidental friendship earns no intimacy penalty.
No score of 10 may claim a supplied native benchmark that was absent.

## Runner evidence

The runner hashes export, contract/schema, dossier/timeline/trace/state references,
knowledge files, tool configuration and prompt. Filename/mtime/parseability alone
cannot admit cache entries. Exact provider exit and schema admission precede atomic
output publication; failed calls retain raw/log diagnostics and usage (or `unknown`).
`review-manifest.json` declares expected artifacts; aggregation reads those paths only,
checks admitted receipts/digests, and preserves missing/failed coverage. These review
receipts are distinct from integration gate receipts owned by the job wrapper.
