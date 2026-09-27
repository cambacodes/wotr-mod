# Yaniel supper progression: independent canon and character review

Source: `storylines/yaniel_supper_progression.py`.

Pinned source SHA-256: `0F75D7CEF54D7A0E2983FA2B0287ECB1939607BAB14343F0487470DAFDCDA4C4`.

Development report: `reference/story-review/yaniel-supper-progression-development.md`.

Pinned report SHA-256: `03AE6B5DED3FE8B425D544BF4E2CA28F2BA56B72CC3B757BA870E7BDBF4866F5`.

This review covers one authored follow-up scene only, not Yaniel's complete romance route.

The two pinned hashes were verified before and after review and still match.

## Canon and continuity

The local game-dialogue inventory supports the key distinction between genuine rescued Yaniel and the impostor, and records her rescue, long captivity, and old-woman presentation (`reference/canon-review/candidate-inventory-dialogue.json:58-70`; `reference/story-review/yaniel-route-opening-rereview-2.md:14-18`).

The opening's research also cites the genuine Midnight Fane identity and Radiance-recognition cues, including her taking Radiance and later returning it to the Commander (`storylines/yaniel_route_opening.py:7-20`; `reference/story-review/yaniel-route-opening-development.md`, “Native evidence and limits”).

This supper scene does not contradict that sword sequence: it names Radiance as hers to use or set aside at her discretion (`storylines/yaniel_supper_progression.py:37-38, 107-108`).

The scene appropriately labels the invitation, room, contact witness, living actor, and setting as authored or unverified rather than presenting them as native events (`storylines/yaniel_supper_progression.py:31-32, 115-119`; development report, paragraphs 2 and 5).

There is, however, a serious timeline question that its caveat does not solve: the opening requires the second contact to occur after the Fane rescue, while the local canon review records Yaniel saying that a day in Drezen was enough before she asked Targona to take her back into the Abyss (`reference/canon-review/dragon-family-dialogue.json`, Yaniel dialogue entry; `reference/canon-review/additional-candidate-table.md:14`).

This prototype puts her in a citadel-kitchen room and on rebuilt Drezen walls after a 72-hour delay (`storylines/yaniel_supper_progression.py:31-32, 49-50, 113-119`), but it supplies no producer or chronology that makes her presence compatible with her established departure.

That can be repaired through a sourced, short pre-departure window or a meeting on her established route with Targona, but neither is implemented or established here.

The scene's domestic routines, remembered patrol, supper, desire, and courtship are authored alternate developments; none is represented as a fact from the game's script (`storylines/yaniel_supper_progression.py:49-50, 64-70, 80-103`; development report, paragraph 6).

## Independent scores

Scores are separate gates, not an average.

The project threshold is strictly above 90 for each applicable reviewed dimension.

- Canon distinction and authored-continuity labeling: **94/100 - pass for this bounded scene**.
The scene keeps the real Yaniel separate from the fake and identifies its setting and contact as authored, not established game events (`storylines/yaniel_supper_progression.py:7-22, 31-32, 115-119`).
- Post-Fane chronology and character availability: **82/100 - revision gate**.
The scene does not account for Yaniel's native statement that she quickly leaves Drezen with Targona, and its 72-hour scene schedule and citadel setting have no verified actor or location producer (`storylines/yaniel_supper_progression.py:31-32, 113-119`; `reference/canon-review/additional-candidate-table.md:14`).
- Radiance handling and respect for her adult age: **96/100 - pass for this bounded scene**.
Radiance remains Yaniel's choice, and silver hair and fine lines are described as part of an attractive adult veteran rather than flaws to erase (`storylines/yaniel_supper_progression.py:37-38, 93-99, 107-108`).
- Character core and agency: **93/100 - pass for this bounded scene**.
Her independent risk judgment, paladin's duty, regret, and refusal to be turned into a symbol are consistent with the established rescued paladin (`storylines/yaniel_supper_progression.py:43-50, 64-75`; `reference/canon-review/additional-candidate-table.md:14`).
- Dialogue voice and fit with the game: **87/100 - revision gate**.
Yaniel has some dry humor and directness, particularly in her legend response and kitchen-song disagreement (`storylines/yaniel_supper_progression.py:43-46, 80-81`).
Several later passages rely on contemporary, highly explicit boundary formulations and abstract instruction-like phrasing, including “not a contract that obliges me to comfort you,” “you cannot decide which risks I am allowed to take,” and “not something we infer” (`storylines/yaniel_supper_progression.py:64-65, 72-75, 98-99`).
Each line can be understood, but their repetition makes the exchange sound more like carefully drafted interpersonal guidance than the game's character dialogue.
- Adult desire, sensuality, and boundaries: **94/100 - pass for this bounded scene**.
Yaniel initiates the second invitation, acknowledges her own attraction, offers her hand, gives a clear affirmative kiss, and sets a limit on the night without denying desire (`storylines/yaniel_supper_progression.py:31-38, 85-103`).
This is a romantic, lightly sensual supper scene rather than mature-spice route completion.
- Choice and check consequences: **93/100 - pass locally, not system-verified**.
The Knowledge (World) DC 24 check enriches a memory rather than granting affection; failure allows accepting correction or defending the mistake, and defensiveness can end the evening (`storylines/yaniel_supper_progression.py:49-63`).
Unasked protection has a meaningful relational consequence, while an apology does not purchase intimacy (`storylines/yaniel_supper_progression.py:68-75`).
The resulting flags are authored names with no demonstrated downstream consumer, so persistence and campaign-level consequences remain unverified (`storylines/yaniel_supper_progression.py:33-34, 56-63, 70-75, 82-109`).
- Local graph and route gates: **96/100 - pass for source-level structure only**.
The source asserts unique node IDs, target resolution, full reachability, one skill check, and a kiss flag (`storylines/yaniel_supper_progression.py:125-150`).
Its scene contract excludes the opening friendship and closed branches and requires a freely invited second meeting (`storylines/yaniel_supper_progression.py:6-22`).
The contract is not a runtime gate until a producer sets and enforces these flags.
- Full-route scope and meaningful-playthrough length: **12/100 - hard failure**.
The scene has 21 nodes and 42 choices, 1,616 node-text words, and 421 choice-label words, for 1,135 words on its longest compatible branch.
That is far below the required 21,000 meaningful words for a complete character route (`reference/story-review/yaniel-supper-progression-development.md`, paragraphs 8-10; source graph at `storylines/yaniel_supper_progression.py:24-120`).
- Registration, native integration, actor/location, and runtime proof: **0/100 - hard failure**.
The module is absent from `development/Story.json`; its required contact, actor, and location producers remain unverified (`storylines/yaniel_supper_progression.py:115-119`; development report, paragraphs 2, 10-11).
No runtime, save/load, ToyBox, or in-game test is supplied.
- Art and art review: **0/100 - hard failure**.
This scene contains no delivered art asset or independent art review.

## Checks performed

`python -m py_compile storylines/yaniel_supper_progression.py` passed.

`python -m storylines.yaniel_supper_progression` passed and reported one unregistered scene, 21 nodes, and valid unique targets and authored route gates.

Independent traversal found 21 reachable nodes, 42 choices, 1,616 prose words, 421 choice words, and a longest compatible branch of 1,135 words.

`python tools/measure-story-content.py --self-test` passed.

`git diff --check` passed.

These are source and documentation checks, not proof of runtime gates or integration.

## Review result

The scene has a promising adult courtship beat, preserves Yaniel's freedom to refuse, and does not turn her rescue into romantic debt.

It does not pass review as a route component for implementation because the post-Fane contact chronology and voice criteria are below threshold, and the scene is not integrated.

Even if those bounded issues are fixed, this remains a short route component, not a complete or approved route.

Do not treat it as ready for in-game testing or as satisfying the project's full-route content, art, path-access, ToyBox, save/load, and runtime gates.
