# Soana v12 scene assignment review

Reviewed on 2026-09-26 by the independent art reviewer.
Approve `SoanaForest` as a general character portrait for the five pages below.
Do not stage it under the global `Soana` key.
No source, asset or installed file was changed for this review.

## Evidence and scope

I viewed `art/expansion/originals/Soana-v12.png` at original detail and read the v11 and v12 reviews.
The reviewed image SHA256 is `323F34726445958368D1441E4929D83C33258457BEF0CDD0B54F429701856334`.
I screened all 35 Soana scene openings and their page inventories in the current development export, comprising 23 visits and 12 ending scenes with 236 pages overall.
I read the complete water-carrier visit and guardian conversation when deciding where the visible carrier's state fits.
The remaining scene openings establish enough setting or activity to exclude them from this deliberately narrow assignment.
This is an assignment assessment, not a new literary review of every route page.

The image shows Soana fully dressed in practical forest clothing, seated on stone in warm daylight, with a dark rocky opening behind her.
She holds a clay vessel's woven carrier and a loose strip near its rim.
The forest and cave surroundings suit her daylight carrier-work visit.
The current art brief expressly permits her attractive adult redesign without rewriting her age or biography.
Consequently, prose about her age does not itself disqualify the portrait or justify restoring the rejected severe facial wrinkles.

## Exact recommended assignments

Assign `Portrait = "SoanaForest"` only to these scene and node pairs.

| Scene ID | Node ID | Why the general portrait fits |
| --- | --- | --- |
| `soana.water_carrier` | `start` | She has brought the clay pot and damaged wicker carrier into daylight and asks the Commander to sit nearby. |
| `soana.water_carrier` | `promised` | Reed preparation takes place at the same outdoor workstation before the repair. |
| `soana.water_carrier` | `work` | The pot and carrier remain the subject of the visit while the two begin weaving. |
| `soana.water_carrier` | `hands` | The same outdoor work continues as she explains how to turn the reed. |
| `soana.water_carrier` | `own_work` | The Commander finishes a crossing at the same workstation before the handle is completed. |

These assignments use a static character portrait in the setting of the scene.
They do not claim that the picture shows every narrated movement, the Commander's offscreen hands, the awl or the exact fingers-over-fingers instruction.
The native text says the cradle split at one handle; the image's most obvious gap is in its body below the rim.
That difference rules out describing the image as an exact reconstruction of the damage, while permitting general carrier-work presentation.
The earlier 87 assessment of exact reed insertion remains unchanged.
It is not averaged into a passing score or hidden by this assignment.

Suggested staging description: "Soana in daylight beside her forest cave, with her water pot and woven carrier; a general character portrait for the early carrier-work pages."
Do not caption it as a demonstration of the repaired crossing or a literal depiction of her guiding the Commander's fingers.

## Remaining pages and scenes

| Scene or group | Assignment decision |
| --- | --- |
| `soana.water_carrier`: `flowers`, `flower`, `learned`, `marriage`, `thanks`, `finish` | Exclude from this initial mapping. The narrative has advanced to a visibly repaired handle, a flower exchange, handing over the vessel or testing the completed repair. The image still emphasizes a loose strip and open gap. |
| `soana.water_carrier`: `stream`, `attraction`, `company` | Exclude. These take place during the stream journey rather than seated at the cave workstation. |
| `soana.threshold` | Exclude. Its basket is an overturned animal trap with a cut strap, not the upright carrier surrounding this large pot. |
| `soana.guardian_question` | Exclude. The pot is explicitly beside her in its repaired carrier and the visit is a seated argument, not unfinished carrier work. |
| `soana.one_account`, `soana.price_of_warning` | Exclude from the initial mapping. Their prepared writing and warning discussion provide no positive connection to renewed carrier work. |
| `soana.watch_line`, `soana.lower_bend` | Exclude. These visits move onto forest paths, the warning crossing or the lower bend. |
| `soana.ordinary_feast`, `soana.name_between` | Exclude. The seating is prepared for food or a personal conversation, and the prominent active craft setup would distract from those changes. |
| `soana.the_thing_in_the_sack`, `soana.the_inherited_debt` | Exclude. The cave-side meetings center on a dangerous sack or Meret's family debt, with distinct objects and participants. |
| `soana.the_dry_offering`, `soana.a_voice_in_the_dark` | Exclude. The action moves toward the shrine and ritual ground; the latter also proceeds toward darkness with sleeves specifically secured for the working. |
| `soana.what_followed_home` | Exclude. Soana is explicitly farther inside the cave where light does not reach her face. |
| `soana.a_promise_still_spoken` | Exclude. She puts a letter aside and faces the Commander with empty hands. There is no carrier work to support this prominent prop arrangement. |
| `soana.the_unwelcome_path`, `soana.a_track_with_two_ends`, `soana.where_the_steps_end` | Exclude. Path inspection, tracking and the thorn experiment need their own setting or neutral portrait. |
| `soana.after_the_last_visitor`, `soana.before_the_far_road` | Exclude. Evening company, a clean shawl, shelter and later intimacy are deliberate changes from practical daylight work. |
| `soana.when_the_road_returns`, `soana.what_the_hollow_costs`, `soana.the_days_she_counted` | Exclude from the initial mapping. Their roots, visitors, stores and marked thorn establish later activities rather than a return to repairing the carrier. |
| All 12 `soana.ending_*` scenes | Exclude from this initial mapping. Retrospective portrait use is possible in principle but needs a separate decision, especially for death, destroyed forest and rewritten-history branches. |

These exclusions are conservative assignment choices, not a rule that static portraits must match every sentence's gesture.
A less activity-specific Soana portrait could cover many of these conversations.
This particular picture gives the pot, working strip and damaged-looking carrier enough prominence that applying it globally would obscure real changes of setting and activity.

## Staging and transition requirement

The existing staging convention uses full images at `art/CustomNpcPortraits/RanRomance-Tirabade/Scenes/<key>.png` and explicit per-page `Portrait` strings.
`src/Main.cs` resolves that key and loads the whole image for the book event.
No fixed registry prevents the new `SoanaForest` name.
This review therefore finds the explicit key structurally appropriate, but does not stage it or certify its loading in Unity.

I checked a possible transition problem in the inspected `BookPatch.Postfix` implementation.
It assigns `EventPicture.Value` only when the portrait loader returns a non-null sprite.
If a later page refers to a missing `Soana.png`, this patch does not explicitly clear the previous `SoanaForest` image.
Fresh decompilation of the installed `Wrath_Data/Managed/Assembly-CSharp.dll` resolved that concern.
Native `BookEventVM.SetPage` calls `SetPicture(page)`, which first sets `EventPicture.Value = DefaultSprite` and then attempts the native page image.
The checked-in `reference/game-BookEventVM.cs` records the same behavior at lines 75-84 and 130-141.
The addon's postfix therefore runs after the native image reset on an ordinary page transition.
No stale-image bug is established and no change to `Main.cs` is required by this assignment review.
With no global `Soana.png` staged, excluded pages retain their native default or page image instead of this scoped illustration.
This conclusion comes from the installed native code, not from executing the Unity page transition.

Runtime book-image sizing, loading, page transitions and small portrait crops remain separate checks.
This assignment approval does not approve the whole Soana route or an installed release.
