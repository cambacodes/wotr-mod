# Nocticula parent extension audit

Date: 2026-09-26.
Scope: independent read-only inspection of installed RanRomance configuration, its localized Nocticula material, relevant native dialogue and state definitions, and existing project references.
No manuscript, integration, resurrection mechanism, art, or runtime compatibility is approved by this audit.
The proposed additions below are design directions, not existing game powers.

Nocticula already has a short parent route, explicit acceptance of other lovers, optional Laulieh participation, and several ending variants.
The extension should continue those histories rather than replace them with another first meeting.
The strongest specific Trickster connection is her native response to exposing Socothbenoth's scheme.
The hardest concurrent-roster conflict is the quest's treatment of Shamira, not jealousy.

## Evidence inspected

The installed parent DLL is SHA256 `281239B19FF12675D2E8E48CD86B3759C38F6598A93E13F254A044C5E990DB68`.
Its `LocalizedStrings.json` is SHA256 `534D49567F0172193CD78F9C56A7A9A8244021F1701E2EC46F0C04FDBFBBCF3F`.
These match the pins in `reference/art-review/ran-route-word-inventory.json`.

I freshly decompiled `RanRomance.Noct.Main`, all three book configuration classes and their eight page classes, the miscellaneous entry class, `NoctEpil`, four ordinary slide classes, and the Aeon slide.
Temporary evidence is in `C:/Users/Z/AppData/Local/Temp/nocticula-audit-8d261252/`.
Decompiler missing-reference comments are not evidence that the installed game fails to execute the code.
I inspected the resulting configuration expressions; I did not run these blueprints in Unity.

Existing supporting files are `reference/art-review/ran-route-il.json`, `reference/art-review/ran-route-word-inventory.json`, and `reference/canon-review/VarEtudes.cs`.
Native records were read from the installed `blueprints.zip` and `Wrath_Data/StreamingAssets/Localization/enGB.json`.
I searched current story modules and review files and found no implemented Nocticula expansion manuscript to duplicate.
The roster's readme-only status understates the prior word inventory but correctly does not establish an extension.

## Parent entry and durable history

| State or witness | GUID | Actual role |
| --- | --- | --- |
| `RanRomNoctInitial` | `8a28bbd82568486bb757d00a2087a6cf` | Chapter 4 intimacy acceptance, separate from the later active relationship. |
| `RanRomNoctActive` | `18affced672d4c56a52bf6ffc00601b9` | Chapter 5 agreement; play and completion adjust the parent's `RanRomCount`. |
| `RanRomNoctReject` | `761ca3572c1145ebb755032d613bff46` | Explicit parent rejection history. |
| `RanRomNoctLaulStart` | `1da8019a9d6f4313adc18e376e663236` | Earlier Laulieh interest history used by the dream conversation. |
| `RanRomNoctLaulRom` | `9591c34df22b4d518a059cf608255458` | Accepted Laulieh participation in the dream relationship. |
| `RanRomNoctLaulRom2` | `19e5d6f04b9b4483b2e2979baf8736e4` | Asked Nocticula to give Laulieh a chance to leave the Abyss. |
| `ProfaneGift` | `0c1695f4a362f0243a4afcfd1957eb0d` | Native patronage state and a requirement for the parent's dream encounters. |
| `NocticulaDead` | `e581f609dc0f44a481e7e88824ac39da` | Native death state; parent play trigger completes Active and all three Laulieh states. |
| `RanRomNoctConvCount` | `cb77f24e9db24eea9d5c0837fc5cd2b1` | Evidence counter for drawing out her ambition in Book 3. |

Book 1, dialog `a0741b09599b4ef2a9958ddd92dbc022`, is an optional chapter 4 dinner before the airship journey.
The added departure answer `75553c3a93ab4c1a960fa56cbffd3179` requires both the added flirt answer `d7bdf135b13b4e7487aa8f2d566423d5` and native `UsedNocticulaPortal`, flag `e0522649dc8f2fa43808c56caabe5393`.
The parent changes the portal dialog's finish actions to launch its book and retains the original departure answer's actions as the book's finish actions.
Do not re-run that travel sequence as a later introduction.

Accepting the gift at `d56ae76f0c904d76b79eb99dcf3b8571` starts both Initial and native ProfaneGift.
Accepting intimacy when already gifted at `c1656acee3184a4797c5301cbab61da0` starts Initial.
The two explicit refusal answers `e288e6fed05b41b3a9c2f4509a6e5188` and `627074b82173416399ebb3f329e7e1ee` start Reject.
Missing this optional book is different from refusing it.

Book 2, dialog `d171314b3b4b4b32bdd83ec31027a8f2`, is the chapter 5 dream offer.
Its camping encounter is `c6c201b6c23f4c0fa89fc3af5c2deec5`.
The parent registers it from summit cue `5baed9197e5992045bda712cff673343`.
Encounter conditions require ProfaneGift, no NocticulaDead, no completed Lich final quest, no Swarm class, no selected summit answer `f165187fb9d7f9144a00f9ae7f4cd617`, no seen summit cue `2536ce7031d04354fbfb202ffb652a7d`, and no Reject.
The readme summarizes the latter mythic restrictions as no Gold Dragon or Legend.
The exact answer/cue history checks should be preserved rather than replaced by a guessed generic alignment check.
The encounter removes itself when it starts the dialog.

Book 2 agreement `e742f8f2102f438980258d9ae5cdeb40` starts Active.
Agreement including Laulieh, `dd85f9d8961b401f80805a7d27f53221`, starts Active and LaulRom.
These answers have prior question gates in the same book.
Starting the dialog alone is not acceptance, and seeing it is not proof that every offer or question was heard.

Book 3, dialog `207f4d90a08a410985b7f80ba0cb4cee`, is the later dream conversation.
Its encounter `8c8fab5f44504bc0a496cc8de8bde457` additionally requires Active, the parent `RanRomC5MythicCompl` state `f694258862674009bd7dea2091d74bab`, Ember's `EmberQ2_NocticulaPersuasionSuccess` flag `48909f9355f52e14ab3a8748fa3e81a0`, and Book 2 dialog history.
The parent milestone is activated from its own chapter, quest-status, and dialog conditions; it should be read, not reproduced as an invented timer.

Book 3 supports deduction from earlier evidence, including the Hand's concealment, an Aeon question, the Elysian meal, her earlier plans, and her Desna claim.
The relevant answers increment ConvCount and remember actual earlier questions.
The disclosure page accepts a count from 3 through 100 or the specific loyal-servant answer `ca1da0587b7d4870b9e1c421756c0603`.
It also includes hidden DC 40 and DC 50 checks around her performed blush and uncertain feelings.
Do not write a new scene claiming the parent was only linear exposition or promising certainty about love that the parent deliberately leaves uncertain.

Asking that Laulieh be allowed to leave, answer `3bff7e8e5b2e49ad9cb3bb9fbaa8095f`, starts LaulRom2.
The dialog finish completes LaulRom if that answer was not selected.
Rejecting further help at `f0b53340b86b4528b0f55937baa251fc` completes Active, LaulStart, LaulRom, and Initial, then starts Reject.
Completion of native `LauliehVsVellexia`, `3361d03d80744947b6cd1df848aaed46`, also completes all three Laulieh states.
These are material histories, not flags to silently restore for a convenient triad.

## Existing outcomes and ending integration

| Parent outcome | Evidence and scope |
| --- | --- |
| Commander ascends and Nocticula becomes the Redeemer Queen | Slide 1, `e242ee7eee34426688c6ae80c64b3bb7`, requires TE_Final, Ember persuasion, Nocticula alive, Active, and absence of parent Threat and Devil ending states. Its relationship text varies by mythic outcome. |
| Ordinary Redeemer Queen ending with continued secret relationship | Slide 2, `bafc1b22afed4f058f3353b0e89dee77`, requires Active, the actual native redemption cue's conditions, and no player-sacrifice ending. |
| Ascension without the Ember persuasion outcome | Slide 3, `4e630f20b32d4c05bc86ca79c8ae7c15`, requires TE_Final, no persuasion flag, Nocticula alive, and Active. Its relationship rumor receives a hostile response. |
| Nocticula remains ruler, with consort or secret relationship | Slide 4, `c38e993874914cb4907dcf8c0822cc83`, requires Active and no player sacrifice. Native Demon intimacy and parent Demon ending status select its consort variants; the non-Demon variant remains secret. |
| Aeon altered history | Cue `21d688a2c41f448e98a2932cb10c1bbc`, appended to native page `8f5dbea30be280a4f8a5c30a96e0ddd6`, requires Active and supplies a distinct reaction to the changed history. |

These page predicates are not by themselves a complete selection contract.
Their order, show-once behavior, and actions matter because broad predicates overlap.
`NoctEpil` replaces the ordinary pages' OnShow with actions marking all four parent pages seen.
It suppresses native page `18c7bbb3a6f7cdf4e98990b6f02685cf` while Active and has additional conditional integration for the `RanEpilogue` Harmony owner.
Any future alternate ending needs the same full topology and action-preservation audit used for other parent extensions.
This report does not approve reuse of the Minagho mapping for Nocticula.

Slide 1 already includes an optional Arueshalae/Nocticula/Commander relationship.
It depends on parent Azata ending status, native Arueshalae epilogue conditions, companion ascension, completed companion quest, and one of the two finished Arueshalae romance states.
That is an existing narrowly gated outcome, not permission to duplicate it as a new universal scene.
Slide 1 also ties absorption of the Midnight Isles to native `ShamiraKilled`, `dd6731e2cb230694f9c394fa32391ad5`.
Preserving a living Shamira for a concurrent route requires a genuinely different authored political outcome, not retaining this death-dependent claim unchanged.

## Text credit

The pinned inventory reports 168 configured localization keys, 6,265 keyed words, and 6,132 words after normalized duplicate-text removal.
These are branch-inclusive static totals, not one playthrough's reading length.
They include epilogues and repeated or borrowed native material, so 6,132 is only an initial upper ceiling for distinct parent credit before a route-specific audit.
This task did not generate a final per-branch eligible-credit ledger.

Against a 21,000-word project floor, even that ceiling leaves at least 14,868 new distinct words required.
Actual needed new material can be higher after exclusions.
The parent's shorter advertised Nocticula length should not lower the project's full-route standard.
Do not count the same Laulieh or Arueshalae shared scene again as full separate-character credit, or count mutually exclusive parent history as content every new recovery entrant has experienced.

## Grounded Trickster design directions

The native c5 Trickster audience supplies a specific political opening.
In `World/Dialogs/c5/Mythic_Trickster/Nocticula/Cue_0016.jbp`, asset `bb552fe4e21cb874fa3c98c2cc328186`, Nocticula accepts the Commander's disclosure of Socothbenoth's scheme, proposes following the Commander back to confront him, and promises a reward.
The corresponding disclosure answer is `fd4f6c1d6397fa94db7aaf08de7dfeca`.
This is useful evidence of her valuing actionable intelligence and strategic loyalty.
It is not itself romantic acceptance.

In that same audience, `Cue_0015`, asset `7cad8bc19e70de14287f638baa6f1a8e`, permits an attempt on Shamira because she covets Nocticula's throne.
`Cue_0021`, asset `84df3b227f54e3e44888b5bb8585089d`, thanks the Commander after Shamira's death.
Those are different witnesses; do not narrate the killing from permission alone.

For a living, allied Trickster, the continuation can build on a separately negotiated exchange of intelligence, safe access, and leverage over the Council's competing plans.
Nocticula should receive a concrete advantage and retain the ability to refuse the personal relationship.
The Commander can be clever through preparation, discovering a false assumption, or arranging a credible competing offer.
A fourth-wall joke or automatic irresistible aura is unnecessary.
Her continued rule, a dangerous alliance, uncertain attachment, or betrayal can all remain valid outcomes without compulsory redemption.

The native Trickster quest seeks planar essences and can transform the Worldwound into a crossroads.
`SocothBriefing/Cue_0012`, asset `e5a9d6bb7dbe3384eaef95fc05a3ec5c`, explicitly proposes killing Shamira and taking her essence.
For the user's attainable concurrent roster, an alternate living-Shamira solution must be designed before route availability is promised.
Possible authored work is to negotiate an essence contribution or demonstrate another source acceptable to the quest, with political concessions and a real cost.
Neither possibility is proven available by the inspected native script.
Its implementation must actually satisfy the required quest step without setting ShamiraKilled, spawning a duplicate Shamira, or announcing that an unperformed murder occurred.

Native `Shyka_Offer/Cue_0010`, asset `5d6810f1e0eb8204fa4c3211fc603769`, makes different futures depend on whether Shyka's essence is included.
`Cue_0018`, asset `f40e9f3552e43054697aa0eba417dbc7`, says inclusion also makes the Commander one of Shyka.
`Cue_0019`, asset `8999609509acd0342a08bf2714e5a71b`, leaves survival uncertain without it.
These are specific costly interventions, not proof that Trickster can rewrite any person's history or revive anyone without conditions.
A crossroads outcome also conflicts with a simple promise to close the Worldwound, which the parent makes central to Nocticula's bargain.
An authored renegotiation must address the actual threat and her power base rather than silently treating those endings as equivalent.

## Missed entry, refusal, gift loss, and death

A missed optional dinner should use a new chapter-appropriate introduction to the existing dream bargain, without inventing dinner memories.
A missed dream encounter can receive a distinct request or contact opportunity after its exact native eligibility is established.
The parent removes its camping encounter on start, so interruption and dialog-seen history require care.

Explicit rejection needs a new offer with changed circumstances and another choice, not erasure of Reject.
Read the original answer history even if a separate extension state later records a renewed agreement.
For a Trickster who no longer has the gift, the parent dream explanation no longer supplies its established communication mechanism.
Native Threshold `Cue_0013`, asset `5fc9c28384bd9a84c80ba2e038a9e284`, explicitly offers the gift again after rebellion; `Cue_0027`, asset `7010a76297d261c45a3ce4c46044e8a4`, offers it after an earlier refusal.
These establish that a second offer is possible in some native histories, not that every rejected or hostile Commander qualifies.
Their enclosing branch conditions still need a full reachability audit before reuse.
An independently negotiated dream channel without the gift would be authored new magic and must be identified as such.

NocticulaDead is a real lifecycle boundary which also closes the parent's relationship states.
This inspection did not establish a native recoverable body, stored original actor, resurrection action, or pre-existing return event for Nocticula.
A dead-history Trickster route therefore remains an experimental recovery requirement.
It needs separate soul/body and actor-provenance research, a story mechanism, and return verification before romantic contact can resume.
Keeping her alive through an earlier alternate political branch is the more directly grounded first implementation.
It does not by itself fulfill support for saves where she is already dead.

## Concurrent relationships and verification requirements

Parent `RanRomNoctBook02Page002Cue0015.Text` explicitly accepts other lovers.
The continuation should preserve that attitude and not add a jealousy lock for unrelated romances.
The parent already offers Laulieh participation and keeps its history separate.
Laulieh's service and the Commander's request are insufficient by themselves to establish a developed mutual attraction between both women; new triad scenes must earn that part through her own participation and choices.
The inspected parent invitation to bring others into dreams is not evidence that every other character agreed.

Native ProfaneGift allows influence over the recipient's mind.
Nocticula's Threshold cue `66248e33df6bf83429bd1336487f9504` explicitly warns that it can stop attempts to act against her will.
This power can remain part of an evil or manipulative relationship, but service, compelled compliance, and freely chosen attraction are different states in the writing and mechanics.
Concurrent romances do not imply concurrent Profane Gifts or require rewriting native patronage mechanics.

Keep the parent's Active lifecycle and RanRomCount bookkeeping intact.
Do not start it repeatedly to represent each new scene, or complete other characters' etudes to permit Nocticula's route.
Preserve non-Trickster restrictions and native death, sacrifice, mythic, and ending consequences.
Trickster exceptions should have their own earned state and clearly authored alternate outcome rather than globally disabling those conditions.

Required next checks are an exact parent-history binding manifest, eligible text-credit ledger, quest-state contract for a living Shamira solution, and a matrix covering initial-only, active, refused, missed, gift-lost, Laulieh variants, death, ascension, sacrifice, and other mythics.
Verify save interruption, rest ordering with other active romances, no duplicated encounters or actors, and no counter corruption.
Run with the installed ToyBox Love Is Free and Jealousy Begone settings and with them off; inspect native and parent relationship outcomes after unrelated romances progress.
Static acceptance of nonexclusivity is not a runtime compatibility test.
No global compatibility claim follows from the parent's readme or this audit.
