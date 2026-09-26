# Seelah late campaign handoff

Six new, unexported Chapter 5 scenes are delivered in `storylines/seelah_late_campaign.py`.
Revised source SHA256: `AD60828FA02270F9D91F480B3E31E07B9F76957B039C5BAA8C8240232FFA604A`.
This is an authoring contribution awaiting independent review, not a finished route or a release approval.
Only this handoff and the new module were created for this assignment.
No shared source, tests, exports, native data or installed files were changed.

## Content and progression

| Scene | Previous authored milestone | Main action and consequence |
| --- | --- | --- |
| late_course | aftermath_ready | Seelah chooses a courier-style obstacle relay because she wants to compete; Commander chooses running or watching; she chooses a regular teaching hour or shared instruction with Istra. |
| late_lesson | late_course_planned | An actual shield lesson puts those two arrangements into practice; a time-limited participant receives either one practiced movement or a useful question exposing misunderstanding. |
| late_page | late_lesson_kept | Seelah makes personal plans with current native quest-outcome reactivity and either an Elan memory, an unsent draft or an unresolved-rescue conversation; Commander names a personal wish. |
| late_race | late_lesson_kept and late_page_kept | Practice consequences appear; Commander runs or judges; the race produces a win or loss, different songs and remembered desire. |
| late_afterglow | late_race_kept | Her competitive pleasure develops into direct attraction; a voluntary non-graphic night, kisses only or quiet company each completes the evening. |
| late_first_step | late_evening_kept | The Commander's chosen wish is enacted as a music visit or a rented cupboard with actual reserved space; existing commitment is acknowledged without setting or removing it. |

Every scene additionally requires `seelah.courting` and `seelah.aftermath_ready`.
All are optional Chapter 5 scenes in Drezen, attached to Seelah's existing native answer list `417fa384f3250634bb71859fbc913453`.
The Drezen area GUID is `2570015799edf594daf2f076f2f975d8`.
All forbid `inhuman`, `seelah.farewell`, `seelah_dead` and `seelah_gone`.
The existing relationship definition also supplies its normal closed/unavailable checks in production Rules.Available.
The ordinary delay is 24 hours after the latest required authored milestone; late_race uses 48 hours.
No old IDs, prerequisites, choice indices or commitment gates were edited.
In particular, the existing road/farewell path can still bypass this addition.
The addition is not a migration gate and does not strand older development saves that already committed without aftermath.

The new terminal milestone is `seelah.late_campaign_kept`.
All newly written state uses the `seelah.late_` namespace, apart from optional kisses setting the already established `seelah.kissed` flag.
No choice sets seelah.committed, seelah.closed, native quest outcomes, death state or another relationship's flags.
The existing aftermath prerequisite follows the ordinary lovers/weight chain, but this contribution does not infer commitment from intimacy.
Root should keep all shared integration ownership until independent review and production checks are complete.

## Sources and authored departures

Read `reference/story-review/seelah-full-arc-gap-audit.md` for the earlier assembled-route deficits.
The relevant gaps addressed here are Seelah's independent pleasures, competing personal and service obligations, seeing her competence, current Chapter 5 outcome reactions, an Elan-related action, and an enacted consequence of the Commander's own wishes.
The audit predates several intervening additions; its old numerical deficit is not used as the current count.

Current sources include `storylines/seelah.py`, `seelah_later.py`, `seelah_abyss.py` and especially `seelah_aftermath.py`.
The roof evening ends with `seelah.aftermath_ready`; its temporary furniture, shared meal and relationship discussion are not counted again here.
The new cupboard is rented, small and temporary, so it does not claim that the permanent shelf or home mentioned by existing road/farewell scenes has already been chosen.
The broad early home/travel preferences are not overwritten by the more specific new wish.

Native predicate evidence is retained in `reference/canon-review/seelah-later-predicates.json` and the accompanying native-source inventory.
Current aliases already supplied by expansion.py are used without new bindings:

| Alias | Existing predicate | Use here |
| --- | --- | --- |
| seelah.souls_returned | Completed native quest `5a5a533c9ce630a48b877f9a194840cb` | Rescue-related interpretations only after actual completion. |
| seelah.ending_bad | Native outcome etude | Grief and a wish for independent travel take precedence over moderate if both appear. |
| seelah.ending_moderate | Native outcome etude | Questions and possible independent travel, when bad is absent. |
| seelah.elan_dead | Native fate etude `148423f1d35917946a5ebeeb4f19246c` | Private memory page after completed rescue; no resurrection or invented live meeting. |

The current native flags are read in late_page rather than inferred from stale aftermath_grief/questions/hope/unfinished flags.
Absence of Elan's death flag alone does not create a live actor.
The non-death branch writes an unsent draft and explicitly does not claim he is in the next street or has replied.
The unfinished-rescue branch does not use either completed-rescue interpretation.
Kiana, Jannah, Curl and Arsinoe are not spawned or assigned invented outcomes.

Tavia, Dena, Breva, Istra, the cooper, the lesson participants and the musician are authored civilian guest characters.
They are not discovered Owlcat NPCs or verified members of native victim groups.
The course, booklet, shield lesson, room rental, songs, cupboard and personal keepsake are authored story props and events.
The cupboard is not a native inventory container, and no item is removed from the player's inventory.
Istra's injured hand remains injured; adapting instruction does not heal it or claim a spell failed.
All introduced potential social peers are adults; none is a new romance participant in this module.
No private scene claims that another partner has consented, ended their relationship or ceased to matter.
No jealousy/exclusivity gates or ToyBox setting changes are introduced.

## Gameplay hooks requested by the user

These scenes currently enter through Seelah's native dialogue and run as branching book events.
They are not rest-triggered remote books.
The yard and guests are narrated, not spawned encounter objects.
The revised close turn uses the implemented native-check schema, with SkillMobility, DC 26, distinct narrow/stumble outcome pages and CommanderOnly true.
The attempted choice sets only late_close_turn, not victory, defeat, affection or scene completion.
The narrow page's existing continuation sets late_race_won.
The new stumble page sets late_race_lost and late_race_stumbled before joining the existing lost-song outcome.
The careful wide line and spectator paths remain non-roll alternatives.
The module itself is still unexported, so this is authored native-check wiring awaiting root's assembly and gameplay verification, not a claim that a live roll has occurred.
There are no actual currency charges, inventory transfers or experience rewards.
The user's request for discovery and physical encounter gameplay remains a broader integration task.

Concrete opportunities for root's future skill-check support:

| Existing scene/node | Suitable check proposal | Success/failure and non-roll alternative |
| --- | --- | --- |
| late_course/course and runner | Athletics or Mobility during voluntary course practice | Success can establish a practiced exchange or tight-turn advantage; failure costs practice time and gives a retry or slower technique. Watching/judging stays available without physical checks. No affection awarded for success. |
| late_lesson/pressure | Athletics to maintain the shield during a demonstration, or Perception to identify footing | Success gives a clean demonstration; failure lets Istra stop, reposition and teach from the visible mistake. Listening and helping with straps remain meaningful non-roll participation. A failed check must not injure the trainees or close courtship. |
| late_race/running | Mobility DC 26, now authored with the native Check schema | Success reaches narrow; failure reaches the new stumble page, then the lost song. The careful wide finish remains a non-roll option. Earlier teaching arrangements have narrative practice consequences but no mechanical modifier yet. |
| late_first_step/music | Optional Performance-like expression only if the installed game offers an appropriate actual skill | Do not invent a Performance stat. Listening, tapping or asking to hear a passage already provide non-roll participation and must not be gated by social success. |

The earlier suggested stumble paragraph is now developed into a reachable failure node and counted once in the module inventory.
Failure does not claim that the Commander deliberately chose the wide line, suffer a native injury, lose the romance or need to buy affection back.
DC 26 is an authored calibration for a practiced civilian contest, not a value prescribed by Owlcat for this new race.
Read directly from installed blueprints.zip, Chapter 5 SoldierParty/Armwrestling/Check_0002 uses SkillAthletics DC 26, GUID `c2f827c1404842fe85bff3ceaa1ff8e6`.
The same party's harder Armwrestling/Check_7 uses SkillMobility DC 44, GUID `21c054da7ddf4e1ca5ae16c41d0bddb3`.
Chapter 5 SinisterVillage/BookEvent_Boat/Check_0009 uses SkillMobility DC 30, GUID `dd025f5cc3eb6d344b00977de3e8f5f2`; Check_0051 uses DC 35, GUID `f58da500a905abb4998affa42f8df0ea`.
These are chapter/mechanic comparisons, not claims that the native events are identical to the relay.
The authored race uses the lower competition benchmark because a casual contest on practiced level ground should not demand the same modifier as those harder late-game checks.
It is expected to be easier for a Commander trained in Mobility; no success rate is asserted without the actual character and game rules.
The installation does not currently contain a custom referee, course trigger or mapped guest actor for these additions.
A fuller delivery could use a journal invitation after aftermath_ready, an actual yard interaction, a race result trigger and a return conversation, but these need location/actor verification and cannot be credited as present.
Discovery should remain Seelah inviting the Commander into something she wants, rather than a checklist purchasing affection.
Her existing quest completion and native outcomes belong in reactions and access conditions, not in invented new rescue flags.

## Checks performed

Read-only import used Python with bytecode writing disabled.
All six scenes and all 65 nodes were traversed under six native histories, each with and without an existing Seelah commitment.
The histories included incomplete rescue, completed rescue, completed rescue with Elan dead, moderate outcome, bad outcome with Elan dead, and overlapping bad/moderate markers.
Revised traversal covered 58,904 choice transitions, including repeated paths, and 2,304 distinct terminal flag histories across these seeds.
It found no missing nodes, dead ends or cycles.
Checks required preservation of native input flags, another active romance's commitment, and the presence or absence of Seelah's earlier commitment.
They also checked exclusive race outcomes and exclusive night/kisses/quiet choices, and that aborts apply no effects.
The local walker follows both Check.Success and Check.Failure and proves neither outcome flag is set before the roll.
Both check outcomes reach the final campaign milestone without changing another romance or awarding commitment.
The check's exact skill, DC and CommanderOnly contract was checked in the authoring data.
Every node was reached by at least one tested path.
These checks use the authoring data directly and do not substitute for production Rules, game blueprint construction or Unity verification.

The existing content inventory tokenizer measures 8,308 raw words and 8,269 distinct-segment words across the revised six scenes.
This exceeds the rough 5-7k assignment target because the participant/spectator, native-history, intimacy and personal-wish branches receive separate developed scenes.
Independent review may cut repetitions; length is not an argument against necessary editing.
A selected-path walk measured 4,362 to 4,866 words of narrative plus chosen answer text across 5,760 complete paths before the final seven-word timing clarification.
That clarification adds seven narrative words to every complete path, yielding 4,369 to 4,873 words without changing any graph edge.
That excludes unselected choice labels, titles and journal metadata and is a module-path estimate, not a whole-route playable-content claim.
No external game/RanRomance prose receives new content credit.
No writing, canon, art or integration score is assigned by the author.

## Review and remaining gaps

Independent writing review should examine both teaching arrangements, a runner victory, a runner loss, the spectator loss, all native page outcomes, all three intimate responses and both personal wishes.
Check that the humor and confidence remain Seelah's without making every generous act a lecture about self-denial.
The teaching conflict is deliberately ordinary and does not satisfy every missing paladin dilemma from the full-arc audit.
The memoir and draft make Elan matter without inventing his presence; they do not replace a separately verified living interaction.

Root still needs production progression/timing tests, actual NativeContact or equivalent Seelah contact evidence where appropriate, blueprint construction, UI/portrait checks, and save/ToyBox testing.
The new scenes do not have generated scene artwork or portrait crops.
The root has implemented native skill-check construction; this module's race use still needs integration, managed construction and actual roll testing.
Course encounter objects and proper journal/discovery delivery remain outstanding.
The larger route still needs the appropriate native friend interactions, sustained Abyss consequences, bespoke attainable Trickster missed/departed access, broader transformed-body treatment where allowed, and endings that consume developed choices.
Existing optional bypasses remain, so aggregate text does not prove that a normal player receives every scene before commitment or farewell.
The per-character minimum remains at least 21,000 meaningful words and full RanRomance depth and quality, with independent required reviews above 90 and no major blockers.
This contribution cannot satisfy those conditions on its own.

## Corrections after independent review

The independent initial assessment was writing 87 and bounded canon compatibility 91 in `reference/story-review/seelah-late-campaign-review.md`.
Those scores describe the previous source, not this revision.
Independent rereview is required before accepting the revised contribution.

The fixed teaching branch now actually shows Istra's brace before a participant praises it.
The lesson aftermath, fixed-hour decision, private victory and final outing replace repeated explanations about useful pleasure with concrete requests, teasing and action.
Narration no longer praises its own restraint about domestic competence, meaningful objects or an ordinary goodbye.
Breva now receives a runner-path introduction as well as the existing spectator-path introduction.
The private room scene explicitly occurs on a later evening, preserving the 24-hour minimum delay.
The last outing has a neutral opening; the music remains the Commander's choice and the parcel appears only at the cupboard.
Existing scene/node IDs and original choice indices remain intact.
The only new node is the native check's distinct failure page, stumble.
The close-turn choice remains at its original index and now uses Check rather than a predetermined Next edge.

## Parent verification of revised contribution

The parent removed the final retained-chalk callback after independent rereview found that the night branch had already rubbed the mark away.
The ending now offers another race and a concrete goodbye without assuming that mark survives.
Revised source SHA256 is `F0D2B57D28012A4A03D8191AC132DCD9078D2C58F18591ED30D145D21D1797F0`.
The staged 186-scene review story is `development/seelah-late-review.json`, SHA256 `BDAA17C88651838298F7C81E3542628CC5E6991FF2A1D59FAE10453CC4A435F0`.
It passed 2,383,630 rules assertions and 20,082 managed construction assertions over 6,115 generated blueprints.
The focused tests cover native quest histories, both teaching arrangements, participation choices, real check success and failure, non-roll alternatives, intimacy choices and older-road bypass compatibility.
Managed construction verifies that the actual authored race choice creates a native Mobility check with the expected DC and distinct result pages, without scene completion on the attempt.
These checks do not execute a die roll inside Unity or prove physical Seelah presence, save interruption or the displayed check preview.
Final independent rereview accepted this exact source at 91 writing and 91 bounded canon compatibility in `reference/story-review/seelah-late-campaign-rereview.md`.
The parent integrated the contribution into the main development export, whose SHA256 exactly matches the tested 186-scene review story above.
The native binding check passed 278 uses against 62 typed targets.
Source-header references to an unexported contribution describe its original delivery; it is now development-exported, not installed or fully approved.
