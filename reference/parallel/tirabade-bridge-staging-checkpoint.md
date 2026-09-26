# Independent relationship bridge staging

The integrated story remains 323 scenes at SHA256 `318A0AC394680CAEC127591505E7E2D333E9DD01BA44137F3ED38B2ABF5CB9C4`.
No independent-wife source or bridge scene has been added to that export yet.
The installed mod remains unchanged.

The staged bridge source is `storylines/tirabade_independent_bridge.py`, SHA256 `E67595DDDD3404E9A53B86A0062769091F32ED97EEB068B614A91B9C90FDF62F`.
It adds local refusal and honest courtship choices, played separate-relationship discussions, a negotiated shared supper, an actual new Abyss letter, and history-specific shared prose and endings.
Existing scene, node and answer identities are retained.
Existing answers that lead to affair-specific prose gain a forbid for the new negotiated-table history; appended alternatives serve that mutually exclusive history.
This is the deliberate exception to the earlier plan's exact-prefix wording: old answer indices and old-history behavior remain intact, while those answers cannot invent an affair for the new route.

The [independent bridge review](../story-review/tirabade-independent-bridge-review.md) identified three history defects, then accepted their corrected passages at 92-94 across its reviewed disciplines.
It does not approve the reviewer's own Anevia campaign, the entire Tirabade assembly or runtime delivery.
Root's `TirabadeIndependentBridgeTests` passed 2,675 focused assertions, including an actual traversal from negotiated supper through the developed shared campaign and ending without fake affair or old-scene flags.
These checks also preserve old answer identities, distinguish local and global refusal, exercise group dissolution and Anevia's real new invitation, and reject missing paired participants.

Run the staged check with:

```powershell
python tests/write-tirabade-bridge-fixture.py
dotnet run --project tests/RulesTests.csproj -c Release -- --tirabade-bridge development/Story.json development/tirabade-bridge-fixture.json
```

The fixture imports the actual frozen Anevia manuscript but uses explicitly labeled Irabeth contract producers while her manuscript is being completed.
It does not prove played Irabeth acquisition, the combined original campaign regression, all interruption/end-state combinations or release readiness.
Both full manuscripts, their joins and their final assembled paths still need independent review and full integration checks.
Anevia's first full review is in progress and has already identified continuity repairs; the manuscript is not approved.

The separate paired-contact engine change passed 18,784,596 full rules assertions and an [independent bounded review](paired-contact-review.md).
It uses an optional AdditionalContactUnits array alongside the existing required primary ContactUnit.
Each actor retains the existing unique, loaded, living and nonhostile native-contact checks.
The predicate proves availability in the loaded area, not proximity; the bridge narrates arranging and arriving at its meetings.

After registering the separately reviewed Jerribeth observation tests, the native-check fixture passed 42,946 managed assertions over 324 scenes and 12,513 generated blueprints.
The fixture contains all 323 integrated scenes plus one mechanical scene, not an extra approved route scene.
Its story SHA256 is `6DB8698D909648EA0C1F45E7038E1D66CCAC69155713FE7B7D96916BDC575013` and DLL SHA256 is `17FBCBEA31F916F4FF4286B58168C8EE1918E7C6E341253891E55DF1754D0FB9`.
Bindings passed 629 uses against 108 archive targets and 29 reviewed parent targets.
Both source and managed projects compiled with zero warnings or errors.
These checks do not execute Unity, the parent's initializer, ToyBox, portrait rendering or a native saved-game round trip.

## Retained campaign regression

The full rules runner initially rejected the bridge fixture because the old witnesses supplied no actors for the newly guarded shared meetings.
Their setups now explicitly supply both native actor IDs and the capital area.
They deliberately choose the retained affair outcomes, rather than letting a highest-flag-count heuristic accidentally select a new local refusal or honest-courtship branch.
The original-only campaign also excludes the developed `three_` scenes, which have their own played progression suite.
This keeps its explicit shorter-farewell witness meaningful once its capital location makes those optional developed scenes available.
No production guard was weakened for these fixture repairs.

The full runner passed 18,786,907 assertions on the staged bridge fixture with the frozen original Anevia manuscript and the explicit Irabeth contract declaration.
The unchanged integrated 323-scene story separately passed 18,784,596 assertions with the revised fixtures.
These passes do not overturn the [Anevia editorial rejection](../story-review/anevia-independent-first-review.md): known manuscript chronology and ending defects require her dedicated repairs and rereview.

The stored original 34-scene artifact predates the newer optional quarrel answers.
Running the current authoring expectations against that historical artifact correctly exposed the mismatch.
An explicit `--installed-legacy` mode now retains the original behavior checks while omitting only expectations for those two not-yet-authored answers.
That mode is restricted to a standalone 34-scene story; default development runs still require both newer answers.
It passed 3,385 assertions on `package/Story.json` without modifying that artifact.

The same staged bridge fixture, SHA256 `368A8BDD76BD594FA29EAAF5C2D70BCA39A8885F572E3E3B7BC6D0041FAD1BDD`, subsequently passed 703 binding uses against 108 archive targets and 29 reviewed parent targets.
Actual managed construction passed 47,199 assertions for its 364 scenes and 13,763 generated blueprints with DLL `17FBCBEA31F916F4FF4286B58168C8EE1918E7C6E341253891E55DF1754D0FB9`.
The 364 includes the explicit Irabeth contract fixture and the unapproved first Anevia manuscript; it is not the integrated scene count or a count of reviewed content.

The [native Anevia bereavement audit](../canon-review/anevia-after-irabeth-death-audit.md) confirms temporary coronation staging followed by native departure and actor hiding.
A generally available post-coronation grief visit is not proved.
The independent routes must preserve that restriction until a credible voluntary return or a genuinely verified earlier opportunity is implemented.
Native Commander-caused Irabeth death also needs its own consequences rather than generic supportive grief.
