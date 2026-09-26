# Konomi political-state investigation

Primary records were extracted from the installed `blueprints.zip` into `konomi-political-native-records.json` and `konomi-political-consumers.json` in this directory.
Localized text was resolved from the installed enGB localization file.
This investigation does not yet implement political reactivity in the romance.

The ordinary officer answer `a24c33ab318c17f4ba5dcb8fc22542f6` selects its first available reply in this order: foreign intervention, domestic recovery, ongoing crisis, earlier fallback.
Foreign intervention cue `9980a1ecf3ca24e42ab3b22f858677b5` requires rank-eight dialogue history and the playing etude `c6e9a69f602a48e18424f4b6d71062b4`.
That etude is named ApprovedHelpFromAnotherCountryDiplomacy7, so it alone does not prove the later intervention has already taken effect.
Domestic recovery cue `60585f7319a294147a54f440865b21a2` requires rank-eight dialogue history and relies on earlier selection of the foreign-intervention alternative to distinguish the outcomes.
Ongoing crisis cue `07459f4d09fa81e4b99beea351fb0434` requires rank-six dialogue history and similarly relies on selection order for later outcomes to supersede it.
Treating the three conditions as independent current-state booleans would therefore produce contradictions.

Rank-six dialogue `30333438aac8d3647bef882fa87e978e` completes the officer etude only when dismissal answer `73c5728c4c6658344bedcc1b666e598c` was selected.
Rank-eight dialogue `6178470b05c75484085753b821a6a614` does not complete that officer etude in its extracted finish actions.
Its final Konomi cue `7f64a30ceb4bfb046990bccbded7ac75` nevertheless states that the Diplomatic Council has served its purpose.
Office presence and continued existence of that council must not be treated as the same fact.

Rank-eight respect cue `8311ef29223c4fe469c95cd8eb80e539` precedes a companion reaction sequence and the final council conclusion.
The reaction sequence exits through `7b47815a75f2baa46a5d9a07499f2a60` into that conclusion.
Seen-cue bindings can support remembered conversations without claiming that every player has asked for a current situation report.
They must not be used as a substitute for current political state when an earlier report can remain in dialogue history after a later resolution.

Next implementation must either read the native dialogue-completion/history predicate with its actual semantics or use carefully bounded known-history responses.
Fresh decompilation now confirms that DialogSeen records dialogue start, not completion; see `konomi-dialog-history-semantics.md` for the exact evidence and resulting integration cases.
It must preserve the rank-eight precedence, distinguish a concluded council from dismissal, cover missing or bypassed reports, and avoid rewriting any native decision.
Private-route patronage and household pressure remain separate authored consequences requiring their own played follow-through.
