# Konomi hearing scene review

Reviewed konomi.hearing and konomi.hearing_after in storylines/konomi.py, SHA256 75CAA0B51266F0B6C58BDF02FD6FED06CEF37D578A1BA3108A54073CAE6C1C79.
This is a bounded review of these newly authored scenes and their immediate dependencies.
It does not approve the full route, its length, final art, unimplemented access recovery, or runtime behavior.
The scenes contain no major native-canon contradiction identified by this review.
The reported wording and prop-continuity corrections are resolved in this revision.

## Native voice and motives

The private dispute fits Konomi's appetite for political work, controlled anger, and distinction between useful evidence and a satisfying argument.
Diplomacy_Officer/Cue_0040, 35c3dcd5356d4bc428e70dbf99230463, explicitly describes political maneuvering as an invigorating hunt.
Her delight in the planted inspection notices and irritation when the registrar finds them insufficient are consistent with that motive.
The registrar's refusal to treat a clever trap as proof of the buyer's original knowledge gives Konomi an obstacle she cannot remove by speaking more sharply.

Diplomacy_Officer/Cue_0016, 2f4b52dd74dd6a14981d0de2f9b631b0, favors political strategy over bloody warfare.
A complaint through a private professional association is compatible with that preference.
Her demand to inspect the wording of the finding, her repeated attempt to persuade the registrar, and her reluctant restraint in hearing_after.still_disagree are more specific to her than a generic declaration about respecting boundaries.
The aftermath allows affection and anger to coexist rather than making her abandon her original judgment for the romantic outcome.

## Invented institution and authority

The copyists' association, registrar, two working copyists, absent buyer, and dispute procedure are new authorship.
The source explicitly describes this as a private association dispute rather than a native quest or statement of Mendevian law.
The scene gives the adjudicators authority over member services and referrals, not imprisonment or national policy.
The buyer has expressly agreed to accept their decision about access to members' work.
Their inability to bind every shop in Drezen further limits the claim.
These bounds avoid presenting invented law as established game lore.

The public branch separates the household's choice of couriers from the unauthorized purchase of the private letter.
Neither finding gives Konomi back the policy-dinner invitation or resolves the household's demand for her recommendations.
The private branch follows the previously authored inspection-notice investigation.
Both therefore extend the addon's leak sequence without overwriting a native resource choice or council outcome.
No native judicial resolution is claimed.
The new participants are described through established professional roles, with no child portrayal or romantic role introduced.

## Choices and consequences

The full-disclosure and covered-passages choices are communicated before the adjudicators read the letter.
The full-disclosure result establishes the stronger complaint while leaving Konomi unhappy about the loss of privacy.
The covered result preserves privacy but leaves the buyer able to commission work.
The same limited action against the copyist occurs in either case.
That is a clear difference in outcome, and the later conversation responds to the actual result rather than simply rewarding agreement.

The current compare node offers withdrawal of permission before the full reading and routes it to finding_covered.
This follows through on whole's assurance that the player can ask for the letter back.
The withdrawal leaves hearing_whole as a record of the earlier choice, but hearing_after uses hearing_buyer_barred or hearing_buyer_unbarred to select the actual outcome.
No false success claim caused by that retained historical flag was found in these scenes.

The almost_denied branch requires the Commander to acknowledge authorship in front of the registrar.
Its aftermath explicitly remembers the previous denial proposal and apology.
That supplies the later behavioral evidence missing from the earlier immediate apology scene.
Konomi's continued disagreement in the covered branch does not become jealousy or a requirement to abandon other partners.
The scene preserves her preference without making it the price of continued affection.

## Political state and contact

The scenes inherit the ordinary helper's positive konomi.present requirement and Drezen restriction.
They are optional, require scandal_answered or hearing_finished respectively, and are excluded after farewell.
The aftermath excludes inhuman, so it does not silently promise the same pastry and physical-closeness scene for every transformed body.
This exclusion leaves alternate content unwritten; it is not proof of a completed transformation branch.

Nothing in these two scenes requires a currently operating Royal Council to exercise judicial authority.
This helps them remain plausible across ordinary Chapter 3 and Chapter 5 political states while the native officer is contactable.
Normal rank-eight council conclusion is not officer dismissal, as established in konomi-availability-review.md.
Rank-six dismissal still removes ordinary access, and no new guest invitation or restoration is implemented by the hearing.
The invented association's continued operation is a reasonable scene premise, not a verified native flag.
Exceptional hostile or ruined-city states still require the separate availability audit and appropriate content.

## Final correction verification

Hearing.courtyard now refers to what the Commander wrote, preserving the authorship established in acknowledge and the earlier route.
Hearing_after.trust now places the finding beneath a book on the common path, making warm's location correct on every result branch.
Both the original and stolen copy remain wrapped before the decision.
In finding_covered, Konomi masks both versions while facing them away from the adjudicators, and the player checks the visible text before handing them across.
The limited disclosure is therefore not undermined by an already-readable copy or by the registrar reading the material while covering it.

Whole now promises withdrawal before the reading begins, matching the actual compare choice.
The arrival transition explicitly says the next morning, removing ambiguity in the narrated chronology.
The pastry wording describes her prior deliberation rather than an unexplained long pause during the visit.
These corrections introduce no new native-canon issue identified in this focused pass.
The narrated overnight transition remains distinct from any requirement to advance the campaign clock mechanically.

## Bounded outcome

These scenes materially improve the leak arc by making the evidence choice playable and preserving an unwelcome consequence into a later intimate conversation.
Their canon scope and private institutional premise are clear.
No remaining major canon or local continuity blocker was identified in these two scenes at the recorded hash.
No full-route score or release approval is assigned.

## Final hash confirmation

Confirmed source SHA256 D8F3C575B06A1E88E0D90EEE7697FD67DF4261B2F732FA3FFCF0839DDE73613A.
Hearing_after.uncertain now folds the finding and lays it aside; the shared trust node still places it beneath the book.
This removes the duplicate placement without changing the bounded findings above.
No new canon or continuity blocker was identified in this focused correction.
