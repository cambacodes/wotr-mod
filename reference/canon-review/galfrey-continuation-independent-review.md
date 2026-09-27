# Galfrey continuation research: independent review

## Verdict

Revision required before adopting this report as the source baseline or full production plan.
The adult romance, personal-trust conflict, native courtship, and ending material are supported.
The report nevertheless misattributes Daeran's kinship to Konomi and Aeon's history change to Trickster.
Those errors directly affect its candidate exclusions and proposed path justification.
All fourteen GUID and individual-member hashes in its evidence table are correct; correct fingerprints do not validate the interpretations elsewhere in the document.

Reviewed input SHA256: `7A00602230607E80D6A2D0C801D095ACD1A4B883EBE85FD9090AF04B97B03190`.
Review date: 2026-09-27.
I independently read the full report and inspected installed blueprint JSON, resolved English text, native incoming dialogue conditions, speaker identities, selected etude components, and the proposed word allocations.
Only this review file was written.
This is research/design review, not manuscript, artwork, runtime, or release approval.

## Reproduced factual corrections

### R1. Konomi is not the speaker calling Galfrey her cousin

`reference/expansion/konomi.txt` contains whole council exchanges with several speakers.
Its filename does not establish that Konomi speaks every line.
The two relevant native records are:

| Record | GUID | Native speaker |
| --- | --- | --- |
| `World/Crusade/RankUps/Diplomacy/Diplomacy_2/Cue_0020.jbp` | `0340e157c73e95544aa614a7eacf46cb` | `096fc4a96d675bb45a0396bcaa7aa993` |
| `World/Crusade/RankUps/Diplomacy/Diplomacy_4/Cue_0011.jbp` | `5e36a292028848f4eb0825fc2c00fd08` | `096fc4a96d675bb45a0396bcaa7aa993` |

That speaker resolves to `Units/Companions/Daeran/Daeran_Companion.jbp`.
These are Daeran's parade and Royal Council remarks.
Konomi's own introduction, `9ee914535aa169240b3a840465a43d55`, establishes her official diplomatic appointment, not kinship.

Remove the claimed Konomi/Galfrey family relationship and the resulting canon-based romantic exclusion.
The author may still choose a solo Galfrey continuation or decide the pairing lacks chemistry.
There is no evidence here establishing mutual attraction either, so removing the false prohibition is not approval of a triad.

### R2. The cited history alteration is Aeon, not Trickster

The actual `GalfreyArrives/Answer_0041.jbp` has GUID `b7a49048c0c93d941b05742e95314e18` and the line about changing the past so Drezen never fell.
The report instead attaches GUID `05ed0f8f89def5d4f94f7f9c93b39126`, which belongs to `Answer_0043` and says the Commander wanted to reminisce about their triumph.

The incoming `Answer_0038` `70912c5968f3eab4187c04dd5f43ed83` requires these states playing:

- `998b505008f960a4b92e679fbd588098`, `MythicAeon_DrezenHistoryChanged`.
- `3d4684e1206164c4281b5540ff78229e`, `GalfreyWithUs`.
- It also requires `ReinforcedByAeon` `6b2512a4d14320849abb05cee821d0d3` not playing.

The alternative incoming `Answer_0050` requires the same changed-history and accompanying-Queen states, with `ReinforcedByAeon` playing instead.
Both lead through the shared answer list containing Answer_0041.
The alarming-power reply `8b7e9e5e7ab68e148a0416e893b1b16e` is genuine, but its authored context is Aeon's altered history.

Correct the GUID and path attribution.
This branch can inform a comparison of Galfrey's reaction to extraordinary power; it cannot prove that Trickster performed this native history change.
The proposed Trickster forgery plot remains authored alternate continuity and needs its own real council and quest anchors.

### R3. The council invitation runs in the opposite direction

`GalfreyArrives/Answer_0001` `e1ea7f81e271449ea88a6b7440e3d9df` is the Commander asking Galfrey to attend the Commander's military and political council meetings.
The report describes it as inviting the Commander to her meetings.
Correct the direction before using it to establish whose council, authority, and attendance are already native.
A diplomatic council and the mythic Trickster Council also need separate actor and scheduling proofs.

### R4. Distinguish achievement and lifecycle states

The Active romance starts achievement etude `b9c6e3e0d6ac42ef8b9a2bad0c36420d`, `48_Spark`.
The Finished romance starts `c95ca64f070f42748f097cc3ff21d505`, `49_Flame`.
They do not both award A Spark, despite a copied comment in the Finished component.

Also distinguish the named Finished etude from completion of the Active etude.
The Active record's native comment explicitly treats its completion as failure.
The ordinary romantic epilogue checks the Finished etude playing, not merely Active completed.
A future adapter must preserve those distinct lifecycle meanings.

### R5. Fix the inline Threshold GUID

The table correctly gives `781c38023c5205f4f9d5f61c33c2a3d7` for Threshold Cue_0022.
The later prose inserts an extra `b`, producing `781c38023c5205f4fb9d5f61c33c2a3d7`.
Use the verified table value consistently.

## Adult identity, dating, and age portrayal

Adult eligibility is unambiguous in the inspected native material.
`GalfreyAfterSex/Cue_0016`, `2b9f7b5cf66b73e4eb6e9c8d4cf1d869`, explicitly describes a century-long life prolonged with sun orchid elixirs.
`Galfrey_Incognito/Cue_0010`, `85cfdab678616fd4f9666352f75a45cf`, says the Church paid for that prolongation and she accepted its responsibility.
Her physical presentation therefore should not be inferred from chronological age alone.

The report's instruction not to make her "magically rejuvenated" needs clarification.
Avoid inventing an addon rejuvenation that erases her history, but preserve the native elixir-maintained appearance.
Do not force geriatric features onto her because of her chronological age, or treat her private self-description as a crone as an objective model specification.

The dating record also includes a past attachment.
`GalfreyDrink/Cue_0033`, `b1e7719164da9064d9a59b789bd15697`, describes falling in love after coming of age with one of her father's knights, a few years older than her.
That supports adult past courtship, not a current spouse and not an assumption that sex never occurred.
The report appropriately limits its current-partner claim to the inspected sources, but should include this actual past-romance disclosure in the characterization baseline.
Native romantic epilogue Cue_0262 uses both male and female Commander pronouns; dating eligibility must not silently become male-only.
This review does not claim an exhaustive race, gender, or mythic entry matrix from that wording alone.

## Native relationship and path conclusions

The personal-trust refusal at Chapter 5 Cue_0041 is verified.
The report reasonably distinguishes trust in the Commander as Queen from personal romantic trust.
That cue itself has empty conditions, however, so its incoming branch must be traced before naming an exact eligibility rule.
The neighboring Cue_0044 has a genuine OR condition for the four cited path etudes.
One conditioned response is not the entire native romance restriction matrix.

The ordinary and ascension ending conditions were independently inspected.
Cue_0249 requires the Finished romance playing, excludes both companion ascension cues, and has an additional negative etude condition.
Cue_0262 requires the Finished romance playing and either of those ascension cues seen.
The report correctly refrains from equating companions ascending with simultaneous romantic partners.
Its broader sentence that the native ending "does not impose simple exclusivity" should stay limited to these observed cue conditions, not imply a complete audit of native jealousy or breakup consumers.

`Galfrey_Final` `e9205b9f9e8ecd04c92852d72d09ca86` excludes the GalfreyDead etude playing.
That supports the report's refusal to treat a dead or missing actor as an ordinary live reunion.
It does not prove universal actor availability whenever that one negative check passes.
No restoration or native romance reacquisition was executed in this review.

## Production-plan gaps

### R6. Reconcile the content arithmetic and scope

The eleven listed allocations total 24,500 to 30,000 words, not 24,000 to 27,000.
The introduction promises 14 to 18 major visits but lists eleven blocks without explaining how they divide into those visits.
Neither error means the route is under the 21,000 planning floor, but both make the deliverable ambiguous.
State a consistent total, identify actual visits, and maintain a ledger of newly authored branches versus native content.

The proposed 21,000 floor is compatible with the per-character volume policy if met by delivered new material.
The project's current measurement tool counts choice text and deduplicates normalized whole segments only.
It cannot certify the report's stricter spoken/narrated-only, meaningful, semantically distinct measure without additional accounting.
Do not count the same ending paragraph in multiple branches or credit the native date, confession, and epilogue toward the new floor.
These are budgets, not measured manuscript quality or length.

### R7. Make acquisition and timeline attainable

The forged instrument, constitutional crisis, public review, and authority limits are proposed plot developments.
None is established as a native legal mechanism by the cited council invitation.
Specify which changes remain authored narrative outcomes and which have implemented campaign effects.
Do not narrate a native decree, jurisdiction transfer, or council resolution as executed solely because a dialogue flag was written.

The current plan gives a promising voluntary courtship premise but no verified native interaction window for the new Chapter 3 audience.
It also needs a Chapter 5 entry for saves that missed that audience, with separate handling for native rejection and for never having courted her.
Saving Galfrey at Iz is a credible survival lane, not itself a romance repair and not a completed death-recovery design.
The universal Trickster requirement remains unfinished until its supported histories, concrete quest anchors, checks, costs, and earned invitation are specified.

The outline puts return-to-Drezen, training, and intimacy before its Iz preparation block.
Pin each to an actual living Galfrey location and campaign phase, or explicitly reorder them around the verified reunion.
A possible messenger during the Abyss absence is not proof that such a native delivery mechanism exists.
The report correctly avoids requiring playable postgame visits.

### R8. Keep consent and characterization specific

The refusal, voluntary reconsideration, and no-global-romance-lock requirements are sound.
Checks should buy evidence or access, as proposed, rather than roll away her objection.
No-jealousy compatibility does not establish attraction or approval of every concurrent partner.
The optional women-only premise should remain optional, and no canon evidence currently supplied proves mutual attraction between Galfrey and either Tirabade wife or Konomi.

The condition that only exposing the forgery builds romance needs reconciliation with the later risky-bluff and negotiated-confession success routes.
Galfrey can demand accountability without every successful Commander becoming morally agreeable or surrendering all ambition.
Show what an effective selfish, threatening, or deceptive choice costs and why she would accept or reject it.
Likewise, a lengthy constitutional negotiation should not displace her martial confidence, faith, age anxiety, awkward humor, anger, and adult desire.
These are design risks; no unwritten scene receives a literary score.

## Verification record

The installed archive SHA256 independently matches `BE61C9B723EF06558DA8D7CFC7F0C7EA869F60BA9952EBBBBD116CF681863EA5`.
Installed English localization independently matches `3289C3EBAB206BA6312D4C2D512C0B5623E52D7E2B86596074B81D355725AA75`.
The roster hash matches `E27C8E458757E5637082705FF5654D41FF5B9944D5866EE1A34EDDFDF49FADF8`.
All fourteen listed archive members passed both AssetId and raw-member SHA256 comparison.
The shared export and etude-index pins match the current independently checked files from the preceding source review.

Additional corrective evidence pins:

| Archive member | SHA256 |
| --- | --- |
| Diplomacy_2/Cue_0020 | `77B850014DFE7C5A522E768A0099DD1C511E26F6A95FB98F4291C69D71315DB6` |
| GalfreyArrives/Answer_0038 | `3F6CA97CDAFE39CD53EB448FBDA25140FD6D34601D0482D75D996FF46FC0C145` |
| GalfreyArrives/Answer_0041 | `5A996A7E9BF9E716EA372A9B32CBC25311F39DE5BAEF22446D0AC7819E5572C2` |
| GalfreyAfterSex/Cue_0016 | `510E1C4C625CFFA9947CA03D66FDD2F527EBD1EAF26866573897F9FE809AA3B0` |

Read-only Python probes and repository searches supplied these checks.
An initial extraction assumed every `Text` property was an object and failed on a string property; the corrected type-checked probe completed.
No failed probe is counted as evidence of game behavior.
No Unity scene, ToyBox combination, physical interaction, resurrection, native achievement, or complete romance graph was executed.
Correct R1 through R5 before using this report as a canon reference, and resolve R6 through R8 before calling it an attainable full-route plan.
