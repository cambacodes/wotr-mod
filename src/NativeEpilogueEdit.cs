using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Kingmaker.Blueprints;
using Kingmaker.Designers.EventConditionActionSystem.Actions;
using Kingmaker.DialogSystem.Blueprints;
using Kingmaker.ElementsSystem;
using Kingmaker.ResourceLinks;

namespace Tirabade
{
    // E14d: a reviewed native epilogue cue is replaced by an RRT epilogue scene's text when an earned condition holds.
    // The original keeps its native checker, wrapped by ParentEndingGuard (shown only when no replacement applies);
    // each replacement is a registered RRT cue inserted right before it, shown only when it is the selected variant AND the
    // original's own checker passes. All read the same per-frame snapshot, so exactly one of them plays. When the mod is
    // disabled or uninitialized every replacement is hidden and the native cue plays.
    //
    // E14d extension (Cue_0311): one native cue may carry several ordered variants (the first attached variant whose When
    // holds is selected), a reviewed OnShow ChangeBookEventImage that a variant may keep, and a page outside
    // CueSequence_Companions. A refusal of a cue marked DegradeOnRefusal = false only skips the edit (the native cue plays);
    // it never disables a relationship.
    //
    // Why not ParentEndingAlternate: its selection is refreshed only inside ParentEndingIntegration's scoped page evaluation
    // (Harmony hooks on the parent's RanRomAdd pages). These native cues are ShowOnce false, have no answers or continuation,
    // so complementary conditions give the same one-of-N selection without new patches.
    public static class NativeEpilogueEdit
    {
        public readonly struct Evidence
        {
            public readonly string Page, Sequence, Key;
            public readonly string? Image;            // the reviewed OnShow ChangeBookEventImage asset, or null for no OnShow
            public readonly bool DegradeOnRefusal;     // false: a refusal skips the edit and warns, the native cue plays
            // E14d extension: the reviewed continuation (Strategy First), or null for none. On a book page the continued cue plays
            // right after the original (DialogController.PlayBasicCue); a replacement never continues, so it hides that too.
            public readonly string[]? Continue;
            // E14d extension (Cue_0461): the continuation the parent mod sets at load (RanRomance SlideArue: Aranka's slide), also
            // accepted (Strategy First); a replacement of such a cue keeps whatever continuation the cue has, so the parent's
            // slide still follows it. 252ccf6: refusing that continuation degraded the relationship in game.
            public readonly string[]? ParentContinue;
            // E14i: a cue of a common dialog: Parent lists it in its Continue (Strategy First), Dialog's FirstCue holds Parent.
            // Page and Sequence are then empty.
            public readonly string? Parent, Dialog;
            // E14i (non-epilogue dialog cues, engine queue 8c/9a): Parent may also be a BlueprintAnswer (its NextCue lists the cue) or the
            // BlueprintDialog itself (its FirstCue lists the cue). Answers: the cue's reviewed answer lists, kept by the replacement.
            public readonly string[]? Answers;
            // E14i (engine queue 6b, Kiana's JewelerFinal/Cue_0051): further cues whose Continue (Strategy First) lists the cue exactly
            // once; the replacement goes in right before it in each. Such a cue sits mid-dialog, so its parents need not open the dialog.
            public readonly string[]? AlsoParents;
            // E14i: the cue's reviewed OnShow / OnStop actions ("Type:guid" of each, in order; ActionShape). The replacement runs the same
            // action objects, so the quest goes on exactly as it would have (only one of the two cues ever plays). Null: none allowed.
            public readonly string[]? OnShow, OnStop;
            // Optional full engine-q3 action signature, including evaluator/options on reviewed native outcomes.
            public readonly string? OnStopSignature;
            internal Evidence(string page, string sequence, string key, string? image = null, bool degradeOnRefusal = true, string[]? continueTo = null,
                string? parent = null, string? dialog = null, string[]? parentContinue = null, string[]? answers = null,
                string[]? alsoParents = null, string[]? onShow = null, string[]? onStop = null, string? onStopSignature = null)
            {
                ParentContinue = parentContinue;
                Answers = answers;
                AlsoParents = alsoParents; OnShow = onShow; OnStop = onStop; OnStopSignature = onStopSignature;
                Page = page; Sequence = sequence; Key = key; Image = image; DegradeOnRefusal = degradeOnRefusal; Continue = continueTo;
                Parent = parent; Dialog = dialog;
            }
        }

        // Whitelist, verified in blueprints.zip: ShowOnce false, no components, and the reviewed parent, text,
        // answer lists, continuation and action shapes. Reviewed OnStop actions run from the selected cue only.
        // Before adding a cue, check that the RanRomance parent never
        // mutates it (reference/canon-review/aranka-*.cs and the parent DLL's UTF-16 strings): Cue_0461 failed live because
        // the parent sets its Continue.
        public const string Companions = "fec3b6f28610c8a48a239f148ed3ed60";
        public const string Special = "f8d7f50e3bb88c143834d234c0b24474";
        public const string QueenSequence = "bb9d36fd37d74bf4792931d6052a7d44";   // CueSequence_Queen (Galfrey's realm slides)   // CueSequence_Special (the Tirabade pair page)
        public static readonly Dictionary<string, Evidence> Reviewed = new Dictionary<string, Evidence>
        {
            ["86bf0569a9029ae4b8c9d300a41e5739"] = new Evidence("223fd069ee25c784db2df011adbf10f8", Companions, "0dfe0435-8149-466d-bf0c-88d648651c3a"), // Wenduag Cue_0409
            ["36a07840d25540eeac6b1c6631196bcc"] = new Evidence("503164ff04ac64543ba42561ea9f970f", Companions, "af56e46e-7e82-4e22-9951-8ddc37dd015f",
                degradeOnRefusal: false), // Camellia Cue_38_master (warning-only, with the other Camellia slides below)
            // Arueshalae Cue_0461 (the dream world): RanRomance's SlideArue sets its Continue to Aranka's slide 959237a3 (aranka-SlideArue.cs),
            // which the cue keeps under a replacement. Warning-only.
            ["78ae1bdc3b0824b4ca2ed618782f1faa"] = new Evidence("e83fff8e997db8e439bf12e09225696a", Companions, "411ef2f1-5168-455f-99b0-ca33960678c5",
                degradeOnRefusal: false, parentContinue: new[] { "959237a34dfe436eb8f088b4be259daa" }),
            ["f76713034f4087a4f80495971c47ca7b"] = new Evidence("e83fff8e997db8e439bf12e09225696a", Companions, "fa1468ba-9679-4805-9dd4-c71997aa4e7f"), // Arueshalae Cue_0462 (NM1)
            // Tirabade BookPage_0307 Cue_0311 (IrabethDead + AneviaGone Playing): "No one ever saw her again." Its OnShow swaps
            // the pair picture for f96ad5fa, as the other departure cue (Cue_0310) does. The parent never names the cue, its
            // page or CueSequence_Special.
            ["3a3e561c6b05a284d93eb3bff7b712a6"] = new Evidence("ae1f824fe248d9f4aac7d39ec2e12140", Special, "4c278ba4-5217-4fae-afec-47c6f6597e00",
                image: "f96ad5fa9c59d7549adff4c90f0703ab", degradeOnRefusal: false),
            // Tirabade BookPage_0307 Cue_0310 (IrabethGone + AneviaGone Playing, both left at the Coronation): "...they could
            // never escape their nightmares of the Fifth Crusade." Same image action and page; the parent never names it.
            ["ccd140dbf2603734aa323261c2445bec"] = new Evidence("ae1f824fe248d9f4aac7d39ec2e12140", Special, "cc716238-3702-4913-977d-6189665672b7",
                image: "f96ad5fa9c59d7549adff4c90f0703ab", degradeOnRefusal: false),
            // Camellia, Epilogues/BookPage_0347 (CompanionInParty Camelia_Companion, dead allowed, Ex not): her departure slides.
            // Lead cues (exactly one plays in every native state): Cue_0392 / Cue_0544 (TE with companions, Q3 completed or not),
            // Cue_28 (romance, no sacrifice), Cue_38_master (romance, sacrifice), Cue_0386 (no romance; continues into Cue_0387,
            // the dagger at the Commander's heart). Follow-ons: Cue_16 (Mireya in Varisia, every non-TE state), Cue_0391 (true
            // romance: came back, left again), Cue_0390 (Mireya's lovers; shared text f25c5ed1). The parent mod names none of
            // them, the page or its sequence (aranka-*.cs, RanRomance.dll strings). Every one is warning-only.
            ["84f892d388bba01489145ecd631f23a2"] = new Evidence(CamelliaPage, Companions, "8f73fe38-c791-4d7e-9bd0-553f1f0b07aa",
                image: "df4a5da19a0a64542929dc8409b29bbe", degradeOnRefusal: false),                                             // Cue_0392
            ["c1b1da84c12d3ac448ec65b4342ce77f"] = new Evidence(CamelliaPage, Companions, "d494dcd7-7f4f-4b8b-a8d7-7dcb41998909", degradeOnRefusal: false), // Cue_0544
            ["4ed8e9723359441dae10ad3068d3f2c7"] = new Evidence(CamelliaPage, Companions, "aee7c6bf-fbe1-4288-83e7-3ff3bd4545ad", degradeOnRefusal: false), // Cue_28
            ["5011dfa46fbb0464ab624d78bcfbd483"] = new Evidence(CamelliaPage, Companions, "4dd21f1d-4280-4598-851d-bbc6bbf2f3e4", degradeOnRefusal: false,
                continueTo: new[] { "f23fb3dacf91b3e4b9d3a85937d323bf" }),                                                         // Cue_0386 -> Cue_0387
            ["3617a648c06a45d1807fde65aedafb06"] = new Evidence(CamelliaPage, Companions, "de512bb2-4d4d-4ca2-b20d-9b2d6384c802", degradeOnRefusal: false), // Cue_16
            ["430ce9767d3ede2479ff9d6aee432304"] = new Evidence(CamelliaPage, Companions, "4819461c-331c-4872-a077-49115a7c9ad7", degradeOnRefusal: false), // Cue_0391
            ["e9a183135b8289544a3144dcf8151920"] = new Evidence(CamelliaPage, Companions, "f31377a1-a78e-47f2-bc10-1721eac2f9c1", degradeOnRefusal: false), // Cue_0390
            // Wenduag, BookPage_0349 Cue_0580 (TE with companions, her Q3 not done): "Wenduag refused to ascend with the Commander."
            // RanRomance's AranEpil replaces its second condition (etude 6eddba95 not playing); the checker object, OnShow and Continue
            // are untouched, and the edit wraps whatever checker the cue has. Warning-only (engine queue 7b).
            ["4bb3706172f1ed54ca11db96254c4638"] = new Evidence("223fd069ee25c784db2df011adbf10f8", Companions, "7d53ebcc-5fe2-4066-b52f-eb54fa081512",
                degradeOnRefusal: false),
            // Galfrey (engine-q2 item 5): Epilogues/CueSequence_Queen bb9d36fd, BookPage_0255 Cue_0259 and BookPage_0258 Cue_0502
            // (GalfreyDead Playing; one shared text e61f5ab8, "Queen Galfrey died leaving no direct heir..."). ShowOnce false, no
            // OnShow/OnStop, answers, continuation or components. The parent mod names neither cue, page nor the sequence
            // (aranka-*.cs, aranka-native.json, every Mods DLL's strings, checked 2026-10-03). Warning-only.
            ["f5906acda82efd5468cb72aff2e68f7e"] = new Evidence("6c50623b48ba8204686e2e426ac00425", QueenSequence, "e61f5ab8-ec4c-439f-b035-802558deebe0",
                degradeOnRefusal: false),                                                                                        // Cue_0259
            ["becde70692b74ab4eba1d0cf82d2958f"] = new Evidence("d9cc48a31f994c64f88c5dec322805a4", QueenSequence, "e61f5ab8-ec4c-439f-b035-802558deebe0",
                degradeOnRefusal: false),                                                                                        // Cue_0502
            // E14i: Areelu's afterlogue (World/Dialogs/Epilogues_afterlogues, a Common dialog, not a book page). Cue_0001 lists, Strategy
            // First: Cue_0002, Cue_28, Cue_0003, Cue_0006, Cue_0004, Cue_29, Cue_0005; each continues into Cue_0007 (her account to
            // Pharasma), which a replacement keeps. Cue_0004 (not redeemed, not dead): the cottage. Cue_0005 (the fallback): "my life
            // ended along with it". The parent mod names none of them (aranka-*.cs, RanRomance.dll strings). Warning-only.
            ["825786e8c5db4511ae30950bb286f0e9"] = new Evidence("", "", "cd04e9ab-c34b-49ce-b0a7-25f064571101", degradeOnRefusal: false,
                continueTo: new[] { AfterlogueAccount }, parent: AfterlogueFirst, dialog: AfterlogueDialog),                         // Cue_0004
            ["1b53c189b767412f921b8294b980a51c"] = new Evidence("", "", "102a4671-6e9d-45b6-a801-32d1706c9698", degradeOnRefusal: false,
                continueTo: new[] { AfterlogueAccount }, parent: AfterlogueFirst, dialog: AfterlogueDialog),                         // Cue_0005
            // E14i on non-epilogue dialog cues (engine queue 9a, 8c). Neither cue, parent nor dialog is named by the parent mod. Warning-only.
            // Devarra: c3/IvorySanctum/DragonEggs/Cue_0007 ("...most likely laid by the dragon you killed."), reached from Answer_0004
            // [Examine the eggs] (NextCue, First); no OnShow/OnStop; its answer list b265afc1 is kept by the replacement.
            ["164c14743ee768f409a04f93a040e678"] = new Evidence("", "", "8e520736-4eaa-4077-aea9-6e4b9a05e854", degradeOnRefusal: false,
                parent: "2330b54637738fe4fb92b6cd80eb68f7", dialog: "63f11843f40edd54795fcc0af3f6a20e", answers: new[] { "b265afc1afe5a4241b1d5d42a4148e75" }),
            // Kiana: Seelah Q3 ElandKianaAftermath/Cue_0001 ("Elan and Kiana fall into each other's arms"), the dialog's FirstCue,
            // continuing into Cue_0002 (Seelah: "Let's give them some space."), which the replacement keeps.
            ["81109ea8fb20dbc478cf67116740f4a1"] = new Evidence("", "", "b261aab4-14ff-41e7-bd72-21aeeab7df44", degradeOnRefusal: false,
                continueTo: new[] { "3f8b3b4fbd6d18d44b91a34c88e2208a" }, parent: "27bc5f6c94108a446b8273800f7da48b", dialog: "27bc5f6c94108a446b8273800f7da48b"),
            // Kiana (engine queue 6b): Seelah Q3 JewelerFinal/Cue_0051 (Seelah pours the bowl of soul-gems into a pouch: "We have the
            // souls..."), reached from Cue_0048, Cue_0049 and Cue_0050 (each Continue First, only it). OnShow plays Seelah_Takes_Jewels;
            // OnStop completes FindSoulGems and Add_JewelerEnd, gives ReturnSouls, completes JewelerHideout and starts PuzzleInHideout.
            // The replacement keeps all of it. Neither the cue, its parents nor the dialog is named by the parent mod. Warning-only.
            ["4255f49c18c69aa4ab4d5582d0b6f39e"] = new Evidence("", "", "8e4494ff-5209-44e1-9e80-98a8b9d2a6a9", degradeOnRefusal: false,
                parent: "800706e8e47847f4e88e2c3c586706de", dialog: "fa5e885aaa9840f419939176d38d176b",
                alsoParents: new[] { "fa5589359feaf8b46a1528ee2257e798", "532171260ae3b3546971f72a488e41f3" },
                onShow: new[] { "PlayCutscene:ec848cfc4af0adc4bac665139ed0ce0b" },
                onStop: new[] { "SetObjectiveStatus:83527eddea019674cb123a6a52bdf169", "SetObjectiveStatus:e12c3a03f692c6e428540247d182f59a",
                    "GiveObjective:5b1e04caadc42114281d29db76c19c4f", "CompleteEtude:392fd757d64a8b549bb8be47b37f0ed8",
                    "StartEtude:371fabce16975d34f87a4ae783bcaef4" }),

            // Engine-q4: StoryTeller_MainDialogue/Cue_0785, Answer_0784. Its answer list stays native.
            ["ca71b79bc9a45b741bcc6599ef017fe7"] = new Evidence("", "", "da750b86-b8b0-4a2f-a6d4-fea3512327b0", degradeOnRefusal: false,
                parent: "fd39fd84212de2047b6b887c9a9cf28e", dialog: "bf328bcec67a5014f9a56ee6220f3bcc", answers: new[] { "33501a1edc26b2c4285096b9214c5414" }),
            // AirAdventures/BookPage_0435/Cue_0482: a standalone adventure page, not an epilogue sequence.
            // The authored rescue changes the account, while TumberdDead still starts from the selected cue's OnStop.
            ["dbec675b71e9d5f4d96055f4bb31762e"] = new Evidence("b8d5d14d96bedab44873aa0520304e73", "", "b5c3d293-f547-4848-895b-03b2bdba5a95",
                degradeOnRefusal: false, onStop: new[] { "StartEtude:90f2e0f1cdc263b41b2e625bf228b226" },
                onStopSignature: "StartEtude:90f2e0f1cdc263b41b2e625bf228b226:False:True"),

            // eng7-f6a begin: extracted graft and returned Beth; preserve every native action/continuation.
            ["5b567bdd747e497cb9f6984b1ca1dfc8"] = new Evidence("", "", "7e3fd30b-9eed-4980-8fd9-1af519d90b99", degradeOnRefusal: false,
                parent: "57e18f5158904030a84a772fb361ceb4", dialog: "57e18f5158904030a84a772fb361ceb4",
                continueTo: new[] { "0fd42edf36604d5fa9563711dc124aca", "5afdbd2e61264e8fa227fd153bf21efb", "aa857d545e124ce9a5148221e07194b9", "2a4aab21bd184c91a39cdde39b3f3b88", "825786e8c5db4511ae30950bb286f0e9", "172325d4df134fdd98e831b93e6d857c", "1b53c189b767412f921b8294b980a51c" }),
            ["a9510daab8a04163933d9ecaeffac563"] = new Evidence("", "", "ea881b36-bb48-4232-9787-0491c91cb01e", degradeOnRefusal: false,
                parent: "71d8a418ce148c647af24e7344cf6497", dialog: "e3fcab126b91a414b821f7390d23b40d", alsoParents: Array.Empty<string>(),
                answers: new[] { "04659d8a1ca2a0a438f655c63ceedc3a" },
                onShow: new[] { "Conditional", "Conditional" }),
            ["f8d2b851faecddf448fe18db41e17120"] = new Evidence("", "", "59491c63-89e0-4924-ba8b-b89d7bd8e9b1", degradeOnRefusal: false,
                parent: "5127f768a916c4a449992d5240e2f35a", dialog: "e3fcab126b91a414b821f7390d23b40d", alsoParents: Array.Empty<string>(),
                continueTo: new[] { "7488e96d702143f4db013dae875b84aa" }),
            ["1c8a6796436a7164fa9d63ec79e0395a"] = new Evidence("", "", "2dd1fdaf-2faf-4af3-b5d5-565064e2b599", degradeOnRefusal: false,
                parent: "71ebf92472f64ff478674e5beb142a07", dialog: "e3fcab126b91a414b821f7390d23b40d", alsoParents: Array.Empty<string>(),
                continueTo: new[] { "7488e96d702143f4db013dae875b84aa" }),
            ["0fa64f1d24f706d41b09dee83acf621d"] = new Evidence("", "", "06df2f80-e5b5-44fb-8e3b-46355ecef58a", degradeOnRefusal: false,
                parent: "91c5eca80c8779c4a8bd5754f5533cad", dialog: "f125dc501dc6e984385332e67f324f01",
                continueTo: new[] { "b4f0abc3dd93ab04f9517079fca09790", "8a50fd9c430a80c498da5c09366ff5fc" }),
            ["ec1219cf3a664baab8987200e0fe1aa7"] = new Evidence("", "", "f0c8aaa0-bdc0-468a-9301-9815c5ac52c0", degradeOnRefusal: false,
                parent: "97efeec1d2aa45a4cab6111d14767825", dialog: "de4cc2dd71694b842be37b75d1705b83", alsoParents: Array.Empty<string>(),
                continueTo: new[] { "922db7269f6420f419d64ae5f119cac8" }),
            // eng7-f6a end

            // Engine-q3: both aftermath answers and all Arsinoe/Seelah siblings, verified in blueprints.zip.
            ["a819e8c85ef23324bb0d8117bb9d7df3"] = new Evidence("", "", "1aef0e95-dc1e-49fa-9852-3fba13bd5e20", degradeOnRefusal: false,
                parent: "245ec8482e1f37b4a8702e54430c5aa7", dialog: "27bc5f6c94108a446b8273800f7da48b", continueTo: new[] { "716683517058beb4ead374bd16b22ff0" }),
            ["df45181e1968f26459f9e8bc2b995a34"] = new Evidence("", "", "0c8edca3-4bab-4535-a37b-ea3d3186213b", degradeOnRefusal: false,
                parent: "245ec8482e1f37b4a8702e54430c5aa7", dialog: "27bc5f6c94108a446b8273800f7da48b", continueTo: new[] { "0e50ec24099196a42b7089ffecdc46b2" }),
            ["0e50ec24099196a42b7089ffecdc46b2"] = new Evidence("", "", "0568c8c8-7e85-4fc3-ba62-309d2bebee00", degradeOnRefusal: false,
                parent: "df45181e1968f26459f9e8bc2b995a34", dialog: "27bc5f6c94108a446b8273800f7da48b", continueTo: new[] { "de9d02036b213594fa780c6025f14004" }, alsoParents: Array.Empty<string>()),
            ["4cd264ce0432bb94a8e80a551190150d"] = new Evidence("", "", "b873d838-c522-4d2f-83e0-b017070b6102", degradeOnRefusal: false,
                parent: "f575d21b1fabec74da1e54484573206b", dialog: "27bc5f6c94108a446b8273800f7da48b", continueTo: new[] { "f6c3d20a92890d84c9020d37d56cc75b" }, alsoParents: Array.Empty<string>()),
            ["73815b731281fdc47bbc59aba42b2126"] = new Evidence("", "", "afe4a854-e6c9-442f-8755-cc08e4fd140c", degradeOnRefusal: false,
                parent: "af455979c98c7484c9e74360b4645c62", dialog: "ff5c54635748e334990879498eb5429b", continueTo: new[] { "e9a5a4c03ea016f47b29d91b2ff3a00c" }, alsoParents: new[] { "5f8060efbd1909c4c92fb77036909d2c", "b34bbc351cd28354fb832e451ac0f8e8", "f462d972dad84fa43b98c2399eb4ff17", "6a8058648f4937d42ad846c811dc6c69" }, onShow: new[] { "PlayCutscene:a4b3b03e1d0e1b64db85061f7f53ecd0" }),
            ["e9a5a4c03ea016f47b29d91b2ff3a00c"] = new Evidence("", "", "6ba1cb04-8e0b-40c5-ac6d-6cf64ff0e094", degradeOnRefusal: false,
                parent: "73815b731281fdc47bbc59aba42b2126", dialog: "ff5c54635748e334990879498eb5429b", continueTo: new[] { "2b133bf7ac66d6241a69a53dce2bf05f" }, alsoParents: Array.Empty<string>()),
            ["2b133bf7ac66d6241a69a53dce2bf05f"] = new Evidence("", "", "c2e4632d-2c47-43cf-bebb-0f8dbbab495b", degradeOnRefusal: false,
                parent: "e9a5a4c03ea016f47b29d91b2ff3a00c", dialog: "ff5c54635748e334990879498eb5429b", continueTo: new[] { "b3e6076282402a1489b6f226567cf8fa" }, alsoParents: Array.Empty<string>()),
            ["b3e6076282402a1489b6f226567cf8fa"] = new Evidence("", "", "3cb6cfc5-ab5e-4ddb-a7d1-8ce3775b987f", degradeOnRefusal: false,
                parent: "2b133bf7ac66d6241a69a53dce2bf05f", dialog: "ff5c54635748e334990879498eb5429b", continueTo: new[] { "aeccec94d6e3246488d7f13577a8380d" }, alsoParents: Array.Empty<string>()),
            ["aeccec94d6e3246488d7f13577a8380d"] = new Evidence("", "", "58ee4b07-0488-4fab-a286-d50f786fe135", degradeOnRefusal: false,
                parent: "b3e6076282402a1489b6f226567cf8fa", dialog: "ff5c54635748e334990879498eb5429b", alsoParents: Array.Empty<string>(), onStop: new[] { "PlayCutscene:fef1b52002b9af642a8e5169802c3b68", "Conditional", "Conditional", "Conditional" }),
        };

        // E14i: a reviewed action's shape, "Type:guid" (the first blueprint reference the action holds), or the type alone.
        public static string ActionShape(GameAction? action)
        {
            if (action == null) return "null";
            for (var type = action.GetType(); type != null && type != typeof(object); type = type.BaseType)
                foreach (var field in type.GetFields(BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.DeclaredOnly))
                    if (typeof(BlueprintReferenceBase).IsAssignableFrom(field.FieldType) && field.GetValue(action) is BlueprintReferenceBase reference)
                        return action.GetType().Name + ":" + reference.Guid.ToString().Replace("-", "").ToLowerInvariant();
            return action.GetType().Name;
        }

        private static bool ActionsReviewed(ActionList? list, string[]? reviewed) => list?.Actions != null
            && list.Actions.Select(ActionShape).SequenceEqual(reviewed ?? Array.Empty<string>(), StringComparer.Ordinal);

        public static string[] AlsoParentsOf(string cueId) => Reviewed.TryGetValue(cueId, out var evidence) && evidence.AlsoParents != null
            ? evidence.AlsoParents : Array.Empty<string>();
        public const string AfterlogueDialog = "57e18f5158904030a84a772fb361ceb4";   // Epilogues_afterlogues_dialogue
        public const string AfterlogueFirst = "5b567bdd747e497cb9f6984b1ca1dfc8";    // Epilogues_afterlogues/Cue_0001
        public const string AfterlogueAccount = "f5e9e257be4241108316b2c0da0dff4b";  // Epilogues_afterlogues/Cue_0007
        public const string CamelliaPage = "503164ff04ac64543ba42561ea9f970f";   // Epilogues/BookPage_0347

        public static bool DegradesOnRefusal(string cueId) => !Reviewed.TryGetValue(cueId, out var evidence) || evidence.DegradeOnRefusal;

        public sealed class Plan
        {
            internal string CueId = "";
            internal NativeEpilogueEditSpec Spec = null!;
            internal int Variant;
            internal BlueprintCue Original = null!;
            internal BlueprintBookPage Page = null!;
            internal SimpleBlueprint? ParentCue;   // E14i: the cue / answer / dialog whose selection holds the original (Page is then null)
            internal SimpleBlueprint[] AlsoParents = Array.Empty<SimpleBlueprint>();   // E14i: further parents (Evidence.AlsoParents)
            internal BlueprintCue Replacement = null!;
            public ConditionsChecker OriginalChecker = null!;
        }

        // The ordered variants of one native cue. The group selects nothing until Enable() (every variant attached), so a
        // partial attachment never hides the native cue or lets a later fallback variant stand in for an earlier one.
        public sealed class Group
        {
            private readonly NativeEpilogueVariant[] variants;
            private readonly Func<Snapshot?> observe;
            private readonly Story? story;          // E14d delivery: with the story, a variant also needs its scene available
            private readonly Scene?[] scenes;
            private bool enabled;
            public Group(NativeEpilogueEditSpec spec, Func<Snapshot?> observe, Story? story = null)
            {
                variants = Rules.EditVariants(spec);
                this.observe = observe;
                this.story = story;
                scenes = story == null ? Array.Empty<Scene?>() : Rules.EditScenes(story, variants);
            }
            public int Count => variants.Length;
            public bool Enabled => enabled;
            public void Enable() => enabled = true;
            public int Selected()
            {
                if (!enabled) return -1;
                var state = observe();
                return state == null ? -1 : story == null ? Rules.SelectNativeEditVariant(variants, state)
                    : Rules.SelectNativeEditVariant(story, variants, scenes, state);
            }
        }

        private static readonly FieldInfo? ImageField = typeof(ChangeBookEventImage).GetField("m_Image",
            BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.Public);

        public static string? ImageOf(GameAction? action) => action is ChangeBookEventImage change
            ? (ImageField?.GetValue(change) as WeakResourceLink)?.AssetId : null;

        // Phase 1: the native evidence must match exactly, or the edit is refused (the caller degrades the relationships only
        // when the evidence says so; otherwise the native cue plays).
        public static string? Check(string cueId, NativeEpilogueEditSpec spec, Func<string, SimpleBlueprint?> resolve, BlueprintCueSequence? aeon)
        {
            if (Reviewed.TryGetValue(cueId, out var reviewed) && reviewed.Image == null && Rules.EditVariants(spec).Any(variant => variant.KeepNativeImage))
                return "a variant keeps a native image the reviewed cue does not have";
            if (!string.IsNullOrEmpty(spec.Parent) || !string.IsNullOrEmpty(spec.Dialog) || reviewed.Parent != null)
                return CheckInDialog(cueId, spec, resolve);
            return CheckEvidence(cueId, spec.Page, spec.Sequence, spec.Key, resolve, aeon);
        }

        // E14i: a common-dialog cue. The parent continues into it exactly once (Strategy First), the dialog opens on the parent,
        // and the cue has the reviewed shape: no OnShow, OnStop, answers or components, and exactly its reviewed continuation.
        private static string? CheckInDialog(string cueId, NativeEpilogueEditSpec spec, Func<string, SimpleBlueprint?> resolve)
        {
            if (!Reviewed.TryGetValue(cueId, out var evidence) || evidence.Parent == null || evidence.Parent != spec.Parent
                || evidence.Dialog != spec.Dialog || evidence.Key != spec.Key || !string.IsNullOrEmpty(spec.Page) || !string.IsNullOrEmpty(spec.Sequence))
                return "not a reviewed native dialog cue";
            if (!(resolve(cueId) is BlueprintCue cue)) return "cue missing";
            var parent = resolve(evidence.Parent);
            var selection = ParentSelection(parent);
            if (selection == null) return "parent cue, answer or dialog missing";
            if (!(resolve(evidence.Dialog!) is BlueprintDialog dialog)) return "dialog missing";
            if (TextKey(cue.Text) != spec.Key) return "cue text key changed (patch drift)";
            var continued = cue.Continue?.Cues;
            bool continueReviewed = evidence.Continue == null ? continued?.Count == 0
                : continued != null && cue.Continue!.Strategy == Kingmaker.DialogSystem.Strategy.First
                    && continued.Select(reference => reference?.Guid).SequenceEqual(evidence.Continue.Select(id => (BlueprintGuid?)BlueprintGuid.Parse(id)));
            if (cue.ShowOnce || cue.ShowOnceCurrentDialog || cue.Conditions == null || cue.ComponentsArray.Length != 0 || !ActionsReviewed(cue.OnShow, evidence.OnShow)
                || !ActionsReviewed(cue.OnStop, evidence.OnStop)
                || evidence.OnStopSignature != null && NativeQ3Recovery.Shape(cue.OnStop) != evidence.OnStopSignature
                || !continueReviewed || cue.Answers == null
                || !cue.Answers.Select(reference => reference?.Guid).SequenceEqual((evidence.Answers ?? Array.Empty<string>()).Select(id => (BlueprintGuid?)BlueprintGuid.Parse(id))))
                return "cue behavior differs from the reviewed policy";
            if (selection.Cues == null || selection.Strategy != Kingmaker.DialogSystem.Strategy.First
                || selection.Cues.Count(reference => reference?.Guid == cue.AssetGuid) != 1)
                return "parent no longer leads First into the cue exactly once";
            // Further parents (a mid-dialog cue): each also leads First into the cue exactly once.
            foreach (var also in evidence.AlsoParents ?? Array.Empty<string>())
            {
                var alsoSelection = ParentSelection(resolve(also));
                if (alsoSelection?.Cues == null || alsoSelection.Strategy != Kingmaker.DialogSystem.Strategy.First
                    || alsoSelection.Cues.Count(reference => reference?.Guid == cue.AssetGuid) != 1)
                    return "a further parent no longer leads First into the cue exactly once";
            }
            // A parent cue must open the dialog (unless the cue sits mid-dialog with further parents); a parent dialog must be the
            // dialog; a parent answer is reviewed by its own NextCue.
            if (parent is BlueprintCue && evidence.AlsoParents == null && (dialog.FirstCue?.Cues == null || dialog.FirstCue.Cues.Count(reference => reference?.Guid == parent.AssetGuid) != 1))
                return "dialog no longer opens on the parent cue";
            if (parent is BlueprintDialog && !ReferenceEquals(parent, dialog)) return "parent dialog is not the reviewed dialog";
            return null;
        }

        // E14i: the selection that lists a dialog cue: a cue's Continue, an answer's NextCue or a dialog's FirstCue.
        public static Kingmaker.DialogSystem.CueSelection? ParentSelection(SimpleBlueprint? parent) => parent switch
        {
            BlueprintCue cue => cue.Continue,
            BlueprintAnswer answer => answer.NextCue,
            BlueprintDialog dialog => dialog.FirstCue,
            _ => null,
        };

        // E14d extension: a suppression is checked against the same reviewed evidence (it has no variants).
        public static string? Check(string cueId, NativeEpilogueSuppressionSpec spec, Func<string, SimpleBlueprint?> resolve, BlueprintCueSequence? aeon)
            => CheckEvidence(cueId, spec.Page, spec.Sequence, spec.Key, resolve, aeon);

        // A cue's text key: its own, or (a shared string, e.g. Cue_0390) the shared asset's. LocalizedString.Key is m_Key only.
        public static string? TextKey(Kingmaker.Localization.LocalizedString? text) =>
            text == null ? null : !string.IsNullOrEmpty(text.Key) ? text.Key : text.Shared?.String?.Key;

        private static string? CheckEvidence(string cueId, string pageId, string sequenceId, string key, Func<string, SimpleBlueprint?> resolve,
            BlueprintCueSequence? aeon)
        {
            if (!Reviewed.TryGetValue(cueId, out var evidence) || evidence.Page != pageId || evidence.Sequence != sequenceId || evidence.Key != key)
                return "not a reviewed native cue";
            if (!(resolve(cueId) is BlueprintCue cue)) return "cue missing";
            if (!(resolve(pageId) is BlueprintBookPage page)) return "page missing";
            var sequence = string.IsNullOrEmpty(sequenceId) ? null : resolve(sequenceId) as BlueprintCueSequence;
            if (!string.IsNullOrEmpty(sequenceId) && sequence == null) return "sequence missing";
            if (TextKey(cue.Text) != key) return "cue text key changed (patch drift)";
            var onShow = cue.OnShow?.Actions;
            bool onShowReviewed = evidence.Image == null ? onShow?.Length == 0
                : onShow?.Length == 1 && ImageOf(onShow[0]) == evidence.Image;
            var continued = cue.Continue?.Cues;
            bool continueReviewed = (evidence.Continue == null ? continued?.Count == 0
                : continued != null && cue.Continue!.Strategy == Kingmaker.DialogSystem.Strategy.First
                    && continued.Select(reference => reference?.Guid).SequenceEqual(evidence.Continue.Select(id => (BlueprintGuid?)BlueprintGuid.Parse(id))))
                || evidence.ParentContinue != null && continued != null && cue.Continue!.Strategy == Kingmaker.DialogSystem.Strategy.First
                    && continued.Select(reference => reference?.Guid).SequenceEqual(evidence.ParentContinue.Select(id => (BlueprintGuid?)BlueprintGuid.Parse(id)));
            if (cue.ShowOnce || cue.ShowOnceCurrentDialog || cue.Conditions == null || cue.ComponentsArray.Length != 0
                || !onShowReviewed || !ActionsReviewed(cue.OnStop, evidence.OnStop)
                || evidence.OnStopSignature != null && NativeQ3Recovery.Shape(cue.OnStop) != evidence.OnStopSignature
                || !continueReviewed || cue.Answers?.Count != 0)
                return "cue behavior differs from the reviewed policy";
            if (page.Cues.Count(reference => reference.Guid == cue.AssetGuid) != 1) return "cue is not exactly once on its page";
            if (sequence != null && sequence.Cues.Count(reference => reference.Guid == page.AssetGuid) != 1) return "page is not exactly once in its sequence";
            if (aeon != null && aeon.Cues.Any(reference => reference.Guid == page.AssetGuid)) return "page is in the Aeon sequence";
            return null;
        }

        // Phase 2 (registration): the replacement cue carries the native cue's presentation and a combined checker. A variant
        // that keeps the native image runs the native cue's own reviewed OnShow actions; any other shows the page's picture.
        // A reviewed OnStop is shared intact so an adventure page keeps its native outcome.
        public static Plan Prepare(string cueId, NativeEpilogueEditSpec spec, BlueprintCue original, BlueprintBookPage page, BlueprintCue replacement,
            Func<bool> replacementApplies, int variant = 0)
        {
            var variants = Rules.EditVariants(spec);
            replacement.Speaker = original.Speaker;
            replacement.TurnSpeaker = original.TurnSpeaker;
            replacement.ShowOnce = false;
            replacement.ShowOnceCurrentDialog = false;
            replacement.OnShow = variants[variant].KeepNativeImage && original.OnShow?.Actions != null
                ? new ActionList { Actions = original.OnShow.Actions.ToArray() }
                : new ActionList { Actions = Array.Empty<GameAction>() };
            replacement.OnStop = Reviewed.TryGetValue(cueId, out var stopEvidence) && stopEvidence.OnStop != null && original.OnStop?.Actions != null
                ? original.OnStop : new ActionList { Actions = Array.Empty<GameAction>() };
            // A cue the parent mod continues (ParentContinue) keeps its continuation under the replacement; any other never continues.
            replacement.Continue = Reviewed.TryGetValue(cueId, out var reviewed) && reviewed.ParentContinue != null && original.Continue?.Cues != null
                ? new Kingmaker.DialogSystem.CueSelection { Cues = original.Continue.Cues.ToList(), Strategy = original.Continue.Strategy }
                : new Kingmaker.DialogSystem.CueSelection { Cues = new List<BlueprintCueBaseReference>() };
            replacement.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] {
                new Applies { Original = original.Conditions, ReplacementApplies = replacementApplies } } };
            return new Plan { CueId = cueId, Spec = spec, Variant = variant, Original = original, Page = page, Replacement = replacement,
                OriginalChecker = original.Conditions };
        }

        // E14i phase 2: a replacement for a common-dialog cue speaks as the original (speaker, listener, animation) and keeps its
        // reviewed continuation, so the dialog goes on exactly as it would have (Cue_0007 and Pharasma's verdict).
        public static Plan PrepareInDialog(string cueId, NativeEpilogueEditSpec spec, BlueprintCue original, SimpleBlueprint parent, BlueprintCue replacement,
            Func<bool> replacementApplies, int variant = 0, IReadOnlyList<SimpleBlueprint>? alsoParents = null)
        {
            replacement.Speaker = original.Speaker;
            replacement.TurnSpeaker = original.TurnSpeaker;
            replacement.Animation = original.Animation;
            ListenerField?.SetValue(replacement, ListenerField.GetValue(original));
            replacement.ShowOnce = false;
            replacement.ShowOnceCurrentDialog = false;
            // Reviewed OnShow / OnStop (Cue_0051's cutscene and quest steps) run from whichever of the two cues plays.
            Reviewed.TryGetValue(cueId, out var reviewed);
            replacement.OnShow = new ActionList { Actions = reviewed.OnShow != null && original.OnShow?.Actions != null ? original.OnShow.Actions.ToArray() : Array.Empty<GameAction>() };
            replacement.OnStop = reviewed.OnStop != null && original.OnStop?.Actions != null
                ? original.OnStop : new ActionList { Actions = Array.Empty<GameAction>() };
            replacement.Experience = original.Experience;
            replacement.Continue = new Kingmaker.DialogSystem.CueSelection { Cues = original.Continue.Cues.ToList(), Strategy = original.Continue.Strategy };
            // eng7-f6a begin: the introduction is itself the parent of the existing fate edits.
            // Main prepares all cues before attaching children; share this reviewed list so those insertions
            // reach both introductions, including the already-shipped cottage and mortal variants.
            if (cueId == AfterlogueFirst) replacement.Continue.Cues = original.Continue.Cues;
            // eng7-f6a end
            replacement.Answers.Clear();
            replacement.Answers.AddRange(original.Answers);   // the reviewed answer lists: the dialog goes on exactly as it would have
            replacement.Conditions = new ConditionsChecker { Operation = Operation.And, Conditions = new Condition[] {
                new Applies { Original = original.Conditions, ReplacementApplies = replacementApplies } } };
            return new Plan { CueId = cueId, Spec = spec, Variant = variant, Original = original, Page = null!, ParentCue = parent,
                AlsoParents = (alsoParents ?? Array.Empty<SimpleBlueprint>()).ToArray(), Replacement = replacement, OriginalChecker = original.Conditions };
        }

        private static readonly FieldInfo? ListenerField = typeof(BlueprintCue).GetField("m_Listener", BindingFlags.Instance | BindingFlags.NonPublic);

        // Phase 3: insert the replacement before the original and guard the original. Refuses if the page moved meanwhile.
        public static void Attach(Plan plan, BlueprintCueBaseReference replacementReference, Func<bool> replacementApplies)
        {
            Insert(plan, replacementReference);
            ParentEndingGuard.Attach(plan.Original, replacementApplies);
        }

        // Phase 3 for a variant group: each variant goes in right before the original, in variant order, so the page reads
        // v0, v1, ..., original. The original is then guarded once (Guard) by "some attached variant is selected".
        public static void Insert(Plan plan, BlueprintCueBaseReference replacementReference)
        {
            if (plan.ParentCue != null)   // E14i: into each parent's selection, right before the original (Strategy First picks it first)
            {
                var selections = new[] { plan.ParentCue }.Concat(plan.AlsoParents).Select(parent => ParentSelection(parent)?.Cues).ToArray();
                // All parents are checked before any is changed, so a drifted parent leaves every selection as it was.
                if (selections.Any(continued => continued == null || continued.FindIndex(reference => reference.Guid == plan.Original.AssetGuid) < 0
                        || continued.Any(reference => reference.Guid == plan.Replacement.AssetGuid)))
                    throw new InvalidOperationException("Native dialog cue changed before attachment: " + plan.CueId);
                foreach (var continued in selections)
                    continued!.Insert(continued.FindIndex(reference => reference.Guid == plan.Original.AssetGuid), replacementReference);
                return;
            }
            int index = plan.Page.Cues.FindIndex(reference => reference.Guid == plan.Original.AssetGuid);
            if (index < 0 || plan.Page.Cues.Any(reference => reference.Guid == plan.Replacement.AssetGuid))
                throw new InvalidOperationException("Native epilogue page changed before attachment: " + plan.CueId);
            plan.Page.Cues.Insert(index, replacementReference);
        }

        public static void Guard(BlueprintCue original, Func<bool> anySelected) => ParentEndingGuard.Attach(original, anySelected);

        // E14d extension: a suppression only guards the native cue (hidden, with its continuation, while `suppressed` holds).
        public static void Suppress(BlueprintCue original, Func<bool> suppressed) => ParentEndingGuard.Attach(original, suppressed);

        // Phase 3 for one cue's variants (plans in variant order, all of them): guard the original by "a variant is selected"
        // (false while the group is disabled), insert every variant right before it, then enable the group. If an insert
        // throws, the group stays disabled: every inserted variant stays hidden and the native cue plays.
        public static void AttachGroup(Group group, IReadOnlyList<Plan> plans, Func<Plan, BlueprintCueBaseReference> reference)
        {
            if (plans.Count != group.Count || plans.Select((plan, i) => plan.Variant != i).Any(wrong => wrong))
                throw new InvalidOperationException("Native epilogue edit variants are incomplete or out of order: " + plans.FirstOrDefault()?.CueId);
            Guard(plans[0].Original, () => group.Selected() >= 0);
            foreach (var plan in plans) Insert(plan, reference(plan));
            group.Enable();
        }

        public sealed class Applies : Condition
        {
            internal ConditionsChecker? Original;
            internal Func<bool> ReplacementApplies = null!;
            internal Exception? LastObservationError { get; private set; }
            protected override string GetConditionCaption() => "Earned replacement of a native epilogue cue";
            protected override bool CheckCondition()
            {
                bool applies = false;
                LastObservationError = null;
                try { applies = ReplacementApplies(); }
                catch (Exception ex) { LastObservationError = ex; }
                return applies && (Original?.Check() ?? true);
            }
        }
    }
}
