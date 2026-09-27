# Konomi retained-return export review

Verdict: pass for the development export integration reviewed here.
No blocking export, registration, fixture or metadata defect was found.
This is one independent review of root-authored integration, not approval of the whole route, art, installed package or Unity behavior.

## Frozen scope

| Artifact | SHA256 |
| --- | --- |
| expansion.py | 209103DE4EF2185A1921D0D75CE66001C4FFDD85973A04DE89FC9C30204C028A |
| development/Story.json | 68DB5A6148241DE959B60A1402F62A23AEEEDE4DEA6B5D00DCDC8E92202DA171 |
| tests/KonomiContactTests.cs | 163F5C4EED6378A444983609C828EBF9316843CA6E68C48E25E41AE318624768 |
| tests/Program.cs | 56870154F0903AD9B360BC347AA164728BA88D82CAAFEEF833A8C7F5D1FE419B |
| storylines/konomi_retained_return.py | B0514BA7BE3BA5115899BB9B4E533EAEDFAE359A599B3670924DD1B2B566E227 |

The manuscript's separate [literary review](../story-review/konomi-retained-return-first-review.md) and the [engine review](konomi-retained-engine-review.md) retain their narrower claims and limitations.

## Independent structural and fixture checks

I compared the actual export with `git show HEAD:development/Story.json` and with a fresh JSON-normalized `expansion.make_expansion()` result.
The actual export equals fresh assembly.
All 533 previous scene objects remain structurally identical and retain their relative order.
Exactly four scenes were added, equal to the frozen retained-return module's scenes and placed immediately before the first existing Konomi scene.
The export contains 537 scenes and Konomi has 74.

All other top-level metadata remains identical except Scenes, Relationships and Revivals.
All non-Konomi relationship metadata and all existing revival definitions are preserved.
The added Konomi revival definition matches the manuscript module.
Konomi's metadata changes are limited to the retained-death unavailable flag, history-neutral description and appended guidance.

Mutation probes changed returned scene text, revival unit, Konomi unavailable flags and guidance.
The module's source constants remained intact and a subsequent assembly reproduced the original expected result.
These probes passed without editing repository files.

The contact fixture correctly classifies inquiry and attempted recovery separately from physical aftercare.
Its remote recovery witness first rejects absent retained-body eligibility, then adds the derived eligibility evidence for the positive availability assertion.
This corrects the witness without weakening production rules or pretending to execute resurrection.
Both aftercare scenes require the exact actor, retained-return proof and current return-contact evidence, without treating council office as proof of contact.
Ordinary scene contact checks remain intact.
The retained-return suite is registered when its inquiry scene is present.
The previously reviewed generic recovery closed-relationship exception remains scoped to Konomi.

## Verification

I created a separate temporary test project at `C:/Users/Z/AppData/Local/Temp/konomi-export-audit-8cf7e3bb` and ran the production validator and focused suites against the actual 537-scene export.
KonomiContactTests passed 1,261 assertions, KonomiRetainedReturnTests passed 76,810, and RetainedRecoveryRulesTests passed 38.
The run completed successfully without warnings in its output.
It compiled repository test and rules source into isolated output and did not rebuild shared production artifacts.

I also checked the [root integration checkpoint](konomi-retained-return-integration-checkpoint.md) for consistency with the frozen artifacts and review scope.
Its reported full Rules result of 24,439,467 assertions and managed result of 67,084 assertions across 19,408 constructed blueprints are root-run evidence, not additional runs by this reviewer.
Its listed export and source hashes match those inspected here.
Its distinction between development integration and unresolved native runtime behavior is accurate.

## Player-facing limitations

The journal no longer assumes prior correspondence merely because recovery opened a relationship entry.
Its guidance describes a possible investigation when the body remains in Drezen, requires availability for subsequent visits, and explicitly preserves earlier refusal and office history.
It does not promise that every recovered actor can immediately meet the Commander.

A recovered actor still hidden by native unappointed or dismissed-office behavior cannot currently enter physical aftercare.
Missing, destroyed and never-spawned actors remain outside this recovery implementation.
The checkpoint states these limitations and therefore does not claim the full Trickster access requirement is complete.
This review does not establish in-game resurrection, native placement, later-frame stability, save/load, ToyBox behavior or successful installed-package playthrough.
