# Soana later progression handoff

Author ownership: `storylines/soana_later_progression.py`, `tests/SoanaLaterProgressionTests.cs`, and this handoff only.
No existing scene, shared exporter, runtime, generated story, native blueprint, art, or other author's source was edited.

## Revision and integration

Source SHA-256: `A1191916459BF773362A0803F868B318CCBD61AC009A373DB7926480B050558A`.
Test SHA-256: `6303F65A695A76E8DF3E4F02A24EED27A4BE759B6548707E8B56632FA03B3318`.
The module exports eight `SCENES` and requires no new alias maps, relationship definition, or mutation of an existing scene.
Append these scenes to the current payload and register the focused test in the parent-owned harness.
No `integrate(payload)` overlay was necessary: the existing `soana.continuation_kept` milestone already provides the entry link.
All original scene IDs, nodes, choice indices, outcomes, and attachment answers remain unchanged.

| New scene suffix | Delay after prerequisite | Main development |
| --- | --- | --- |
| `the_thing_in_the_sack` | 24 hours | A displaced hunter brings a voice-stealing bowl from an abandoned shrine; Soana recalls protection she gave and a disputed inherited obligation. |
| `the_dry_offering` | 24 hours | Examine the altered shrine through Lore Religion DC 24 or a slower survey; failed reading costs a day of investigation and broken charcoal, not route access. |
| `the_inherited_debt` | 24 hours | Hear the hunter's refusal and Soana's uncomfortable claim; choose Soana's voluntarily offered voice or the destruction of her nursery as the containment cost. |
| `a_voice_in_the_dark` | 48 hours | Play the working with named responsibilities; respect Soana's continuing signal, interrupt through the costly escape, or carry out the agreed ridge method. |
| `what_followed_home` | 48 hours | Distinct intrusive-voice, overridden-choice, and agreed-loss consequences; a new limited agreement with the hunter; native Orso outcome remains unresolved. |
| `a_promise_still_spoken` | 48 hours | Soana names a present choice while Corven's status remains unknown; existing courtship may continue or become friendship, waiting receives an answer, established friendship stays friendship. |
| `the_unwelcome_path` | 48 hours | Negotiate real competing wilderness interests: protect the deer hollow at travelers' carrying cost or allow limited flood-time passage with disturbance risk. |
| `after_the_last_visitor` | 48 hours | Earned private evening with chosen night, kiss-only, quiet physical pace, or friendship; branch-specific consequences of the path agreement remain present. |

Every ID has prefix `soana.`.
All eight scenes require living native Chapter 3 contact, the postquest stage, `soana.continuation_kept`, and their predecessor milestone.
The inherited-debt scene is required by its completed scene ID because its terminal choices record which working was chosen.
The opening prerequisite appears twice in the first scene's Requires array because it is both the common continuation gate and the immediate predecessor; it has identical set-membership semantics and does not alter timing.

## Canon and authored invention

Read before authoring: both existing Soana modules, `reference/canon-review/soana-route-evidence.md`, the contact and continuation integration reviews, and the Soana roster entry.
The installed `blueprints.zip` records were independently reopened for the Soana unit, repeatable postquest dialog and answer list, and postquest cues concerning mages, Corven, and the bear outcome.
Native unit `64805abb52739e44280a758f850b300c` is female, True Neutral, and references dwarf race `c4faf439f0e70bd40b5e36ee80d06be7`.
Its native mechanical class record is not evidence of a player-class witch spell list; no new spell feature or castable spell is granted here.
The native dialogue establishes her dangerous spirit binding, territorial protection, prejudice toward mages, marriage memory, and differentiated bear outcomes.
The new rite draws on those themes but is authored alternate fiction, not a recovered native ritual or a claim about a published Pathfinder spell.

Native attachment remains repeatable answer list `2b1776f3e398685479ff6b16290b4cc2` in dialog `1a2202cb676601344942aed3edab7498`.
Direct inspection confirmed the list has empty conditions and ShowOnce false.
The source retains exact actor contact, Chapter 3, native `soana.after_quest`, and OldDefender/BearDead alternatives.
As in the existing modules, no additional area GUID is imposed; actual local contact and native dialogue attachment remain authoritative.
Dead-bear dialogue takes precedence when both native outcome flags exist.
Soana death, Camellia's killing, forest destruction, closure, and the existing `inhuman` entry exclusion are preserved.

Meret, Varn, their family history, the water shrine, old hunter agreement, altered carving, hostile residue, nursery, temporary ritual signs, and passage negotiation are authored additions.
The site, incidental people, water, tools, seed, blanket, and bowl are narrative props and encounters within dialogue.
They are not newly spawned units, inventory rewards, world-map objects, actual combat encounters, engine-timed overnight rests, or stat penalties.
The low-risk investigation and dangerous working are playable dialogue decisions, not newly implemented tactical combat or cutscenes.
Soana's night cost is several nights of intrusive imitated voices and a specific painful memory; her nursery is the alternate local cost.
Interrupting her chosen working changes practical trust: she says she would choose another person to close a future bowl, while remaining free to want the Commander's company.
No reward requires the player to praise her coercion or surrender the ability to stop their own participation.

The separate surfaces in the rite are now explicit: a copied old sign on the prepared clay lid, the lid-to-bowl seam sealed during the working, and the altered cut on the shrine stone filled afterwards.
The same position-marking and rehearsal occur on both working branches.
Those were two concrete continuity repairs requested by the independent reader; they changed prose only, with no IDs, choices, gates, or outcomes changed.
The final pass also replaces an unsupported stone-struggle callback with Varn's shared recollection of the agreed restrictions, removes narrator explanations of choices already shown, and gives Soana's Corven decision more personal language.
Those revisions likewise change prose only.

Soana's uncertainty about Corven continues the already-authored continuation rather than inventing a verified native death or divorce.
She makes a present decision about her own conduct and explicitly does not claim his consent, an ended past, or a convenient new fact.
No living Corven, message delivery, family reunion, or genealogical discovery is delivered.
The nursery and shrine resolution never frees a living Orso, revives a dead Orso, clears native forest destruction, or produces a new guardian.
She retains dangerous protective priorities and unresolved prejudice; this is not a universal redemption ending.

## Relationship state and compatibility

New intent flags `soana.later_courting` and `soana.later_friends` describe the current decision without rewriting historical courtship/waiting/friendship flags.
A previously waiting player can now choose courtship or friendship.
An existing friendship never offers romance in this contribution.
An existing courtship can become friendship, retaining its earlier kiss or touch as history.
The final physical pace is chosen separately and may be slower or faster than a previous evening.
Only the voluntarily chosen shared night sets `soana.lovers`; no path sets `soana.committed` or marks the full campaign complete.
`soana.progression_kept` records this local arc's conclusion.
No other romance state, native quest state, pet state, or relationship is modified.
The relationship conversation permits other loves and asks for honest promises, with no exclusivity or jealousy gate, compatible in scope with ToyBox free love and no jealousy.
No specific ToyBox-version runtime test was performed by this worker.
Adult dwarf identity, age, recognizable features, and existing art assets remain intact; no new image or visual approval is supplied.

## Counts and actual selected paths

The project's tokenizer measures 8 scenes, 56 pages, 11,871 raw words, 11,855 distinct whole-segment words, and 16 exact repeated words in this contribution.
Across the original opening, continuation, and this contribution, Soana has 17 scenes, 23,712 raw words, and 23,597 distinct whole-segment words.
That aggregate includes mutually exclusive alternatives and is not the length of one campaign.
The new eight-scene completed paths contain 6,994-8,047 selected prose-plus-choice words across native histories and prior relationship intentions.
The complete earned seventeen-scene local arc contains 13,314-15,074 selected words.
The overlapping OldDefender/BearDead case matches dead-bear text and length.
Counts exclude titles, journal metadata, entry labels, unselected choices, and external game/RanRomance text.

Selected-path measurement used the same tokenizer and exact choice predicates, traversed both check outcomes, excluded abort/closure paths, and retained counts/minima/maxima while merging states only on flags no remaining scene or choice reads.
This avoids enumerating the many equivalent historical choice combinations while preserving exact selected-path bounds.
The contribution exceeds the requested approximate 9,500 distinct-word increment and takes the distinct aggregate above the 21,000-word planning floor.
That floor applies to meaningful aggregate content, not a mandatory 21,000-word selected playthrough.
The selected-path bounds are separate evidence for comparing actual player experience with RanRomance character depth, quality, and amount.
The local arc still lacks a multi-act campaign and has not received that full comparative approval.
Neither aggregate volume nor this authoring pass grants RanRomance parity, full route approval, or an author-assigned score.

## Focused checks and remaining work

Temporary harness: `C:/Users/Z/AppData/Local/Temp/soana-later-check-j1190gmc/Check.csproj`.
It compiles actual `Story.cs`, `RecoveryAttempt.cs`, `TerendelevDeliveryAttempt.cs`, and test sources against a candidate JSON assembled only in that temporary directory.
Command: `dotnet run --project <harness> -- <same-directory>/story.json`.
Result on the final released revision after all reader-requested prose repairs: `PASS 178422` following `Rules.Validate`.
No shared build or installed payload was replaced.

The focused test earns the first nine scenes from actual choices for living, dead, and overlapping bear histories, covering each prior intimacy/friendship/wait outcome.
It then traverses every new page and every new outcome, both roll results and the non-roll route, choice consequences, exact delays, replay before terminal commit, native interruption blockers, missing actor, wrong chapters, preserved original decisions, and preserved other romances.
All new authored flags commit only on terminal choices, so an interrupted new scene leaves no partial outcome to combine with a different replay.
Entry aborts leave progression untouched; completed scenes do not replay.
These are Rules-level checks, not a new Unity E2E session or an independent literary/canon verdict.

Independent review is required on this exact revision before promotion.
Actual later-act Soana contact, a fully implemented attainable Trickster recovery when she is dead or the forest destroyed, native actor/corpse/hostility reconciliation, guardian/forest outcome handling, later campaign development, completed art, and live save verification remain separate work.
No historical flag clearing, proxy actor substitution, pretend Drezen presence, or new access on other mythics is used to conceal those dependencies.
