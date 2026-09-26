# Konomi political consequence and ordinary closing callback

## Review candidate

This contribution addresses item 4 of [the assembled Konomi readiness review](../story-review/konomi-assembled-readiness-20260926.md).
It contains two optional retained-office visits that resolve an authored political correspondence decision, plus a short earned callback in the original ordinary close.
The author supplies no quality score or full-route approval.

Owned files are `storylines/konomi_political_consequence.py`, `tests/KonomiPoliticalConsequenceTests.cs`, and this handoff.
Existing story modules, shared engine/export files, art and installed game assets were not edited.

| File | SHA256 |
| --- | --- |
| `storylines/konomi_political_consequence.py` | `C2C1B917481A6A178BACF0666F44D6D90C864978EE6D5828483C200562D91559` |
| `tests/KonomiPoliticalConsequenceTests.cs` | `87C64B9AFD9BBD61D15E3671923445341DCC26331AF280C77346B950C91F91BC` |

These identify the revised frozen candidate after independent review.
The reviewer requested natural player questions in place of three unconfirmed-context labels that exposed history-checking language.
Only those three labels changed from source `16D6AA3BCE3084259A49E077C8CF79A448C0DAF72C6A21F49BDF2221D7DC9A06`.
Reversing the three substitutions reconstructs that exact prior file; indices, gates, effects and destinations are unchanged.

## Political decision and resolved consequences

`konomi.the_names_admitted` follows the existing `political_account` invitation to see what Konomi does with a difficult reply.
An authored Nerosyan correspondence circle invites her to compare accounts of who issued and carried out instructions.
Its organizer Veyra admits people whose service can be confirmed by an office already represented and shares only extracts whose authors permit that audience.
A former acting clerk, Marenne, can document work but cannot obtain confirmation of an appointment she never formally held.
The appointed secretary's interest in excluding her is understandable without making her entire account automatically true.

Konomi can accept the established place and broader reading, considering Marenne's submitted account without admitting her to the restricted discussion.
Alternatively, she can sponsor Marenne for a limited comparison, surrendering the broader reading and taking responsibility for corrections under both their names.
Both choices retain Konomi's desire for influence, an accountable institution and access to people who can answer her.
She identifies two arrangements she can defend before asking for the Commander's opinion.
The Commander does not become an adjudicator whose approval determines her moral improvement.

`konomi.the_answer_on_record` delivers the result after a correspondence delay.
With broad access, Konomi finds a date contradiction in the secretary's own letter; the circle circulates a definitive correction, retains her as a reader, and leaves Marenne outside the restricted correspondence.
The secretary stops answering Konomi's personal letters, and Marenne does not supply gratitude in exchange for the correction.
With sponsorship, Marenne's first date proves mistaken and is corrected under both names; the secretary still cannot substantiate the authorization he claims.
The final finding records that limited uncertainty rather than inventing proof, gives Marenne a direct answer, and does not admit Konomi to the broader reading.
That finding closes the presented comparison; no further investigation or sequel task is promised as a prerequisite to enjoying the relationship.

The second visit separately acknowledges a witnessed council conclusion and a witnessed native expression of political respect.
It finishes with either a kiss and private time or a walk.
Neither professional choice gates affection.
No arbitrary skill roll determines admission, preference, or consent.

Veyra, Marenne, the secretary, the correspondence circle, its permission terms, letters and corrections are authored alternate developments.
They are not verified native actors, a new native council, legal authority over Mendev, or an implemented change to crusade politics.
The scenes explicitly distinguish the circle's discussion from Konomi's continuing appointment and from an order issued in the Commander's name.
Only authored route flags are written.

## Native evidence and actual observed memories

I read `konomi_political.py` and the complete ordinary expansion, the actual underlying blueprint records in `konomi-political-native-records.json`, the political-state findings and dialogue-history semantics, and the five relevant strings directly from installed `Wrath_Data/StreamingAssets/Localization/enGB.json`.
The original officer report chooses foreign intervention before domestic recovery, then crisis, then its earlier fallback.
The new scene preserves that precedence and additionally requires the relevant report cue to have actually been seen before recalling it as a shared account.

| New seen-cue alias | Native cue | Supporting native report |
| --- | --- | --- |
| `konomi.foreign_report_seen` | `9980a1ecf3ca24e42ab3b22f858677b5` | Diplomacy_Officer/Cue_0029; foreign garrisons have improved order and taken over taxation/administration. |
| `konomi.domestic_report_seen` | `60585f7319a294147a54f440865b21a2` | Diplomacy_Officer/Cue_0042; Mendev resolves the crisis without outside intervention. |
| `konomi.crisis_report_seen` | `07459f4d09fa81e4b99beea351fb0434` | Diplomacy_Officer/Cue_0032; divided rule, failed services, unsafe roads and threatened famine. |

Foreign memory also requires `rank_eight_started` and `foreign_help_playing`.
Domestic memory requires `rank_eight_started` and excludes `foreign_help_playing`.
Crisis memory requires `rank_six_started` and excludes `rank_eight_started`.
Each context has a disjoint unconfirmed alternative if the applicable seen report is missing; an earlier or stale report cannot supply a new current settlement.
No dialog-start predicate is called completed business.
No set of all three native reports is required.

Council conclusion remains `konomi.council_conclusion_seen`, bound by the existing module to `7f64a30ceb4bfb046990bccbded7ac75`.
Political respect remains `konomi.political_respect_seen`, bound to `8311ef29223c4fe469c95cd8eb80e539`.
Those memories are independent of the current report selection and do not imply dismissal, new office authority or completed finish actions.
The second visit does not repeat a saved national-context claim from the first; its reply resolves the authored correspondence, and its role/respect branches read the histories currently available.

## Access and integration

Both visits require `konomi.present` and `konomi.political_account`.
The second also requires `konomi.political_terms_sent`.
They run only in Chapter 5, Drezen area `2570015799edf594daf2f076f2f975d8`, attached to answer list `0dc8b8604bb33c846a63f3eb62443674` with exact ContactUnit `ca2d58c5c65723945857e04fb85d30ce`.
Both forbid dismissed, closed, farewell and inhuman states.
The first delay is 24 hours; the second is 168 hours.
They are optional ordinary dialogue entries, not remote invented contact with a dismissed officer.
No event restores the officer, resumes a completed council, or clears a native result.

Append this module's `SCENES` and invoke `integrate(payload)` after existing Konomi scenes are present.
The overlay registers the three exact seen-cue aliases, rejecting conflicting bindings.
It appends one answer at `konomi.ordinary/start` and five callback nodes without changing original text, choices, answer indices or metadata.
Repeated integration is idempotent.
No existing scene acquires a new prerequisite.
Existing farewell/ordinary saves are not reset or forced to replay a closing scene.

The new ordinary answer requires `ordinary_expanded`, `trial_lived` and `readers_answered`.
It first recalls either the evening stopping time with two casks left or the morning arrival with the watch, charcoal and blocked entrance.
It then recalls either the accepted two-report joint arrangement and question addressed to Oselda, or the six-copy circular and its initial responses.
It returns to a copy of the original ordinary opening choices and retains their existing terminal `at_home` result.
The reply to the report is not inferred from merely proposing it: completed `ordinary_expanded` supplies that later event.
Short-course or older ordinary saves without this played history receive no fabricated callback.

## Measurements and tests

The two visits contain 22 pages; the ordinary callback adds five pages.
The contribution contains 2,651 raw new words and 2,601 distinct new words using the project's tokenizer and normalized text segments.
Copied original ordinary answer options are not credited as new writing.

Across the four report contexts, both council and respect memories, both institutional choices and both personal conclusions, 64 complete selected two-visit paths contain 1,373-1,400 words each.
The small closing callback contains 158-173 selected words before its copied original answer, plus the new entry answer.
These counts do not combine mutually exclusive reports, institutional choices or trial/publication memories.
They do not certify all-route quality or RanRomance parity.

Isolated candidate runner: `C:/Users/Z/AppData/Local/Temp/konomi-political-consequence-check-8bpdfavo/Check.csproj`.
Its adjacent Story.json was assembled in memory from current `expansion.make_expansion()` plus this module and overlay.
The final rerun includes the parent-integrated ordinary Konomi contact overlay from main303 and the repaired choice labels.
The runner uses actual shared `Rules.Validate` and `Program.Walk` helpers.
Result: **139,967 focused assertions passed**.

Tests earn margin through reckoning, Chapter 5 return and political account through actual choices.
They cover 128 combinations of current native report context, all three seen-cue bits, council conclusion and respect, including stale or absent report history.
Each reaches exactly one appropriate context; both institutional choices then produce their played reply.
They verify unchanged native/other-romance history, no unfinished new-page flags or timestamps, correspondence delays, deferral and replay prevention.
Missing office, dismissal, contact loss, wrong area and wrong chapter are rejected at entry and by the contact-continuation guard.

The callback tests separately play the full ordinary trial and publication chain for all four evening/morning and joint/circular combinations before entering the original ordinary scene.
They verify the correct remembered outcome, absence of the unchosen one, preservation of the original conclusion and exclusion when any required completion history is missing.
Every new page is visited.
An independent structural comparison of the in-memory payload confirms original scene metadata/text and answer prefixes remain unchanged; only the specified ordinary append and new aliases/scenes are added.

Independent writing/canon review, combined registration/build/binding checks and TTS presentation remain pending.
These checks do not establish live Unity interaction, current physical actor behavior on a particular save, portraits or ToyBox coexistence.
