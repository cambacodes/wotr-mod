# Tirabade saved-actor observer review

Accepted for read-only integration.
This does not approve resurrection, relocation, restored contact or a completed Trickster route.
The author did not approve their implementation; root reviewed the released source and native-object tests independently.

Reviewed source: `src/TirabadeRecoveryObserver.cs`, SHA256 `5D2A772B15E2B98FDF89828A647CAB77360F64634A95600EF49F4BB4CB75872D`.
Reviewed tests: `managed-tests/TirabadeRecoveryObservationTests.cs`, SHA256 `5A4DDFC80D8187015B5F0D78279DFF63C41E6939367863DBCF00CC8B7530B7F6`.
The native source records and exact Iz scene-name evidence are in `reference/parallel/tirabade-recovery-observer-handoff.md`.

The wrapper reuses the previously reviewed `JerribethRecovery.Inspect` implementation and immutable source records.
It supplies the two capital sources and three Iz alternatives without introducing a second copy of saved-actor inspection logic.
It returns each observation independently and marks both claimants when separate spawners reference one actor ID.
It has no method that loads a missing area, creates a scene state, spawns an actor, writes a native flag, revives a corpse or moves a unit.

The loaded-area guard and scene readiness checks remain in front of the native registry reads.
Retained life is explicitly separate from physical contact, willingness and recovery eligibility.
An observed living capital body leaves all unloaded Iz sources unknown.
Distinct living and dead Iz bodies remain separate results requiring later reconciliation.
This avoids treating the capital representation as proof that Irabeth survived her native death scene.

Root read the entire new wrapper and managed fixture, then reran the isolated test executable.
All 154 assertions pass using actual saved-state, spawner, unit-reference, unit-descriptor and life-state types.
The tests cover conflicting storage and registry identities, missing references, loading state, wrong blueprints, retained life and death, multiple representations and preservation of saved data.
They bypass Unity-dependent constructors and supply loading and registry delegates; they are not real save deserialization or a live hidden-actor test.
The singleton-based top-level entry remains compiled and inspected rather than executed inside a running game.

Root registered these tests in the normal managed runner and rebuilt both production and managed projects with zero warnings and errors.
The integrated 431-scene payload passes 53,343 managed assertions over 15,604 generated blueprints, including the new 154 observer checks.
Existing dialogue answers, finish actions and repeated construction remain preserved.
Production DLL SHA256: `EEBA86B2454713BFFF1DEECE2D7B96040B9ABC59C4251F4139B4B78B117BE428`.
Story SHA256: `9E144F6D7961177C92C40C70A9818B03DA96CF02524D938D71EB91D5136BD489`.

There is no story caller or restoration operation yet.
The next native audit must identify an identity-preserving transfer and positioning operation before returning an actor to a new meeting location.
Historical death and departure, voluntary agreement, refusal, native actor ownership and ending selection remain separate requirements for that implementation.
The installed mod remains unchanged.
