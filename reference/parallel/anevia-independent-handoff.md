# Anevia independent campaign handoff

Frozen for independent review on 26 September 2026.
This is a complete campaign manuscript and focused source-model test release, not an approved or installed route.
Only `storylines/anevia_independent.py`, `tests/AneviaIndependentTests.cs` and this handoff were written for the authoring task.
The original 59 scenes, shared builder, engine, generated exports and other author's files were not edited.

## Released revision

| File | SHA256 |
| --- | --- |
| `storylines/anevia_independent.py` | `23A3E38B03621C25A9CDF762E695B2005651D7507D47FD87E7B6AF0F1D2BB7B0` |
| `tests/AneviaIndependentTests.cs` | `4DA6EC71C3DB94AD60D0E761F61DA63BA0B0107039540729EC9FE090F0AB5D43` |
| Temporary candidate including the labeled bridge-declaration fixture | `3A4C84C24110C4EDA9552623BDE1E8BBC1C385FC97BA19421F45135E1F1E03B4` |

The module exports `RELATIONSHIP` and `SCENES`.
Root owns registration and the separate bridge overlay.
No author-assigned writing score or approval is supplied.

## Campaign and scene contracts

The normal negotiated acquisition is `unborrowed_hour -> a_question_at_home -> beths_question -> beths_answer -> her_own_answer`, with the `anevia.` prefix on every new ID.
The first invitation can begin without completing any old acquaintance scene.
It reads current native availability through the capital contact and excludes an existing affair or shared relationship rather than replaying first attraction for established lovers.
It earns `anevia.courtship_requested` only through the actual new conversation.
Root's appended honest-request choices may also earn that flag and lead into `a_question_at_home`.

Irabeth has two separate interviews with the Commander, using her own actor contact while Anevia is absent from the room.
The first hears the request or actual betrayal; the second gives Irabeth's own answer after time to think and talk with her wife.
Her agreement changes no native marriage state and does not start an Irabeth romance.
The Commander can reject the arrangement, and a persistent demand for obedience causes a local refusal.

| State | Producer and meaning |
| --- | --- |
| `anevia.spousal_conversation_requested` | `a_question_at_home` or `one_truth`, after the actual invitation to speak with Irabeth. |
| `anevia.single_affair_disclosed` | `one_truth`, recording Anevia's explicit disclosure of the actual single affair. |
| `anevia.spouse_heard` | Completed first Irabeth interview; this is not agreement. |
| `anevia.marital_terms_agreed` | Completed second interview with Irabeth's chosen agreement. |
| `anevia.lover`, `anevia.personal_ready` | Completed personal invitation and actual mutual answer, never installation migration. |
| `anevia.committed`, `anevia.future_chosen` | Chosen lasting independent relationship in `a_key_that_is_hers`. |
| `anevia.open_future`, `anevia.future_chosen` | Chosen continuing romance without a lifelong promise. |
| `anevia.developed` | Completed final personal farewell after the career consequence, ordinary intimacy and future conversation. |
| `anevia.closed` | Local refusal or ending only; it does not set legacy `closed` or Irabeth's closure. |

Actual single-affair access is `one_truth -> beths_question -> beths_answer -> her_own_answer`.
`one_truth` requires earned `a_affair`, `a_morning` and `a_will_tell`, and excludes an unresolved `i_affair` or already established shared route.
It preserves the affair, distinguishes agreement now from consent then and does not manufacture the other wife's affair.
The old two-affair reckoning remains root's existing route.

An active old triad may play `a_place_of_our_own`, reading actual `trying` or `committed`.
It acknowledges the existing relationship and earns the new personal-continuation markers through a date without replaying attraction, confession or the old table.
It leaves the shared relationship intact.

Root's separate played dissolution or declined-proposal bridge may supply `tirabade.group_closed` and `tirabade.anevia_continuation_invited`.
Those exact flags unlock `an_invitation_afterward`, even if the old table was declined before `trying`.
That scene distinguishes a shared arrangement actually ended from a proposed arrangement never begun.
It supplies a new voluntary personal answer and does not set old shared scene completions.
An existing `anevia.personal_ready` relationship does not replay either catch-up.

The substantial continuation is:

`borrowed_signature -> the_paper_seller -> the_woman_with_the_basket -> the_counting_room -> what_the_warning_cost -> the_evening_without_a_case -> the_life_she_lived -> a_key_that_is_hers -> the_last_ordinary_thing`

The civilian case concerns counterfeit inspection notices collecting names and addresses.
Ressa, Tovra, Dema, Cale and Helve are authored adult women, not disguised native quest actors.
The case's investigations, money, packets, questioning and civilian arrangements exist in the book-event narrative; the module does not debit inventory, alter native quests or spawn those civilians.

The paper offers a real Commander Perception DC 24 check with success and failure pages, plus sorting and asking approaches without a roll.
Success establishes a place and time; sorting establishes a narrower place; failure and declining the reading retain uncertainty and seek Dema's practical knowledge.
Dema chooses limited cooperation and can instead be spared the delivery.
The confrontation trades preserving receipts against stopping the buyer, and the consequence scene retains the resulting repayment and evidence limitations.
No investigation outcome awards or removes affection for passing a roll.

The ordinary private evening includes competition, playful experimentation, personal disclosure and a choice among adult non-graphic intimacy, quiet sleep or keeping a promise elsewhere.
All lead to a real continued relationship rather than treating sex as mandatory progression.
The later key conversation offers lasting commitment, open continuation or a local parting.

## Campaign chronology and endings

`departure_note` is Chapter 3 only and records `anevia.departed_together`.
`the_blank_half` is a remote Chapter 4 scene requiring that actual farewell.
It keeps a letter or memory with the Commander and invents no Abyss courier.
`the_life_she_lived` is Chapter 5 and distinguishes the actual earlier absence from a fresh post-return courtship.
It does not infer a pre-Abyss romance from completing a scene in Chapter 5.

`a_grief_with_a_name` requires native `irabeth_dead`, an already chosen Anevia relationship and physically available Anevia.
It distinguishes grief, continuing affection and replacement, with a local ending if the Commander cannot continue.
It does not set a recovery flag, clear the native death or infer a particular unverified manner of death.
This is current native-baseline bereavement support.
Historical sticky death flags and any future verified recovery service need explicit integration before claiming recovery-aware bereavement delivery.
No speculative recovery marker is included.

Eleven ending scenes cover developed commitment, developed open continuation, unfinished romance, local parting, acknowledged survivor continuation, Anevia's own death, departure without assuming death, Commander sacrifice, incompatible transformed power, ascension without automatic inclusion and the dedicated Aeon dispatcher.
All have explicit scene guards because epilogue availability bypasses ordinary relationship-record closure checks.
Individual endings suppress themselves for active legacy `trying` or `committed`, with authored overrides only for the actual `tirabade.group_closed` bridge result.
Global `closed`, local `anevia.closed` where applicable and native guards remain binding.
Two separately earned individual romances need not become a triad to receive their own compatible outcomes.

## Other relationship and parent compatibility

The spouse interview distinguishes absent Irabeth romance, current `irabeth.lover`, and historical `irabeth.lover` with `irabeth.closed`.
It never describes an already chosen partner as merely a potential platonic acquaintance, or treats an ended relationship as current.
No Anevia choice writes Irabeth's lover, commitment or closure flags.
No choice changes another character's relationship state.
Additional lovers and keeping prior appointments are supported without treating another partner's existence as an offense.

Installed `RanRomance.dll` SHA256 is `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
I decompiled `RanRomance.Anev.Main` with the local ILSpy executable and inspected the `RanRomAnevChpt03Dial001` and `RanRomAnevChpt05Dial001` localization entries in `reference/art-review/ran-route-il.json`.
The parent Anevia classes are dispatchers for Nurah, Aranka, Targona, Terendelev, Minagho and other invitations, rather than a discovered Anevia romance to duplicate.
`Main.Configure` replaces the native Anevia dialog finish actions with conditional parent-dialog dispatch and rebuilds answer list `33960c7f7af40cd43b7f801a76c87a0b` with native answers and its two additional chapter dispatcher entries.
This module changes neither finish actions nor that list.
Root's existing append-after-parent integration must preserve every parent answer and invitation when attaching the new entries.
The author did not test live mod load order or every ToyBox patch combination.

## Native actor evidence

I inspected the actual `drezencapital_default_mechanics.scenes` bundle with the existing UnityPy environment.
Bundle SHA256 is `D451FEF29C6B22F5D13E8BACEA70BA063175DDEE8B3F43F48D6CAE7F22B4A9E3`.
Anevia GameObject 298, `AneviaTirabade_DrezenCapital`, has spawner `86b332a9-5910-4d46-9951-8e06f7dcf0cf`, unit `b5e867e13503c6f41bb1316705efb4a2` and dialog `de4cc2dd71694b842be37b75d1705b83`.
Irabeth GameObject 477 has spawner `3dc302d8-58ce-44f3-9766-2a437a080108`, unit `280d4712dceb37f4a88e98f1f4c6e64f` and dialog `20e94a828d4016d45a6b723765306522`.
Both spawn on scene initialization and do not respawn if dead.
These components establish actual actor bindings, not guaranteed current physical availability.

Installed blueprint entries were also inspected directly.
`Units/NPC/Unique/Act_3_DemonsHerecy/Drezen/AneviaTirabade_DrezenCapital.jbp` has SHA256 `98288BE73EA58F42D9ACD88675DBE8F6BFBE15BCF86AD45A5777FD9F72760618`.
`World/Dialogs/NPC_Common/Anevia/Dialogue_AneviaMain.jbp` has SHA256 `1430B8DB048CCA7752A41AE387A6218BD96009E0C4BF82406CC1CC6919C6B9C3`.
`World/Dialogs/NPC_Common/Anevia/AnswersList_0003.jbp`, the explicit reusable answer list, has SHA256 `DE56F133C85029C95C875D7E4780232BA839DBA436EB9DC3496F05C66FF0E77C`.
Irabeth's capital unit entry has SHA256 `17D81275AB6821EDBA0FC2DB211B8B11185679D70AF371194E91ACBAE627CC05`.
Her main dialog entry has SHA256 `E5F5B10E91941C0B0D0B6CFB62E6C3FD52AD90B4F5A388D9F4EDAB1DFA6D443B`.
Root separately owns the complete typed trace and native etude analysis in `reference/canon-review/tirabade-capital-contact-records.json` and its probe.
That work should not be replaced with a claim that the spawner alone proves visibility.

Every new physical scene specifies Drezen, Chapters 3 or 5 as appropriate, the correct native answer list and one actual actor contact.
Irabeth-only interviews use Irabeth's actor and answer list `871af36f2ab2b1f40b5de77976c54276`.
No new scene relies on a scalar contact to prove that both wives are in the room.
The remote letter and ending pages do not require a live speaker actor.

## Size and played-path evidence

The module contains 20 main or alternative scenes and 11 endings.
Using `tools/measure-story-content.py`, it contains 24,757 raw words and 24,729 distinct normalized segment words.
The raw total comprises 22,292 prose words and 2,465 answer words.
Only 28 exact repeated words were removed by that segment method; it does not certify semantic originality or absence of repeated ideas.
No old game, parent-mod or shared Tirabade prose is credited toward this module's 21,000-word per-character planning floor.

The existing selected-path measurement functions were reused in memory for Anevia, retaining compatible path minima and maxima and one ending.
An early negotiated path with the actual Chapter 3 farewell and Chapter 4 letter contains 10,898-13,104 selected words across 17 scenes including one developed ending.
A fresh Chapter 5 negotiated path contains 10,073-12,246 selected words across 15 scenes including one developed ending.
The calculation assumes appropriate physical location, live contacts and sufficient waits.
It measures source choices, not Unity or a native campaign played from a fresh save.
The installed RanRomance benchmark is an aggregate inventory, so these selected lengths must not be compared with its full-branch totals as if both measured the same thing.

## Focused verification

The temporary standalone project is `C:/Users/Z/AppData/Local/Temp/anevia-independent-z5an3x98/Check.csproj`.
It compiles actual `src/Story.cs`, the new focused tests and the existing `Program.Copy`/`Program.Walk` helpers.
`Rules.Validate` and the focused suite passed 315,136 assertions.

```powershell
& 'C:/Users/Z/AppData/Local/RanRomanceTools/dotnet/dotnet.exe' run --project 'C:/Users/Z/AppData/Local/Temp/anevia-independent-z5an3x98/Check.csproj' -- 'C:/Users/Z/AppData/Local/Temp/anevia-independent-z5an3x98/candidate.json'
```

The candidate adds one explicitly labeled, never-played `test.bridge_flag_declaration` scene solely to declare root's pending authored bridge output flags for override validation.
The bridge output states in the relevant tests are likewise labeled fixtures.
They do not prove that root's shared conversations produce those states.
Actual bridge integration must replace that fixture and play the real shared responses before release.

The suite plays both starting chapters, no/current/ended Irabeth romance, four paper approaches, both Dema choices, both confrontation outcomes, open and committed futures, the real original single-affair acquisition, the real original dual-affair table and the new personal continuation.
It checks post-group invitations before `trying` and after an actual shared table, under the stated bridge-output fixture limitation.
Every non-epilogue page is reached in those histories.
It checks current contact loss and area change, partial-page completion, preservation of prior flags and timestamps, other lovers, truthful fresh Chapter 5 history, bereavement, independent ending conflicts and global/local closure boundaries.

No source-only test proves live actor state, book presentation, native campaign timing, endgame dispatch order or real save serialization.
The source does not implement Trickster resurrection or retrieval, and surviving availability after every native outcome remains dependent on the actual actor and native restrictions.
Independent literary/canon review, root's real bridge integration, broader checks, art and live presentation are still required before calling Anevia delivered.
