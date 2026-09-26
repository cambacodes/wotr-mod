# Seelah Act 5 copyist bridge

This is one necessary catch-up scene, not a second Abyss arc or full-route approval.
Owned files are `storylines/seelah_return.py` and this handoff.
No shared source, export, test file, installed content, or existing scene was edited.
The unslop and ponytail instructions were applied using the existing authoring helpers.

Source SHA256: `5E6014F73C0AC3A095A414DBD5703E2BA40DE3F07DE4CA5493A9D8BF0BDD1B50`.
The project measurement function reports 2,005 raw words, 1,977 distinct-segment words, 1,750 prose words, and 255 choice-label words.
The scene contains 20 nodes and 30 choices.
Selected paths contain 934 to 1,132 words depending on the actual history and answers.

## Reason and source history

The assignment addresses finding 2 in `reference/story-review/seelah-assembled-readiness-20260925.md`.
Read the complete `storylines/seelah_abyss.py`, the relevant current Seelah progression and aftermath definitions, and the assembled audit.
The original `letter` scene distinguishes a recovered letter whose owner became publicly identifiable from a burned letter whose remaining contents were not read aloud.
Both histories set `seelah.letter_unsettled`.
The original follow-up conversation sets `seelah.letter_discussed` and either `seelah.check_person` or `seelah.check_signal`.
The played follow-up with the copyist sets `seelah.copyist_followed`.
Those original scenes are Chapter 4 only.

The new scene is `seelah.letter_return`, offered through Seelah's existing answer list in Drezen during Chapter 5.
It requires `seelah.letter_unsettled` and at least one original public/burned outcome flag.
It excludes `seelah.copyist_followed`, its own completion, closure, farewell, death, departure, and inhuman states.
There is no extra delay because it repairs a conversation already owed before leaving the previous act.
It is not Remote; root should attach discovery guidance or a reminder when the current progression requires it.

The scene supports both a departure before `letter_after` and a departure after discussion but before `letter_work` completes.
The latter explicitly remembers the actual person/signal agreement and does not make the characters discover it again.
A defensive discussed-history fallback handles legacy saves without either agreement flag without inventing a prior promise.
The fully played copyist follow-up is excluded and must not receive this catch-up.
If root's progression contract treats `letter_discussed` alone as sufficient relationship resolution, this scene can remain optional on that subset while addressing the missed practical follow-through.
Do not require players who completed `copyist_followed` to play it.

## What happens

Halven is a new authored adult writer in Drezen collecting accounts of the Abyss.
Seelah mentioned the stall to him and now confronts his premature heroic heading before supplying any detailed account.
Neither his collection nor his room is a native quest, physical actor, or installed location.

Public and burned memories have separate scenes and separate Commander answers.
The Commander can stand by the original priority or reconsider it.
Seelah acknowledges the value of recovering the letter or protecting the remaining contents while retaining the specific cost.
She does not demand that the Commander confess an intention they never selected.
On the public defense path she can continue disagreeing about what should have been done.
On the burned path she owns her participation instead of retrospectively claiming the diversion was entirely the Commander's error.

They do not know the copyist's present circumstances.
The scene neither claims that she followed them to Golarion nor invents work, rescue, reconciliation, a known delivery address, or forgiveness.
The wording concerns her present situation rather than claiming Seelah could never have met her after the stall, because a player may have seen the opening of `letter_work` and deferred it.
The new draft is not a letter to the copyist and is never delivered to her.

The present actionable choice is a limited account of their own intervention or withdrawal of the incident from Halven's collection.
Both outcomes are played with Halven on the page.
The account omits the copyist's trade, sister, identity, and location within Alushinyrra; Halven accepts it as written without the heroic title.
The withholding path makes him cross out the heading and return the empty page.
Neither outcome claims a published book, circulation, repaired reputation, or a measurable change to the crusade.

The ending closes the overdue conversation between Seelah and the Commander while preserving the external uncertainty.
Company and solitude both complete the bridge.
There is no mandatory touch, kiss, new commitment, forgiveness claim, or jealousy consequence.
The carrier and folded-cloth moment on the company branch is a small physical joke, not another morality lesson or new quest.

## State contract for root integration

Every completed path sets `seelah.letter_return_addressed`.
This means the Act 5 conversation has occurred, not that the copyist's loss has been repaired.
The new scene deliberately leaves the original `seelah.letter_unsettled` history intact.
The authoring helper supports additive flags, and clearing an old outcome would erase evidence needed for later callbacks.

The following additional flags describe selected behavior.

| Pair | Meaning |
|---|---|
| `seelah.letter_return_stood` / `seelah.letter_return_reconsidered` | Current judgment of the original decision. |
| `seelah.letter_return_account` / `seelah.letter_return_withheld` | Actual disposition of Halven's proposed account. |
| `seelah.letter_return_company` / `seelah.letter_return_space` | Selected ending of this conversation. |

The bridge does not set `letter_discussed`, `check_person`, `check_signal`, `copyist_followed`, or a native quest outcome.
Their existing meanings remain tied to the scenes that actually established them.
It does not clear, overwrite, or grant any unrelated romance flag.

For progression, treat the unfinished episode as addressed when the played Abyss follow-up or the Act 5 catch-up supplies the appropriate earned evidence.
The proposed strongest predicate is no original unsettled episode, or `copyist_followed`, or `letter_return_addressed`.
Root must decide whether `letter_discussed` without either later completion is sufficient for a particular weaker promise, rather than silently treating all three as the same experience.
An unconditional check of `letter_unsettled` alone would remain true forever and incorrectly block every history.

The progression contract still needs migration for already committed and late-installed saves.
This scene accepts an already committed save if contact and the remaining conditions are valid; it makes no claim that the Commander has not yet committed.
It forbids farewell so it cannot casually restart the route after the last conversation.
Root needs an explicit pre-farewell catch-up path and a separate policy for saves already past farewell.
Do not invent a retroactive completion merely to satisfy the new gate.

## Verification performed and remaining

A read-only Python import and exhaustive traversal covered all 20 nodes across public/burned outcomes and four discussion states: unspoken, person agreement, signal agreement, and defensive discussed-without-agreement legacy history.
All 64 complete paths and eight initial deferrals were inspected by the traversal.
Every reachable page had an available answer and all edges resolved.
Assertions verified final addressed state, preservation of an unrelated romance sentinel, unchanged original discussion status, absence of fake `copyist_followed`, and one selected account disposition.
All aborts are at the initial page before progress writes.
No new persistent test file was added and no shared C# or Unity suite was run by this author.

Root tests should exercise actual scene availability in Chapter 5 Drezen, rejection in Chapter 4 and other areas, no originating incident, missing outcome, fully followed history, already addressed state, closure, farewell, death, departure, and inhuman state.
Include both agreement histories and the absence of discussion, and confirm that interrupted conversations do not establish premature completion.
The new progression condition needs explicit tests for unplayed incidents, full Abyss follow-up, catch-up completion, and already committed saves.
Native contact, installed dialogue presentation, save/load, and ToyBox free-love/no-jealousy remain integration verification.

No skill check was added to determine moral agreement, consent, or whether the characters acknowledge the incident.
The authored choices have distinct played consequences without pretending to be dice rolls.
No art was generated or installed.
Independent review is still required; no writing or canon score is self-assigned, and the assembled Seelah route remains subject to every full-route quality and readiness constraint.
