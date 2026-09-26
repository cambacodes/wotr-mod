# Konomi early reciprocity handoff

This contribution addresses item 3 of the assembled Konomi audit with an optional played encounter before established intimacy and four earned callbacks during the original first supper.
The author does not assign approval scores.
Shared registration, independent review, combined checks, and export promotion remain with the parent agent.

## Frozen release

| File | SHA256 |
| --- | --- |
| `storylines/konomi_early_reciprocity.py` | `DA17B6053180AE3C6D8372057B84A712ECE257BA89FB09472DED9D35FD79D1CC` |
| `tests/KonomiEarlyReciprocityTests.cs` | `9BF092200052E639E7DB537697BCC33FC1E9A3FDE9A06C5ABD8833097E2A3A6A` |
| `development/Story.json` input | `F9D935107A1CD0DD503A60C5C77A6575289204FC4E19001070F8FB2123017E84` |
| Standalone staged `after.json`, 292 scenes | `0076E2184ED4BC2295E1DA9CC6BB5F6ED0BF155C5A0D0B6540B25153C6D3943B` |

## Encounter and canon boundary

`konomi.a_turn_for_herself` follows the already played reception while Konomi holds her office.
She wants to finish a dance she enjoyed and arranges a private borrowed room herself.
The Commander can follow her, lead with her corrections, or learn alongside her without holding hands.
These choices produce distinct played choreography without a skill roll that would turn competence or disclosure into a prerequisite for attraction.

The subsequent shutter choice lets the Commander request quiet because of habitual vigilance, prefer ordinary street noise, or choose pleasure without disclosing a hurt.
Konomi answers each specifically and expresses her own wants.
The pleasure branch allows either improvised play or watching her enjoy a beautiful movement.
The resulting quiet, street, play, or beauty memory unlocks its own appended answer at `konomi.evening/supper`.
Every callback rejoins the original kiss, night, transformed companionship, and quiet options with their original conditions and effects.

Native characterization was read in `reference/story-review/Konomi.txt`, `reference/expansion/konomi.txt`, and the political-state evidence.
The native introduction identifies an authoritative attaché and noble kitsune from Tian Xia.
Her recruitment of council members, royal-policy pressure, patronage bargaining, and shifts in confidence support precision, pride, strategic interest in recognition, and an appetite for influence.
The source preserves those qualities without making the Commander purchase political agreement through affection.

Her dancing, soft shoes, borrowed room, sleeve, and remembered maid are authored personal developments.
They are not native facts, a new festival, a claimed Tian cultural tradition, or an implemented dance skill.
The reception itself belongs to the existing authored romance.
The scene does not claim to alter native politics, payments, inventory, or placed room objects.

## Access and save continuity

The new scene requires `konomi.present` and the completed `konomi.reception`, accepts Chapters 3 and 5 in Drezen, and has zero delay.
It is optional and adds no requirement to `letter` or `evening`.
Those invitations keep their existing 24-hour waits.
Fresh Chapter 5 acquisition receives the same present-tense scene, without invented Chapter 3 memories or Abyss absence.

`konomi.evening` or `konomi.lovers` prevents a compulsory return to early courtship on established saves.
Dismissal, an inhuman body, or relationship closure prevents this embodied early outing; the existing dismissed and transformed routes remain unchanged.
Declining the hour aborts without consuming the scene or closing any relationship.

The exact `ContactUnit` is `ca2d58c5c65723945857e04fb85d30ce`.
The scene uses existing answer list `0dc8b8604bb33c846a63f3eb62443674`.
`reference/canon-review/konomi-physical-contact-plan.md` and its records establish the native officer spawner, unit, dialogue, answer list, and hidden-state limitation.
The new scene requires the actual loaded actor through the shared contact guard as well as the office predicate.
Losing native contact, office presence, valid area, or chapter suspends continuation through the existing guard.
No actor is unhidden or created.
The narrated visit is delivered through that native conversation attachment; an actual Unity room transition is not implemented.

Each later callback requires both the completed new scene and its matching choice flag.
A partial preference saved before completion therefore cannot fabricate a completed memory at supper.
An interrupted encounter can be retried, and actually played preferences from multiple attempts may remain as history under the existing monotonic flag model.
No timestamp migration or flag clearing is introduced.

Original scene metadata and text are untouched.
Original node IDs and answer indices remain unchanged.
The overlay appends four answers to `evening/supper` and four new nodes; duplicate integration raises an error.
The callback nodes copy the four original supper options rather than changing their effects.
Neither the private-career author's module nor any shared source/export was edited.

## Verification

The standalone candidate passed `Rules.Validate` and 3,464 focused assertions, including the existing harness traversal assertions.
The harness compiles actual `src/Story.cs`, reuses `tests/Program.cs` through its `Copy` and `Walk` helpers, and calls the owned test directly without shared registration.
It remains in `C:\Users\Z\AppData\Local\Temp\konomi-early-1tkbagrq`.

```powershell
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --project 'C:/Users/Z/AppData/Local/Temp/konomi-early-1tkbagrq/Check.csproj' -c Release -- 'C:/Users/Z/AppData/Local/Temp/konomi-early-1tkbagrq/after.json'
```

Result: `PASS 3464 early reciprocity assertions`, exit code 0, with no build warnings printed.

The tests play actual margin, reception, encounter, letter, and evening sequences in Chapters 3 and 5.
They traverse all 12 complete combinations, verify distinct earned callbacks, preserve other romances and office history, and retain the original invitation deadlines.
They also play the skip path through intimacy, reject replay for established lovers, test partial saved preference flags, and reject missing contact, missing office, dismissal, closure, transformation, wrong area, and Chapter 4 entry.
Native contact loss is tested during continuation, with restoration allowing resumption.
A later transformation after the dance preserves the remembered callback while excluding embodied kiss/night choices and retaining the original companionship result.

A structural comparison against the original evening found unchanged metadata, original node text, and exact original answer prefixes.
Using the existing content tokenizer, the new prose and answers contain 1,864 distinct words, excluding the duplicated existing supper options.
The encounter has 12 complete traversals of 777-818 selected words, counting only visited text and selected answers.
Alternative preferences and callbacks are not summed into a fictional single playthrough.

These checks exercise source-model availability and dialogue traversal, not Unity rendering, live-save input, native actor execution, or ToyBox runtime behavior.
No full-route parity or final art approval follows from this contribution.

## Integration

Add this module's `SCENES` once and invoke its `integrate(payload)` after the original Konomi scenes are assembled.
Register `KonomiEarlyReciprocityTests.Run(story, Check)` in the shared test runner and rerun combined verification.
The ordinary actor metadata upgrade across other scenes is separate parent-owned work.
Independent review should judge the personal activity, the specificity of Konomi's responses, and whether the early placement improves the assembled pacing.
