# ENGINE Q7 lane l12

Base: integration `4a28a03767c9438f92de8412d28a3ebbda602dec`. No commit.

## CHANGES

- `storylines/engine_q7_l12.py`, `expansion.py`: one final assembly pass after all route appenders, delimited `eng7-l12`. Preserves every relationship, scene, node and choice position. Isolates shared COMMON paragraph dictionaries before variant compilation, and leaves factual blocks with an existing direct or derived witness intact. Wires the existing q6b native-history readers, which the input export omitted. No new prices, attraction requirements, commitment requirements, devices or reconciliation conditions.
- `tools/location_inventory_contracts.json`: E-Q7-15 and genuine L3 staging defects. Constrains physical Hepzamirah body/courier deliveries, Nenio's Melazmera reaction and other physical encounters to their venues. Melazmera's off-island fallback uses the Nexus, including manual reads. Horzalah's watch/quarters aftermath and ending recollection cover Drezen and Threshold without inventing a relocation. Both Nenio visitor volumes stay in Drezen; Last Call distinguishes visitor observation from the native companion's distance-neutral observation.
- `tools/epilogue_world_inventory_contracts.json`: E-Q7-16 and L5. Original factual paragraphs require actual native closure/Crossroads/rebuilding evidence; appended neutral alternatives keep earned outcomes reachable elsewhere. Neutral node lead-ins do not claim closure. Aeon Irabeth remains unmarried and Anevia remains dead, verified against their native sequence and enGB. The Kenabres cue establishes the city, not the cathedral. Existing explicit Council-convened/ceased paragraph readers and Galfrey queen-slide tests were retained.
- `tools/commander_block_contracts.json`, `tools/earned_presence_lint.py`, `tools/crossroute_checks/commander_alive.py`: E-Q7-05 (`anevia:005`–`008`). All living-future siblings get an unreturned-sacrifice exclusion and a bereavement alternative. This includes the reunion's accompanying paragraph, door rule, widow continuation, correspondence and friendship, plus Irabeth's related futures. Historical costs remain visible. The predicate uses existing Derived/DerivedForbids semantics; the runtime needs no modification. EP6 and L2 reject declared living continuations even on mourning/allowlisted pages.
- `tools/crossroute_checks/location_staging.py`, `world_facts.py`: repair recognition by class for provenance, recollection, distant cutaways, similes, explicit existing wardrobe travel, closing eyes/a hand, and “closed or failed to.” Unrelated physical staging in the same block still fails.
- `tests/test_engine_q7_l12.py`, the three `*InventoryTests.cs` files, `tests/Program.cs`: save-layout equality, guard-removal mutations, actual Rules availability/rendering, wrong-venue rejection and earned-return positive coverage. Minimal fixture corrections in `DelamereTricksterTests.cs`, `MelazmeraTricksterTests.cs`, `NocticulaTricksterTests.cs` and `GalfreyTricksterTests.cs` replace absent/placeholder/wrong venue inputs; original checks remain.
- `tools/crossroute_lint_baseline.json`, `tools/crossroute_lint_report.md`: regenerate remaining debt. The report individually refers every remaining fingerprint to its route, scene, node, block and missing condition. No remaining finding is waived as a false positive.
- TEMP cleanup: remove the six tracked .NET sentinel/cache files under the pre-existing `tests/DelamereGateTemp/.dotnet` folder. It contains no test or story source. All l12 build/probe/report artifacts lived under system temp and were deleted; generated Python caches and verifier reports were also removed.

## CLASS SWEEP

The complete original L3 (29) and L5 (117) finding inventories were checked, including every repeated paragraph and incoming branch. All epilogue siblings receive the shared finale/survival corrections. Historical costs, deliberate kills/closures, earned return conditions and other women's exclusion rules were preserved. No echo slots or foresight mechanics changed.

Historical audit references to a separate Chadali-spoke paragraph and Horzalah `c6_retry_morning_refused` / `c6_retry_morning_letgo` copies do not exist in this integration snapshot. The present wager and Chapter 5/6 aftermath were corrected; obsolete content was not reintroduced.

## GATE

All required gates passed on the final regenerated export:

| Command | Result |
| --- | --- |
| `PYTHONHASHSEED=0 python expansion.py` | Exit 0; 2867 scenes |
| `python -m unittest discover -s tests -p 'test_*.py' -q` | Exit 0; 259 tests, 5 skips |
| `RRT_GAME_DIR=/wrath python tools/rrt_verify.py --strict` | Exit 0; 0 hard failures |
| `python tools/crossroute_lint.py --strict` | Exit 0; 0 new findings; L2/L3/L5/L6 = 0 |
| `dotnet run --project tests/RulesTests.csproj -c Release -- development/Story.json` | Exit 0; 133443087 assertions |

Remaining baseline: L1 = 1665, L4 = 1128 (2793 referrals). The original L3 = 29 and L5 = 117 are fully resolved.

`RRT_GAME_DIR=/wrath` selects the supplied blueprint/localization bundle. Verifier JSON/text output paths were explicitly set under `/tmp`. C# `BaseIntermediateOutputPath=/tmp/rrt-eng7-l12-build/obj/` and `BaseOutputPath=/tmp/rrt-eng7-l12-build/bin/` kept both build and run outputs outside the repo. Generated `development/Story.json` is restored after checks because it is outside the allowed edit scope. No build-expansion script, harness, game, merge or commit was run.

## ESCALATE

Remaining L1/L4 debt belongs to the parallel route/shared-consumer lanes. Every occurrence is listed in `crossroute_lint_report.md`. No production shared-code change is required by l12.

## PROPOSE

None implemented or required beyond the assigned findings.

## RISKS

The finite prose vocabulary and explicit survival contracts need extension for future differently worded assertions. Venue/rendering tests use earned input histories and native facts; they do not claim a live-game delivery audit. The full game, harness and expansion build were not run. No independent rubric score is claimed.

## Original L3/L5 dispositions

One row per original fingerprint follows. “Variant” preserves the old paragraph and appends its neutral alternative, or makes a node's lead-in neutral; “recognition” is a false positive resolved in the lint with the evidence described above.

| Original fingerprint | Check | Route / scene / node / block | Resolution |
| --- | --- | --- | --- |
| b1825e08e2c472df1d71ce3f2e15267a14c8e08a46b712be06c7bf8959e7e788 | L5 | anevia / anevia.ending_ascended / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| 784b235020dd92120e569b57bf075113c2705d88772d3ecddbd2bc2bf26e129b | L5 | anevia / anevia.ending_changed_power / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| 2cf9bcbcb318af64ae7f008a7621452356d2fe7f8329bb39157573bf70245d2f | L5 | anevia / anevia.ending_kept / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| 33e1ae31cdeb6ebff88ba79a5910f99e75b77f23d5f92ba4b24a58f33b676e1b | L5 | anevia / anevia.ending_open / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| 34c9dc10e20d73d12ddca859a636b796f9537f7c33c643e77448f1131727fbaa | L5 | anevia / anevia.ending_parted / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| a8fd0c2f55b4136c2100cc462a44a660c55035c6bfdeef102dd9ed01b6e99fd5 | L5 | anevia / anevia.ending_promised / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| da1e28fbe703dd9009c8fcad3ff9c488a728bd12eab550ff5f6e65b41319552c | L5 | anevia / anevia.ending_sacrifice / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| c1d28a223cf25d9b37cf0be715aebfc72188dca7fc35f9c4f5acda04ef5d155a | L5 | anevia / anevia.ending_unfinished / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| f2d86020a592c5ad02409f601ba07a19ac85a4219a7f5a6b0d32e95e4b5af71d | L5 | anevia / anevia.trickster.epilogue.nailed_wardrobe / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| 065bfe251d02658c9ea6190e4de0a7f5c43e6b5738143a65bccb448d095a367f | L5 | anevia / anevia.trickster.epilogue.nailed_wardrobe_closed / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| 818bd13a601d0b8841c3812537dd1534de1b2085ff5c5cb018c947791cb6a024 | L5 | anevia / anevia.trickster.epilogue.nailed_wardrobe_lover / end / paragraph[17] | Variant: native-fact paragraph or neutral lead-in |
| 2870e6053bb5ea8c4a8c3c47e09b0cfbcd215689b87e4aac83cae608c29eab7e | L5 | areelu / areelu.trickster.finale.unnamed / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| a15602b93eedc386de2766ce9894ce8099a69b0bf240c693aee67f4c66ee6b4c | L5 | areelu / areelu.trickster.report.rooms / knock_witch / text | Recognition: closure is qualified or concerns a body part |
| 084cc480b0c2de3123eb0254dd558ce2c7bd79ecc58cf30c3f8f7e61c4867f24 | L5 | arueshalae / arueshalae.treatment.epilogue.freed / page / text | Variant: native-fact paragraph or neutral lead-in |
| de4e479e5ba03f94b5f6034d693598ac02ae8cdd9ce0f3f84efb20fa00d50a05 | L5 | arueshalae / arueshalae.treatment.epilogue.together / page / text | Variant: native-fact paragraph or neutral lead-in |
| 23e68966cdb5f0d3a00bc7d924b7dd7d08181f41a426b380b82bee731a0b30d0 | L5 | arueshalae / arueshalae.trickster.epilogue.kept / page / text | Variant: native-fact paragraph or neutral lead-in |
| 403e1953c21860006eeda40d0f78cbdac8b527f03bc78a5e98abbb16098fcb5b | L5 | arueshalae / arueshalae.trickster.epilogue.kept_fallen / page / text | Variant: native-fact paragraph or neutral lead-in |
| cee26ec57d575045c611853ac1a87697a7de53fdf0e4c4fdf2184908fc805d67 | L5 | chadali / chadali.trickster.epilogue.lucky_night / page / paragraph[15] | Variant: native-fact paragraph or neutral lead-in |
| 0f445f07010efcb03c8d99495b2defbada07ed79532d8b76e250051bb331ad54 | L3 | delamere / delamere.trickster.discovery.pilgrim / start / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 82093fd24217b127e56fcb9718316f2a16dc97989cfc1aa2f4df41735362789b | L3 | delamere / delamere.trickster.woken.feasting_table / white_stag.fire / text | Validated venue contract |
| a21078046d9b49242ea225dba3681529c8e077d6c962a1050ed63c4d8d56eaaf | L3 | delamere / delamere.trickster.woken.white_stag / fire / text | Validated venue contract |
| d131332b98959722f704fa9b128648c1770e11f331da0f0933e88b8950564604 | L5 | dorgelinda / dorgelinda.trickster.epilogue.after_the_war / page / text | Variant: native-fact paragraph or neutral lead-in |
| 196e2af882292a6a14ea32d1e4ea8a8d1ae22b79d7521e9e75fde455ba7eea86 | L5 | elyanka / elyanka.trickster.epilogue.eaten / page / text | Variant: native-fact paragraph or neutral lead-in |
| de9de20fb658247dda2495b62ee4ea79d9724dc2a156cf8b64c940b26441a582 | L5 | eritrice / eritrice.trickster.epilogue.we_did_meet / page / paragraph[22] | Variant: native-fact paragraph or neutral lead-in |
| 0fcb3cc6e2df3c0c0000ccfb042cf4ceed595ee3d843db78c1bbb6c99043e7a3 | L3 | galfrey / galfrey.trickster.ch3.standing_orders / start / text | Validated venue contract |
| 87a2fa2f99bbf7024b1f0ecc0eed352422260f1338c780793fa27ddee0500ec9 | L3 | galfrey / galfrey.trickster.ch4.letter / open / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| e18c76efdefc2e04dbe4676f6cf2164b8e41659703b0c960f3d8786864de5121 | L3 | horzalah / horzalah.trickster.react.wenduag_morning / start / text | Validated venue contract |
| 4ff094ad2d0e6c3bba6322db792244c7b3fa53255881d519e1e1f24c91778ee3 | L3 | household / household.table.offered / kept / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 3c7e5fb7011675a6aa87bea4412485e2fe4ac608d24f359a5a0a5ac9814a1e2a | L3 | household / household.table.offered_c5 / kept / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 7165bce67bb03413747d4d0b5a1341aad851d40d3271bf605ae5f8af0b8512f1 | L5 | iomedae / iomedae.trickster.epilogue.unanswered / page / paragraph[3] | Variant: native-fact paragraph or neutral lead-in |
| 158d56104f613e2a3cfaf227e21ad821657fa584315951e81d24733e78bc0bed | L5 | iomedae / iomedae.trickster.epilogue.unanswered / page / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| fda81a8b423640d089aa406ca16c6f61472963531e4f1a24914f7f43c8123815 | L5 | iomedae / iomedae.trickster.epilogue.unanswered / page / text | Variant: native-fact paragraph or neutral lead-in |
| d6e8ae608a37f79c5ef2534df823797c81c86257774100061327e4e1467cbe6d | L5 | irabeth / irabeth.ending_ascent / end / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| 9541a507001f3faf42eba3e684b4bd36931d15f8b8e96c28b92f334ed5a207ed | L5 | irabeth / irabeth.ending_ascent / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| 2bb4dd3b318aa713f5f56efaa47eabe7a3da80557323c65f7e3a6be3eb2b221d | L5 | irabeth / irabeth.ending_ascent / end / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| 26e4486da438eea8e502bb6ff4fda0d922cfecca4ea274aca422d69b9375a299 | L5 | irabeth / irabeth.ending_ascent / end / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| e77f4baa4d9098159fd0fd7f1832997b028511eb5df17a5eb572bfc4e5e00ef4 | L5 | irabeth / irabeth.ending_ascent / end / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 2338e1c5cca7e5876cbdd6d4fd864c2541c2a84d3739f85f94386d65a98e1d0b | L5 | irabeth / irabeth.ending_ascent / end / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| d28b03a4f90c5241bdb93e6d7b4daaf6047869b9f1ef906543cfeb5c14cca726 | L5 | irabeth / irabeth.ending_changed / end / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| e3df2485ab358b08d38b67a8316164d0a0e4c72c6e4b7dc6de11fc464ae25bf6 | L5 | irabeth / irabeth.ending_changed / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| e781a1df1036c8c127e1ce9d9c9a71835618912aa06cc5897ffbe8c11b0283d9 | L5 | irabeth / irabeth.ending_changed / end / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| 240e83d9cdb6f525e22a867cfa6b215530806539a04c9b494e3a56ccf270cc38 | L5 | irabeth / irabeth.ending_changed / end / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| 7279a5838b46b5cbfe8a169704c06751a17466e88531a0e570c385e7ec403069 | L5 | irabeth / irabeth.ending_changed / end / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 17f4cad0c549b289c9a042ae73a3acc268f9c0c100f48191bb8ce3f816bb293b | L5 | irabeth / irabeth.ending_changed / end / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| 311a32f43ba04f84bc2a92b99367bbe3c2c58ffe5a62157b44efa9fef5634667 | L5 | irabeth / irabeth.ending_friends / end / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| 11c9d37320c07fd69b34f6c82ff1f83a0bea8f0fbb90ff366af2b4e901b49218 | L5 | irabeth / irabeth.ending_friends / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| 50d3dc9f1b0a69fc37ef06fcca02c2c2440a6902d84b4fb45232d1951c1b0a54 | L5 | irabeth / irabeth.ending_friends / end / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| cba8ae195ce3e6a8df54dd02568180217c01349bfc06057c340fc2cee8241043 | L5 | irabeth / irabeth.ending_friends / end / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| 556140b11c17b22fbfbe8954856cccd00ba97fdbd0d446b2238a7b2c5d225fc2 | L5 | irabeth / irabeth.ending_friends / end / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| ebd88e1b0cbb9445c3b95449b1d2bd736223858165e470456f427362cc3ad6b9 | L5 | irabeth / irabeth.ending_friends / end / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| c5b429951a9c00938db42532490aaed43a0ca27c5ae9406e4cc3dc68ccf9ec3c | L5 | irabeth / irabeth.ending_lasting / dead / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| 39630ddb9bde30a3bdaccc66e1b889f76c4962c14a301d9c394a60a4a717425b | L5 | irabeth / irabeth.ending_lasting / dead / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| 9ae5c287221e930483bde0d2970adac2dae86e1eea078b97c4e93997d4337b5d | L5 | irabeth / irabeth.ending_lasting / dead / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| 6b95d747475b749459f6e800360296fb370d27eff1960b4040a258cdf18375cc | L5 | irabeth / irabeth.ending_lasting / dead / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| cf773418698385082bb4b025acefce2bb9ad4480a36b96a0c3e9d3e18bd47c21 | L5 | irabeth / irabeth.ending_lasting / dead / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 399115c16be17df508cb0fad27d8b6793a3031bedbedd7b5b30f421a6d3eafa5 | L5 | irabeth / irabeth.ending_lasting / dead / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| a9473ed378567b8fa04f92a213c6d4fc1c23cec5c893bd06219d6cf73c252505 | L5 | irabeth / irabeth.ending_lasting / gone / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| 21453652fd81bd722908eb0e0a1d03dda586f4609326358d4c22cf517530fcc8 | L5 | irabeth / irabeth.ending_lasting / gone / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| 5bdb16d384fd45bd3f1306554234480834677bcf04c11bfbec653bcd978a5bb3 | L5 | irabeth / irabeth.ending_lasting / gone / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 78485848761e33a86393e4af9226d26a7156c9c5b797e957096183a1ab8dc52e | L5 | irabeth / irabeth.ending_lasting / gone / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| d0e46575a1e4896b4fe1f00bd71035ef9870b0084246a18e231406b989660310 | L5 | irabeth / irabeth.ending_lasting / living / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| c420ad8410bb8d9240cdbcf05dd773d313fad8cab096ae254c936581e9fe1fed | L5 | irabeth / irabeth.ending_lasting / living / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| 7ad8fef673faabe4346a6a00ff9bb5c415c5ee86caf9c2509d8ef05ac51cac94 | L5 | irabeth / irabeth.ending_lasting / living / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| cd609ac54282765dcee7acadcb001cade9536c3bceda555466c9e4fef6560574 | L5 | irabeth / irabeth.ending_lasting / living / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| 24606da7eba2296fdae6226e4d98cb2502e9a29bc0643491fa8677d2e25372f5 | L5 | irabeth / irabeth.ending_lasting / living / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| fe0e868e6485babc26b9488db665a4825b57475ce8ea0bbc5c9951cdaf4e9b1e | L5 | irabeth / irabeth.ending_lasting / living / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| c9d0ece67eae070c4387195b5888d21ff5a2ddcfb5f6c24a29f1e6411897bf28 | L5 | irabeth / irabeth.ending_lasting / returned / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| f6876366459e7a9e754787498e2bcb12952978d26a189045bf3370411aa485ea | L5 | irabeth / irabeth.ending_lasting / returned / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| ddbf3358df2d50ba7f33f2afe77badc6ab1475e26f6f1dcec51e446fe99e761e | L5 | irabeth / irabeth.ending_lasting / returned / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| 8569e6b658cdaa9f729c976dbeec8d0efef15094e3f04429dca73296a94254ad | L5 | irabeth / irabeth.ending_lasting / returned / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 18a8b0f066f9eb17c2e33aac478975ccc85fb1cc56fd7228b4aa06f44420800c | L5 | irabeth / irabeth.ending_lasting / returned / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| fbbbe973e142627c68ddf36fcc1aa6e046318b25a2811f3f0cd07c6e14f1540f | L5 | irabeth / irabeth.ending_open / end / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| a785232a0b14d17230dba8bdfbee82fd0b07247b0d2763d1d92e0456aa21c508 | L5 | irabeth / irabeth.ending_open / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| b97caa98338d7afc9e348baf8b2d822829c64861a31131ea9718e24d0d91ec25 | L5 | irabeth / irabeth.ending_open / end / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| c4d4134f9af68f341ab64f0a1b5761380a234029c6900f15329799aab5e5a498 | L5 | irabeth / irabeth.ending_open / end / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| 3fa26a1c50d4ceef3db54920e880caa9b1afc1f91de87f184eb36cdbc28c6bee | L5 | irabeth / irabeth.ending_open / end / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 987566f09bfb1572889555fb651cba52ed57f1aa022cabd3414e05e3cc682956 | L5 | irabeth / irabeth.ending_open / end / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| 7bc3bad929140bc5ba927c85932b4d754fc024ff5e9c584f01736da2e719bdc9 | L5 | irabeth / irabeth.ending_sacrifice / end / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| 0feef1de1d2412561eb8323b72d6e8c529be9a3e26a79e21099415f337ff77d6 | L5 | irabeth / irabeth.ending_sacrifice / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| e9bf514d8caa7195d7108d35159824dd26d4728708a05954236e9a5eef0c3fbf | L5 | irabeth / irabeth.ending_sacrifice / end / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| 2a05cb69f41819a748175d8d0b697d843e2db8fff1f69f7256270869b1e03d38 | L5 | irabeth / irabeth.ending_sacrifice / end / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| 4c7d9978957f4357004f8104957c56a623685aae8d5749a2c7faa13547592179 | L5 | irabeth / irabeth.ending_sacrifice / end / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| bacb098fb4e11b22fbd69bcc8478f45bb6a1447c579f12f4e96c9f0dbb935ff5 | L5 | irabeth / irabeth.ending_sacrifice / end / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| 91291eb3ab0ab197c0d1edd7395efa914e16e48843c689c2fbf6a3163b708f52 | L5 | irabeth / irabeth.ending_unfinished / end / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| d7ca53c4af48986f74ae97297c08c7612234a426daa87ff7c4155809f20154ee | L5 | irabeth / irabeth.ending_unfinished / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| e02a4a342e93cd780efdd7b74d13c11e3c076126b915484eca793c103e03dcff | L5 | irabeth / irabeth.ending_unfinished / end / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| e4aed2daec04701f2a6ee59de01b1a1cf86d11a07cee9f9adbb7c604cf5a3450 | L5 | irabeth / irabeth.ending_unfinished / end / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| 9b1911ed14b19b6ba42aeb909e98e0143cd1d38f4603206fbb1569215cca67be | L5 | irabeth / irabeth.ending_unfinished / end / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| d48d2d49d7fb0c9fe8c2886460d5e89ae247e23eab40c39c63baa8b76a7e4161 | L5 | irabeth / irabeth.ending_unfinished / end / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| 27292cd8199816f7fd3da4a07ad179c98e5037a7f5e1f91eb954d05f0e1e12b8 | L5 | irabeth / irabeth.trickster.epilogue.native_tirabade_south / page / text | Variant: native-fact paragraph or neutral lead-in |
| 04062da0311d4503fac1f2531a66138ea8561ea4223a9fb2fb08945c9c6477ef | L5 | irabeth / irabeth.trickster.epilogue.off_the_record / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| 59849dccab05385356945a7a94cffd17fbc852f6727125ad6caf74152ad6bc45 | L5 | irabeth / irabeth.trickster.epilogue.off_the_record / end / text | Variant: native-fact paragraph or neutral lead-in |
| 4c56be21a6b3521ab99e568a322e0d1afdb5e518e605bf82df21c3568e250c36 | L5 | irabeth / irabeth.trickster.epilogue.under_orders / end / paragraph[10] | Variant: native-fact paragraph or neutral lead-in |
| 60e293cf6cf2e750a0cf516333c4f85def2ecac078add196216ea05973647380 | L5 | irabeth / irabeth.trickster.epilogue.under_orders / end / paragraph[5] | Variant: native-fact paragraph or neutral lead-in |
| 47d17ff33e4013398516f6e9bbf979d8f71c325fbe577c5ba68af30d0da39a0d | L5 | irabeth / irabeth.trickster.epilogue.under_orders / end / paragraph[6] | Variant: native-fact paragraph or neutral lead-in |
| 734e7f4ce2d74f484af1f17a8c716a228b292ceabf6180ee09330d6ecb3f189f | L5 | irabeth / irabeth.trickster.epilogue.under_orders / end / paragraph[7] | Variant: native-fact paragraph or neutral lead-in |
| bae1dbb52b78750bc895ad294ed709b665ef28def704d31326707159ed5e97b9 | L5 | irabeth / irabeth.trickster.epilogue.under_orders / end / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| f8d740815137a0df012e7d629b6dfc2b01f7e779caa58afd26e5cb0a0e42e168 | L5 | irabeth / irabeth.trickster.epilogue.under_orders / end / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| 8649ceea44f925eba122589aba0d9253276cb1e34b75826fea834be35b4143c5 | L5 | irabeth / irabeth.trickster.epilogue.under_orders / end / text | Variant: native-fact paragraph or neutral lead-in |
| 0f8d98316dd216984fc4b1348acdb73253a7d144b368a1f7b47aadcc6d6b927c | L5 | jerribeth / jerribeth.ending_sacrifice / start / text | Variant: native-fact paragraph or neutral lead-in |
| af8329cbbfc0db182dd6938f3f60a3814fd678f07b785246d59a77f3b15cdc51 | L5 | kaylessa / kaylessa.trickster.epilogue.declined / page / text | Variant: native-fact paragraph or neutral lead-in |
| a5b346da722fcd39489c9da5cbcd8c620a5ff11b6e7e755aecf72c006d68b46a | L5 | kiana / kiana.ending_ascended / start / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| aad12bed4c5bf9365cedc360ec394f331b6b38d99a711209087fb879747332aa | L5 | kiana / kiana.ending_ascended / start / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| 18ac01623e8aa17837b4b58a6ad7005605e662a1c5c06020108574871e32681c | L5 | kiana / kiana.ending_bereaved / start / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 1a79a240133b781a025d3fc965873c1cd72da4c962a62554ef172e19539e5906 | L5 | kiana / kiana.ending_bereaved / start / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| 9f276957e866d74ebc32b8819f994ec389fed7cd663277c8dfdf2cffe53ff3f5 | L5 | kiana / kiana.ending_promised / start / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 408cb4d0247444a1f9ac11d83e38808aa1b83497c04e250d4dce491cd68eb116 | L5 | kiana / kiana.ending_promised / start / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| 3ac8124d386e62f36f8c95a5a65b8bf9a74ea3e7eb095d86441869f637586140 | L5 | kiana / kiana.ending_together / start / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| f677136574665d6558a9a1987ba9498c19064aee84a59f699cbeb8d6354ca1f2 | L5 | kiana / kiana.ending_together / start / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| cf707c3df9521230c53093f0839c4ea48154574c88865906308bb751e443bb47 | L5 | kiana / kiana.trickster.epilogue.betrothed_kept / start / text | Variant: native-fact paragraph or neutral lead-in |
| 8904cf027dbc504bb8da94d7400a6dd069d6d36172e8b0272e42154131cbd283 | L5 | kiana / kiana.trickster.epilogue.commit / margin / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| 1f14406b56a2cd502148ae1c93366bf30fff8dd9617bd3a10037e34ec5d14fdb | L5 | kiana / kiana.trickster.epilogue.commit / margin / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| f5f50d1fcb852ed75ec29174cad8c83406aecdb501655ff032bbe405a4a0d443 | L5 | kiana / kiana.trickster.epilogue.commit / stage / paragraph[8] | Variant: native-fact paragraph or neutral lead-in |
| a0ef63ae4361b1b6bc697c9f89bb21a8a157e1b27dbe3fad208c6603f99bdc47 | L5 | kiana / kiana.trickster.epilogue.commit / stage / paragraph[9] | Variant: native-fact paragraph or neutral lead-in |
| c59898bf5f4fa9d10c2781cf8212c29ebeaf072967be46a849219dc78a243925 | L5 | konomi / konomi.trickster.epilogue.envoy / start / text | Variant: native-fact paragraph or neutral lead-in |
| 6013192d3829e2b140d15765bcdb649ad342e3e3f73151053af875f6e1a34e63 | L3 | lastcall / anevia.lastcall.call / call / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 9e76e3962cc0bcd272207417976a57e9d6e1578fbb790f334379f96f815894ac | L3 | lastcall / horzalah.lastcall.call / call / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| bdd20e2959a652764da1b2e2c95ef0171bf8611ef91ef1871660c3ab6b8d4dbd | L3 | lastcall / irabeth.lastcall.call / call / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| c2801944d4a9ee028c0b85e7247481882e7a264a2229863f711e690b9dbb0d4a | L5 | lastcall / jannah.lastcall.page / page / text | Recognition: closure is qualified or concerns a body part |
| 24ce65f6f385ef7bdb5afbfcf1889c9472e81759b8739cf86c5c2ebfdeeaa680 | L5 | lastcall / nenio.lastcall.page / page / text | Recognition: closure is qualified or concerns a body part |
| 9abd3ff2ba490d8ada7e3cbdd8454851e30d5358d8d94e7130c7c5aa31cf4d11 | L5 | lastcall / wenduag.lastcall.page / page / paragraph[0] | Recognition: closure is qualified or concerns a body part |
| 239e463705c307922bb8702dc7815db296b419aed694f9cd942af0ccaaff66e9 | L3 | minagho_chivarro / minagho_chivarro.trickster.reunion.wardrobe / press / text | Validated venue contract |
| 6c94502ea4049ba395922034fde2f69935daf1e2be6f91bd505c014a9b88c731 | L3 | nocticula / nocticula.trickster.defeated.chair / threshold / text | Validated venue contract |
| 13c93d0cb9329371897e027d0216f51b2188ac2b85937e8d2d5ba9b9805a2f00 | L3 | nurah / nurah.trickster.abyss.sky / blank / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| f30140ad3c50cddc043351ffec5a404c50ca512f86b706d359bef7dd8a9e3024 | L3 | shamira / shamira.trickster.killed.drowning / n_h_home / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 49c898d4446c30daadf994d0e33c39ae3286e15ef62cb34acd60b78d57c7c054 | L3 | shamira / shamira.trickster.killed.drowning / n_h_wardrobe / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| beb0399360f0910fb166754673499197bce667120e87b33aa60703fbc0b2b56e | L3 | shamira / shamira.trickster.killed.setup / ha_home / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| b59e0f3d32ce53b041cc13131f3788c45be6a148f0fa21505dcf0f3122de916a | L3 | shamira / shamira.trickster.killed.setup / ha_wardrobe / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| c789a1db57603529e6e88e1c52daf743d3cae80bea9f91f32ae358a75769622b | L3 | shamira / shamira.trickster.killed.voice_letter / n_h_home / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| fdf53d6dc9afc0609cbf1dd05149b7f48c8d69d25470e8a3ac46dde1d8b68ec3 | L3 | shamira / shamira.trickster.killed.voice_letter / n_h_wardrobe / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| a4609f1f6764217ec0b34322cbc5be9b07e8f1a08672c094559ab5e5cbd3aca1 | L3 | shamira / shamira.trickster.mind.first_night / h_home / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 702d7eff7d3fbbb342e7b51a42bc125f0ec182031c827839d87843bbce3711c0 | L3 | shamira / shamira.trickster.mind.first_night / h_wardrobe / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| a78eb5e051c12b4c6a719665d9cbc4e9c70bca9c70baa974bd5390de0cc2f788 | L3 | shamira / shamira.trickster.mind.heist / home / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 6ebd4148c0f90c78e882686e306c791d701beec11767ba0a2f96239cb83d2d4f | L3 | shamira / shamira.trickster.mind.heist / wardrobe / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| ac522ca020a26c81ac1a92e5d72b4b3df7e56316197cd87be2f64735eb002539 | L3 | shamira / shamira.trickster.mind.heist_alone / home / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 44e285ec537db255919851fadebe7cef739a920a955ed831e2e801b484b37be6 | L3 | shamira / shamira.trickster.mind.heist_alone / wardrobe / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 1ebdfa33fcce51df4d44a409490a84b6f94aa97849ec6871c42d91fb88cc324d | L5 | soana / soana.trickster.epilogue.commit / start / paragraph[4] | Variant: native-fact paragraph or neutral lead-in |
| 2769fe749a942cc2369493cb5009607fe0a0ecbda274523319c783be7e9d16c0 | L5 | soana / soana.trickster.epilogue.luck_late / start / text | Variant: native-fact paragraph or neutral lead-in |
| ff720425eeec8c22ca1b546c46f25e9c628d7b505a936aa84bac98bdbe583fa8 | L5 | soana / soana.trickster.epilogue.unfinished / start / text | Variant: native-fact paragraph or neutral lead-in |
| 53ff805014a1c74bfeaffc24b25e3c48ba458561d2c9a69badfbc9d6e8412a56 | L3 | terendelev / terendelev.trickster.watch.third_bell / abyss / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| c7fac265ff7a0c6d414ce14e6746816505d35928d54dfde82c7aa70007b1e97c | L5 | terendelev / terendelev.trickster.epilogue.debt / page / paragraph[4] | Variant: native-fact paragraph or neutral lead-in |
| 225a3c1f84eb71c8394193ff1fa23b54b0adb29a709d62966a3f54decbacb83b | L5 | terendelev / terendelev.trickster.epilogue.guardian / page / paragraph[4] | Variant: native-fact paragraph or neutral lead-in |
| 16e0a04141d7553941893437636e45ea912f2ed4096252f6e2f6db81224587fb | L5 | terendelev / terendelev.trickster.epilogue.late / page / paragraph[4] | Variant: native-fact paragraph or neutral lead-in |
| bf10e0c21ddf8834198ca5189d0e7d0b275eb810db5bb42aa4a2e6ee55d98961 | L5 | terendelev / terendelev.trickster.epilogue.watch / page / paragraph[4] | Variant: native-fact paragraph or neutral lead-in |
| f32f70477904abb55d88047b8534e0c027e7d6e9db0833b7490a5e43b8a25509 | L3 | vellexia / vellexia.trickster.mirrored.fetch / left / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
| 85ab62a30aff1965a3f400d042e2db1000e750ef727f826361960039e0ba4dc3 | L3 | vellexia / vellexia.trickster.mirrored.speaks / sheet / text | Recognition: distant/provenance/recollection/simile or existing explicit travel |
