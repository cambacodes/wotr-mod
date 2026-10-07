# Konomi ordinary Chapter 5 expansion handoff

Released for independent review on 2026-09-26.
The author assigns no quality score and does not claim a complete Konomi route.

Source SHA256: 3DF0A02357BF23CE09DEC04C2A7A46C5A45F5365BCE4718715834DA316258CA8
Tests SHA256: B34EF199159175F7F374A9EC6A867A804D9FD16E5A0895AADDD0DE3437DC7D91

## Contribution

Six played visits follow the existing retained-office return, political account and power commitment.
A seventh scene is an explicit manual invitation for older saves that already completed ordinary or farewell.

The visits are a_useful_supper, the_upper_passage, two_bad_prices, the_trial_day, a_name_beside_hers and the_evening_she_kept.
Konomi proposes a civilian merchant's evening unloading trial and must revise it after hearing the yard from the occupied rooms above.
A Commander-only Perception DC26 check can identify the loose plank promptly; failure and a non-roll method both find it by taking longer and respecting the tenant's request to stop.
The early result permits an additional carrying trial; the late result commits no unperformed experiment.
Neither outcome withholds the romance.

The player can support Konomi's limited evening trial or Oselda's hired waiting yard.
Both plans have costs, and their separate enacted trials reveal inconveniences absent from their initial estimates.
Konomi can lose the preferred recommendation, help the alternative work, and remain annoyed without punishing the relationship.
The work leads to a private offer for further reports.
The player can encourage a joint paid arrangement with named access for the coauthor or a public circular with more control of subjects but no guaranteed fee.
The final visit supplies different actual answers to those choices, followed by supper, arrangements for shared time, and a voluntary night together or a walk and goodbye.
Private affection appears before the final visit too, and is not awarded for supporting her preferred proposal.

The protagonist's attendance is never falsely advertised as official sponsorship.
The plot is not another public notice correction or letter-theft hearing.
It does not replay Kiana's borrowed-page incident or Konomi's earlier association complaint.
Konomi remains ambitious about influence, introductions and being the first person a reader asks.
She does not renounce her professional interests as the price of romance.

## Native and authored boundaries

The ordinary route still requires the existing konomi.present office predicate and its already-played power scene.
The power scene still depends on the existing konomi.political_account overlay for new histories.
No political binding, witness predicate, council conclusion, foreign-aid state, native appointment or quest result is added or changed.
The proposal concerns Varine's private storage lease and voluntary paid work, not a new kingdom policy passed by the Commander.
No native NPC is reassigned to a new office.
Varine, Oselda, Hesset, Bel, Sella and the off-screen correspondents are authored supporting characters.
Their trial and report outcomes exist in the story and route flags, not as placed actors, inventory contracts or simulated commerce.
The paid reports exclude confidential office information and leave her existing appointment's duties first.
The offer is not represented as a canonical career event or a RanRomance scene.

No artwork is supplied by this module.
It uses the existing Konomi portrait identifier and inherited ordinary conversation delivery.
It does not bind a new ContactUnit, so the inherited distinction between retained-office availability and verified physical contact remains unresolved.
The new availability gates suppress further visits after dismissal or loss of presence; this is not a claim that the current unitless engine cancels an already-running conversation at the exact instant an external mod changes those flags.

## Integration and save compatibility

Append SCENES from storylines.konomi_ordinary_expansion, then call integrate(payload) after the existing Konomi overlays.
Register KonomiOrdinaryExpansionTests.Run when konomi.a_useful_supper is present.
The existing generic artificial-prerequisite walker should not seed mutually exclusive outcomes to enter later new scenes; the focused suite earns them through actual predecessors.

The only existing-scene change is ordinary.RequiresAny set to konomi.ordinary_expanded or inhuman.
The inhuman alternative preserves the existing transformed-companionship passage without requiring the embodied new visits.
The new visits themselves retain the inhuman exclusion.
Source comparison against the current main export proves every original scene is unchanged except this new alternative-prerequisite field.
All existing IDs, node texts, answer indices, effects and existing ordinary/farewell predicates remain untouched.

For a fresh eligible ordinary route, the six visits precede ordinary and farewell.
Completed ordinary/farewell scenes remain completed on older saves.
The manual another_evening invitation requires ordinary, power and commitment, and sets only the authored opt-in plus its own completion.
Its override waives only the older ordinary and farewell exclusions on the new visits.
It cannot waive closure, dismissal, absent presence, inhuman, chapter, area or earned predecessor requirements.
The invitation cannot enter the automatic rest queue.
It is unavailable once the extension finishes.
The existing private dismissal route and private future endings are unchanged.

The first five inter-visit delays are 24 hours except the enacted trial, which waits 48 hours.
The final supper waits at least 96 hours after the report decision to allow the two writing evenings, distribution and replies described by the prose.
Both invitations now schedule supper after the answers rather than promising tomorrow while the mechanics wait longer.
Every new consequence flag occurs on a terminal answer after its associated narrative.
Deferral changes no flags or timestamps.

## Executed checks

An isolated temporary project compiled the actual src/Story.cs, src/RecoveryAttempt.cs, Program.Copy, Program.Walk and project test sources without using shared build output.
The runner called only KonomiOrdinaryExpansionTests.Run on a generated current-main-plus-module candidate.
It passed 394,893 focused assertions.

The temporary project is C:/Users/Z/AppData/Local/Temp/konomi-ordinary-check-31n3jv7k/Check.csproj.
The candidate is its adjacent Story.json.
The command was dotnet run --project <temporary project> -c Release -- <temporary Story.json>.

The suite plays the actual Chapter 3 margin, reception, letter, evening, disagreement, leak and reckoning scenes, then Chapter 5 return, political account and power.
It exercises ordinary and Trickster histories, fresh progression, old ordinary completion and old farewell completion.
It reaches every new campaign page and both outcomes of every terminal decision group.
It checks changed location, chapter, native presence, dismissal, closure, inhuman, every required predecessor, delay boundaries and old timestamps.
It restarts every reached page from a saved partial snapshot and checks that outcomes cannot overlap.
It preserves native political flags and unrelated romance flags throughout the new contribution.
The final fresh path plays existing ordinary and farewell successfully.
The transformed-companionship alternative is checked separately.
These tests do not run a native die roll or certify Unity, actual saves or ToyBox.

## Length and remaining scope

The project inventory tokenizer measures 7,780 raw and distinct-segment words, including prose and choice labels, across seven scenes and 39 pages.
An exhaustive source walk of the six new visits found 192 completed selected paths containing 5,207 to 5,338 words.
That measurement counts only chosen answers and visited pages, including one skill-check outcome per path.
It excludes the older-save invitation and does not add mutually exclusive branches to a single playthrough.
The first invitation is not credited as new content for a fresh route that never sees it.

This materially expands the ordinary Chapter 5 campaign but does not alone establish RanRomance parity for the full route.
The project's 21,000-word planning floor is an aggregate threshold; attainable playthrough depth requires a separate comparison with the benchmark and cannot be inferred from that aggregate.
A new assembled depth audit must measure the actual complete retained-office progression and identify the remaining short sections.
Full-route art, story review, native access, save compatibility and ToyBox verification remain required.

## Early independent review repairs

The reviewer identified a malformed tactile description in the upper passage, a glove stain assumed on the wrong trial branch, a daylight-only successor after an evening trial, and invitations whose tomorrow wording conflicted with the later scheduled scene.
The released revision fixes the wall beneath the hand, makes the shared shelter time-neutral, removes the unsupported stain callback from its successors, and schedules supper after the reports have returned.
These are inspected source changes, not the author's claim of review acceptance.
Independent review of the released hash remains the acceptance gate.

A second inspection found that the neutral shelter opening had removed the gloves before the later fastening action.
The released revision keeps the gloves on until that action and explicitly removes the second glove before folding them after the kiss.
