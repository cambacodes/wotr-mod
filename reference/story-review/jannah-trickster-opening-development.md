# Jannah Trickster opening development record

This is a new, unregistered route opening for a living Jannah who chose to return to Seelah's soul mission and completed it.

It is not a complete route, an all-path implementation, or an approval for integration or game testing.

## Canon evidence

The additional-candidate audit classifies Jannah as an adult through her Eagle Watch service and identifies the Kenabres and Molten Scar quests as route hooks.

The same audit says the game provides no numeric age for her.

In `reference/expansion/seelah.txt`, Seelah's `Cue_0142` says she and Jannah met in Kenabres, went drinking, and that Jannah was a capable but inexperienced Aldori fighter.

The Q3 `ktc_DeserterJoins/Cue_0019` GUID `651ecf0cde0e1a54dbc93761d1751b43` contains Jannah's own agreement to help with the stolen-souls mission.

The Q3 `Cue_0001` GUID `7f36934ad41f4a14a9cbb7484844d5f7` gives her return a fresh temple scar and a changed, more collected demeanor.

In `Cue_0013` through `Cue_0015`, the prison-history branch says the Queen approved her appeal, Irabeth supported it, and the army assigned her to a Condemned unit escorting civilians.

She was on parole and had to return if the Commander rejected her request.

Her `Cue_0027` GUID `aaa9f637319779047ad9a373352ba918` says she has her word and a desire to redeem herself, while leaving the decision to the Commander.

That original request is about joining the mission and is not a romantic invitation.

`reference/canon-review/seelah-later-predicates.json` confirms that the successful `WeightOfMySword` terminal is quest Completed at GUID `5a5a533c9ce630a48b877f9a194840cb`.

It also distinguishes the two death-history etudes, the prison etude, the Condemned etude, and the free-release etude.

In particular, the prison etude being Completed records a transfer and does not prove that Jannah is currently imprisoned.

The new scenes require the successful quest, Jannah's own mission-acceptance cue, a current Trickster, and the absence of either death state.

They do not require the Molten Scar cue, so the surviving prison-history route can reach the opening if Jannah later returns and joins the mission.

## Authored material

The misrouted after-action report, practice-yard conversation, inn meeting, optional Trickster delivery fold, and independent parole/reporting-line request are new events.

They are not base-game quests, dialogue, or a native Jannah romance.

The Trickster delivery option appears only after Jannah has chosen to send an answer.
It changes no person, command, letter contents, or answer, and the ordinary courier route remains available.

The Commander can pressure her by treating the meeting as payment for service; Jannah refuses and closes that branch.

The other branches keep the chain of command, her parole, and romantic consent separate.

The optional sparring checks test physical reading and timing, not whether Jannah likes the Commander.

The intimate continuation appears only after both characters affirm a courtship.
Jannah names her boundaries and can stop or change her mind, and the Commander now stops and checks in before any new touch after she says "Not yet."

The current module addresses only a post-mission survivor branch on Trickster.

It does not yet provide the requested fate intervention for Jannah's death outcomes, a missed native mission, or any of the other nine mythic paths.

`PATH_ENTRY_PLANS` records future design ideas only.

The inn and practice yard are authored locations with no verified actor placement.

The `JannahCorrespondence` portrait is a placeholder key, not a commissioned or reviewed image.

## Current size and checks

The source now has five scenes, 63 nodes, and 115 dialogue choices.

A local `\w+` count finds 4,165 node-text words and 1,275 choice-text words, for 5,440 words in total.

This flat source count includes mutually exclusive branches and does not claim a selected-playthrough count.

The fourth scene puts Jannah's request for an independent parole officer and reporting captain on the page, then lets the Commander support, defer to, or undermine that boundary, with an optional Knowledge: World check affecting how accurately the safeguards are written.
The pressure choice is an explicit route-ending action; Jannah refuses to let the Commander erase her request to keep her under his control.
Jannah's authored request explicitly asks for an independent parole review, reporting captain, field-order evaluator, and complaint channel.
The Queen's designated parole authority approves that exact request in writing, with Irabeth copied as the advocate who supported Jannah's original appeal.
This office and amendment are authored additions, not named procedures from the native script; the Commander has no approval or signature role.
The fifth scene lets Jannah answer a recruit's challenge to her orders, with an optional Diplomacy check that clarifies the independent complaint process without deciding its outcome.
The recruit may question a plan before action when time allows, but must follow immediate field orders and submit concerns afterward.
If the Commander uses rank to silence the recruit or override Jannah, she can pause or end the romance rather than reward the interference.
That fifth scene now requires the `independent_chain` outcome, and local assertions confirm that `trust_earned` alone cannot make it eligible.
The module remains far below the project's minimum of 21,000 meaningful selected-playthrough words for a complete individual route.

`python -m py_compile storylines/jannah_trickster_opening.py` passed.

`python -m storylines.jannah_trickster_opening` ran the graph and cross-scene state assertions successfully.

Those assertions check node targets, check outcomes, reachability, meeting-flag production, the next-scene prerequisite, courtship-flag production, death-state exclusions, and each scene's actual combined prerequisites and forbids.

They do not test dialogue export, native binding resolution, game scheduling, actor presentation, save/load, ToyBox settings, or a chronological playthrough.

The first revised opening's source SHA256 was `2938A9881BA5BF2C6A5538F6FC1F5FAB49134F807A5269A7BDFA4770175F68CF`.

The first independent review is `reference/story-review/jannah-trickster-opening-independent-review.md`.
It found that the earlier Trickster mail action was automatic, that the touch sequence crossed Jannah's stated boundary, and that chronology, one optional-kiss description, privacy, and scene eligibility checks needed clarification.
Rereview 2 at `reference/story-review/jannah-trickster-opening-rereview-2.md` confirmed those specific fixes for that three-scene snapshot, while withholding route approval.
The fourth scene adds a consent-centered, consequential separation of parole and reporting authority, including an evil-pressure refusal branch and a bounded Knowledge: World check.
Rereview 3 at `reference/story-review/jannah-trickster-opening-rereview-3.md` documents only the prior four-scene hash `8F5F7E91B87D585C914C02994C81C6463FB263EDE06E55F79F79E49BBFFC530D` and explicitly marks its findings stale after the fifth scene was added during review.
Rereview 4 at `reference/story-review/jannah-trickster-opening-rereview-4.md` reviews the earlier five-scene hash `DC62F2242731C428409137599311CB531AE64DF0B652AD334F1DE46FA5B85A78` and finds that the new scene lacked a finalized-order gate and clear authority for amending parole.
This revision routes the request to the Queen's designated parole authority, gives Irabeth a supporting-copy role rather than decision authority, records written approval, and gates the recruit scene on the resulting independent chain.
Rereview 5 at `reference/story-review/jannah-trickster-opening-rereview-5.md` confirms that every continuing branch produces `independent_chain`, but asks that the approved order explicitly include the field evaluator and complaint channel used in scene five.
Rereview 6 at `reference/story-review/jannah-trickster-opening-rereview-6.md` confirmed the exact written authority but found that the recruit scene misstated whether immediate orders are followed before a complaint.
This revision aligns Jannah's request and the approval, then explicitly distinguishes time-permitting questions from following immediate orders and reporting concerns afterward.
The current five-scene source SHA256 is `FF893A99A01450050E0C0F240CA80D882153567328E1D7474ADAE522C84EFEF7`.
The current development-report SHA256 is recorded externally in the roster readiness audit, and the fifth scene has not yet been independently reviewed.
