# Kiana consequence continuation handoff

Source: `storylines/kiana_consequences.py`.
Frozen SHA256: `10F909E147FAF874A27F5008C2E241423D1D600C9E46B2E0D049593EBB81F574`.
This recovery preserved four surviving scenes and added the missing fifth scene, the roof supper that pays off the invitation and clothing choices.
The interrupted source had an unterminated string in the picture response, which is repaired.
Both source and this handoff are released to the parent.
No shared source, export, tests, art, native assets or installed files were edited.

## Contribution and insertion

Import `SCENES` from `storylines.kiana_consequences` and append its five scenes to Kiana's development content.
Their availability requires `kiana.morning` and the existing native `seelah.souls_returned` alias.
The narrative insertion is after `kiana.morning` and before `kiana.farewell`.
All are optional remote Drezen book events in chapter 5.
The new helper forbids `kiana.closed`, `kiana.farewell` and `inhuman`.
It deliberately does not forbid `loss`, which `src/Main.cs` derives from the Tirabade wives' death, departure or sacrifice rather than Kiana's circumstances.

| Scene | Predecessor | Delay | Content |
| --- | --- | --- | --- |
| `kiana.guest_table` | `kiana.morning` | 48 hours | Kiana introduces civilian friends; the Commander can answer a thoughtless remark or leave Kiana to answer it. |
| `kiana.market_weather` | `kiana.guest_table` | 24 hours | An outing, a new shawl and an overlooked invitation; waited, affair and widow histories receive distinct conversation. |
| `kiana.lenna_door` | `kiana.market_weather` | 24 hours | The friend explains her withdrawal; the earlier speaker choice changes the encounter and available responses. |
| `kiana.blue_room` | `kiana.lenna_door` | 48 hours | Private preparations recall the established letter or picture, offer pin choices and allow kissing or hand-holding. |
| `kiana.roof_supper` | `kiana.blue_room` | 0 hours | The promised supper pays off the pin and public/quiet choice, returns Kiana to ordinary company and recognizes her prior marriage. |

The last scene follows the preparation on the same narrated evening, so it has no authored waiting requirement.
The runtime still queues remote scenes through rest handling.
Testing must establish whether that delivery presents this sequence coherently; zero delay does not itself prove same-evening Unity delivery.
Do not silently make the contribution mandatory by adding its completion flag to old farewell requirements.
The existing changed-body branch remains separate, and an older development save may already have reached farewell.
Full-route integration needs an explicit migration and pacing decision.

## Native evidence and authored developments

Native evidence is in `reference/canon-review/kiana.txt`, `kiana-authoring-predicates.json` and `kiana-appearance.md`.
The native adult Kiana is an oread with blue skin, a pale crystalline head silhouette and explicitly described blue-green eyes.
The authored prose preserves that appearance.
The wedding vampire princess is costume play, not true vampirism or a transformation.
Native married and widowed aftermaths are distinct; `seelah.elan_dead` is not inferred merely from a tragic tone or a desperate Elan state.

All five new events, Lenna, Odrin, Edris, Meral, their occupations and shared history are authored alternate developments.
No claim is made that these civilian friendships or Elan's table-moving anecdote appear in the game script.
Kiana's separation and the optional earlier affair are developments from the existing expansion, not canonical marital outcomes.
The picture and surviving letter are recalled from `kiana.morning` rather than introduced as newly discovered native facts.
The source neither recruits civilians nor creates physical NPC actors, native quest outcomes, equipment or wealth changes.

The scenes retain Kiana's theatrical humor, romantic initiative and ability to discuss her former partner without degrading him to justify the Commander romance.
The affair path explicitly remembers the kiss before the separation conversation and her responsibility for it.
The waited path remembers waiting.
The widow path allows grief and present affection together without treating the Commander as a replacement Elan.
This description is author intent, not independent characterization approval.

## State changes

The engine records the five scene IDs as completed.
The module sets only these additional authored flags:

```text
kiana.guest_table.spoke
kiana.guest_table.listened
kiana.guest_table.kept
kiana.market_weather.public
kiana.market_weather.quiet
kiana.market_weather.walked
kiana.lenna_door.plain
kiana.lenna_door.rank
kiana.lenna_door.listened
kiana.lenna_door.invited
kiana.blue_room.letter
kiana.blue_room.picture
kiana.blue_room.learning
kiana.blue_room.leaf
kiana.blue_room.round
kiana.blue_room.kissed
kiana.blue_room.ready
kiana.roof_supper.performed
kiana.roof_supper.told
kiana.roof_supper.quiet
kiana.roof_supper.kept
kiana.consequences_ready
```

It does not create, reset or remove Kiana's love, commitment, affair, separation, widowhood or waiting flags.
It does not alter native quest state, other romances, ToyBox settings or exclusivity.
`kiana.consequences_ready` is a future integration hook, not a full-route readiness claim.
Existing scene IDs, node IDs and choice indices in shared modules remain unchanged.

## Checks actually performed

A direct Python graph walk imported the module with bytecode writing disabled.
It enumerated all eligible choices through all five scenes for waited, affair and widow histories, each committed and uncertain, both with and without unrelated Tirabade loss.
It applied authored choice flags and completed scene IDs while retaining the input native history and an unrelated Arueshalae commitment.
All 56 nodes were reached across 2,304 complete paths and 24,716 traversed choice edges.
No missing target, cycle, empty eligible choice set, abort mutation, lost preexisting flag or manufactured commitment was found.
An earlier pass also checked new scene IDs against the existing Kiana module and found no collision.
The walkthrough models valid existing histories, not arbitrary contradictory flags injected by a save editor.
The generic `loss` gate was removed after checking its real derivation in `src/Main.cs`; the final walk proves those unrelated loss histories remain traversable.

The project inventory functions measured 6,378 raw words, 5,792 prose words, 586 choice words and 6,326 distinct whole-segment words in the new module.
Complete paths through this contribution contain 4,002 to 4,298 words using the same tokenizer and only the selected choices.
The existing Kiana module plus this contribution totals 22 scenes, 10,305 raw words and 10,231 distinct whole-segment words.
These combined inventory figures do not establish attainable full-route length or semantic originality.
The character remains well below the 21,000-word planning floor.

## Remaining gates

No independent quality score is assigned by this author.
Independent writing and canon review must inspect the frozen source, including whether the invented friendships, humor and grief balance remain convincing across the full sequence.
The parent must add engine-level progression checks, export verification, binding validation and managed-construction checks after accepting the contribution.
The direct graph walk is not a test of remote queues, chapter transitions, timestamps, relationship journals or Unity execution.

The contribution adds no new art.
All nodes use the existing `Kiana` portrait key, whose staging, crop and native likeness need art and in-game review.
Headless source checks do not prove game-save, ToyBox, portrait or physical-scene behavior.
The broader route still needs substantial content, complete-route review, bespoke attainable Trickster access beyond the currently accessible native aftermath, and the remaining release verification.

## Parent integration correction

Final source SHA256: `75CAAD005CC28DAF4AE54690C9CEADAC997A4668C6CB5C5C98A8CA83903E2AC6`.
The boot description now says dried rather than soaked beside the fire.
Preparation and roof supper are composed into one continuous book because zero delay alone still required another rest.
The redundant late supper abort is removed; the initial preparation deferral remains.
All continuing preparation paths must reach supper in the production-rules checks.
This contribution therefore adds four scene entries, with five narrative sections and the same remaining decisions.
The current total Kiana inventory is 10,295 raw and 10,221 distinct-segment words, still incomplete.
