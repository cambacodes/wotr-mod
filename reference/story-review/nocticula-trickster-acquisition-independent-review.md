# Independent review of Nocticula's acquisition opening

Reviewed source SHA256: `7336233EF283E6E87E2EC6A77ACC3463422B221A1FA1DD140ECCC5A7BE1348B8`.
Source: `storylines/nocticula_trickster_acquisition.py`.
Author handoff: `reference/story-review/nocticula-trickster-acquisition-development.md`.
I researched the earlier acquisition map but did not author this source.
This review independently reads the implementation, its selected paths and the installed native blueprints.
No source, registration or art was edited.

## Verdict

Hold for repairs to branch continuity and one speaker reference.
The source correctly gates a preliminary correspondence attempt behind genuine native evidence, but it does not yet provide a playable acquisition route, post-conflict recovery or a compatible join to the completed harbor continuation.
The local source tests pass while the prose defects below remain reachable.
No average score overrides a failed dimension.

| Scoped criterion | Score | Verdict |
| --- | ---: | --- |
| Native audience identification and read-only evidence | 95 | Pass for the proposal |
| Actual selected history and object continuity | 87 | Repair required |
| Nocticula's agency, ego and dangerous interests | 93 | Pass for an introductory contact exchange |
| Commander's wit and resourcefulness | 92 | Pass for this opening |
| Adult romantic tension and refusal | 92 | Pass for introductory graphic and explicit content |
| Finite local checks, costs and closure | 94 | Pass at source level |
| Prose and speaker accuracy | 90 | Repair required under the strictly above 90 rule |
| Honest scope and selected content measurement | 96 | Pass as an incomplete opening |

Native delivery, resumed conversation, full-route minimum, completed courtship, integration and in-game compatibility are unverified and receive no approval score.

## Required repairs

### The earliest refusal invents the divided wax

In every audience variant, select `history -> request -> decline`.
The request's second answer declines private access before entering `price`.
Only `price` describes creating and splitting the disc.
Nevertheless `decline` says that Nocticula closes her hand around the wax and that both pieces disappear.
The later refusal from `price` legitimately has both pieces available.
Use separate early and later refusal prose, or remove the object-specific gesture from the shared refusal.
Verify the two selected paths separately rather than merely checking graph reachability.

### The candid path recalls a score created only by the watchful path

Select `price -> bounded`, finish the genuine native disclosure/reward sequence, then complete either living channel preparation.
The universal `her_hand/start` says the answering line hesitates at the scored edge.
Only `leverage` says Nocticula scores a line across the wax's back.
The candid `bounded` branch establishes a broken edge and an incomplete reflection, not that additional score.
Use the shared broken edge or condition this callback on `petition_watchful`.
The differing immediate attitudes need not create different political outcomes yet, but physical details still need matching producers.

### Nocticula assigns her brother to the Commander

At `price`, Nocticula says, "not the name your brother found amusing".
The scene concerns Socothbenoth, her brother.
The Commander has not acquired that kinship through this route.
Correct the speaker-relative reference and check other pronouns in the audience.
The Commander's references to "your brother" elsewhere are correctly addressed to Nocticula.

## Native insertion and the reward chain

I inspected the actual JSON under `World/Dialogs/c5/Mythic_Trickster/Nocticula/` in the installed `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip`.

| Native object | Verified ID and relationship |
| --- | --- |
| `Nocticula_TricksterC5_Dialogue` | `2c57f65d4b98d764d98794ae8ef9ffdd` |
| `Cue_0006` | `20451daada07f744b9d7f3e14a37a864`, owns the audience answer list |
| `AnswersList_0007` | `2729c49e2bf20c64caa4f54b352e03f6`, includes the real disclosure answer |
| `Answer_0011` | `fd4f6c1d6397fa94db7aaf08de7dfeca`, starts `8ee3df5466722b94091a3b867b33063a` and continues to the reward cue |
| `Cue_0016` | `bb552fe4e21cb874fa3c98c2cc328186`, continues directly to departure |
| `Cue_0019` | `19a0d2e4bae6246469852a4abf7705e6`, teleports the party and hides the portal on stop |

The proposed insertion point is genuinely before departure.
The reward cue has no answer list returning the player to the initial request point.
The author correctly avoided requiring that reward before the request itself.
Both living follow-ups require the request, received seal, selected native disclosure and seen reward response.
I independently tested that either native evidence flag alone remains insufficient.
None of the choices writes the disclosure alias, reward alias, parent history or native Gift state.

The hook is still a proposal, not an exercised native lifecycle.
`src/Main.cs` creates an inserted answer whose `OnSelect` queues the addon scene, and `Rules.EntryTargets` accepts its explicit answer list.
I found no source-specific mechanism that returns this new scene to `AnswersList_0007` afterward.
The closing choice's words about returning to the audience do not implement that behavior.
The existing queue starts the addon book event after dialogue disposal; engine registration must demonstrate how the real disclosure answer remains reachable after completing the addon request.
This is an integration blocker to calling the living path playable, not proof that the chosen native answer-list ID is wrong.
Do not solve it by writing the native disclosure or reward flags from the addon.

## History precedence and schema

The missed variant forbids both parent Active and Reject.
The rejected variant requires Reject and wins even if Active is also present.
The lost-patronage variant requires Active, forbids Reject and original Gift, and requires evidence of original Gift completion, broken/refused patronage or renewed Gift.
An intact Active plus original Gift history has no reacquisition request.
An initial encounter without an accepted parent agreement enters the missed wording rather than inventing an earlier romance.
Later parent-history choices preserve rejection precedence.
Later Gift choices prioritize renewed Gift over original Gift and provide an absent-Gift answer otherwise.

The scene fields are existing authoring fields, including `AnswerLists`, `RequiresAnyGroups`, `Areas`, `Chapters`, `Remote`, `ManualOnly` and the ordinary `Check` form.
The actual book-event entry is `Nodes[0]`, not the display text held in `Entry`.
The source does not register native bindings or its relationship globally.
The future commitment and resolution producers must be resolved before claiming engine validation or registering the blocked draft as normal available content.
The module's final assertion checks the misspelled/nonmatching `noct.renewed_agreement`, rather than `noct.acq.renewed_agreement` used by the relationship.
My independent write audit checked the correct flag and found no producer, so this is a coverage weakness rather than a false commitment currently produced by the story.

## Character and authored magic

Nocticula grants permission to submit a request, not an immediate romance or unrestricted personal audience.
Her interest has a concrete basis: the Commander offers Council intelligence face to face, where she can interrogate it.
Her pleasure in receiving a well-framed request does not erase the remembered rejection or promise a favorable answer.
Her demand for the failed construction gives her information and control the Commander can refuse at the price of ending this contact attempt.
Her final instruction asks for a proposal which accounts for other characters' interests instead of declaring political rivals harmless.

The Commander's strongest exchanges offer a reason for her curiosity without treating cleverness as a universal command.
The seal remains narrow, can be ignored, and does not award native patronage or turn memory into an answering person.
The independently supplied matching stroke is a credible authored signal within the proposed paired-seal magic.
It is not a canon item, a proved native authentication system or a complete response to an adversary who obtains either half.
The later source should preserve that distinction when developing hostile recovery.

The tension is adult and personal without forcing touch, sex or agreement.
Several passages discuss the terms of contact more than Nocticula's particular ambitions; that suits a short acquisition opening but should not become the voice of a full romance.
The next substantive quest needs her concrete stake in the Council, Shamira or the Worldwound, plus a reason to want this Commander beyond admiration for careful phrasing.
The work does not yet demonstrate a fully developed good/evil political split; candid and watchful requests are different immediate attitudes, as the author accurately reports.

## Costs, checks and closure

The Arcana 34 attempt writes and forbids the same attempt flag.
Success preserves a bounded reflection, voluntary slow contact yields letters, and failure records exposure and leads to a different repair demand.
Failure cannot cycle back to the check.
Surrendering the working sketch produces repaired letters and leaves the original fold unusable.
Refusing the sketch writes closure before the ending page and never produces the trial flag.
Postponement is available before attempting the opening and does not erase a failed attempt afterward.
These are witnessed story and information costs, not an implemented gold, inventory or statistical deduction.
The exposure remains recorded; repairing the fold does not claim to prove nothing noticed the original attempt.

## Independent selected-path checks

`python -m storylines.nocticula_trickster_acquisition` passes with six source scene definitions, 37 delivered nodes, six history fixtures and 36 trial outcomes.
I separately traversed eligible choices from `Nodes[0]`, applied actual choice flags, explored both check outcomes and used the repository tokenizer.
The traversal excluded closures and postponements, counted one audience variant and both living follow-ups, and did not credit the blocked post-conflict preparation.

| Initial history | Minimum | Maximum | Successful trial paths |
| --- | ---: | ---: | ---: |
| Missed agreement, no original Gift | 1,582 | 1,931 | 6 |
| Missed agreement, original Gift | 1,581 | 1,930 | 6 |
| Rejected agreement, no original Gift | 1,603 | 1,952 | 6 |
| Rejected agreement, original Gift | 1,602 | 1,951 | 6 |
| Active agreement, original Gift completed | 1,582 | 1,931 | 6 |
| Active agreement, renewed Gift | 1,581 | 1,930 | 6 |

These independently reproduce the author counts.
I also tested rejection precedence when Active and Reject coexist, and found only the rejection request eligible.
No choices write native aliases, `noct.acq.renewed_agreement`, `noct.acq.conflict_resolved_verified` or `noct.acq.postconflict_reply_verified`.
The 37 delivered nodes include duplicated request variants and are not 37 unique scenes or evidence of full-route length.

## Precisely what remains incomplete

`after_the_council` is a single unsent preparation with an intentionally missing verified-resolution producer.
Council fight and death flags alone cannot admit it.
It supplies neither an authenticated reply nor a restored body, government, romance or reusable actor.
It is not a working death/hostility recovery route.
The Chapter 6 Threshold response remains reference evidence and is not treated as an event already experienced in Chapter 5.

The living endpoint is `correspondence_trial`, not `renewed_agreement`.
The source still needs an earned concession, an actual personal invitation, acceptance or refusal, and history-aware integration into the existing continuation.
It does not recover a player who already departed the audience without making this request.
The existing full continuation's Gift, earlier bargain and city-agent assumptions remain unverified for these new histories.
The introduction's counts cannot be added to an arbitrary continuation maximum to prove a 21,000-word recovered route.
ToyBox simultaneous-romance compatibility, native dialogue resumption, rest delivery, save/reload and all required path timing remain in-game integration work.
No artwork or portrait assignment is approved by this review.
