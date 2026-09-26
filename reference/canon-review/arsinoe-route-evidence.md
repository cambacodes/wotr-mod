# Arsinoe source evidence for the opening

This is an author's evidence record, not an independent canon review or an assigned score.
Sources were read from `reference/expansion/arsinoe.txt` and the installed `D:/SteamLibrary/steamapps/common/Pathfinder Second Adventure/blueprints.zip`.
Additional Seelah wedding text was resolved against the installed `Wrath_Data/StreamingAssets/Localization/enGB.json`.
No internet biography or inference from Arsinoe's name was used.

## Identity and voice

The active Drezen unit is `Units/NPC/Unique/Act_3_DemonsHerecy/Drezen/Arsinoe.jbp`, AssetId `a609ed9b2205d034bb3bb04d2a255681`.
It specifies female gender, lawful-neutral alignment, and twelve cleric class levels.
Vendor `Cue_0016` explicitly identifies her as an aasimar and describes her resemblance to her great-great-grandmother.
It also establishes that she knows her appearance is attractive and that she values its usefulness in gathering a congregation.
Her exact age and current partner status are not established by this inspection.
Her long adult career and independent priestly work establish an adult participant without inventing an age.

Vendor `Cue_0003` establishes birth and upbringing in Absalom, extensive travel, and her preference for bringing Abadar's teaching where it is needed.
`Cue_0013` establishes a lengthy stay in the Stolen Lands and departure after the barony became prosperous.
`Cue_0015` identifies law, trade, and urban prosperity as central to her account of Abadar and describes his alliance with Iomedae.
`Cue_0014` establishes her scroll business and practical concern for whether a customer can actually use a scroll.
`Cue_0036` refuses speculative healing of a patient who is not dying, and `Cue_0037` recommends systematic observation of the Commander's condition.
Those passages support professional confidence and caution, not a miraculous romantic cure.

The opening's interest in truthful merchandise, civic construction, practical comfort, and deliberate courtship develops these traits.
It does not treat her faith as a disguise for loneliness or something the Commander must persuade her to abandon.
The bridge journey, preferred cups, travel book, printer, rooftop meal, attraction, and first kiss are new fiction.
The native text does not establish them.

## Quest passages require their actual context

Vendor `Answer_0018`, AssetId `a0e745124f165d144b6b22ca7a29fd1b`, is gated by a started objective and an active etude.
Its response `Cue_0019` describes her wish for clean streets, whole cobbles, and blooming flowerbeds.
That cue completes Arueshalae's Arsinoe dream addendum `70645c40b5246cb4389194ffcef77852`.
The wish supports characterization, but the opening must not complete that quest or claim the Commander has already asked its question.

Vendor `Answer_0020` is gated by etude `3a040afde22f4b742a2f607354ab17e7`.
Its approving response `Cue_0021` must not be treated as an unconditional judgment of every mythic Commander.
The opening does not quote it as such.

Vendor `Answer_0025`, AssetId `41d9638f7d971164fab4efdbbbffbe70`, requires quest `a1024628f074e4d4f9d2b15956975459` completed, quest `5a5a533c9ce630a48b877f9a194840cb` in state None, and PlayerIsLocust not playing.
Its response `Cue_0026` describes ongoing attempts to find the stolen souls and her anger at the crime.
It is not evidence that the souls have already been returned or that Elan has any particular later fate.

Seelah Q2 `ArsinoeAtWedding/Cue_0006` establishes a preference for a church ceremony alongside tolerance and appreciation of the unusual celebration.
The cue uses the active Arsinoe unit as its speaker.
The neighboring `Cue_0009` about removing costumes uses a different explicit speaker GUID and must not be attributed to Arsinoe merely because it is in her dialogue folder.

Lann `Event3/ArsinoeWedding/Cue_0001` shows solemnity and excitement at conducting a wedding.
`Cue_0011`, AssetId `5bf81b66636f3fe43aaa994c68a4c7dc`, explicitly uses Arsinoe's active unit, blesses the union, and grants the two native wedding rings.
The whole wedding dialogue is `cd16c391d4260a64fbfe7ce35a53ce7f`.
Conducting the wedding is not blanket consent from either participant to a later additional relationship.
The opening does not remove Lann, rewrite vows, grant rings, or infer that Arsinoe herself is unmarried.
Integration still needs distinct marriage, interrupted ceremony, and rejection histories where they affect her response.

## Actual contact and interruption conditions

The normal vendor dialogue is `d5adc0bbbad5f054098b527cf9cc64f1`, with common answer list `ecaf5cfe8087a4f45a2269974f4885c9`.
These are the proposed entry attachment and the source of the opening's explicit AnswerLists binding.
The scene ContactUnit uses the active Drezen unit, not the unused Seelah Q2 unit `459aba8a61a75514fbf0495545cd52d1` or DLC1 replacement `711332472d374599ac7a3696b3f3de04`.

`Arsinoe_Capital`, AssetId `3f3fbb973a4ffee47956b4c7714c939a`, requires NotInCombat etude `e0d8b253efedb70488badaaa3d47632c` playing.
It unhides the native spawner and relocates it to ArsinoePosition in Drezen.
The spawner entity is `31b377f4-f461-47b1-98a1-4dbb02f23a05` in scene `3e2b5ea054cd5b2479e7f13134363ef4`.
The linked area is `2570015799edf594daf2f076f2f975d8`.
The lower-priority `Arsinoe_DefaultActor` etude `ddcbffad4e51e5c449f646e5ddb620f8` hides that same spawner.
Checking that an Arsinoe blueprint exists does not prove her actor is currently available.

Drezen `Arsinoe_Dialogue_Conditions`, AssetId `c4fa13c72fc350d4bae7431242eb095a`, excludes Playing `VictimsRevived`, AssetId `6d3fb96f9b60c0449a01add4be5c4a49`, under Seelah Q3.
The new opening must respect that suppression and the native quest's ownership of her actor, including resumed conversations.
Do not unhide or summon her to make a date available during a conflicting event.

Vendor `Cue_0023` is conditional on PlayerIsLocust `439e63fed37f52048887d98f99255e40` playing.
It preserves professional services despite grim disapproval.
Continued vendor service therefore does not establish romance availability on Swarm.
Character-specific mythic refusal and restoration remain required before export.
