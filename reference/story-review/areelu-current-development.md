# Areelu Trickster route: current development record

Status: 14-scene experimental route, still unintegrated and not independently reviewed at this revision.

Source: `storylines/areelu_trickster_rivalry_opening.py`.

Source SHA256: `37A42DE5D06AA609F5F2A56833C9F01DE3F548A16441EE40C87AE6F470B09A22`.

This record supersedes earlier development snapshots for scene count and authored content, including `reference/story-review/areelu-trickster-opening-development.md`.

Earlier independent reviews were performed against different source hashes and do not approve this revision.

## Canon and authored AU

The route preserves the native failed restoration, the Commander's original mortal soul, the dead child's grafted remnants, and Areelu's grief.

The premise that the Commander's soul belonged to an unrelated adult before the graft is an authored AU detail, not a fact established by native dialogue.

The native c6 line in which Areelu says she cannot think of the Commander as anything but her child remains intact in the game's dialogue history.

The route's `NATIVE_GRIEF_CONTEXT` records that line as grief-driven identification, not proof of kinship, and explicitly forbids treating it as a route veto.

The route does not clear, rewrite, or reinterpret the native cue.

The Commander and Areelu confront the tension between the authored adult biography and Areelu's grief-driven identification through dialogue, rivalry, and player choices.

All new meetings, survey events, relationship state, and Trickster interventions are authored additions, not recovered native game scenes or existing game mechanics.

The Trickster route remains conditional on an explicit contact request and Areelu's explicit acceptance.

Every scene requires the current Trickster path.

Existing terminal etudes that prove Areelu dead or unavailable block contact.

The redeemed and ascension endings remain gated on independent proof that Areelu is alive and contactable.

The c6 grief-identification cue is recorded as context only and does not block the route.

## Current authored scope

The opening names the adult-before-graft biography as a deliberate AU premise and preserves the graft's failure and unresolved effects.

The early rivalry gives Areelu space to challenge the Commander's memory and the Commander's claims about her grief.

The Trickster interventions manipulate authored copies and present reconstructions only.

They do not alter the native soul, graft, dialogue history, or past events.

The route includes field work, a public-accountability arc, a boundary breach and repair arc, a dangerous gate decision with resident consent, and a later relationship choice.

The new 72-hour private meeting scene adds direct adult desire and consensual intimacy after the longer public and relationship arcs.

In that scene Areelu asks about the Commander's authored pre-graft adult life and begins to recognize the person she treated as an available soul for her theory.

The player can accept a kiss and private night, choose nonsexual closeness, defer intimacy, or stop the relationship.

The scene preserves an open relationship state and does not make intimacy a reward for Areelu's remorse.

The later campaign ending distinguishes a committed relationship, open continuation, pause, and closure.

It does not claim that attraction heals grief or absolves harm.

## Length measurement

The source contains 14 scenes and 163 nodes.

The modeled Trickster romance playthrough contains 24,977 words of node text and selected choice labels.

That modeled path clears the project planning floor of 21,000 words by 3,977 words.

The count uses `tools/measure-story-content.py`'s markup removal and Unicode word tokenizer.

The route solver carries choice flags from scene to scene, enforces scene and choice requirements and forbids, explores both check outcomes, and excludes abort choices.

The modeled starting state includes an accepted route entry, the current Trickster path, and a verified non-declined native c5 crib-memory answer.

Those inputs are required native and future-runtime conditions; the manuscript does not produce or verify them in-game.

The modeled route keeps the relationship active and reaches the authored committed-ending choice.

Per-scene word counts on that compatible path are 1,188, 1,228, 751, 1,271, 691, 785, 723, 848, 772, 3,655, 3,773, 3,519, 2,262, and 3,511.

The count is a structural path model, not a game playthrough or an independent assessment of meaningfulness, pacing, voice, or quality.

The 21,000-word gate is provisionally met for the modeled path only.

An independent reviewer must verify the route length against this exact source hash and judge whether the prose earns its volume.

## Checks and limitations

`py -m storylines.areelu_trickster_rivalry_opening` passes the local scene and transition assertions.

`py -m py_compile storylines/areelu_trickster_rivalry_opening.py` passes.

`git diff --check -- storylines/areelu_trickster_rivalry_opening.py` passes.

The graph checks validate local targets, check branches, contact eligibility, memory transitions, and route progression flags.

The path model also confirmed one flag-compatible route from the opening through all 14 scenes to the committed-ending choice while remaining on Trickster.

The source remains an unintegrated authoring contract.

There are no Unity dialogue bindings, native-state readers, game flag writers, ToyBox tests, save/load tests, in-game rendering checks, or manual playthrough results.

Art and an independent art review are still missing.

The experimental romance concept and current revision need separate canon, characterization, writing, and relationship reviews.

No review scores are claimed in advance.

Do not mark Areelu ready until independent reviewers assess this exact source hash, the art passes its separate review, and the runtime, ToyBox, and game checks exist.
