# Soana living Chapter 5 campaign handoff

## Release and integration

Author ownership is limited to `storylines/soana_late_campaign.py`, `tests/SoanaLateCampaignTests.cs` and this report.
No existing Soana source, builder, generated payload, native blueprint, installed asset or shared test registration was changed.
The source is frozen for independent review, with no author-assigned scores.

| File | SHA256 |
| --- | --- |
| `storylines/soana_late_campaign.py` | `B938947E6E84F926A825C82B739EF03A2A416B9D37609B5441A5C86497AB2018` |
| `tests/SoanaLateCampaignTests.cs` | `547D2C13C0ECC3ED5D5F07F112B98A5E20FE0B524A38BCFC4DB20AC14737ECE5` |

The module exports eighteen `SCENES`: six local visits and twelve epilogue scenes.
Integration requires appending a deep copy of `SCENES` and registering `SoanaLateCampaignTests.Run` in the root-owned harness.
No overlay, native alias map or relationship metadata mutation is required.
Existing scene IDs, choice indices, gates and earned history remain untouched.

| Visit suffix after `soana.` | Delay | Development |
| --- | --- | --- |
| `when_the_road_returns` | 0 hours | Return to Soana; nursery, prior relationship and passage callbacks; Meret reports an intrusion while retaining her right to leave. |
| `a_track_with_two_ends` | 24 hours | Read the snare line through Lore Nature DC 26, fail with an injured dog and delayed inspection, or deliberately take the slower survey. |
| `what_the_hollow_costs` | 24 hours | Hear Hessa and Mava's needs; choose a closed refuge or a limited three-day harvest with real food, travel and attention costs. |
| `where_the_steps_end` | 0 hours | Test an authored temporary warning; keep a stronger, visibly marked warning or soften it at the cost of more frequent inspection. |
| `the_days_she_counted` | 72 hours | Resolve the chosen local agreement, Meret's departure and the letter to Corven; choose partnership, continuing courtship or friendship. |
| `before_the_far_road` | 24 hours | A pre-final-battle farewell with separately chosen night, kisses, holding or friendship. |

The boundary test can follow the meeting immediately so the departing people need not be invented anew at a later visit.
The narrative also leaves Hessa and Mava waiting to see the boundary before their departure, while Meret leaves with her own camp.
These scenes schedule authored encounters in dialogue; they do not create engine-timed appointments, deadlines or NPC travel.

## Native access and source grounding

Read in full before authoring: `soana_opening.py`, `soana_continuation.py`, `soana_later_progression.py`, the route evidence, prior handoff and `reference/canon-review/soana-late-access-audit.md`.
That audit's exact extracted records are in `reference/canon-review/soana-late-access-records.json`.
The audit supports the continuing native actor and postquest conversation at Wintersun in Chapter 5 through static scene, etude and map inspection.
It does not replace a real Chapter 3 to Chapter 5 save replay.

Every new visit requires Chapter 5, WintersunOutdoor `0a5654e7dc18f074d9356009d55eb51b`, unit `64805abb52739e44280a758f850b300c`, and native postquest answers list `2b1776f3e398685479ff6b16290b4cc2`.
Each requires `soana.after_quest`, earned `soana.progression_kept` and the preceding new milestone.
OldDefender or BearDead must be present; BearDead takes precedence in the narrative if both histories exist.
`soana.dead`, `soana.killed_by_camellia`, `soana.forest_dead`, `soana.closed` and `inhuman` continue to block local entry.
The existing contact adapter supplies the live, present, nonhostile speaker test.
No scene claims an Abyss or Drezen actor, marks a hidden actor alive, clears hostility or replaces a spawner.

Soana's dwarf identity, protective territorialism, native spirit binding, medallion and bear-brand connection, Corven memory and uncertain later family history remain the basis of her characterization.
The native text does not establish a divorce or Corven's death.
The existing authored uncertainty remains uncertainty after she finishes the letter.
A written letter is a dialogue prop, not a new inventory object or a delivered message.

Hessa, Mava, Tarn the dog, the snare line, harvest dispute and turning-thorn rite are authored additions.
Meret and her limited obligation continue the earlier authored arc.
The rite's claim to Soana's earlier personal practice is also authored background, not recovered native dialogue.
It creates a localized sound and can be ended with water; it does not enslave a creature or replace the medallion's life binding.
No native spell, buff, skill bonus, animal injury state, inventory reward, map marker, curse or protection mechanic is granted.
The investigation, releases, survey, magical demonstration and negotiated consequences are played book events.

The old guardian problem is explicitly retained.
The new protection neither frees living Orso nor restores a dead or released Orso, produces a replacement guardian, repairs a destroyed forest or revives Soana.
The native medallion's physical ownership is never assumed, and no intact medallion is required as an item.

## Choices, continuity and flags

The Chapter 5 entry assumes the full earlier seventeen-scene arc was played.
It does not move missed Chapter 3 content into Chapter 5 or manufacture those history flags for a late install.

`late_returned` records the return.
`late_track_read`, `late_track_missed` or `late_track_slow` records the investigation, with shared `late_trail_known`.
Success frees Tarn promptly and finishes the inspection before dark.
Failure frightens him into pulling against the snare, requires his owner to settle him, leaves him unable to bear weight immediately and costs a return at dawn.
The non-roll survey takes longer but avoids that additional struggle.
All three paths establish the line and continue without a repeat roll.
No failure closes the romance.

`late_reserve` or `late_harvest`, with `late_boundary_agreed`, records Soana's selected response.
The reserve keeps food in the refuge and sends named people away with less.
The harvest spends three of Soana's mornings and disturbs the edge, while allowing the travelers a limited saleable crop.
She defends either choice and remains able to dislike its cost.
The Commander does not obtain a confession of moral improvement as a romance reward.

`late_thorn_strong` or `late_thorn_soft`, with `late_thorn_tested`, records the tested warning.
The strong branch retains its fear while adding visible markers and reducing its physical reach after testing.
The soft branch reduces fear and requires more frequent personal inspection.
The earlier interrupted voice rite receives a separate practical-trust conversation and a deliberately different task.
No old choice or remembered injury is erased.

The future conversation sets exactly one of `soana.committed`, `soana.late_open` or `soana.late_friends`, plus `late_future_chosen`.
An existing friendship remains friendship.
A current courtship may become friendship, adding `late_romance_ended` while retaining past attraction or intimacy as history.
Corven's unreceived answer is not fabricated to make partnership easier.
Other loves are explicitly permitted and other romance flags are never changed.

The farewell sets `late_campaign_kept` with exactly one of `late_farewell_night`, `late_farewell_kiss`, `late_farewell_held` or `late_farewell_friend`.
Only the chosen night adds `soana.lovers`; an already earned lovers flag remains historical on every later choice.
All new scene decisions persist only at terminal choices.
Aborted or interrupted visits do not leave partial outcomes to combine with a different replay.

## Earned endings and limits

| Ending suffix | Required outcome and precedence |
| --- | --- |
| `kept_life` | Late farewell completed, partnership chosen, embodied surviving ordinary outcome. |
| `chosen_visits` | Late farewell completed, open courtship chosen, same ordinary outcome restrictions. |
| `familiar_company` | Late farewell completed, friendship chosen, same ordinary outcome restrictions. |
| `sacrifice` | Completed late farewell and verified existing `sacrifice`; excludes native loss, inhuman change and ascent. |
| `beyond_the_forest` | Completed late farewell and derived `ascended`; excludes native loss and inhuman change. |
| `unrecognizable_return` | Completed late farewell and `inhuman`; excludes native loss. |
| `native_loss` | Completed late farewell and any Soana death, Camellia killing or forest loss; exact pages distinguish those histories. |
| `aeon` | Earlier `progression_kept`; attaches only to the separate `AeonEpilogue` sequence. |
| `unfinished_sacrifice` | Earlier `progression_kept`, no completed late farewell, sacrifice; same incompatibility precedence. |
| `unfinished_ascent` | Earlier `progression_kept`, no completed late farewell, ascent; same incompatibility precedence. |
| `unfinished_change` | Earlier `progression_kept`, no completed late farewell, inhuman transformation; native loss still takes precedence. |
| `unfinished_loss` | Earlier `progression_kept`, no completed late farewell, native Soana/forest loss; separate Camellia, death and forest pages. |

All ordinary endings explicitly exclude sacrifice, ascent, inhuman transformation and every native Soana/forest loss flag.
The ordinary outcome table is mutually exclusive over tested valid histories.
For conflicting exceptional flags, native loss takes precedence over inhuman change, which takes precedence over ascent, which takes precedence over sacrifice.
The separate Aeon sequence does not promise that Soana remembers the Commander or that Corven's relationship has an invented fate in the rewritten world.

The module uses existing shared bindings rather than adding hypothetical IDs.
`story.py` binds sacrifice `381a296094804761af0893d2e70dc2df` and four ascent outcomes, with `ascended` derived by the existing runtime.
The existing exporter dispatches `AeonEpilogue` through its distinct native sequence.
Root's native and managed binding checks remain required for the combined export.

The completed special endings retain their late-farewell requirement.
Separate provisional endings now cover exceptional outcomes after the earlier seventeen-scene arc and after any partially completed late visit.
This includes transformation before the late return, which correctly prevents the later living visits from starting.
Their prose refers only to the earlier visits, work and company, without claiming that the new thorn, harvest or farewell was played.
The sacrifice text remains neutral about a partnership already chosen during the fifth late visit.
The two loss versions reuse two truthful earlier-history pages, counted as exact repeated segments rather than extra distinct content.
The original six visits and eight completed/special ending scenes were independently compared as JSON and remain identical after this added coverage.

An ordinary player who skips this late development does not receive its earned partnership ending.
No new ordinary happy ending is supplied for an incomplete late arc.

Dead-Soana recovery, Camellia's hidden actor/corpse reconciliation, Orso restoration or release recovery, destroyed-forest consequences and any broadened late-install acquisition remain separate implementation work.
The current living arc is attainable in principle through ordinary Chapter 5 Wintersun access on the supported prior histories.
A universal Trickster recovery route is not delivered by this module.

## Counts and checks

The project tokenizer measures 18 scenes, 71 pages, 12,182 raw words and 11,981 distinct normalized whole-segment words in this module.
Combined with the seventeen earlier scenes, the authored Soana inventory is 35 scenes, 35,894 raw words and 35,578 distinct whole-segment words.
The totals include alternative choices and endings.
They are not a selected playthrough length or a quality score.

The six new visits plus one eligible ordinary ending contain 5,487-6,325 selected prose-and-answer words across supported histories.
The complete twenty-three visits plus one ordinary ending contain 18,803-21,387 selected words.
Bound-bear histories measure 18,809-21,387 for that complete path; dead and overlapping histories measure 18,803-21,381.
Counts carry actual choice flags through the graph, include both check results and non-roll routes, exclude aborted/closed paths, and merge only histories indistinguishable to future predicates.
The same tokenizer as `tools/measure-story-content.py` excludes titles, entry labels, journal metadata and external native/RanRomance words.
The aggregate planning floor is not a mandatory selected-playthrough floor.
No verified selected RanRomance baseline or comparative quality approval is claimed here.

Python compilation passed.
The isolated candidate appends a deep copy of this module to `make_expansion()` without writing the main export.
`Rules.Validate` and `SoanaLateCampaignTests.Run` pass 4,208,976 assertions.
The runner compiles actual `src/Story.cs` and copies the actual `Program.Walk` and `Program.Copy` helpers.
Its command is:

```powershell
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --project 'C:/Users/Z/AppData/Local/Temp/soana-late-campaign-xxn0bw8k/Check.csproj' -- 'C:/Users/Z/AppData/Local/Temp/soana-late-campaign-xxn0bw8k/candidate-revised.json'
```

The focused suite earns all seventeen predecessors from choices for bound, dead and overlapping native guardian histories, three shrine outcomes, both passage agreements and prior friendship or courtship.
It then traverses every new page, all future/intimacy choices, the roll's success and failure and the non-roll path.
It checks delay boundaries, replay, interruption, original contact disappearance, all native loss blockers, wrong chapter/area, missing prerequisites, preserved native and other romance flags, and immutable earlier timestamps.
It checks mutually exclusive ordinary endings, each exceptional ending, combined exceptional flags and the separate Aeon dispatch role.
The revised suite also triggers each exceptional outcome directly after the played seventeen scenes and after each incomplete late visit, including blocked transformation and precedence across overlapping exceptional flags.

Independent writing/canon review, the combined native and managed checks, actual Chapter 5 contact and save/reload verification, art review and live ToyBox coexistence remain outstanding.
No new image was generated or approved by this work.
