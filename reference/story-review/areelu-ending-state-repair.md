# Areelu ending-state and physical-meeting repair

This repair follows the independent review of source `37A42DE5D06AA609F5F2A56833C9F01DE3F548A16441EE40C87AE6F470B09A22`.
The repaired source SHA-256 is `74C2F6B2BCCF23CAEEBD0BBD7FB00FE8247414758DF396786559802FEA27C0AD`.

Reproduction followed the actual year-end breakup choice with an earlier commitment flag present.
The old final menu still allowed the committed future and did not offer the closed future.
The breakup now records the closed-ending marker, and the active, open and paused ending choices exclude a recorded breakup.
The commitment option also requires the selected commitment ending, rather than accepting a historical commitment alone.

Exhaustive local traversal exposed a second problem: open and paused future pages were unreachable because the common epilogue ended before the final menu.
The common transition now settles the private papers at the garden meeting and leads to that menu without inventing a year of commitment for those branches.
The dedicated open, paused, committed and closed futures are now reachable.

The survey-station meeting now uses `Remote=False`, matching its physical staging.
This supplies no actor, location hook or runtime producer by itself.

The new `_assert_final_outcomes` follows actual available choices from the final scene entry with and without an earlier commitment flag.
It verifies one available final outcome at each reached final menu, all four outcomes reachable, and only the closed future after the year-end breakup.
The module's graph and state checks, Python compilation and whitespace check pass.

The prior 24,977-word measurement belongs to the independently reviewed source, and is not a new measurement of this repair.
Immersion-breaking technical language, characterization, evil-path depth, art assignment and runtime integration still require work.
No complete-route approval is granted.
