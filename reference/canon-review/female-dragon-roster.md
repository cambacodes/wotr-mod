# Female dragon roster audit

The family-loss lead is Devarra, and the remains-and-scale lead is Terendelev.
These are distinct stories.
The lost family is branch-dependent, with explicit confirmation in DLC1 dialogue.
No missing side conversation was reconstructed.

| Candidate | Sex, adulthood, and form | Native campaign evidence | Integration decision |
|---|---|---|---|
| Terendelev | Adult female silver dragon, with a human form and a long-established guardianship; Hal's childhood memories describe her distant past. | Main campaign death, scale and claw memories, Iz Ravener, Aeon survival, Gold Dragon recovery of awareness, and Lich enslavement are distinct states. | Extend the existing RanRomance romance; do not create another scale/remains arc. |
| Devarra | Female red dragon and mother of a clutch; adult portrayal is explicit through motherhood and established dragon career, not an invented numerical age. | Main campaign Greybor hunt and Ivory Sanctum eggs; DLC1 explicitly explains the hostage clutch and either loss or mercy. | New experimental Trickster route can use supported family history, but must author actual rescue and restoration separately from the DLC premise. |
| Melazmera | Female umbral dragon, Huge, 33 dragon class levels, boss CR26; mature-dragon portrayal is inferred from the encounter, with no numerical age given. | Main campaign optional Colyphyr boss and Fulsome Queen quest; native reports establish mockery, predation, soul-eating boasts, and illusion-disguised treasure. | Valid experimental addition, with substantial new conversation and peaceful-contact authorship required. |
| Nidalynn | Female silver dragon and adult teacher among Hal's peers; unit gender and mature mentor role agree. | Main campaign Gold Dragon trials and reward, with kindness, sincerity, and enjoyment of cheese in her own dialogue. | Another valid addition with more direct conversational evidence than Melazmera; Trickster introduction is newly authored. |

## Exact key evidence

Devarra says, "my clutch was pillaged, and my offspring died before their birth."
Source: World/Dialogs/DLC1_Megaepic/StorytellersTower/Chaleb/Cue_0006.jbp, d368680393304b5ba324dd5a517140ed.
The alternative says, "I was forced to fight you by the demons who had captured my clutch."
Source: World/Dialogs/DLC1_Megaepic/StorytellersTower/Chaleb/Cue_27.jbp, 8c53478782244b90a37f727f7b814318.
That second cue also thanks the Commander for mercy toward her brood.
Its condition is DragonEggsReleased Playing, 4ba6fd446353825459f469fe5973fd87, OR kingdom project 4aa538f07bd542f7a013b90464577d67 done.
Cue_0006 has no condition of its own and is the fallback, so it must not become an unconditional claim that every player killed her children.
The DLC character's presence is not proof that a living main-campaign Devarra has already been restored.

The Fulsome Queen reports Melazmera's boast about eating "even dead souls."
Source: World/Dialogs/c4/FinalDungeon_Colyphyr/FulsomeQueen/Cue_0102.jbp, d9cf5c5e87a72e943afa9737b02bfbe7.
The same source describes her giggling, while Cue_0024, e0dab46a6a2842c4ba0502e82f2981cf, says she mocked, chased, and tried to eat the Queen.
This is an enemy's report, not neutral narration of her private motives.
Cue_0078, ee90b60ecefa31f44aeb8a58c1e5ebab, describes real treasure disguised as rocks and rocks disguised as treasure.
Her exact unit is Units/Monsters/UmbralDragon/ColyphyrDungeon/Melazmera.jbp, 85c7a3fd80f93db43a3e588ba5f5f9bc, with Gender Female.
No direct dialogue assigned to that unit speaker was found, and no family-loss story was found for her.
A convincing route can develop these predatory, mocking, and deceptive traits; it should label newly invented biography as new authorship.

Nidalynn says, "As a silver dragon, I believe kindness and sincerity are of the utmost importance."
Source: World/Dialogs/c5/Mythic_Dragon/DragonsKenabres/Cue_0015.jbp, 115f3b59eade2374196abbc646bb8a54.
Her unit is Units/NPC/Unique/Act_5_HeraldOfTheIvoryLabyrinth/MythicDragon_Ch5/NidalynnDragon.jbp, c966ef14763c5e649beab50af6e22972, with Gender Female.
The same scene offers cheese and asks the Commander to savor it slowly.
She also confirms in Cue_0058, 7e1a31d409836274b93e59796d60c19e, that dragons disguised themselves as druids to receive the rescued Ivory Sanctum eggs.
Do not make her the pregnant human petitioner simply because her trial concerned that woman's request.

## State distinctions for implementation

Main-campaign Devarra death branches use RedDragonDead, 581521b398fb9dd4eb52bbfffb3b5c43, and RedDragonKilledInIvorySanctum, 056ba61e04cca104a9c95ac2d4658c67.
Native dragon-hunt consumers test both as Playing when determining whether attacks should continue.
World/Etudes/Common/Devarra_dead.jbp, d713e8b772484376a7da810c37ab7922, is consumed by the DLC Battle_Agains_Law and Caleb encounter; do not use it alone as the main-campaign death predicate.
Melazmera's native death etude is ColyphyrMelazmeraDead, fee0f0cf006c96f4f90f895ba8d73d97, tested as Playing by the Queen's kill-report choices and the lair mechanics.
Absence of a death marker alone does not provide a peaceful actor or establish that the character has been met.

TerendelevScaleItem is 816f244523b5455a85ae06db452d4330.
TerendelevClawCollected is 7ef78c8e02070af428efe1dd851ec8a1, started by the collectible claw action in GibberingSwarmCave.
A collected claw is a historical progress marker, not proof of a living Terendelev or an intact soul.
Storyteller Cue_0766, 4e1d9c5a6266ce8479c10e5359af0505, calls the memory a spiritual resurrection; it recounts her earlier recovery from corruption, not a present bodily resurrection.
Native Aeon TerendelevPresent Cue_0006, a0d4e597a9e31634d9b50d422fd98b8c, explicitly says altered history saved her life.
Native Gold Dragon TerendelevUndeadCompanion Cue_0006, 2c706e4948f23b54a9b87f42cc3cd5f6, still describes torment and unlife after her awareness returns.
Native Lich DeadTerendelev_lich Cue_0001, 21ffae2a289a3a048b1c3cd6869cf8e2, offers to bind and enslave her soul before judgment; this is not voluntary restoration or romance consent.
Relevant separate state blueprints include TerendelevWasNotKilled 6b98ec3e704599149b99fe70b5f793ab, TerendelevSaved_Aeon bc62db9c34c4db149839dd21d1ab74f1, TerendelevAlive_Dragon 6c31fca14a4c4fb499f5eccee5eda148, TerendelevInZiggurat 85a90025d84c2b34ab7abfcfebf7a363, and TerendelevUndeadInCapital a4fbd26974c84e04da3b050574ad9d19.
Their names alone must not replace inspection of the chosen native branch and its actor changes.

## Existing mod ownership

Installed Mods/RanRomance/readme.txt documents a Terendelev romance exceeding sixteen thousand words, beginning with the Storyteller and modified scale and continuing through Ravener-killed or Ravener-ignored branches.
It explicitly says the story blocks the Gold Dragon unique Ravener-remains interaction.
Its changelog 0.1.7 and 0.1.11 also documents fixes to remains-versus-scale ordering and Ravener death checks.
Any Trickster extension must preserve these existing scenes and predicates rather than compete for the same remains interaction.
The same installed readme documents Targona's wing-healing, small/large mythic-power branches, and Aeon/Trickster reactivity.
The earlier candidate table has been corrected to classify Targona as an existing-route extension.
No romance for Devarra, Melazmera, or Nidalynn is documented in the inspected installed readme; that is not a substitute for a full assembly integration audit before implementation.
Hal/Halaseliax is male and remains a nonromantic introducer.
Tyvanadis is also male in the inspected unit blueprint and is not added to the female roster.
Ember and Aivu remain full friendship routes only.
