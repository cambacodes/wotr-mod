# Aranka continuation next-development record

This record documents four follow-up scenes after the already integrated six-scene island arc.
The source is in `storylines/aranka_continuation.py`.
The current source SHA-256 is `F2A068C8DEBC5B11694096FC7D36D057541770D6EBF147A4AE8CD405AA828AF2`.
This work advances the existing relationship but does not complete Aranka's requested route.

## Revisions after independent review

The independent review is recorded in `reference/story-review/aranka-two-scene-independent-review.md`.
It reviewed the earlier two-scene revision at source hash `400594C71651A006B09BE3967D0958376B5E31D4F91B08F7C5E3A8D60391FBD9` and required a clearer truth boundary, a neutral follow-up, a real consequence for an empty answer, consumed route flags, and a future-facing artistic action.

The moon verse is now explicitly introduced as a fabrication before the travelers hear it.
The travelers visibly agree to hear it before Aranka performs it, and she then gives the uncontested final correction in her own words.
The fiction is a shared joke only with her consent, while the actual song remains hers.

The former morning-after scene is now `the_next_verse`, a neutral meeting several days later.
Its opening explicitly avoids implying an overnight encounter, so the prior private, kiss-only, and road choices all reach it honestly.

An answer that only offers Aranka freedom to leave no longer resolves the conflict through reassurance.
She says that it puts all the burden on her, declines to continue that conversation, and asks the Commander to return after three days with a considered answer.
The retry is `the_deferred_answer`.
If the Commander still has no answer, Aranka travels without waiting for permission or company, and she explicitly leaves all future contact to her own choice.
That branch does not promise or schedule another scene.

The direct-plan branch now says Aranka will leave in two days, matching the 48-hour delay before `the_song_and_the_road`.

The persistent branch flags have explicit readers.
`aranka.story_game`, `aranka.story_restraint`, and `aranka.story_left_alone` select the appropriate opening of `the_next_verse`.
`aranka.story_conversation_done` gates that scene.
`aranka.after_story_deferred` gates the delayed retry.
`aranka.relationship_plan` gates `the_song_and_the_road`.
The focused flag-flow check found no unconsumed new relationship-state flags.

The concrete future action keeps Aranka's work and independent travel active.
She retains her original, credits Sella and Rovan for their parts, controls whether copies travel, and plans to visit three Desnan camps over ten days to exchange songs.
She travels alone unless she invites the Commander to meet her.
The route records this as authored dialogue rather than claiming to implement a physical travel event or new actor placement.

## Canon and design basis

The existing `reference/canon-review/aranka-extension-evidence.md` records native dialogue supporting Aranka's love of travel, musical craft, irreverent humor, and resistance to blind obedience.
It also records that the Dream Warden island and its living Aranka actor are tied to Azata campaign mechanics, including Chapter 5 placement.
The new Trickster passage uses her established taste for freedom and music as its conflict, but it only adds a Trickster choice after an earned relationship and island meeting are already available.
It does not make Aranka universally reachable or romanceable for Trickster.

The source module continues to require the installed RanRomance relationship, successful parent quest, a recognized finale, and the living native island contact.
No native actor, parent romance state, quest objective, dream artifact, or contact adapter is changed here.
The prior canon review describes the Aranka and Alluring Reverie partnership as an existing parent relationship and limits its callback to earned history.
This change adds no new Reverie presence or throuple event.

## Amount and checks

The earlier final review reports 8,308 distinct normalized-text words in the six existing continuation scenes.
The four revised additions contribute 2,337 distinct node-text words using the same markup-stripping and Unicode-word rule.
The resulting continuation source has about 10,645 distinct node-text words before selected-path attribution.
The earlier parent-route report counts 15,758 distinct normalized words across configured dialogue, epilogues, journal text, and alternatives.
That aggregate is not the amount read on one playthrough and does not prove RanRomance parity for a meaningful selected route.
The current work remains substantially below the hard 21,000 meaningful per-character target when evaluated as playable route content.

`python -m py_compile storylines/aranka_continuation.py` passed.
A focused Python graph check confirmed unique node IDs, reachability of every node, and valid in-scene targets in the four additions.
The graph check measured 1,145 distinct normalized words in `the_story_that_follows`, 756 in `the_next_verse`, 214 in `the_song_and_the_road`, and 222 in `the_deferred_answer`.
The same check confirmed that every new state flag is read by a scene or choice prerequisite.
`git diff --check` passed for the two owned files.
The current generated Story export now contains all four revised scene objects, and the independent rereview confirmed they match the exact reviewed source objects.
The managed build and route-rule suite pass on the 631-scene export, with dedicated seeded-history checks for this contribution.
Those checks do not prove the Trickster acquisition route, an attainable full campaign, in-game dialogue, save/load, ToyBox behavior, portrait quality or TTS presentation.

## Remaining required work

Aranka still needs a specific, attainable Trickster acquisition path that can begin without an already earned RanRomance etude.
She also needs a credible Trickster contact route that does not assume the Azata island actor is available in a non-Azata campaign.
An established Chapter 1 rescue, later Desnan contact, and deliberate fate intervention remain research directions rather than a verified implementation.
They must be checked against the installed parent script, native spawn lifetimes, actual areas, and same-save prerequisites before they become gameplay promises.

The expanded route needs additional substantial visits and selected-path word accounting to meet the RanRomance-level minimum.
The revised scenes require a new exact-source independent literary and canon review, followed by integration-owned tests and a separate runtime review.
No review score is assigned in this report.
Art must preserve recognizable Aranka design while meeting the project's conventionally attractive humanoid redesign direction.
Actual game verification must cover the acquired Trickster route, the existing Azata island route, all relevant finale histories, concurrent romance settings, native actor interaction, save/load, and ToyBox Free Love and No Jealousy coexistence.
Only after those checks and independent review should the full route be presented for the user's in-game test.
