# Konomi retained recovery engine checkpoint

The engine now dispatches configured Konomi revival choices to the retained-body service rather than the companion roster service.
It saves the exact authored choice identity and records only a current verified return.
Later polling can finish recording that earlier action without invoking resurrection again.
The reviewed manuscript remains a separate integration step.

The new verified-return marker is `konomi.retained_return_confirmed`.
The preexisting `konomi.returned` marker still means the ordinary visit in the original campaign.
Current retained death and permission to attempt restoration are separate observations, so a second death is not hidden by the one-return limit.
Physical aftercare requires the same original actor, usable native contact and confirmed return history.
Recovery and explicitly validated aftercare can proceed after a prior refusal; ordinary romance remains closed.
Other recovery routes retain their previous closure rules.

The validator rejects manufactured proof through choice effects, completed scene IDs, journal-state aliases or native binding aliases.
One terminal Konomi request is permitted per scene, preventing ambiguous saved requests.
The terminal restoration choice can award only the verified-return marker.
Starting a book also uses the existing journal entry mechanism; manuscript integration must use a history-neutral description.

## Verification

The independent engine review is `konomi-retained-engine-review.md`.
The source and managed test projects build in Release with zero warnings or errors.
The full original 533-scene Rules run passed 24,303,393 assertions, including 38 focused recovery-policy checks.
The corresponding managed run passed 66,293 assertions and constructed 19,199 blueprints while preserving native answer and epilogue structures.
Tested DLL SHA256: `3A2C280601E80742B128F8B7CDF077B5B54757B337ECA3D642056883CC67F333`.
Unchanged 533-scene Story SHA256: `D0D019E06C1A9656CA2145DCD06EF717DB5D356F663DC7A202CE8F3D250E6045`.
The generic recovery test's closure expectation is now scoped to this explicit Konomi exception before testing a candidate that includes her new recovery scenes.

These full runs preserve the existing campaign and exercise managed construction; they do not yet exercise the new manuscript through Main.Build.
The standalone resurrection fixture continues to expose the Unity ECall boundary, not a successful revival.
Actual resurrection, later-frame stability, physical delivery, save/load and ToyBox execution remain unverified.
Hidden, destroyed, missing, never-spawned and other unsupported histories remain unfinished work under the full Trickster requirement.
