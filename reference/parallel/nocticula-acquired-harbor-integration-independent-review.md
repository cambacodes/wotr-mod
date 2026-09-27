# Nocticula acquired harbor integration independent review

The registered families and selected-state tests have a sound basic contract, and the shared journal wording was corrected during this audit.
The inherited ending-scheduling defect found in the initial audit was reproduced and repaired during this review, as documented in the final addendum.
The repaired export-selection and scheduler contract passes this scoped integration review; native runtime readiness remains unapproved.
This report records code and export inspection, not a reviewer-run C# build or Unity playthrough.
Root owns those executions and any repair.

## Inspected versions

| Artifact | SHA256 |
| --- | --- |
| Initial `expansion.py` | `18EFBD255D1818CEAAFCAB1E983EAEC1D53E7ABDED0BB7216683D28979389BBC` |
| Initial `development/Story.json` | `3421867D230611DB42A813E64778375026310E7345E012CDD18CE672FFEC9394` |
| Journal-corrected `expansion.py` | `DD0D3DCB3D2BADE4ECA30E61D35CDDDDD093C041BA4BB2750A32D924B3DCCCD4` |
| Journal-corrected `development/Story.json` | `8194A71F0A5780CEC21BB28DE4A04F8DC6E18A2E781D39590F72ED6432B19DD2` |
| `tests/NocticulaAcquiredHarborTests.cs` | `1BBD37EC2C0D2DEA171C828E75A8F9991B672433DA2D24CDDA3B4D1F98643989` |
| `tests/NocticulaContinuationTests.cs` | `CC17921F79AF0231FE69F6C997882ECB0634BE6E7E7DCD723D93AE53127B2470` |
| `tests/Program.cs` | `6CE0BB604223C62FC46630CD9D72DDCE583D0486F6CC53EAD10424F55CEC3463` |
| `src/Main.cs` | `28F41F461816C721BF14660B4F516C525CE41EED375E7FC1EEE318087B837948` |

The acquired manuscript is the repaired `4EE87A39D86ACEF60D838BB7C471E3197DDDB742C66E78BFB2A7F89399A9F3FC` source reviewed separately.
The donor remains `11B5B48D10DEDC903FE7FB9A64C3BA265636CED33E96A2508ACED15A5DC2764B`.
Only this audit report was edited.

## Export and family selection

A read-only comparison found 753 unique exported scene IDs.
Every acquired scene exactly matches the repaired source dictionary.
Each of the 32 original definitions exactly matches its donor except for the appended `noct.join.harbor_variant_ready` prohibition.
That includes all original recollections, not just visits.
The original manuscript itself is not rewritten.

Once acquired readiness is present, the original family is unavailable.
Acquired delivery additionally requires recurring acceptance, the demonstrated exit, bridge completion and exactly one provenance witness.
Readiness alone therefore suppresses the original family before it permits the acquired family, during the final bridge response.
This is not a duplicate offer, but interruption and resumption at that precise boundary need a save/cancel test before being called safe.

Acquired scenes forbid their original scene IDs and write those aliases only on non-abort terminals.
Existing original completion thus suppresses the corresponding acquired copy; acquired completion suppresses its siblings and preserves shared progress.
Current Gift selection gives renewed Gift priority, and the shared face alias prevents replay after Gift changes.
No native parent, Gift, quest or cue alias is forged by these choices.
Arbitrary mid-route migration is still not established by this contract alone.

## Journal defect and correction

The first export retained the description about an undertaking beyond an original bargain and appended acquired instructions after guidance saying these dreams could not recover a missed or refused relationship.
For new/refused entrants, that produced a false prior-bargain claim and conflicting instructions.
`Main.BuildJournal` binds these strings directly to quest and objective text, so this was a player-facing defect rather than unused metadata.

Root corrected the description to a hidden-harbor investigation through chosen meetings.
The current guidance explicitly distinguishes an existing Chapter 5 dream relationship from an earned Trickster correspondence invitation, then explains the bridge's limits.
I inspected those corrected exported strings.
They no longer invent a prior accepted bargain for new/refused entrants or imply that dream access restores a lost Gift.
The shared objective and lifecycle flags remain consistent with this undertaking.

## Blocking scheduling finding

`Rules.NextRemote` selects the first scene satisfying `IsRemote`, not `ManualOnly`, and `Available`.
It does not exclude an owner ending in `Epilogue`.
The new recollections inherit `Remote = true`, minimum chapter zero, maximum chapter 99 and zero delay.
Their ordinary prerequisites become true at harbor completion, without a native endgame-phase requirement.

For example, `noct.ending_company.acquired.new` requires completed harbor, chosen company and completed bridge history.
`noct.ending_aeon.acquired.new` requires completed harbor and bridge history but relies on its owner, rather than an explicit Aeon flag, to select the proper native presentation.
`Rules.Available` returns true for eligible epilogue owners before applying ordinary relationship availability and delay handling.
`Main.Update` calls `NextRemote` after a rest and then starts `dialogs[scene.Id]`.
`BuildScene` creates standalone book dialogs for these scenes as well as pages later attached to native epilogue sequences.
There is therefore a complete inspected code path for premature rest delivery, not merely a naming concern.

This predates the acquired copies, but the new registration inherits it.
After other pending eligible remote visits have been consumed, an ordinary recollection can be selected at rest; the Aeon recollection can also become eligible despite the character remaining a Trickster.
Displaying a show-once ending page early may also affect its later native presentation.
The last consequence needs Unity verification and is not asserted as an observed save result here.

Root was asked to reproduce this through `Rules.NextRemote` using an actually earned completed witness.
The minimal robust fix belongs in the shared remote scheduler: exclude epilogue owners from ordinary rest delivery while leaving their native epilogue predicates intact.
A focused test should keep an ordinary pending remote visit selectable, reject ordinary and Aeon recollections at rest, and confirm native-ending `Available` evaluation still works in its intended owner context.
No scheduler repair or test result is claimed by this frozen report.

## What the tests actually earn

`NocticulaAcquiredHarborTests` begins with six explicit native-history fixtures.
It plays the real acquisition entry, the two remote follow-ups, the concession and the bridge through `Program.Walk` before entering acquired visits.
It does not seed a finished channel, romantic agreement, provenance witness or bridge readiness to skip that work.
The Council disclosure and reward aliases are explicitly supplied native boundaries.
Current Gift transitions and endgame outcomes are separate predicate probes, not claims that their native events were played.

The test uses `Rules.Available`, preserves actual timestamps, and retains played representative states when merging future-equivalent histories.
It checks unique delivery, original-family exclusion, prerequisites, closure, native-state preservation, abort/retry behavior, terminal aliases and post-completion replay.
The original continuation test now excludes acquired IDs, and `Program` calls the dedicated acquired tester.
Its generic scene loop skips those scenes only after their focused suite runs in the full registered export.

The coverage assertions are narrower than all generated nodes.
They require each family to enter each visit, both first-question callbacks, and both outcomes of eligible checks.
The base fixtures do not supply every optional parent ambition or Laulieh witness, and the Gift-transition probes do not add their visited nodes to the main coverage dictionary.
Do not describe this suite as playing all nodes of all 102 definitions.
Source-level optional-witness tests and the original family's separate checks provide additional evidence within their own scopes.

The suite's ending probes call `Available` and walk the selected recollection after supplying endgame outcomes.
They do not test `NextRemote`, so a passing ending-precedence assertion cannot detect the premature-rest defect.
The in-memory `Program.Copy` check establishes retained state behavior, not disk serialization or Unity scene cancellation.
The walker also records terminal scene completion for epilogues, while actual compiled ending actions rely on the explicit original alias and native page behavior; managed blueprint checks remain necessary.

## Execution and remaining limits

Root reported 38,070,122 Rules assertions and 101,435 managed assertions over 27,147 blueprints for the initial `3421867...` export.
The acquired test reported 92,616 projected outcomes, 23,286 closures, 144 Gift probes and 144 ending probes.
I did not rerun those builds or independently observe those execution logs in this task.
The later journal correction was inspected as content; no new full-suite result is attributed to it here.

Native return from the Council audience, actual renewed-Gift timing, death-alias truth, native epilogue scheduling, save/reload, displayed journal transitions and ToyBox play remain separate verification requirements.
The earlier selected-length and literary reports retain their exact scopes.
The initial integration hold remained until the scheduling finding was reproduced and resolved at the versions recorded below.

## Scheduler repair and final rereview

The final inspected `src/Story.cs` hash is `22C68F5464DD4488DD94E3E23A3AF06EBD2C9FC7FEA79A15B892B4ABEE878019`.
The final inspected acquired-test hash is `EFFB315259B3B26CCF84EC6915BE27FFB3472AD240F456A49DA1F11D65AF2603`.
Root first added a regression that takes nine actually earned history/finale witnesses, advances each by 24 hours, and invokes the real `Rules.NextRemote` on the harbor's original and acquired scenes.
That reduced story retains the actual relationship metadata and prevents an unrelated campaign's pending visit from hiding the faulty selection.
The retained reproduction log fails on `noct.ending_company.acquired.new` being scheduled at rest.
I inspected the failure log and the test code; this is a real managed scheduler reproduction, not a Unity playthrough.

Root then added an `Owner.EndsWith("Epilogue", StringComparison.Ordinal)` exclusion directly to `Rules.NextRemote`.
The fix leaves `IsRemote`, native page attachment and `Rules.Available` ending predicates unchanged.
It excludes both ordinary and Aeon ending owners from ordinary rest scheduling while preserving their intended native presentation path.
The existing ordinary Jerribeth delivery assertion still exercises positive remote scheduling, and the acquired suite still exercises ordinary ending availability after its explicit outcome boundary.

I inspected the completed fixed Rules log, which reports 38,070,131 passing assertions, including the nine new scheduler witnesses.
It retains 1,296 earned joins, 92,616 acquired projected outcomes, 23,286 closures, 24 postponements, 144 Gift probes and 144 ending probes.
The fixed managed run was also retained in `acquired-scheduler-fixed-managed.log`; root reports 101,435 assertions and DLL SHA256 `B4356C92547764AF3FB49854648BAE808F9C7ECC887B8AA7A4B0DE743A4DDE97`.
No builds were launched by this reviewer.

The original scheduling hold is resolved at these hashes.
The shared journal correction, exact original/acquired export separation, earned selected-state tests and focused scheduler fix now pass the scoped code-and-export audit.
This does not certify actual native ending production, the death alias's truth, save serialization, interruption/resumption, scene-art display or ToyBox behavior in a running game.
