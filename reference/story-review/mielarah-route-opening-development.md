# Mielarah opening contribution - development record

This is an unregistered contribution with sixteen authored scenes, not a complete romance route, runtime implementation, quality approval, or claim that the player can test it in game.

The previous reviewed source SHA-256 was `5829B7F37EA8FF3D314B662D2834BA636D70D060BC06C008FAEE576172DD492F` and its report SHA-256 was `9ECB3AF427BA81DB0F8A4FFC6A3D3EDE0F66F9F4086DBABBC1783927303971AE`.
Independent rereview 9 found that choosing to continue as friends still allowed later romance scenes.
The friendship-only flag now excludes the romantic outer-shoals, shore-week, and new-sail scenes.
That choice enters a separate friendship voyage and correspondence continuation, with no romance or partnership flag award.
Focused source assertions cover every exclusion and the platonic continuation.
No review score, readiness, or route approval is claimed.
A fresh rereview of the exact current snapshot remains required.

## Chronology and native evidence

The proposed ordinary opening follows the native Colyphyr Tumberd service exchange, at which Mielarah offers Starcatcher the Third and its crew.
The inspected cues establish her service offer and alive-at-that-dialogue moment only.
They do not establish a parent answer chain, persistent contact flag, later actor placement, or an extension hook for this contribution.
The authored chart conversation and all later ordinary scenes therefore require a future producer that has not been implemented.

The native crash binding is specifically conditional: AirAdventures `Cue_0426` GUID `1b4e78245cb3a244588f9ec0fda54ea8` requires `Answer_0351` GUID `b98a0a14e5741ea4c90ae015154bc861` selected and `CaptainMielara` etude GUID `8d0fcb697a43a464fa7119e274bf9d7b` playing.
The cue depicts the Gravedragger panic, Mielarah losing the wheel, and the Ishiar crash.
The native raid outcome uses `Answer_0404` GUID `1eececde9d7a70c44be526ea668f3ed4` and `Cue_0482` GUID `dbec675b71e9d5f4d96055f4bb31762e`, which depicts her protest and death.
The authored Trickster landing, ship repair, three-day passage, and return to a Tumberd berth remain counterfactual fiction.
No inspected native state proves survival, later Colyphyr presence, healer availability, cue suppression, or campaign continuation after the crash.
No interception hook or runtime producer is claimed.
Failure, refusal, or boundary violation cannot be treated as reaching the authored alternate history.

## Scene sequence and characterization

The opening continues through the chart invitation, conditional Trickster intervention and landing, authored arrival bridge, Mielarah's delayed note, amulet case, captain's evening, crew meeting, and quay day.
The ordinary contact premise remains conditional on a future verified producer.
The Trickster concept remains a proposed pre-crash intervention, not a working path.

The repair ledger, sail trial, and storm watch follow the quay-day invitation.
A later departure notice branches into a personal exchange with Jori or a separate meeting that makes no claim about a private answer.
A source-level graph assertion verifies that only the Jori conversation can set the flag consumed by the private-answer branch.

The short voyage gives a crew member the chance to refuse the amulets.
Mielarah takes the longer route and accepts a lost contract rather than compel him.
The player can affirm a shared future, defer, or end the courtship over the possibility that she may use coercive magic again.
The previous friendship-only option now enters a distinct platonic voyage.
That scene allows the Commander to travel as a friend or stay ashore and continue letters.
It sets a friendship-continuation flag only and awards no romantic future, date, or partnership state.
The romantic outer-shoals scene rejects the friendship-only flag.

A shore-week dinner follows only an open or deferred romantic outcome and after a seven-day delay.
If the Commander leaves at dawn, a distinct short-visit endpoint records the departure without setting full-week completion.
A full stay leads to a sail-contract scene, where Mielarah catches an overcharge, negotiates it herself, and accepts a written loan only if she chooses those terms.
The new act asks whether the Commander wants the ordinary partnership she can offer, a slower future, or a clean ending.
Both shore-week and new-sail scenes reject friendship-only history.
The Commander can remain a friend or leave, but cannot continue to romance or partnership outcomes after choosing friendship-only.
These are authored expansions, not base-game events.

The route keeps Mielarah proud, abrupt, fallible, and capable of wanting the Commander while retaining command of her ship.
Relationship development has visible costs in wages, crew trust, lost income, a delayed sail, and decisions around her curse.
The mature intimacy remains sensual and graphic and explicit, with initiation, choice, and stopping or departure branches.
Her coercive past is neither absolved nor repaid with intimacy.

## Remote delivery and validator

All sixteen scenes set `ManualOnly=True` and `Remote=True`.
The source check reads `src/Story.cs` and verifies the validator predicate `if (scene.ManualOnly && !IsRemote(scene))`.
This combination passes that source-level condition.
It does not prove a credible in-game meeting or physical presence.
The scenes remain unregistered and have no native `ContactUnit`, verified location restriction, or actor attachment.
Manual remote delivery is only an authoring fallback pending a reviewed integration design.

## Focused checks and measured scope

`py -3.12 -m py_compile storylines/mielarah_route_opening.py` passes.
Running the module reports sixteen unregistered scenes and 168 nodes, then passes node uniqueness, local topology, graph reachability, external-state, branch, delay, refusal, contradictory-state, and remote-validator assertions.
The focused transition checks require quay-day completion before the ledger, the ledger invitation before the sail trial, the trial invitation before the storm watch, the completed watch before the crew departure notice, and the crew invitation before either the romantic or friendship voyage.
They verify the Jori history distinction, all three romantic voyage endings, friendship-only access to the platonic continuation, friendship-only exclusion from romantic outer-shoals, shore-week, and new-sail scenes, the seven-day shore duration, the short-departure boundary, and the delayed new-sail scene after a full week.
These checks test the author-authored Python model only; they do not establish that a producer writes contracted flags or that the game scheduler delivers scenes in chronology.
They do not exercise registered export, runtime flags, save/load, or in-game delivery.

The repository tokenizer measures 16,569 raw words: 13,050 prose words and 3,519 choice words.
It finds 16,539 distinct normalized segment words.
The eight latest local scene graphs have maximum branch sums of 477, 545, 795, 664, 540, 276, 776, and 827 words respectively, or 4,900 together.
The friendship voyage is mutually exclusive with the romantic voyage.
Independent rereview 9 measured 9,882 ordinary and 9,569 Trickster words along the longest valid romantic progression through the new-sail completion before the friendship-only split was added.
This revision preserves those romantic choices and adds a separate friendship continuation.
Those remain modeled source paths rather than integrated in-game playthrough counts.
All routes remain below the hard 21,000 meaningful-word requirement.
The contribution is incomplete.

The source SHA-256 for this revision is recorded in the handoff because the report cannot contain its own stable hash.
The report SHA-256 is likewise provided in the handoff.
No review score, readiness, or integration approval is claimed.

## Remaining work

- Verify the exact native parent-choice chain and produce ordinary contact only while Mielarah is alive and available; then establish credible later scene delivery.
- Implement and test Trickster answer interception, native cue suppression, campaign progression, survival state, repair sequence, and save/load behavior.
- Design, implement, and verify attainable character-appropriate routes for all ten mythic paths, including death, expulsion, rescue, and unavailable histories.
- Expand each intended route to at least 21,000 meaningful reachable words and measure selected paths through the integrated story.
- Continue the relationship with further consequences for the curse, captaincy, crew, and shared future without making Mielarah compliant to unlock content.
- Create and independently review art against her in-game model and the project's redesign constraints.
- Resolve whether manual remote delivery is credible for the narrated settings or replace it with a verified physical event/contact integration.
- Verify ToyBox Free Love and No Jealousy compatibility after registration; no such check is claimed here.
- Obtain fresh independent canon, chronology, character, craft, chemistry, consent, path, runtime, scope, and art review of the exact revision.
- Keep the scenes unregistered until required gates pass, then run headless integrated validation before manual in-game evaluation.
