# Minagho and Chivarro export integration review

Independent review on 2026-09-26.
The isolated 585-scene export preserves the shared 538-scene export exactly and appends the expected 47 continuation scenes.
The focused visit suite is an appropriate replacement for the generic minimum-prerequisite walker on the 23 visits.
The original registration also skipped 24 endings without replacing their page traversal; root corrected that during this review.
The corrected registration and ending-witness assertions pass this bounded integration review.

## Compared artifacts

| Artifact | SHA256 |
| --- | --- |
| `C:/Users/Z/AppData/Local/Temp/minachiv-root-export-ygfaj8pa/candidate.json` | A70A8AA1290C12BC2003CBA175031CCE04B1D2C24013F4FE541D78127C6D4EA4 |
| Shared `development/Story.json`, 538 scenes | 8DCEB83D44925E5C07C7407D1FCEABE9381CE147D9A862B22E4E88420583C300 |
| Final inspected `tests/MinaghoChivarroContinuationTests.cs` | 1CBBDCA1AFCB7DC5035107ED03E91EF6116D78A67419BD5F1BABE6206A368662 |
| Corrected `tests/Program.cs` | 55433C12577E1D456C66EE4E945DC884048C8AED9BCA11D6A0D85484EEA4D81A |

An independent Python comparison established four facts.
The first 538 candidate scene objects equal the shared export's scene objects, in the same order.
The remaining 47 equal `minagho_chivarro_continuation.SCENES` exactly.
Reconstructing the expected payload from a deep copy of the shared export, the module's `integrate` function, copied scenes and copied parent metadata produces an object equal to the entire candidate.
Only Scenes, Relationships, Etudes, CompletedQuests, SeenCues, ParentEpilogueEdits and ParentEpilogueLossRules differ at the top level.
This comparison concerns the isolated candidate above, not later Soana portrait assignment changes or a later shared export.

The integration function rejects conflicting existing native bindings and copies inserted values.
The root call also deep-copies scene and parent metadata objects.
These additions do not alter the preceding route objects in the compared candidate.

## Why the generic factor fixture fails

`minachiv.a_factor_at_the_table/start` offers three responses, requiring `source_found`, `ribbon_spent` or `fate_address` respectively, all with the `minachiv.` prefix.
The preceding visit records `evidence_kept` together with one of those outcomes at its actual terminal choices.
The factor scene's minimum entry prerequisites alone do not express which evidence method the player chose.
A fixture that injects only those minimum prerequisites therefore fabricates a history that the earlier visit does not produce.

The focused suite begins with external parent observations, checks that no addon history has been fabricated, and plays each preceding visit with `Program.Walk`.
That walker enumerates every offered choice and fails on an encountered page with no selectable answer.
The suite then carries earned results forward and checks every visit node has a witness and every authored outcome flag has a played producer.
Its future-state grouping retains flags read by subsequent scene gates, choice conditions and endings, so the three factor evidence methods are not accidentally merged away before use.
Replacing the generic factor fixture with this suite does not conceal the reported missing-choice condition on a reachable played history.

The eleven parent fixtures include freed Trickster and other histories, redemption, cult, dragon, legend, sanctuary, ordinary and soft refusal, and Demon romance and refusal.
The assertions also cover lost current Trickster powers, native blockers, missing parent witnesses, Demon service restrictions, chapter and area changes, chronology, aborted progress and unrelated relationships.
They do not execute the parent DLL's actual books or prove every possible native save combination.

## Ending coverage finding and correction

The initial root registration added all 47 continuation IDs to `playedContinuations`.
The focused suite traverses only visits.
Its ending checks evaluate selection and arbitration from completed and selected interrupted histories, but do not call `Program.Walk` on ending pages.
Thus the original registration removed the generic ending traversal without supplying an equivalent traversal.
I reported this before treating the integration as accepted.

Root changed the registration to exclude owners ending in `Epilogue`, leaving all 24 ending scenes under the generic walker.
I inspected that corrected condition in `tests/Program.cs`.
Every current ending consists of one `end` node with one unconditional terminal choice, no next target and no effects.
There is consequently no concealed conditional ending-page branch in this candidate.
The restored generic walker checks each current page's selectable terminal, while the focused suite checks ending availability from earned route histories.

I also requested an explicit earned-witness assertion for every ending ID.
Root added `witnessedEndings`, populated only after ordinary, special and Aeon selection from the already played histories, then checked every ending ID against that set.
I inspected the exact change and the final test source hash above.
This closes the possibility that one normal ending remains permanently shadowed while another still satisfies the unique-selection assertion.
It adds 24 assertions without manufacturing addon ending flags.
Partial histories are sampled after selected visits rather than every visit; do not describe that as exhaustive interruption-position coverage.

`ParentEndingRulesTests` is separately registered when typed metadata exists.
It checks metadata round trips, cue policies, loss arbitration and malformed contracts.
It does not substitute for either played route-history coverage or the native helper's separate integration review.

## Validation boundary

I did not duplicate the root's running full Rules test process or mutate shared builds.
Root reported 25,958,573 passing full Rules assertions after restoring all 24 endings to the generic walker.
Root then reported 123,261 passing focused continuation assertions after adding the 24 ending-witness checks, up from 123,237.
Those execution results are attributed to root; I independently inspected the changes rather than duplicating the runs.
The earlier 25,958,477 result preceded the ending-registration correction and is superseded for that claim.
The source comparison and the concrete coverage correction above are independently verified here.
This report does not approve native Unity execution, art, deployment, every parent ending suppression mapping or the whole romance release.
