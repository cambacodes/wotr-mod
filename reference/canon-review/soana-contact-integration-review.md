# Soana contact integration review

Independent technical review on 2026-09-25.
This reviews source behavior against the installed API investigation and Soana's native evidence, not Unity runtime behavior or a complete character route.

| Reviewed file | SHA256 |
| --- | --- |
| src/NativeContact.cs | `27E573ECFB994609730B265646EA7B6D4AFFC47B394A50B6D6BB2287D0FA957D` |
| src/Story.cs | `DFAFC304CDFD13602FF11E7054E6A9B13CDC51D0E2AEA4504F2E14DF517D9D1F` |
| src/Main.cs | `588736FF48FBDAFA2AD770C5C7298A083168BEBE6827B4C1F47EDBCDD864435E` |
| expansion.py | `1FB1F138887A22371EEE8A415549A8887DBD4EBF01B25625F9AF4A3300E02805` |
| storylines/soana_opening.py | `360D90AFC1F2CEBB1626CBE1136B875B7D215D6307731354A0FA219A2BE54055` |

## Blocking defect

Contact is rechecked at entry selection and immediately before the queued book opens, but is not enforced when choosing an answer inside an already opened or resumed book.
BuildScene attaches `RouteCondition { Choice = choice }` to ordinary answer visibility and selection.
That branch of RouteCondition evaluates only the choice's Requires and Forbids arrays.
Ordinary RouteAction repeats only that choice check before RecordProgress; only revival actions also recheck their completed scene.
Neither the book's dialog conditions nor its ordinary page conditions supply the missing scene/contact check.

Consequently, a resumed Soana page can still apply authored flags or complete its scene while contact is missing, Soana is unavailable, or the player no longer satisfies the native route stage.
This contradicts the opening handoff's explicit requirement to verify contact when opening and resuming.
The defect is visible in the source without assuming normal combat continues during a book event.
A save resumed inside a page or externally changed actor state is enough to expose the absent guard.

Pass owning scene context through ordinary choice conditions and actions for contact-gated scenes, and check current continuation eligibility before applying progression.
Provide an exit that remains available when eligibility is lost.
Simply hiding every answer on contact loss would leave a book with no usable exit on pages that lack an authored abort.
The correction needs a focused loss-of-contact and resumed-page test, including proof that an unavailable click cannot write a progression flag.

## Confirmed implementation strengths

NativeContact uses the actual Blueprint identity and refuses an ambiguous active match instead of selecting the first actor.
It checks loaded-area membership and HoldingState.IsSceneLoaded, addressing the API finding that State.Units enumeration alone does not establish locality.
It excludes destroyed, destroy-marked, disposed, hidden, suppressed, unconscious, dead, finally dead and hostile actors.
It rejects a missing Commander and combat before negating the hostility result.
The chosen installed IsEnemy method already checks hostility in both directions.
It does not use DialogSpeaker.GetEntity or deliberately revive, wake, recruit, unhide or change factions.

Contact is represented as a transient Snapshot.AvailableContacts GUID set rather than a persistent authored flag.
The scene requires the correct GUID and cannot be unlocked by another NPC's contact entry.
Build preflights that GUID as a BlueprintUnit before attaching dialogue entries.
Rules.Validate checks the compact GUID format and validates nonempty, distinct RequiresAny alternatives.
The queue checks Rules.Available with a newly constructed State after the old dialogue has closed and the waiting frames have elapsed.
The existing pending-player identity check cancels work after changing the player instance.

The supplied Soana aliases match the native IDs documented in soana-route-evidence.md.
Playing etudes are the intended interpretations in that evidence, so their absence from PermanentEtudes is not a mismatch with the current introduction specification.
AfterQuest plus OldDefender or BearDead is required.
BearDead takes precedence over OldDefender inside guardian_question because the bound option forbids BearDead.
The native reusable postquest AnswersList is the documented insertion target.
The introductory scenes remain Chapter 3 only and do not claim an implemented Trickster restoration or later campaign contact.

## Limitations and follow-up

Duplicate detection currently precedes loaded-area filtering.
An active matching record from an unloaded area can conservatively suppress an otherwise valid local contact.
This fails closed, but can create a false negative if the game retains multiple active records of that blueprint.
Check native scene transitions before treating this behavior as desirable for future characters.

No explicit Wintersun area restriction appears in the scene metadata.
The native dialogue attachment plus actual local actor is the present location mechanism.
That is reasonable for this verified introduction, but it is not permission to reuse the same blueprint in arbitrary authored locations and assume the cave prose remains correct.

The NativeContact call can initialize the game's internal group state through IsEnemy's Group getter.
Documentation should describe the absence of authored life/quest/faction mutations rather than promise literally no internal native writes.

The module header and handoff still say contact predicates are unimplemented and the module is unexported, while expansion.py now imports and adds it.
Update those records once the integration and this correction are settled so the next worker does not treat stale prohibitions as current state.

This review did not run or approve a Unity encounter.
Compilation proves signatures; managed construction proves blueprint wiring; snapshot tests prove only the supplied state decisions.
Actual scene-manager loadedness, actor retention, native book resume, event closure and ToyBox display/selection behavior still require runtime evidence.
No full-route score or release approval is awarded.

## Proposed correction assessment

Root proposes a separate ContactAvailable predicate reused by entry and continuation, scene context on contact-gated choices, action-time rechecking, and a stable contact_lost exit per page.
That is preferable to applying the complete Rules.Available function midscene, because delay timestamps and authored closure flags can change before the final goodbye.
The continuation predicate should retain chapter, explicit area and positive scene prerequisites, including the native AfterQuest stage, as well as actual contact, native unavailability and supported outcome checks.
The contact_lost exit must apply no flags and no scene completion.
Its action should remain usable even if contact returns between display and selection.
This is an assessment of the proposed design only; the revised source still requires rereview and focused checks.

## Revised source review

The revised source was read after root implemented the continuation correction.
The initial table above identifies the defective version; this table identifies the rereviewed version.

| Reviewed file | Revised SHA256 |
| --- | --- |
| src/NativeContact.cs | `27E573ECFB994609730B265646EA7B6D4AFFC47B394A50B6D6BB2287D0FA957D` |
| src/Story.cs | `FF1BA609124CE0DBAB0729E9534F057ACA04682BB0DB64CD4545166BA7D2E736` |
| src/Main.cs | `17CA2079429D7842CE3E8574345AC8F1FEC7B06687E9A8783E731C07ABC703DD` |
| expansion.py | `1FB1F138887A22371EEE8A415549A8887DBD4EBF01B25625F9AF4A3300E02805` |
| storylines/soana_opening.py | `409D9513A0A719C1CA17D2A893E9E33E6902E8CF849A69697C71B504458CD52F` |

The initial continuation blocker is corrected in this source.
ContactAvailable preserves live contact, chapter limits, explicit areas, positive scene prerequisites, native unavailable states and supported outcome alternatives.
It deliberately avoids general authored closure and delay checks so that the final goodbye remains possible after an authored closure choice.
Ordinary contact-gated choices now carry their owning scene through visibility, selection and action-time conditions.
The action returns before RecordProgress if the contact check fails.
Non-contact scenes retain their prior behavior.

Every contact-gated page receives a separately named contact_lost answer after its existing indexed choices.
Its empty NextCue and empty OnSelect provide an exit without effects or scene completion.
Existing authored choice indices are preserved.
The module header now correctly describes a development integration with Unity verification outstanding.

One small exit robustness correction remains in the rereviewed Main.cs hash.
The new exit's SelectConditions also require ContactLost, so a displayed exit becomes unselectable if contact returns before selection.
Keep the contact-lost ShowConditions, but retain InitializeAnswer's empty SelectConditions for this flag-free exit.
This affects the reliability of leaving a stale displayed page, not the progression guard.

No focused continuation tests were present in the inspected test-source search at this review point.
Root is responsible for executing and recording those checks against the final revision.
The source correction does not replace the runtime limitations and full-route requirements above.

## Parent verification after review release

The parent removed the exit's SelectConditions as requested.
Final Main.cs SHA256 is `195269A13191C107C0C9CAA7800DC821DFF7DBA66F5A19DC8A9AD87A43F63502`.
The other revised source hashes above are unchanged.
Focused Soana rules tests now cover contact and prerequisite loss on continuation, closed-goodbye access and delay timestamp changes.
Managed construction tests assert every contact-gated answer's visibility, selection and action context and the exit's stable identity, empty selection conditions, empty actions and empty continuation.
The full rules run passed 2,251,996 assertions; managed construction passed 17,714 assertions over 5,412 generated blueprints.
This is the parent's implementation and verification record, not a new independent score or Unity execution claim.
The managed native-reader invocation initially failed with empty stdin through the PyManager launcher; selecting the installed Python interpreter by prepending its directory to PATH resolved the failure.
Use `C:/Users/Z/AppData/Local/Python/pythoncore-3.14-64` at the front of PATH for this managed check in the current environment.
