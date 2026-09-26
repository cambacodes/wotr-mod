# Konomi ordinary-contact independent review

Reviewed on 2026-09-26 independently of the proposed contact change.
Decision: adding `ContactUnit = ca2d58c5c65723945857e04fb85d30ce` to the identified ordinary physical meetings is technically justified.
Keep their existing `konomi.present`, chapter, area, history and choice gates.
Do not apply that metadata to every scene that requires `konomi.present`.
The solitary remote invitation is a concrete exception.
No shared source, module, test, installed asset or original evidence record was edited during this audit.

## Independent asset reproduction

I reran `tools/probe-konomi-contact.py` through `reference/asset-extraction-env/Scripts/python.exe`, changing its output destination in memory only.
The capture is `C:/Users/Z/AppData/Local/Temp/konomi-contact-independent-qex9l5cn/records.json`.
It recovered two scene objects and four native blueprints, and its parsed result equals the parent's saved `konomi-contact-records.json` exactly.

| Input | SHA-256 |
| --- | --- |
| Installed `Bundles/drezencapital_default_mechanics.scenes` | `D451FEF29C6B22F5D13E8BACEA70BA063175DDEE8B3F43F48D6CAE7F22B4A9E3` |
| Probe source | `2E759ABBED7A5C726982249094D95BCBF31AC2A213B4D82A6C8459044F224940` |
| Parent saved contact records | `D2AF29F3EAB3D4877D59731C095974464FD87A143D853D9DC3995AC708804F40` |
| Inspected `src/NativeContact.cs` | `018BE371E40D1950564D6C74D1EB79CD195E781DCF2C28FA0A8CC826D10170B3` |
| Inspected `src/Story.cs` | `D6AF931FA196A40A16E9D791D711B04AB308DD054AA3AFF5D995A4A7C30C0B48` |

GameObject 535 is `RankUpOfficer_Diplomacy`.
Its component 2855 has unique spawner ID `c658c4cf-116e-4b61-9ff9-8905bcf4fd6b` and unit blueprint `ca2d58c5c65723945857e04fb85d30ce`.
It has `m_SpawnOnSceneInit=1`, empty spawn conditions, and `m_RespawnIfDead=0`.
Component 2856 binds dialogue `a81655ed97277974e947c1aaf9e33525` without a component-level condition.
Component 2857 has `m_SpawnHidden=1` and `m_SleepWhenFarAway=1`.
I separately scanned all MonoBehaviours in the bundle for the exact unit reference and found only component 2855.
The probe's object-name filter therefore did not conceal a second same-blueprint spawner in this bundle.

GameObject 521 is `DiplomacyOfficer_Position`.
Its locator component 2829 carries `e6a7de2a-ce6f-4413-b24d-06daf1990e4c`.
Its transform has local position approximately `(-28.41, 53.5, -24.97)` under parent transform 1074.
Those are local coordinates, not a verified replacement spawn destination or world-space navmesh claim.

The installed blueprint record resolves the unit's localization key `a2c32cde-bf45-4648-9d85-eb465bfc1033` to `Lady Konomi`.
The proposed contact identity therefore follows the actual scene binding and native unit, not a guessed display-name match.

## Native presence and dialogue chain

The replayed presence etude is `b5f301fbc4c44535a6309d610d5bd28a`.
Its repeating play trigger unhides that exact spawner and translocates it using the exact locator's position and orientation in scene `3e2b5ea054cd5b2479e7f13134363ef4`.
It requires NotInCombat `e0d8b253efedb70488badaaa3d47632c` Playing and links to Drezen `2570015799edf594daf2f076f2f975d8`.
It contains no death check and therefore does not replace a live-actor observation.

I also reopened the native hidden fallback and both ordinary greeting cues from `blueprints.zip`.
Fallback `0b828275326053d4cb989baddb20bce7` hides the same spawner and has priority -100 in conflict group `12b19db05c70a2a4fa3210293d35bfd0`.
The positive presence etude has priority -20 in that group.
Rank-up displacement and dismissal must remain native-controlled, as described in the existing availability audit.
This review does not restart or override those states.

Dialogue `a81655ed97277974e947c1aaf9e33525` is the component-bound ordinary root.
Cue_0001 `3269417315940ed4daf2a345b5812c4f` is ShowOnce, while Cue_0002 `bd0fd5f2a10163941a4e01ada9edc850` repeats.
Both supply answer list `0dc8b8604bb33c846a63f3eb62443674`.
The root and answer list have no additional conditions that would make the ordinary insertion one-shot.
The actor must still be available to enter that native conversation.

## Exact metadata scope

I enumerated the current result of `expansion.make_expansion()` without exporting it.
These 22 existing scenes are ordinary physical meetings and require `konomi.present`:

```text
konomi.margin
konomi.reception
konomi.letter
konomi.evening
konomi.disagreement
konomi.leak
konomi.reckoning
konomi.return
konomi.power
konomi.ordinary
konomi.farewell
konomi.parting
konomi.hearing
konomi.hearing_after
konomi.new_letter
konomi.political_account
konomi.a_useful_supper
konomi.the_upper_passage
konomi.two_bad_prices
konomi.the_trial_day
konomi.a_name_beside_hers
konomi.the_evening_she_kept
```

The separately staged `konomi.a_turn_for_herself` in `konomi_early_reciprocity.py` already has the correct ContactUnit and belongs in the physical group when integrated.
The scenes named `konomi.letter` and `konomi.new_letter` contain ordinary meetings despite their names.
They must not be excluded by a substring rule.

The solitary scenes `konomi.unsent` and `konomi.another_evening` must remain unitless.
`konomi.another_evening` is a remote manual invitation read alone in Drezen and still legitimately requires `konomi.present` as history/context.
Adding ContactUnit to it would make reading a received invitation depend on a currently loaded officer view.

These remote private-route scenes must not inherit the ordinary officer contract:

```text
konomi.fate_post
konomi.fate_reply
konomi.private_meeting
konomi.private_history
konomi.carriers
konomi.before_road
konomi.private_departure
konomi.capital_letter
konomi.return_offer
konomi.private_reunion
konomi.lease_offer
konomi.chosen_evening
konomi.private_future_choice
konomi.private_hearing
konomi.private_hearing_after
konomi.private_new_letter
konomi.private_political_account
konomi.private_absence
konomi.private_absence_catchup
```

The separately staged `konomi.private_return_terms`, `konomi.private_kept_hours`, and `konomi.private_last_visit` are also remote private-route scenes and excluded.
Some private scenes narrate in-person visits; their current delivery still needs its own presentation verification.
The hidden dismissed officer cannot be used to certify those visits by assigning her old ContactUnit.

All current epilogues are excluded:

```text
konomi.ending_public
konomi.ending_private
konomi.ending_changed
konomi.ending_ascended
konomi.ending_apart
konomi.ending_dismissed_apart
konomi.ending_unfinished
konomi.ending_aeon
konomi.ending_distance
konomi.ending_distance_open
konomi.ending_distance_apart
konomi.ending_distance_changed_open
konomi.ending_distance_ascended_open
```

The staged `konomi.ending_distance_lived` and `konomi.ending_distance_open_lived` remain excluded too.

## Entry and interruption behavior

`NativeContact.IsAvailable` requires exactly one loaded-state unit matching the blueprint, a current valid storage membership, a loaded active view referring back to that unit, in-game and unsuppressed state, consciousness, no death/final death, and no hostility toward the Commander.
It rejects loading/unloading, combat, an unconscious Commander, disposed/destroyed actors, absent views, and multiple matching units.
It observes without calling `DialogSpeaker.GetEntity`, which could wake or restore a speaker.
It accepts valid current cross-scene storage for native units as well as storage in the current area's scene states.
That broader storage support does not make an unloaded view eligible.

The observer identifies the unit by blueprint and uniqueness, not by the spawner's saved entity ID or distance from its locator.
The exact spawner evidence establishes the intended native actor; it does not certify an arbitrary single same-blueprint actor inserted by another mod.
No additional registry or spawn mechanism is needed for this scoped ordinary-contact change.

`Rules.Available` applies contact at entry.
The queued start rechecks availability before opening the book.
For contact-backed scenes, `Rules.ContactAvailable` rechecks the actor, chapter/area, all Requires predicates including `konomi.present`, RequiresAny, native forbids, and relationship-wide unavailability.
Temporary disappearance or suspension of the presence etude therefore stops further choices even when the book was previously eligible.
The action path rechecks immediately before recording progress, and native skill-check conditions also use the continuation check.
Each page receives a contact-lost exit with no progression effects.

This is suspension, not rollback or relationship closure.
It does not erase previously selected flags, complete the scene on behalf of the player, or remove native dismissal history.
Previously displayed prose is not withdrawn, and a skill check that has already advanced may display its next page before only the leave option remains.
Restored normal contact permits normal replay of an unfinished scene under its own existing prerequisites.
The generic continuation function intentionally does not reapply every authored forbid, closure flag or delay midscene.
Derived flags such as `inhuman` are not automatically classified as native by that helper.
Do not claim this metadata change introduces a universal midscene state validator beyond its actual predicates.

## Reproduction and integration fixtures

An isolated C# probe compiled the actual `src/Story.cs` and read a temporary in-memory export.
It reproduced all 22 ordinary scenes accepting a presence-only state with no available Konomi actor.
Assigning ContactUnit only in that temporary process rejected absence, accepted valid contact, rejected midscene presence loss and actor loss, and allowed contact after a temporary presence suspension ended.
It also checked that the remote invitation retained its separate contract.
Result: `PASS 199`.
Temporary project: `C:/Users/Z/AppData/Local/Temp/konomi-contact-rules-audit-j0oxnpnw/Audit.csproj`.
This is an actual Rules-level differential reproduction, not a fresh Unity interaction.

Permanent integration fixtures should cover the exact physical inclusion set and all exclusions above.
They should test presence true with no actor, actor available without presence, valid ordinary contact, rank-up displacement followed by return, dismissal after a book starts, actor disappearance before queued opening, and loss before a skill-check or terminal selection.
They should verify that the contact-lost exit writes nothing, existing IDs and authored answer indices stay unchanged, completed scenes do not replay, and already-recorded progression is preserved.
Managed observer fixtures should retain current-area and cross-scene storage cases and reject stale storage, duplicate blueprint matches, hidden/inactive view, unconscious/dead/hostile actors and combat.
These engine-observer cases are separate from merely adding a GUID to a Snapshot.

No source-evidence blocker remains for the scoped metadata change.
Live Chapter 3/5 native dialogue, rank-up return, save/load and hidden-actor behavior remain runtime verification work.
This review gives no approval for the private route's actor delivery, a resurrection implementation, writing quality, art, or a full campaign.
