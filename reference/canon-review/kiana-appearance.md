# Kiana appearance adjudication

Use the blue-skinned, white-crystalline oread appearance as the installed game's supported Kiana likeness.
The evidence combines her explicit unit race, saved prefab appearance options, portrait reference, and the same unit's use before and after the wedding disaster.
The alternate dark-haired human-looking portrait exists in the game bundle, but its filename alone does not establish that it is the current ordinary Kiana.
Calling it a legacy asset is a plausible inference, not verified development history.

## Unit and portrait chain

Units/NPC/Unique/Act_3_DemonsHerecy/Seelah_Q2/Kyana.jbp is BlueprintUnit 180b0eaa5dce387458d2ebf0ee943985.
It specifies Gender Female, race 4d4555326b9b7144f93be1ea61337cd7, prefab ad4aac3138a248646a42424c9e3ca79a, and portrait cc92e7a3b8944f7da3bcceec9f7ce0ec.
Races/OreadRace.jbp resolves that race GUID to RaceId Oread.
Units/PortraitsGenerated/ad4aac3138a248646a42424c9e3ca79a_BCT_Kyana.jbp resolves the unit's portrait GUID to raster d0532fe50faad104daa3d975fa70edc7 in all three image slots.
I visually inspected the extracted raster and confirmed blue skin, a white crystalline head silhouette, greenish eyes, and dark clothing with bright metallic ornament.
The portrait is an initiative-sized image, so a painted expansion should preserve its broad identity rather than pretend it proves fine facial details at full resolution.

The prefab extraction reference/art-review/kiana-native/unit-prefab.json saves female head 28680b13930e71543aae24947f6f8abf and hair 7f632035eba6e0d4a99b4167e68311cb.
Both appear in OreadRace's FemaleOptions, independently supporting the portrait's crystalline appearance.
The prefab's GameObject name Head_Human_0 is insufficient to override its saved equipment and explicit unit race.
Shared internal model names are not a character biography.

The alternative Units/Portraits/InitiativeBlueprintPortraits/Characters/Common/BCT_Kyana.jbp has GUID dd6263efb47946d29232dcd7c37ba213 and uses raster b01a38ed9eb2e3c44bd548a975bb59c0.
That is the brown-haired, human-looking image I also inspected.
It is not the portrait reference on the inspected native Kyana unit.
Do not average the two designs or treat the human-looking image as proof of an ordinary pre-transformation body.

## Quest chronology and physical description

World/Dialogs/Companions/CompanionQuests/Seelah/Q2_TillDeathDoUsPart/KyanaWelcome/Cue_0001.jbp, 0bb8e464eb1a6aa458e8d5dba62f5413, introduces her before the wedding disaster.
It describes a slender young woman in a flowing dress and eyes that are striking blue-green.
Its Speaker points to unit 180b0eaa5dce387458d2ebf0ee943985, with no speaker portrait override and no OnShow action.
The same unit is Speaker for Q3_WeightOfMySword/ElandKianaAftermath/Cue_0006.jbp, a819e8c85ef23324bb0d8117bb9d7df3, and KianaAloneAftermath/Cue_0001.jbp, aebbc1845e827dd4da4e28014e7b4162.
Those inspected aftermath cues likewise have no speaker portrait override or OnShow transformation action.
This establishes that the currently referenced oread unit and portrait are not specific to a post-disaster conversation.
I found no physical-description evidence in the inspected Seelah dialogue that explains blue skin and a crystalline head as a consequence of stolen souls.

KyanaWelcome/Cue_0004.jbp, 466c4a8957da5f14fa958d1718b4a552, explicitly explains the vampire theme as beautiful dresses, candles, and red wine pretending to be blood.
Cue_0014.jbp, 2b07731a9219e87478d488b7947d86b3, says none of them actually wants to become a vampire.
The wedding role is costume play and is not evidence of true undeath or a racial transformation.
Preserve blue-green eyes from the explicit narrative even if the small native raster appears greener under its lighting.

## Current authored prose

Reviewed storylines/kiana.py SHA256 CD53586EDABF6603FB35979254C6832B3C6FA54884E53929F215B905D61C3836 for human-only appearance assumptions.
No description of ordinary human skin, brown hair, braids, or a soft human scalp was found.
Hands, fingers, a mouth, smiling, kissing, dresses, and a ribbon remain compatible with the inspected humanoid oread unit.
The inhuman conditions and kiana.date.changed refer to the Commander's changed body, not a claim that Kiana is human.
No prose edit is required to repair a demonstrated race contradiction in this revision.
Art prompts or metadata that currently identify her as human do require correction before likeness approval.
This focused check does not replace the earlier story review or approve unreviewed art.

Supporting native objects and dialogue are saved in kiana-appearance-sources.json and kiana-appearance-race.json.
Image hashes and extraction provenance remain in the parent-owned reference/art-review/kiana-native/provenance.json.
No production source or art asset was edited.
