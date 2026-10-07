# Konomi complaint after private return

The previous development export recorded a pending complaint but offered no hearing once native officer contact was lost.
The production-rules scenario reproduced this missing continuation before the adapter was added.

`storylines/konomi_private_hearing.py` creates alternate contact entries for the existing hearing, its aftermath and the promised new-letter outing.
It copies the original authoring objects at build time and changes only contact metadata and the three opening passages.
Existing nodes, choices and shared outcome flags retain the ordinary sequence's evidence decisions, withdrawal of permission, actual findings, trust repair and prize ownership.
The original scene objects are not mutated by the adapter.
The ordinary entries now forbid their shared completion flags so a changed contact state cannot replay an already completed event.

Source SHA256 is `FEED83920A2A8D4EE137F6E057A414DAFE303A6283DBEC94CD4C9C6876E25F5F`.
The original source with shared completion blockers has SHA256 `68F7D5C9F133EFB49731334BF49FB3635939E61381BFBEA0A10D93529E6C25CD`.
The three new scene IDs are `konomi.private_hearing`, `konomi.private_hearing_after` and `konomi.private_new_letter`.

## Contact and progression

All three require native dismissal, completion of the officer etude and the authored `konomi.private_returned` event.
They are remote book entries after rest in Drezen during Chapters 3 or 5.
They forbid native officer presence, inhuman form, farewell and the completed private-future departure, while the relationship's closed flag remains enforced by production rules.
They do not require current Trickster power because the earlier intervention already established contact and ordinary travel brought Konomi back.
They do not grant native presence or reverse dismissal.

The hearing additionally requires the existing investigation response, `konomi.scandal_answered`.
It does not require the newly added pending-hearing marker, allowing older development histories with the same actual investigation to continue.
The aftermath and promised outing use their original shared prerequisites and delays.
Players who completed the hearing through ordinary contact can resume an unfinished aftermath or promised outing after private return without repeating the hearing.
The historical `konomi.private_hearing_needed` marker is retained, while `konomi.hearing_finished` records resolution.
No text consumer treats the former marker as proof that the complaint is still pending.

## Content accounting and remaining work

These are three contact variants of existing events, not three independently authored additions to route depth.
The route's raw exported inventory grows by 4,071 words, but exact segment deduplication grows by only 348 words for the adapted openings.
Even the latter is inventory, not evidence of increased dramatic depth.
The main benefit is that a dismissed-history playthrough can now reach its previously stranded consequences.
Whole-route approval, native political reactivity, the household courier dispute, roof follow-up and an Act 4 private-contact bridge remain outstanding.
The optional hearing can still be skipped before the final departure.

## Verification

The updated 162-scene export at SHA256 `2338792EC99EC67C064EEA5C4224984E6BC294F2C3A5BE957F2275EE3C110BF3` passed 1,646,741 production-rules assertions.
Focused scenarios traverse public and discreet responses, prior denial and apology, both evidence findings, permission withdrawal, the trust aftermath and all promised outing branches.
They check scheduling, blocked contact, unchanged native dismissal, preservation of another romance and suppression of replay through ordinary contact.
Native binding verification passed 239 uses resolving to 54 typed targets.
Managed construction passed 13,874 assertions over 4,693 generated blueprints.
Independent editorial review of the corrected adapter scored 92; actual runtime integration remains unverified.
These checks do not establish Unity execution, actual save persistence, ToyBox behavior or portrait display.
