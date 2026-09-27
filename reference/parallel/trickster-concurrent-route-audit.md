# Trickster concurrent adult route audit

Reviewed on 2026-09-26.
Verdict: the current implementation does not establish the hard requirement that every eligible adult partner is attainably romanceable in one Trickster campaign.
The addon largely avoids unrelated romance exclusivity, but it still has missing acquisitions, native access restrictions and incomplete recovery paths.
Free Love and No Jealousy cannot be treated as evidence that those separate problems are solved.

## Authoritative snapshot and scope

The committed 585-scene `development/Story.json` hashes to `780BDC23146431CECD7F1ED9594B5F129C5E149DB535CC40F2BD128A2126647A`.
The actual rules source `src/Story.cs` hashes to `4442C5D543C46D8B3A6744448ED03B92E7A7BB463BDECF09749CA9B5DCB1E889`.
Unexported prose, morale and native-history revisions are excluded from this audit's findings.
I inspected route metadata, every authored choice's writes, cross-route reads, runtime state observation and the available parent Aranka evidence.
I also compiled a temporary probe against the actual Story.cs and its two required support sources.
The probe and isolated build outputs are in `C:/Users/Z/AppData/Local/Temp/trickster-concurrent-audit-d409g9k5`.
No shared output or source file was changed.

The export has 16 relationship containers, including Ember and Aivu friendship content.
Its adult content represents 14 distinct women: Anevia, Irabeth, Seelah, Konomi, Jerribeth, Kiana, Soana, Arsinoe, Targona, Gesmerha, Vellexia, Aranka, Minagho and Chivarro.
The shared Tirabade container does not count Anevia and Irabeth again, while the Minagho/Chivarro container covers two women.
Representation in this inventory is not an approval or a completed standalone romance.
The 37-character roster includes planned, experimental and friendship entries; it is not 37 implemented adult romances.
Existing native romances and parent-only routes require their own integration and joint-playthrough evidence.
Ember and Aivu are excluded from adult completion priorities, as requested.

## Flag isolation findings

Rules.Available has no gender, romance-count or generic one-partner limit.
It applies each scene's conditions, its relationship's own closure/unavailability conditions, contact, chapter, area and delay.
It does not consult ToyBox toggle values to override those authored conditions.
The runtime retains select-time guards even when ToyBox displays otherwise unavailable answers.
That prevents a hidden answer display setting from being mistaken for a supported acquisition.

I scanned every choice Set against all native aliases in Etudes, CompletedEtudes, CompletedQuests, SeenCues, SelectedAnswers and StartedDialogs.
There are no collisions in this export: authored choices do not directly write those native observations.
Outside the Anevia/Irabeth/shared relationship family, I found no choice that writes another implemented relationship's committed, closed or started flag.
The shared `arsinoe.introduced` flag has producers in Seelah, Konomi and Kiana scenes; it records an introduction, not commitment or closure.
Jerribeth's optional `vellexia.introduced` callback is read in Vellexia's opening choices and is not a mutually exclusive romance condition.

The generic `closed`, `committed`, `trying`, `a_affair` and `i_affair` reads remain inside the Anevia/Irabeth/shared family.
The generic `loss` scene gate is confined to the shared route.
`inhuman` is used across multiple routes as a path/world-state restriction; it is not produced by committing to an unrelated partner.
This is not evidence of an accidental global romance closure.

## Actual Rules probe and its limits

For each scene, the isolated C# probe supplied its positive requirements, a matching chapter and area, required contacts, and enough elapsed time.
It then added every other relationship container's committed flag and compared actual Rules.Available.
This deliberately synthetic check tests interference, not the attainability of the supplied facts or a chronological playthrough.
All 585 scenes had a baseline synthetic witness.
Thirty became unavailable after foreign commitments were added, all in the independent Anevia/Irabeth containers because the shared `committed` flag suppresses their alternative acquisition or individual ending presentation.
No unrelated adult relationship caused another container's scene to fail this comparison.
Adding all other closure flags likewise affected only the intentionally linked Anevia/Irabeth/shared family.

Those 30 results are not 30 jealousy bugs.
An existing group commitment should not replay an alternative first courtship, and individual epilogues can be replaced by the shared ending.
The required follow-up is to prove that both individual affections and earned shared content coexist with all unrelated commitments, with one consistent set of endings.
Flags alone cannot establish that proof.
The current tests that seed Seelah and Arueshalae commitments only establish preservation of those supplied flags.
They do not acquire every partner or prove native romance counters, exclusive conversations and parent quest progress remain compatible.

## Concrete access gaps and conflict cases

| Case | Actual current restriction | Required next work |
| --- | --- | --- |
| Trickster requests Aranka continuation | `aranka.the_wrong_refrain` requires current parent romance, successful parent quest completion, a reviewed finale, the live island Aranka and AzataIsland area `31bab5549f7ea384186159a238360c8d`. | Implement and review a real Trickster acquisition and contact opportunity; do not seed the romance etude, teleport an arbitrary actor or pretend the island is universally available. |
| Trickster reaches Chapter 5 without starting Soana | `soana.threshold` is Chapter 3 only; the later campaign depends on earned earlier visits. | Add a credible late introduction through her actual forest and quest history, with a separate continuation that does not invent the missed visits. |
| Trickster reaches Chapter 5 without starting Gesmerha | `gesmerha.unbought_work` and the initial craft visits are Chapter 3 only. | Supply an earned later acquisition if missed-entry access is part of the required Trickster promise; ordinary early scheduling alone does not satisfy recovery coverage. |
| Commander accepts Vellexia's native arena invitation before addon gallery visits | `vellexia.unfinished_likeness` forbids `vellexia.arena_invited` and `vellexia.native_finished`, and is Chapter 4 only. | A distinct missed-gallery intervention or another credible entrance is needed; adding other lovers does not remove this gate. |
| Soana dies, Camellia kills her, or the forest outcome kills her | Her relationship is unavailable under `soana.dead`, `soana.killed_by_camellia` or `soana.forest_dead`. | Provide actual restoration/contact design before claiming those histories recoverable; no Soana revival is registered. |
| Jerribeth becomes unavailable or Vellexia dies/fights | Their native unavailability/death/fight guards persist. | Existing Jerribeth living-contact correspondence is not dead/hostile recovery; Vellexia also needs an actual alternate opportunity after adverse history. |
| A Minagho/Chivarro parent outcome kills either woman or lacks the completed parent story | `minachiv.two_answers` requires parent completion, the actual Book 3 ending and Chivarro searching; both deaths forbid the continuation. | Prove a compatible earned parent history in the joint campaign and implement any promised recovery separately. |
| Targona parent acquisition is absent | Her six scenes require freedom, the parent treatment quest and its finale; a Trickster parent-state alternative is accepted. | Verify the actual parent Trickster acquisition and its joint quest schedule instead of treating six continuation scenes as a new complete route. |

The Aranka access finding is supported by `reference/canon-review/aranka-extension-evidence.md` and its retained class-specific decompilations.
The reviewed native mechanics chain leads through AzataIsland beneath PlayerIsAzata, whose activation uses actual mythic-class conditions.
The current continuation deliberately preserves that parent entry restriction.
The parent romance etude also increments RanRomCount on play and decrements it on completion.
The addon does not change that counter.
The native island requirement is therefore a separate problem from additive addon flags or a ToyBox jealousy toggle.

Only Seelah and Konomi have entries in the export's Revivals map.
Those are limited retained-actor mechanisms, not proof that every lost or killed candidate can be restored.
Konomi has authored Trickster missed-introduction, dismissed-contact and retained-return work, while Jerribeth has a living-contact intervention.
Their presence should be reported as partial implemented examples, not extrapolated to the entire roster.

The Soana/Camellia case is an adverse-history branch, not a demonstrated unavoidable conflict between the two romances.
Likewise, optional cruel choices that end one relationship are not automatically defects in concurrent eligibility.
The target is a credible attainable joint path, with explicit recovery where promised, rather than every mutually exclusive outcome occurring at once.
An actual dual-path claim such as remaining both Azata and Trickster must not be inferred from placing both flags in a synthetic snapshot.

## Required verification before claiming the hard constraint

1. Build one chronological Trickster witness covering Chapters 1 through 5 and the actual native/parent acquisitions.
Track quest decisions, actor access, deaths, scheduled visits and the parent romance states that produce each addon prerequisite.
Do not inject future quest-complete flags merely to make a scene pass.

2. For each implemented adult container, rerun its chosen positive path with all already-earned unrelated commitments present.
Require unchanged unrelated state, retained reachable next visits, and compatible final outcomes.
Include the Anevia/Irabeth negotiated and shared transitions as a linked family rather than counting duplicate acquisitions as additional partners.

3. Add targeted failed-entry cases for the concrete rows above, preserving native history until an authored intervention actually changes an opportunity.
Test the missed Chapter 3 and missed Chapter 4 windows separately from ordinary early play.
Keep informed refusal distinct from absence or bad timing.

4. Verify actual ToyBox Free Love and No Jealousy behavior with native and RanRomance relationships in game.
Observe parent counters, jealous/exclusive dialogues, invitation delivery, save/reload and endings with the intended toggle configuration.
No live ToyBox session was run for this audit.

5. Maintain a per-character evidence matrix for the remaining roster.
Require acquisition, playable continuation, art, length, independent literary review, concurrent-state tests and live verification separately.
No row should become ready solely because a synthetic commitment flag survives another route's test.

The next adult engineering priority is the missing attainable acquisitions and contact/recovery paths, particularly Aranka's Trickster entry and the missed-entry windows.
The present flag isolation is useful groundwork, but the all-partner concurrent campaign remains unproven and incomplete.
