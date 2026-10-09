# Checkpoint reviewer contract

You review **one checkpoint dossier** (`runs/<policy>/chapter-<N>[-part-<k>].md`) produced by
`tools/playthrough/dossier.py`. Read only; do not edit the mod or the knowledge repo. Your output
is **one JSON object** matching the schema below and nothing else.

Default reviewer: Luna (medium effort), one chapter part per call. Every finding marked
`"certainty": "uncertain"` is re-checked by Terra (medium effort) with the same contract, given the
finding and the dossier; Terra answers with the same schema, keeping or dropping each finding and
setting `certainty` to `certain` or removing it.

## What the dossier is

- A deterministic **simulated** playthrough under one policy (see the dossier header). Native
  quests are present only as the native state keys the export reads ("Native progress around
  this part"). Checks always succeed. Crusade resources are assumed sufficient.
- Scenes are in play order. For each scene: how it is reached, what gameplay it touches, where it
  sits among native progress, the player-visible text along the path taken (node text, the
  conditional paragraphs `[pN]` visible with the flags held there, the chosen answer, the other
  answers shown), the flags it set and its approximate word count.
- "State at the start/end of this part": who is started, committed, closed, departed or dead.
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
4. **continuity**: state contradictions: a dead or departed woman (state table) appears, speaks,
   writes, or is spoken of as present without an earned return; a committed/closed relationship
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

## Output schema (strict)

Machine-checkable form: [`reviewer-schema.json`](reviewer-schema.json) (JSON Schema 2020-12).

```json
{
  "schema": "rrt-checkpoint-review/1",
  "dossier": "runs/<policy>/chapter-<N>[-part-<k>].md",
  "policy": "<policy>",
  "chapter": "<N or epilogue>",
  "part": 1,
  "reviewer": "luna|terra",
  "findings": [
    {
      "id": "<policy>-c<N>-p<k>-<NNN>",
      "chapter": "<N or epilogue>",
      "scene": "<scene id>",
      "node": "<node id or null>",
      "flag": "<flag name or null>",
      "kind": "fact|chronology|character_knowledge|continuity|game_feel|character_truth|fun|gameplay_integration",
      "claim": "<one or two sentences: what is wrong and why it matters>",
      "evidence": "<address(es) + quote <= 40 words, and/or flag, and the canon/knowledge path used>",
      "certainty": "certain|uncertain",
      "severity": "hard|major|minor",
      "recommended_form": "sidequest|companion_interaction|area_encounter|camp_event|journal_quest|crusade_event|check|combat|item|keep_as_is|cut|null",
      "recommendation": "<concrete fix: what to change, where, in one or two sentences>"
    }
  ],
  "characters": [
    {
      "character_id": "<knowledge id>",
      "present_in": ["<scene id>"],
      "state": "present|committed|departed|dead|absent",
      "voice": "on|drifting|off",
      "truth": "on|sanitized|flanderized|off",
      "notes": "<two sentences at most>"
    }
  ],
  "verdict": {
    "chapter_status": "pass|pass_with_minor|needs_fixes|blocking",
    "hard": 0,
    "major": 0,
    "minor": 0,
    "fun": {"score": 1, "justification": "<one line>"},
    "feels_like_part_of_the_game": {"score": 1, "justification": "<one line>"},
    "summary": "<three sentences at most>"
  }
}
```

Rules for the JSON:

- `findings` may be empty; `characters` lists every woman in the dossier appendix.
- Counts in `verdict` equal the findings by severity. `chapter_status` is `blocking` when any
  finding is `hard` and `certain`; `needs_fixes` when any `hard` or `major` remains; otherwise
  `pass_with_minor` or `pass`.
- `fun.score` and `feels_like_part_of_the_game.score` are integers 1-10 for this dossier
  (10: plays like the best of the base game; 5: tolerable reading; 1: a menu of text). Each
  needs a one-line justification naming at least one scene.
- `recommended_form` is a required non-null value for `fun` and `gameplay_integration`
  findings; `null` is allowed otherwise.
- No prose outside the JSON object.
