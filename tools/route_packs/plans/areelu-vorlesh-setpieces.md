# Areelu Vorlesh — round 2 set pieces

Planning only, 2026-10-06. Relationship ID remains `areelu`; filenames use `areelu-vorlesh`. This sheet and the accompanying brief JSONs are the entire change. Nothing here implements scenes, flags, gates, native overrides, or generated prose. Every proposed situation is **AUTHORED**, not a claim about a native encounter. Explicit slots below contain non-graphic staging briefs and heated-cut defaults; their eventual contents are a separate production step.

## Binding decisions and evidence

Read: POLISH-AGENT-PROMPT steps 1–3; 00-WRITING-GUIDE; all ROUND2-TURNING-POINTS revisions; CANON-PARTNERS-DESIGN; TRICKSTER-RUBRIC; this route's handoff; origin/claude/tp-areelu-vorlesh:tools/route_packs/plans/areelu-vorlesh-tp.md; atlas/turning_points.json and sameness_atlas.md; review1/TRIAGE ARE rows; storylines/areelu_trickster.py and areelu_afterlogue.py; the exported Areelu scenes and shared Areelu entries in development/Story.json, longcon.py and lastcall*.py. Shared files were read only. `rg` is unavailable on this machine; Python and targeted source reads supplied the inventory.

**Atlas reservation wins over the older sheet's proposed reclassification:** `experiment_or_ritual`; Ch6; “Threshold survival-wager conclusion across the hall, notebook still open”; payoff “failed prediction yields chosen company tonight and the unresolved child research tomorrow.” Her pursuit is the response to that failed prediction, not a replacement device. Distinguish Nenio's selective-memory experiment and Shamira's mental disclosure: no memory deletion, mind entry, intoxication, aphrodisiac, magically generated desire, duplicate records, false proof, or purchased acquiescence. Do not edit either uniqueness registry in this task.

**Canon source index**, checked directly in /wrath/blueprints.zip against /wrath/Wrath_Data/StreamingAssets/Localization/enGB.json. Paths below are relative to `World/Dialogs/`; GUIDs identify blueprints, keys identify localized text. Characterization evidence does not establish that every Commander heard a cue.

| Ref | Native evidence and use |
|---|---|
| C1 | `c4/Palace/Audience_Areelu/Cue_0103`, `9e9b0200f3e64964b8996734684b7fa2`, key `6e09b702-753c-4683-83f3-12403f7c9154`: detailed lifelong observation. Answer-list `199a940b97b11664aace4101733cd963`; return `46603da28aa69bf49840cd15040e82f5`. Surveillance supports the entry conflict, never parental eroticism. |
| C2 | `c5/Iz/AreeluIntro/Cue_0024`, `dbea944bb36596d4d99f9b5b8e74e14a`, key `4489282b-48d5-4164-94ef-e95fa17a7fd7`: personal purpose, contempt for praise/reproach. Iz list `09b8d5eb5dae3634d9dc3d8c7bdd6e9d`; return `c000ae3d47250b943953b1bd25333f30`; warning `f4eee511a0c0f9e4cace9e0ced47bfba` remains. |
| C3 | `c5/AreeluLabAgain/AreeluCell/Cue_0008`, `52830ee630aa6ee4dbe8e187367454d5`, key `a489dccb-3632-4ce1-81a0-a324df93333b`: anger at pity and her promise. Cue_0037 `a4b8a109874919c4cba9cef817ec148c`, key `f02e0340-b25b-4287-a6b5-dda9c9a365cc`: one must burn; list `74989c07fc5fd8a42b18b333dc40acc1`; return `3d63aae9686620845acc8be95e490c26`. Cell Areelu is a projection: no bodily intimacy there. |
| C4 | `c6/SecondFloor/AreeluLetsFinalFight/Cue_0021`, `57ec93f6a4eb8c24cadcc4db8e36947c`, key `bd28132f-e15b-4825-929a-7b442115bfc1`: crimson eyes; the current Commander must die to surrender the shared soul; she will retry. Supports the unresolved threat, not a proven separable pair of souls or a successful cure. Native rift list `90861396a1375684eb5bf894bedecff3`; return `c4f9dac3d26416d43b3c1662d07a99c0`. |
| C5 | `c6/SecondFloor/GrandFinal/Cue_0001`, `d309c3051dcba12458a481eb7d5a24c9`, key `c077eb83-7019-4986-bd65-75200f0dbd01`: bleeding, trembling, defiant, defeated creator. List `f56a69dc64a48b14096a557697f43f2a`, existing ReturnToList. Answer_0011 `10e6b2a8c754dae4b81e55ad6d0918b2`, key `60e27138-f9ca-4942-bb1a-c498a5c64586`: Commander punchline. Answer_0055 `91c5eca80c8779c4a8bd5754f5533cad`, key `93856d20-bee8-4b72-a4c2-1bb3b4278f9d`: Areelu sacrifice. Retain existing actual siphon possession, filled-state and collection requirements. |
| C6 | `c4/Palace/Audience_Areelu/Cue_0097`, `c3cdce201fd02f342bbfda40be5f0ed1`, key `497e9570-2b1c-4726-8e11-4838f9a99801`: the wound as her failure. Treatment and ownership are different. Cue_0111 `af6df0ada7cbeb240ad917d70a60eda6`, key `48bc35f3-f699-4afa-80a3-36a174368cf0` has speaker blueprint `cb29621d99b902e4da6f5d232352fbda`: the source identifies this as Lann's line. Do not reuse the handoff's erroneous attribution to Areelu. |
| C7 | `Epilogues_afterlogues/Cue_0004`, `825786e8c5db4511ae30950bb286f0e9`, key `cd04e9ab-c34b-49ce-b0a7-25f064571101`: isolated cottage; Cue_0005 `1b53c189b767412f921b8294b980a51c`, key `102a4671-6e9d-45b6-a801-32d1706c9698`: native death fallback. Keep parent `5b567bdd747e497cb9f6984b1ca1dfc8`, dialogue `57e18f5158904030a84a772fb361ceb4`, and native judgment continuation. Authored replacements must follow actual fate and separation. |

**Source drift matters:** the present checkout still uses `COMMITTED_ANY` containing `late_committed`, lacks the raise's whole-scene extraction prohibition, contains the no-burn paper destruction and fourth-winter first-night wording, and has the H1 wound-page conflict. Do not assume the spec's later implementation notes describe this checkout. Conversely, the audience has already removed the Suture and hunters now buy only three days with the straw decoy: retain those repairs. No new price, score, affection requirement, or reconciliation condition follows from this sheet.

## 1. The observer is answered — entry

**Where/when:** Ch2 Drezen's native disguised-Yaniel exchange (`areelu.early.*`), then Ch4 Nocticula's palace, `areelu.trickster.audience.notes`. **Present:** Commander and disguised/actual Areelu respectively; native audience participants only when actually present. **Risk:** exposing her scrutiny while the Commander still depends on unexplained power and an Abyssal ruler's audience. **Lead-in:** recognizing the mask earns memory; freeing/refusing it retains its native consequences, never attraction.

**Beats:** recognition stops at a knowing exchange, with no flirt aimed at the Yaniel disguise. At the palace the Commander asks for the file; Areelu refuses, reveals only what serves her experiment, and notices where the Commander's conduct diverges from her expectations. Commander can joke, inquire, or return to native business. Her counter-move is to turn questions back on the person demanding access, not to provide a confidential romantic dossier.

**Her decision/payoff:** she chooses continued observation, not sex or commitment. Preserve `notes_told`/actual disclosure recalls. **Carry:** the future lens is a two-way exposure, and neither a courtesy nor a file request produces `committed`, a household invitation, or arrival. No Last Call debt yet. C1; native Long Con lists `e47ef9ec640a1b4488ffb0c6a9983348` / `4ab7a78f96a994446a56a9bc27ac2bfb` remain untouched.

## 2. A wager addressed to smoke — build-up

**Where/when:** Ch5 Iz during her warning; optional lens at the Commander's campaign quarters; laboratory cell after the actual burn cue. **Present:** Commander and Areelu at Iz; only correspondence at the lens; Commander and her projection in the cell. **Risk:** Deskari's trap, the coming final fight, and conceding the personal wound as a stake. **Lead-in:** failed predictions at the palace, or a truthful late first approach when that exchange was skipped.

**Beats:** the Commander offers “neither”; she counters with the wound claim and asks what could be won from her. The lens reveals attention and sleeplessness but no touch through glass. In the cell she holds out smoke; the Commander may shake it, name work, or refuse. Her counter-move is to hold the Commander to the specific words and postpone any real hand until Threshold. Keep crib/promise memories conditional on the actual selected answer/seen cue.

**Her decision/payoff:** she accepts a gamble and correspondence. No diagnostic test here, no potion, no additional isolated event. **Carry:** term.life, named work, late terms and wound cession stay distinct; she remembers a real-hand request only where made. Romance still needs her later affirmative choice. C2–C3; return to the Iz warning and cell exit, not an invented private laboratory visit. No explicit slot in a projection scene.

## 3. The result she cannot reduce to her child — registered turning point

**Where/when:** Ch6 defeated-Areelu list at Threshold, `wager.raised`, followed by the earned survival conclusion. **Present:** Commander and living Areelu; companions do not witness a private night. **Risk:** the rift, her life, the Commander's personal wound, the graft, and the mistake of treating the current Commander as a substitute child. **Lead-in:** native soul revelation, early or late wager, actual terms accepted. C3–C5.

**Beats:** retain her decision in `her_choice`, her bloody handshake/kiss and refusal. A single **diagnostic-only** observation is folded into the existing conclusion, adapting ARE-01/02: she reviews the survival result, checks an observation against the Commander's actual response, and admits the test cannot tell her what her child would have chosen. The Commander can answer as themself, decline to be examined, or ask what she intends next. She closes the notebook herself. No soul surgery, signature separation, child manifestation, compulsion, success flag or test-pass condition. The inference is her changed interpretation of this adult person's choices, not proof that the child's share vanished. Desire is directed at the current independent Commander; no parent/child endearment or sexualized “creation” language.

**Counter-move:** she corrects the Commander's assumption that a failed prediction invalidates her research; she keeps the child problem and her notes. Her affirmative company choice remains separate from agreeing to extraction, surviving, being rescued, or passing this observation. No bargain promises sex. She can say no after accepting survival work.

**Payoff/carry:** her accepted raise earns chosen proximity; later refusal defers intimacy without rewriting the wager. The original fate receipts alone decide mortal/half-demon/ascended presence. Preserve all named work and wound debts; no-burn does not call the burn clause. Paper can burn only under the actual agreed substitution/native destruction, or a separately shown voluntary choice. Do not invent burning as a new intimacy fee. No Shyka echo is allocated to Areelu: no vision, other-life knowledge or page-created desire.

## 4. Across the hall tonight — first-night payoff and branch mornings

**Where/when:** immediate Ch6 survival continuation, in the existing authored lodging across the hall, after treatment and a time cut sufficient for Areelu to be lucid and physically recovered. This is the finale's report-style continuation, not a new native Threshold bedroom or a required post-campaign playable scene. **Present:** Commander and Areelu alone by their own choice. **Risk:** she can live without accepting the offered bed; mortality and unfinished soul work remain. **Lead-in:** set piece 3, actual commitment and actual survival. C4–C6.

**Beats:** append the optional `areelu.trickster.finale.company` continuation for ordinary `survived` / collected `after` histories; she comes across the hall, leaves instruments behind, names her immediate appetite and initiates the kiss. Commander receives her, postpones, or stops. She answers each option; no automatic welcome because a debt was paid. Her counter-move is to reclaim the night from both the file and the Commander's attempt to interpret it as surrender. Default cuts reach bare-skin contact and the initiating motion. Slots COMPANY-M/W below. Morning shows rumpled clothing, her remaining beside the Commander briefly, then taking up the unresolved research herself. She returns later by choice; refusal does not become consummation off-page.

**Existing outcome alternatives, not extra first nights:** H2 `lien_bottled/across` gets BOTTLE; `not_burned/nb_across` gets BRIDGE; `ascended/asc_night` gets ASCENT. Only the selected finale's opportunity plays. Flask is on a safe surface, cork undisturbed: remove the impossible wrist-bearing bottle. H2 morning names fear of losing the living witness and shows a deliberate return. Iomedae-return morning grudgingly acknowledges an intervention she did not build, without claiming a flask; both appointment/rescue histories need accurate text. Ascension morning has equal power and actual postponed work, never the loss of mortal magic. Distinguish a refused night from a later invitation by showing a fresh choice, not diagnosing the refusal.

**Carry:** first night happens once; set piece 5 is return/deepening. Preserve all legacy terminal exits, `continue` identity, refusal targets and outcome mechanics. Shared household/Last Call read existing accepted company and presence, not a kiss/slot/completed-night flag. The longer report becomes an optional recollection sequence with every legacy node still reachable; implementing the shared sequencing requires coordinator authorization if it cannot be done route-locally.

## 5. Somewhere without instruments — returning appetite and household terms

**Where/when:** post-finale report, first suitable quiet evening in already-authored Drezen lodging; an unnamed inn room booked under one of her existing aliases. Its existence and booking are AUTHORED, no assertion of a native inn asset. One small report vignette only. Later the existing fourth-winter `report.participation` night deepens the relationship. **Present:** Commander and Areelu; nobody invented to trigger a discovery. **Risk:** hunters know their connection; she remains dangerous, secretive and free to leave. **Lead-in:** the diagnostic interpretation and a chosen earlier night; where an earlier night was declined, the invitation must not claim consummation.

**Beats:** adapt ARE-06's inn to a return, keeping Threshold as the unique turning point. She picks an alias and a room without apparatus; the Commander asks why here, accepts her invitation or leaves. She refuses to justify appetite as a study. Slot INN carries that privately chosen night; morning she collects her own belongings and returns to the research and the Commander, not a farewell postcard. No new cost/gate. The existing `participation` approaches route to RETURN-M/W after their distinct staging; `notebook` is a third approach to the matching body-state slot, not another act/first night.

**Counter-move:** she retains ownership of her notes, chosen nights and packed escape case. At the existing morning-after proposal she insists on all four actual conditions; Commander accepts, retains separate rooms, closes the door, or disputes the arrangement. Her refused shared-room offer keeps the relationship across the hall, not a forced breakup. ARE-07's separate tables mean child research remains a different purpose; no new child vessel is manufactured.

**Carry:** letters scene admits other romances honestly while she excludes others from the research room. This is her household position, not a partner stance: no share/exclusive/secret flags. Keep her possessive trespass and the Commander's response as drama, no therapy treaty and no demand that other women vanish. Named current residents may answer in shared household content only after coordinator integration. Hunters' next move, existing mortal fever or surviving graft's call, and repeated returns replace tidy domestic reform. No sex during incapacitating fever. A packed case matters later.

## 6. The second notebook — discovery, confrontation and aftermath

**Where/when:** ninth winter and following spring, `report.name` → `report.promise`, at their existing lodging. **Present:** Commander and Areelu, then an envoy only in the already-existing appropriate report event. Optional Targona reaction is a route-local proposed dialogue variant only if actually present and coordinator-owned integration is supplied; never mandatory or another hearing. **Risk:** the current Commander's soul and her child's unfinished claim; private tenderness does not erase her capacity to kill. **Lead-in:** earlier shared soul disclosure, actual room terms, hearing the unnamed child in sleep, ongoing research. C3–C4, C7.

**Beats:** near-discovery is the name in sleep; she wakes and refuses its appropriation. Discovery is the notebook in its binding; the broken hair supplies physical evidence when it is put back. Confrontation is over her written method, not marital betrayal. The Commander can confront, replace the book, take her hand, suggest a petition, or follow the existing burn exits. She owns the purpose and chooses what she will do. Preserve `why`'s frightening threat as a threat, never erotic reassurance. This is not an intimacy slot.

**Counter-move/earned answer:** she takes the petition in her own name and excludes the Commander from its hearing; on keep she postpones the method each day without surrendering it; on burn she leaves with her remembered research. Those are different outcomes, not a new score or reconciliation scheme. Optional ARE-04 adaptation: present Targona contests the captivity/soul implications from her own grievance, Areelu refuses absolution, Commander may hear both or end the exchange. Do not adopt ARE-03's shared defence or ARE-05's new sacrificial assembly.

**Payoff/carry:** file and keep codas explicitly return her to the lodging after her own work; separation ends with her own continuing work elsewhere and letters that do not prove arrival or current cohabitation. Child remains unresolved. Afterlogue retrospection can acknowledge earlier company without asserting lifelong residence after burn. Native judgment remains; authored changes are current-Trickster-only and confined to facts the earned survival explains. Household, Last Call and afterlogue state corrections are ESCALATE where they require shared files.

## Partner applicability and outcomes that must differ

No live or possibly-live partner is documented for Areelu in the binding partner design or the reviewed route/canon evidence. No partner discovery, stance demand or partner move is applicable. Her child, Targona and Pharasma are not sexual rivals. Daeran's existing courtly hand-kiss supplies an independent social reaction, not a new affair or partner. Do not copy Kiana's interruption or add a spouse to fill the template.

| Histories | Required difference |
|---|---|
| Wager-only / accepted raise | Settlement and research only / chosen company available; `late_committed` alone is not acceptance. |
| Requested life / named work | No work substitution / existing paid, collected substitution; no retroactive paper debt. |
| Neither burned / actual substitution burned records | Keep unowed notes / remember the actual loss; subsequent child-notebook burn must not falsely recall another fire. |
| Native death or deliberate execution / exact earned rewrite | No bodily presence / mortal survival only under the existing exact exception. Deliberate kills and user closures stand. |
| Commander unreturned / H2 / Iomedae kept or rescued / shared ascension | Memorial only / sealed flask / outside return without bottle / equal ascended company. |
| H1 / ordinary continuing pull | Corked fate / possible recurring wound; no H1 reopened Worldwound. |
| Intimacy accepted / postponed / refused | Own night / fresh later choice / no assumed act or new free reconciliation. |
| Shared room / separate rooms / closed door | Actual four terms / continued knocking / acknowledge the refused winter before a later invitation. |
| Promise kept / petition filed / research burned | Daily postponement with return / her own pending case with return / departure, no lifetime roof claim. |
| Current Trickster / former Trickster or other path | Only the authorized alternate fate and native rewrites / native fate stands. Historical `trickster.ever` alone cannot authorize a canon change. |

## Slot manifest and cut continuity

These are proposed dedicated nodes, not inserted code. All are optional expansions of a mutually chosen private night. Briefs use the example's tagged format and fields, with traits instead of reusable character quotations, canon facts separated from authored staging, an exact final line, and anatomy variants. They contain no graphic prose. Defaults below remain usable if a slot is empty. The final line of each eventual take is exactly its default cut (tagged `N:` in JSON); after it the specified existing/proposed morning begins. No slot creates flags. New choices append; old night answers and mornings retain their identity. At an existing staging node, append an entry answer to the new slot; keep the legacy Continue and its old morning target intact as the default cut path. The manifest's ingress names placement, not permission to repoint old answers. Newly appended slot nodes return to the same morning. For new company/inn nodes, define both slot and refusal choices at creation.

| Label | Slot ID; ingress → egress | Default heated-cut text |
|---|---|---|
| COMPANY-M | `areelu.trickster.finale.company.explicit.1`; new mortal welcome → new mortal morning | `{n}She draws you onto the bed, her mouth against yours. The lamp burns low beside the closed notebook.{/n}` |
| COMPANY-W | `areelu.trickster.finale.company.explicit.2`; new half-demon welcome → new half-demon morning | `{n}She pulls you close; the violet light above her heart falls across the discarded robe.{/n}` |
| RETURN-M | `areelu.trickster.report.participation.explicit.1`; in_mortal_2 or mortal notebook approach → morning | `{n}She catches your face between her hands and kisses you again. The notebook lies forgotten beside the bed.{/n}` |
| RETURN-W | `areelu.trickster.report.participation.explicit.2`; in_witch_2 or half-demon notebook approach → morning | `{n}Her grip loosens as you draw her close. Her hair hides the lamp from both of you.{/n}` |
| BOTTLE | `areelu.trickster.finale.lien_bottled.explicit.1`; accepted across → morning | `{n}She draws you down beside her. On the washstand, the flask remains sealed.{/n}` |
| BRIDGE | `areelu.trickster.finale.not_burned.explicit.1`; accepted nb_across → nb_morning | `{n}She kisses you hard and pulls you close. The lamp and the closed notebook stay on the floor.{/n}` |
| ASCENT | `areelu.trickster.finale.ascended.explicit.1`; accepted asc_night → asc_morning | `{n}She takes your hand and draws you down beside her. Both names remain on the closed notebook.{/n}` |
| INN | `areelu.trickster.report.inn.explicit.1`; new accepted return-night vignette → its new morning/return | `{n}She catches your sleeve before you can turn toward the lamp and pulls you back into the kiss.{/n}` |

Physical limits: no invented sexual anatomy, hair/eye colors beyond verified crimson eyes, permanent injuries or demonic appendages. Graft removal and later aging are authored consequences, not universal native facts. Retained graft light is current route staging. Any proposed graphic expansion must keep the Commander distinct from her child; desire, survival, treatment, coercion and soul research cannot substitute for each other.

## Ordered round-2 implementation checklist — not executed

1. Reconcile source/export/spec drift and record every existing scene/node/relationship ID, choice index, explicit answer ID and line ending. Keep the current relationship `areelu`. No rename, reorder, deletion or repointing of a legacy answer. Retire only by gating and retain every old target. Keep all ending exits' identity and mechanics.
2. Repair only the older sheet's documented acceptance/term/history classes: replace wager-only romance consumers with actual `areelu.committed`; preserve a nonromantic settlement exit; remove false primed-late `stake_named`; forbid post-collection raises by the whole-scene rule already requested; reconcile actual burn/no-burn and wound ownership. Never add affection, attraction or new payment requirements.
3. Stage set piece 3's single diagnostic observation inside the existing earned conclusion. No new test flag, magical extraction, fee or dependency. Preserve late-entry truths and her yes/no. Current-path bounds for canon rewrites and exact earned death exceptions must be coordinated with native ownership.
4. Append ordinary company opportunity and branch-specific morning in the existing finale continuation. Keep legacy report entry and every report answer reachable. Add dedicated COMPANY slots and heated defaults; keep refusal selectable. H2, Iomedae and ascent nights use their own slots/mornings and actual presence. First-night wording occurs once per history; later invitations do not claim a prior act that was declined.
5. Add the one inn return vignette and adapt participation into deepening; attach RETURN slots without consuming the refused branch. Preserve shared/separate room terms and the packed case. Keep discovery in set piece 6 distinct from appetite; no child retrieval or involuntary operation.
6. Apply the complete heat inventory below by class: scientist tics in courtship, repeated lamp/notebook choreography, premature night cuts, flattened mornings, threatened vulnerability, memorial/return/departure truth. Preserve adequate existing staging rather than adding sex to every tender scene.
7. Coordinator handles shared household, Last Call and native afterlogue dependencies: current presence, conditional visitors, correct personal wound debt, flask outcome, intact wrist, no H1 recurring pull, and no future cohabitation after separation. Route-local future receipts, if needed solely to prevent repeated first-night wording, must use `areelu.trickster.*`; propose none as new requirements. No kiss/rescue/letter-derived arrival or commitment.
8. Static acceptance review: unraised/declined/stake-only has no romantic night/home; accepted raise with actual survival has invitation and refusal; extraction cannot be renegotiated afterward; collected replacement changes only its exact fate; every native-death/Commander-sacrifice combination is accounted for. Test former-Trickster/other-path inertness when implementation is authorized.
9. Review each slot with its body/fate/history variant and morning. Empty default reads coherently; no mode repeats first night; no anatomy assumed; exact final line matches; no new partner or unexplained witness. Verify keep/file/burn and shared/separate/closed-door histories through codas and native afterlogue; no accidental reconciliation.
10. Future implementer runs the authorized generation, strict verifier, relevant Python and Rules/progression checks in their implementation task. This shared-machine planning task runs none of those gates, creates no build/audit artifacts and makes no commit, per the final instruction.

## Escalations, exclusions and risks

- Shared `lastcall_partners.py` / ledger entries: wrong missing wrist, optional Iz memory, reversed “I ceded the Wound,” bottle-state specificity. List these for the coordinator; no shared edits here.
- Shared household/presence and native afterlogue infrastructure: existing E14i story integration is present in source, but runtime correctness cannot be certified by this planning task. Both Iomedae returns and promise separation need accurate existing native continuations. C7 identifies the targets. Do not broadly suppress unrelated native judgment.
- Optional Targona ARE-04 response needs her actual presence and shared owner approval; if no suitable existing host exists, omit rather than create an archive hearing/quest.
- Not adopted: ARE-03 shared defence, rejected ARE-05 sacrifice assembly, blackmailing the woman, divine-proof vessels, addiction diagnosis, new spouse, exclusivity gates, magical affection or echo. An inn alias is an existing escape practice, not another counterfeit-evidence turning point.
- Planning risk: current exported content and the spec describe different revision states. The heat inventory records this checkout, not repaired passages claimed by later notes. No passing rubric score or gameplay gate is claimed.

## Heat audit of existing scenes and nodes

The inventory below covers sensual staging, romantic touch, intimate aftermath and adjacent vulnerability/social reactions in all 58 exported Areelu-owned scenes, with source siblings checked. A quoted passage is an existing anchor, not always a defect: passing rows explicitly retain appropriate heat. Ratings are editorial assessments against WotR's register, not independent rubric scores. **H** = heated situation rewrite, **S** = attach the named slot after staging, **K** = keep the adequate physical beat and repair its situation/continuity if specified. No graphic slot in illness, treatment, grief, coercive research, projection or memorial. Paragraph rows are identified by zero-based `Paragraphs` index.


### areelu.trickster.audience.notes

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| trade | “"You keep notes on me." It is not quite a question. She tilts the mirror toward you as if it might show her the page. "Read me the first entry."” | 86/H | Set piece 1: make surveillance and selective attention carry the exchange; trim portable proofreading/specimen flirt. No bodily intimacy in a public audience. |
| entry | “"Accurate, and useless. You have written down what you saw. You still do not know why I did it." She lowers the mirror. "That ignorance will matter at Threshold."” | 86/H | Set piece 1: make surveillance and selective attention carry the exchange; trim portable proofreading/specimen flirt. No bodily intimacy in a public audience. |
| offer | “"No. You may not have a copy." She lifts the mirror, considers her own reflection in it, and lowers it again. "But I will give you something rarer than my notes. An entry of your own." Sh…” | 86/H | Set piece 1: make surveillance and selective attention carry the exchange; trim portable proofreading/specimen flirt. No bodily intimacy in a public audience. |
| silent | “A gong sounds elsewhere in the palace. Areelu waits until it falls silent. "Nothing? You came all this way to waste an answer? Very well. I will remember that you can keep quiet when it c…” | 86/H | Set piece 1: make surveillance and selective attention carry the exchange; trim portable proofreading/specimen flirt. No bodily intimacy in a public audience. |
| smudged | “Areelu turns the mirror toward the light and wipes its edge with her thumb. "A fault easily corrected. You should bring me more of those." Her gaze returns to you. "Now the real question."” | 86/H | Set piece 1: make surveillance and selective attention carry the exchange; trim portable proofreading/specimen flirt. No bodily intimacy in a public audience. |
| spelled | “"I did not write it down." Her mouth twitches. "I will remember it. Ask your questions before I change my mind about answering them."” | 86/H | Set piece 1: make surveillance and selective attention carry the exchange; trim portable proofreading/specimen flirt. No bodily intimacy in a public audience. |

### areelu.trickster.rivalry.lens

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| window | “"Because it works both ways. When you look, I learn when you are awake, when you are alone, and what makes you put the glass away." The frost briefly hides the hand beyond it. "I have giv…” | 90/H | Set piece 2: keep two-way scrutiny and failed sleep as dangerous attention; remove ornamental hand/frost tics. No projected touch, prior-night claim or affection receipt. |
| keep_looking | “You do not put it away. The frost clears, and forms again, faster, as if the hand on the other side had been waiting.” | 90/H | Set piece 2: keep two-way scrutiny and failed sleep as dangerous attention; remove ornamental hand/frost tics. No projected touch, prior-night claim or affection receipt. |
| slept | “"Accurate." The frost holds the word a long time, as if she were looking at it. "I have not slept properly since the hunters came to my house. Most people who notice that try to kill me f…” | 90/H | Set piece 2: keep two-way scrutiny and failed sleep as dangerous attention; remove ornamental hand/frost tics. No projected touch, prior-night claim or affection receipt. |
| last | “"Sleep." The letters come at once. "You lay on your left side, with one hand under the pillow. I could not see what you were keeping there. You spoke once. I could not make out the word."…” | 90/H | Set piece 2: keep two-way scrutiny and failed sleep as dangerous attention; remove ornamental hand/frost tics. No projected touch, prior-night claim or affection receipt. |

### areelu.trickster.lens.watched

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| face | “The frost clears completely. For one long moment the glass shows you nothing but a desk, a lamp, and the edge of a sleeve. Then the sleeve moves, and the lamp is turned, deliberately, so …” | 90/H | Set piece 2: keep two-way scrutiny and failed sleep as dangerous attention; remove ornamental hand/frost tics. No projected touch, prior-night claim or affection receipt. |
| keep_looking | “You do not put it away. The frost clears, and forms again, faster, as if the hand on the other side had been waiting.” | 90/H | Set piece 2: keep two-way scrutiny and failed sleep as dangerous attention; remove ornamental hand/frost tics. No projected touch, prior-night claim or affection receipt. |
| slept | “"Accurate." The frost holds the word a long time, as if she were looking at it. "I have not slept properly since the hunters came to my house. Most people who notice that try to kill me f…” | 90/H | Set piece 2: keep two-way scrutiny and failed sleep as dangerous attention; remove ornamental hand/frost tics. No projected touch, prior-night claim or affection receipt. |
| last | “"Sleep." The letters come at once. "You lay on your left side, with one hand under the pillow. I could not see what you were keeping there. You spoke once. I could not make out the word."…” | 90/H | Set piece 2: keep two-way scrutiny and failed sleep as dangerous attention; remove ornamental hand/frost tics. No projected touch, prior-night claim or affection receipt. |

### areelu.trickster.wager.struck

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| why_bet | “"No." The answer comes too quickly, and she hears it come too quickly, and her mouth tightens. "Yes. Very well. Yes. Everyone else who has stood in this cell came to kill me, or to beg me…” | 91/K | Set piece 2: smoke-hand contact seals only the wager; keep the physical impossibility and her counter-terms. No sex or commitment earned here. |
| not_war | “"I have not been anything but at war for a hundred years, Commander." The projection looks down at its own hands of smoke. "I do not know what I am like when I am not. Nobody does. I kill…” | 91/K | Set piece 2: smoke-hand contact seals only the wager; keep the physical impossibility and her counter-terms. No sex or commitment earned here. |
| sealed | “For a moment the projection is perfectly still. Then she laughs, once, without any pleasure in it, and the device hums as if it had been struck. "What is left of me. You do not even know …” | 91/K | Set piece 2: smoke-hand contact seals only the wager; keep the physical impossibility and her counter-terms. No sex or commitment earned here. |
| into | “Your hand passes into the projection up to the wrist. There is nothing there: only a faint cold, like putting your hand into a stream in early spring, and the hum of the device in your bo…” | 91/K | Set piece 2: smoke-hand contact seals only the wager; keep the physical impossibility and her counter-terms. No sex or commitment earned here. |

### areelu.trickster.threshold.welcome

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| sleep | “"I have slept badly for a hundred years. You have not improved it." The smile she gives you is thin, and very old. "Be flattered, if it pleases you. It is the last pleasure you will be of…” | 90/H | Keep the confrontation under siege pressure; sleepless attention is not a promise of sex. Her child-purpose remains. |

### areelu.trickster.truth.the_desk

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| wait | “She looks at you. Something in her face that has been held shut for a century moves, very slightly, like a door in a draught. "You will wait." "Everyone else came through the door. The hu…” | 91/K | Retain chosen courtesy and hostility to pity in the demiplane; no tender cure of the child's fate. |
| witch | “Her laugh is short, and dreadful to hear. "They have wanted one since before your crusade had a name." "Very well. If I burn today, I will burn as your wager, Commander, and not as their …” | 91/K | Retain chosen courtesy and hostility to pity in the demiplane; no tender cure of the child's fate. |

### areelu.trickster.rift.odds

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| romantic | “"Then you have been courted badly." Her gaze returns to your chest. "Every hour I spend on you is an hour I do not spend on my child. I resent the expense. I have not yet decided to stop …” | 92/K | Retain frank contradictory desire beside the threat; research and current Commander remain distinct. No sex beside the active rift. |
| feelings | “The violet light throws her shadow between you. "I want you alive when this is over. I had other plans for you. I have not abandoned them." She looks toward the rift. "If you mean to make…” | 92/K | Retain frank contradictory desire beside the threat; research and current Commander remain distinct. No sex beside the active rift. |
| after | “"After." She repeats the word as if it belonged to a language she used to speak, a long time ago. "Very well. I will ask you after. One of us will be there to answer." She turns back to t…” | 92/K | Retain frank contradictory desire beside the threat; research and current Commander remain distinct. No sex beside the active rift. |

### areelu.trickster.wager.raised

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| her_choice | “Areelu studies your face. Her hand remains pressed to the wound. "You have me beaten, and you are bargaining. I would like to know why. If neither of us burns, I stay close enough to find…” | 94/K | Keep bodily reciprocity and her actual yes/no in set piece 3; no further explicit escalation while defeated and bleeding. Collection alone earns no company. |
| kiss | “You cup her face and kiss her. She catches the back of your neck, pulling you hard against her mouth. Her palm leaves a smear of blood along your jaw. When she breaks the kiss, her hand s…” | 96/K | Keep bloody, forceful, reciprocated kiss and her counter-demand. Heated encounter ends here; no bedroom act while she bleeds at the rift. |
| hand | “Her hand is cold, slick with her own blood, and much stronger than it looks. She grips back hard enough to hurt, and does not let go when a sensible person would. "There. The real one, as…” | 94/K | Keep painful grip and real-hand recall only if requested; touch/commitment identity remains, no automatic night. |
| kissed | “You kiss the back of her bloody hand. Her fingers close on yours. "You have chosen a strange time to court me." She does not pull away. "Do it again after Threshold. I would like to see w…” | 94/K | Keep hand-kiss and her demand to court her after Threshold; pay the anticipation with set piece 4's invitation, not a new debt gate. |
| refused | “"No." She says it without heat. "I do not renegotiate at the edge of the Wound, with a sword at my throat. The wager stands as it was struck. Collect your stake, if you win it. Nothing mo…” | 94/K | Keep bodily reciprocity and her actual yes/no in set piece 3; no further explicit escalation while defeated and bleeding. Collection alone earns no company. |

### areelu.trickster.wager.last_words

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| start | “Areelu raises her chin. Blood has dried on it. "You speak as if there will be time after this. Choose, Commander. I would like to find out whether you are right."” | 91/K | Keep anticipation under the final choice; survival is uncertain, not an intimacy promise or page-earned yes. |
| will | “"Then choose. I will not beg, and I will not flinch. If your wager works, I intend to be awake to see it."” | 91/K | Keep anticipation under the final choice; survival is uncertain, not an intimacy promise or page-earned yes. |
| print | “She looks down at the blood drying on her hand. "You would add a clause now. Very well. Choose, Commander. If there is an afterwards, I intend to collect."” | 91/K | Keep anticipation under the final choice; survival is uncertain, not an intimacy promise or page-earned yes. |

### areelu.trickster.finale.rewrite

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| inventory | “She sat in the ash and tried a word of power. Nothing. A gesture that had once split stone. Nothing. Last she counted her own pulse, holding her wrist so tightly that her fingers left whi…” | 92/K | Keep painful mortality and offered-hand response; recovery first, then a new freely chosen invitation. Extraction is not erotic. |
| mortal | “"Mortal." She tried a word of power on the Commander, very deliberately, to see what would happen. Nothing happened. "You took a century from me with a crystal and a pun, and you are reco…” | 92/K | Keep painful mortality and offered-hand response; recovery first, then a new freely chosen invitation. Extraction is not erotic. |
| terms | “When she stood up, her face was composed again, and colder than the Commander had ever seen it. "Here is what I will do," said Areelu Vorlesh. "I will follow you until I understand how yo…” | 92/K | Keep painful mortality and offered-hand response; recovery first, then a new freely chosen invitation. Extraction is not erotic. |
| hand_again | “She takes the offered hand and pulls herself to her feet. Her grip hurts. "I lost the wager. I have not agreed to be carried."” | 92/K | Keep painful mortality and offered-hand response; recovery first, then a new freely chosen invitation. Extraction is not erotic. |

### areelu.trickster.finale.after

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| end | “"You reduced a century of work to a pun, and took the Abyss out of me. How thorough." She did not thank the Commander. Nobody had expected her to. "You lost the bet," said the Commander. …” | 82/H | Set piece 4: separate settlement and recovery from chosen company; append COMPANY-M. Do not grant rooms through wager-only acceptance or claim lifetime company after separation. |
| end/Paragraphs[0] | “A kitsune scholar arrived within the week, with calipers and a folio, to measure her. Areelu allowed it exactly once, and corrected the arithmetic.” | 82/H | Set piece 4: separate settlement and recovery from chosen company; append COMPANY-M. Do not grant rooms through wager-only acceptance or claim lifetime company after separation. |
| end/Paragraphs[1] | “A kitsune scholar arrived within the week, with calipers, a folio and a list of questions she had brought back with her from further off than most scholars travel. Areelu allowed the meas…” | 82/H | Set piece 4: separate settlement and recovery from chosen company; append COMPANY-M. Do not grant rooms through wager-only acceptance or claim lifetime company after separation. |
| end/Paragraphs[2] | “The first inquisitors who came looking for the Architect of the Worldwound found a tired woman with ink on her hands and no magic about her at all, living under the Commander's roof, and …” | 82/H | Set piece 4: separate settlement and recovery from chosen company; append COMPANY-M. Do not grant rooms through wager-only acceptance or claim lifetime company after separation. |
| end/Paragraphs[3] | “She did not sleep the first night. She sat by the window of the Commander's lodging with a borrowed pen and wrote, from memory, the first page of the report she had been writing all her l…” | 82/H | Set piece 4: separate settlement and recovery from chosen company; append COMPANY-M. Do not grant rooms through wager-only acceptance or claim lifetime company after separation. |
| end/Paragraphs[4] | “The late terms had promised the Commander nothing of hers if she burned. She held the Commander to them with great precision for the rest of her life: the Commander was never once allowed…” | 82/H | Set piece 4: separate settlement and recovery from chosen company; append COMPANY-M. Do not grant rooms through wager-only acceptance or claim lifetime company after separation. |
| end/Paragraphs[5] | “Among the few things she kept was the entry she had dictated in Alushinyrra, which she had never written down and did not need to: "Further observation required." She wrote it on the firs…” | 82/H | Set piece 4: separate settlement and recovery from chosen company; append COMPANY-M. Do not grant rooms through wager-only acceptance or claim lifetime company after separation. |

### areelu.trickster.finale.survived

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| end | “Neither of them burned, which was the bet the Commander had made: "My money's on neither."” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[0] | “Areelu Vorlesh paid what she owed on the bet in person. She burned her own notes in front of the Commander, page by page, without comment, for a whole night. What was left of her she kept…” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[1] | “The Abyss had gone into the Council's crystal before the final choice, and it did not come back to her. What walked out of Threshold was a Sarkorian woman with grey coming into her hair, …” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[2] | “A week later she came to the Commander's door with a proposal, set out as she would have put it to a patron funding a study: rooms across the hall, unrestricted access to the subject, and…” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[3] | “She objected, on principle, to the fact that the winner was now partly Shyka the Many, and required every observation to be initialled twice: once for each of them.” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[4] | “She had been told that the winner would come back partly Shyka the Many, and had prepared a second column for the initials. The Commander came back one person, badly behaved, with Shyka's…” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[5] | “Nenio offered to buy the ashes for her encyclopaedia. Areelu sold them to her at a price that made the kitsune's ears go flat.” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[6] | “Nenio, who had come back from further off than most scholars travel, offered to buy the ashes for her encyclopaedia. Areelu sold them to her at a price that made the kitsune's ears go flat.” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[7] | “She kept every appointment she made. The first was at the Commander's door, the morning after Threshold, with her hand held out: the real one.” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[8] | “Some of the pages she burned the Commander recognised. The notes from Kenabres. The observations from Drezen, in Yaniel's borrowed hand. A thick bundle tied with black ribbon, labelled on…” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[9] | “The lens she had sent she did not burn. She took it back without asking, polished it on her sleeve, and set it on the windowsill between the two rooms, where it stayed.” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |
| end/Paragraphs[10] | “The Commander, as the report records with some irritation, fell asleep in a chair before she was halfway through, and she burned the rest by the light of the Commander's snoring. "The sub…” | 78/H | Set pieces 3–4: correct unowed no-burn paper destruction; append immediate COMPANY-M/W opportunity after recovery. No four-year wait or automatic company. |

### areelu.trickster.report.rooms

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| start | “The report resumed in a fresh notebook. Areelu took the room across the hall and left her door open while she worked. When the Commander passed it, her pen stopped. Neither of them mentio…” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| knock_mortal | “"Enter." She clears a place beside the lamp. A silver probe and a sand-glass lie among the papers. "Sit down. I want to look at the wound." She takes the Commander's wrist and does not re…” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| knock_witch | “The sigils flared at the first knock and went out at the second. "Enter," she said, and the door opened by itself, which she clearly thought was funnier than the Commander did. She did no…” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| walk_mortal | “She stands at the window with a vial held to the light. Inside is a drop of the Commander's blood. "Taken while you slept. You had been moving all evening." She sets it among her papers a…” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| walk_witch | “The sigils hissed like a kettle as the Commander stepped through them, and did nothing else. She had keyed them, it turned out, to everyone in Golarion but one. "You did not knock," said …” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| note | “The note said: Knock knock. The answer came back under the Commander's own door the next morning, in a hand as small and even as a row of stitches: "Who is there. (Do not answer. I have a…” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| hands | “She sketches the Commander's hand beside a diagram of the cauldron. When the Commander makes a coin vanish over the open page, she catches the wrist before the second flourish. "Again. Sl…” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| laugh | “The Commander tried. A joke about the Worldwound, which she corrected. A joke about Deskari, which she improved. Then, out of nowhere, a very old joke from the border taverns about a pala…” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| coin | “The Commander makes the coin vanish again. Areelu follows the empty hand, then catches it and opens the fingers herself. "Nothing. Very well. Again." After the twentieth attempt she pushe…” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| pen | “The Commander takes her pen. She keeps hold of the wrist that took it. "Give it back." Her thumb presses against the pulse. "Or keep it and stay. I have not finished with either of you."” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| hers | “"I thought I knew what you would do. I had built enough of you to be certain." She turns the pen between her fingers. "Then you brought me a wager I did not know how to win. I would like …” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |
| end | “By the end of the month, the chair beside her desk had acquired the Commander's cloak. She complained when it covered her papers. She did not move it to the other room.” | 85/H | Set pieces 4–5: make remaining appetite visible in wrist/pen proximity and an invitation she can reject; keep instruments for real wound findings. No new sex slot in routine examination. |

### areelu.trickster.report.hunters

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| herself_mortal_after | “She came back upstairs with her face very still. "He did not believe a word of it," she said. "Good. A man who believes me is a fool, and fools come back with more fools. That one will co…” | 92/K | Preserve danger, her own escape plans and knowing return upstairs; shelter does not buy intimacy or immunity. |
| doorway_mortal | “The Commander stood in the doorway beside her, with nothing in either hand, and let the inquisitors look. "You will want to arrest the Commander of the crusade as well, I suppose," said A…” | 92/K | Preserve danger, her own escape plans and knowing return upstairs; shelter does not buy intimacy or immunity. |
| doorway_witch | “The Commander stood in the doorway beside her, with nothing in either hand, and let the inquisitors look. "You will want to arrest the Commander of the crusade as well, I suppose," said A…” | 92/K | Preserve danger, her own escape plans and knowing return upstairs; shelter does not buy intimacy or immunity. |
| cellar_after | “"The last time they came," she said, "I did not hide. I did not know to. I was at my desk, and I did not hear them until it was over." She closed the notebook. "This time I heard every st…” | 92/K | Preserve danger, her own escape plans and knowing return upstairs; shelter does not buy intimacy or immunity. |
| doorway_after | “When they had gone, she stayed in the doorway a while longer, looking at the empty street. "The last time they came to my house," she said, "nobody stood in the door." She did not say any…” | 92/K | Preserve danger, her own escape plans and knowing return upstairs; shelter does not buy intimacy or immunity. |

### areelu.trickster.report.grey

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| start | “In the second winter she fell ill. It was nothing: a cough, a fever, the kind of thing that goes through a city every winter and kills the old and the unlucky. The woman who had opened th…” | 91/K | Keep spite, physical frailty and a chosen bedside vigil; cut coy spelling jokes. No sex while fever impairs her, no instant cure or grateful lover. |
| dare | “She opened her eyes, and for a moment they were the eyes the Commander remembered from Threshold, entirely without mercy. "Let it take me," she repeated. "In a bed, of a cough, a hundred …” | 91/K | Keep spite, physical frailty and a chosen bedside vigil; cut coy spelling jokes. No sex while fever impairs her, no instant cure or grateful lover. |
| sit | “The Commander sat with her. Near midnight she woke, and saw who it was, and did not tell the Commander to go. "This is what you did," she said. Her voice was a thread. "Death. Weakness. S…” | 91/K | Keep spite, physical frailty and a chosen bedside vigil; cut coy spelling jokes. No sex while fever impairs her, no instant cure or grateful lover. |
| healer | “The healer the Commander found was a priest of the Lady of Graves, because that was who was awake at that hour. Areelu opened her eyes, saw the grey robe and the spiral at his throat, and…” | 91/K | Keep spite, physical frailty and a chosen bedside vigil; cut coy spelling jokes. No sex while fever impairs her, no instant cure or grateful lover. |
| cold | “"Nobody will," she agreed, from behind a wall of blankets. "That is the most dangerous kind of truth. Write it down for me. My hand is shaking." The Commander wrote it down. She dictated …” | 91/K | Keep spite, physical frailty and a chosen bedside vigil; cut coy spelling jokes. No sex while fever impairs her, no instant cure or grateful lover. |
| after | “The fever breaks on the third day. At the mirror she parts the grey at her temple and finds white beneath it. She pulls one hair free and holds it against the lamp. "More of it. So this i…” | 91/K | Keep spite, physical frailty and a chosen bedside vigil; cut coy spelling jokes. No sex while fever impairs her, no instant cure or grateful lover. |

### areelu.trickster.report.graft

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| start | “In the second winter the Commander woke one night and found her gone. She had not paid the Abyss back when she paid her stake. It was still in her, the half of her she had sewn to her own…” | 88/H | Preserve danger and chosen return from the wall; reduce observer diary jokes. Any wrist touch expresses warning, not child's erotic response or a cure for Abyssal hunger. |
| follow | “The Commander found her at the edge of the city, where the old walls gave out onto open ground, standing perfectly still with her face turned toward the north, toward the Wound. The wound…” | 88/H | Preserve danger and chosen return from the wall; reduce observer diary jokes. Any wrist touch expresses warning, not child's erotic response or a cure for Abyssal hunger. |
| says | “"That I was right." Her eyes stayed on the north. "That everything I did was correct, and there is more to do, and I am wasting the Abyss in me on a kitchen and a notebook and a Commander…” | 88/H | Preserve danger and chosen return from the wall; reduce observer diary jokes. Any wrist touch expresses warning, not child's erotic response or a cure for Abyssal hunger. |
| stand | “The Commander stood beside her until the sky went grey. Neither of them said anything. Once, near dawn, something under the Commander's breastbone stirred in answer to the north: the soul…” | 88/H | Preserve danger and chosen return from the wall; reduce observer diary jokes. Any wrist touch expresses warning, not child's erotic response or a cure for Abyssal hunger. |
| mine | “"Yes." She turned at last, and her crimson eyes were very bright. "I changed myself by sewing my soul to the Abyss, and then I changed you. Those fits of rage in Kenabres were the other h…” | 88/H | Preserve danger and chosen return from the wall; reduce observer diary jokes. Any wrist touch expresses warning, not child's erotic response or a cure for Abyssal hunger. |
| wait | “She came back an hour before dawn, with frost in her hair and nothing in her hands. She saw the Commander sitting up in the dark, and stopped in the doorway. "You waited," she said. "I di…” | 88/H | Preserve danger and chosen return from the wall; reduce observer diary jokes. Any wrist touch expresses warning, not child's erotic response or a cure for Abyssal hunger. |
| sleep | “The Commander went back to sleep, and she came back, and in the morning there was a new entry in her notebook in a hand that was not quite as steady as usual. "Went out. Did not answer. S…” | 88/H | Preserve danger and chosen return from the wall; reduce observer diary jokes. Any wrist touch expresses warning, not child's erotic response or a cure for Abyssal hunger. |
| after | “It happened perhaps twice a year. She never answered. Once, near the end of the report, she wrote: "A hundred years ago I would have gone. The difference is not virtue. The difference is …” | 88/H | Preserve danger and chosen return from the wall; reduce observer diary jokes. Any wrist touch expresses warning, not child's erotic response or a cure for Abyssal hunger. |

### areelu.trickster.report.sarkoris

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| wants_after | “She took the roll. She wrote at the bottom of it, under the god-caller's unfinished name, in the old Sarkorian letters the woman recognised: "Areelu Vorlesh, of Sarkoris. Lost in the firs…” | 87/H | Keep the casualty conflict unsensual and her evil intact; no blanket redemption or comforting kiss that settles the dead. |
| silence | “The Commander said nothing, and so neither did anyone else. The three of them sat in the kitchen with the roll across the table until the candle burned down. When the woman from the camps…” | 87/H | Keep the casualty conflict unsensual and her evil intact; no blanket redemption or comforting kiss that settles the dead. |
| away | “The Commander met the woman at the gate and sent her back to the camps with money and a lie. Areelu had watched it all from the window. "You protected me from a list," she said. "How sent…” | 87/H | Keep the casualty conflict unsensual and her evil intact; no blanket redemption or comforting kiss that settles the dead. |

### areelu.trickster.report.participation

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| start | “In the fourth winter, she comes to the Commander's door with her hair loose and the notebook tucked under one arm. She shuts it before she knocks.” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| start/Paragraphs[0] | “She was mortal now, and cold at night in a way she had forgotten a body could be. She said so, as a fact, standing in the Commander's doorway with her notebook under her arm and her hair …” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| start/Paragraphs[1] | “The wound above her heart glowed faintly in the dark, as it had at Threshold. She stood in the Commander's doorway with her notebook under her arm and her hair loose over her shoulders, a…” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| start/Paragraphs[2] | “"Well?" said Areelu Vorlesh. "Open the door, Commander. I did not come to take your pulse."” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| in_mortal | “She unbuttons your shirt and pushes it off your shoulders. Her fingers are cold; her mouth is warm. At the wound from Kenabres she pauses, presses her lips beside it, then looks up at you…” | 93/K | Keep cold fingers/warm mouth and possessive scar-kiss; shift first-night framing to deepening. Continue to RETURN-M after the existing second staging node. |
| in_mortal_2 | “She lets the grey dress fall. In the lamplight you can see the marks the graft left, the lines at her mouth, the heat rising along her throat. "Look. I want you to see what is left." She …” | 84/S | Attach RETURN-M after accepted staging, before morning; body-state branch remains mortal. Let appetite carry the scene rather than inventory of what remains. |
| in_witch | “Her hand closes over yours and brings it to the fastening of her robe. She watches you undo it. Beneath the cloth, the wound above her heart burns violet. "You wanted close enough to stud…” | 93/K | Keep her initiating hand and hungry kiss; retained graft belongs only in the correct body state. Continue to RETURN-W after second staging node. |
| in_witch_2 | “She pulls off your shirt and lets her robe slip after it. The violet light spills over both of you. At the bed she rolls you beneath her and catches your wrists against the pillow. Her ha…” | 84/S | Attach RETURN-W after accepted staging, before morning; keep her forceful initiative visibly reciprocated and allow the established stop before entry. |
| want | “"Yes." She sets the closed notebook on the floor. "I want you. Do you require a cleaner answer than that? I will not give you one. I have not stopped wanting what brought us to Threshold.…” | 95/K | Keep direct desire and unresolved purpose; stop option remains playable. Do not turn this strong answer into a diagnostic pass. |
| notebook | “She holds the notebook out. You take it and set it on the floor. Two fingers settle against your throat, and her thumb tilts your chin toward her. "There. The pulse I kept beating in the …” | 86/S | Keep kiss and lap contact; route to RETURN-M/W by actual body state. This is an alternate approach to the same night, not another slot or first time. |
| morning | “At dawn she sits beside you, barefoot, writing on her knee. When you stir, she closes the notebook against your reaching hand. "No. This page is mine." She lays it aside and returns her p…” | 83/H | Show bodily ease after the actual night, then protect private research through her action; replace preference-for-observation punchline with her own return to work. |
| morning/Paragraphs[0] | “At breakfast Nenio looks from Areelu's loose hair to the two cups at the Commander's place and opens her folio. "A new observation—" Areelu lays a hand over the page. "An unpublished one.…” | 83/H | Show bodily ease after the actual night, then protect private research through her action; replace preference-for-observation punchline with her own return to work. |
| morning/Paragraphs[1] | “At breakfast Nenio looks from Areelu's loose hair to the two cups at the Commander's place and opens her folio. "A new observation—" Areelu lays a hand over the page. "An unpublished one.…” | 83/H | Show bodily ease after the actual night, then protect private research through her action; replace preference-for-observation punchline with her own return to work. |
| aloud | “The Commander reaches for the notebook again. Areelu catches it first and closes it. "You have heard what I want. That does not give you my notes." She puts it in the locked drawer and po…” | 88/H | Keep appetite and notebook privacy distinct; she takes the book and returns to the bed or her own work by choice. No therapy lecture. |
| morning_after | “That afternoon she went back across the hall and moved her own desk under the one window of her room that faced the street, where she could see who came to the Commander's door before the…” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| propose | “She did not answer at once. She took out her notebook and wrote the proposal down, word for word, and read it back to herself. "Conditions," she said. "The desk goes under your window, no…” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| shared | “She moves the desk that evening and sets the packed case beside it. "I want the bed. The notebook stays on my side of it." She hangs the four agreed conditions above the desk. Some weeks …” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| refused | “"Then no." She closed the notebook without heat. "I did not survive a century by sharing the choice of when I am vulnerable, Commander. I will not start because you asked nicely. Ask me a…” | 91/K | She refuses shared rooms and remains across the hall; retain independent nights and a fresh knock. Do not close the romance or require other partners to leave. |
| stay | “"On my terms." She read the sentence back to herself, as if checking it for a clause she had missed. "Very well. Two conditions. I leave the day you bore me, and I take my notes when I go…” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| rules | “"Your roof," she repeated, and unpacked the case, slowly, item by item, onto her own bed: a knife, a vial of something that smoked, three forged letters of passage to three different coun…” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| door | “"Very well." She wedged her own door open with the desk that same evening, so that she could see the Commander's across the hall. "You wanted a door," she said. "You have one. It is open.…” | 84/H | Set piece 5: this is return/deepening after the immediate conclusion; keep her appetite, packed case and actual room terms. Morning must carry the chosen night and unfinished work rather than a notebook punchline. |
| letters | “Within the month she had read every letter in the Commander's desk, and put each one back exactly as it had been, and said so at breakfast, to the Commander's face. "I do not share well. …” | 87/H | Show possessive letter-reading and a concrete household answer; retain privacy of research and honest coexistence. No newly invented exclusivity terms. |
| closed | “The Commander closed the door gently between them. Through the wood, after a while, came a dry sound that might have been a laugh. "Subject declined," said Areelu Vorlesh. "Noted." Her fo…” | 85/H | Keep winter refusal and spring knock; change subject/noted quip to a pointed answer. A letter or knock is not arrival/consummation/reconciliation. |

### areelu.trickster.report.wound

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| start | “In the fifth year the wound from Kenabres opened again, as the old wound of an unclosed Worldwound will. It opened in the night, without warning, and the Commander woke in a bed full of b…” | 91/K | Keep treatment concrete and nonsexual, history-correct personal-wound ownership; forbid H1 recurring pull through the documented correction. Love does not make her medically omnipotent. |
| work_mortal | “By morning it had closed. Not healed: held, with silk and salt and a paste she would not name, and a patience the Commander had not known she had. Her hands, when she finally took them aw…” | 91/K | Keep treatment concrete and nonsexual, history-correct personal-wound ownership; forbid H1 recurring pull through the documented correction. Love does not make her medically omnipotent. |
| work_witch | “By morning it had closed. Not healed: held, with a working that made the lamps burn violet and the Commander's teeth ache, and something of hers laid into it that the Commander could feel…” | 91/K | Keep treatment concrete and nonsexual, history-correct personal-wound ownership; forbid H1 recurring pull through the documented correction. Love does not make her medically omnipotent. |
| why | “"Because it is mine." She said it at once, as if the answer had been waiting. "The Wound in the world is mine. This one is mine. You are the only record of my work that I have not burned,…” | 91/K | Keep treatment concrete and nonsexual, history-correct personal-wound ownership; forbid H1 recurring pull through the documented correction. Love does not make her medically omnipotent. |
| end | “Afterwards she wrote for a long time. The Commander, lying very still, read the heading upside down: "The Wound: Observations. Volume One." There would be others. It opened again the next…” | 91/K | Keep treatment concrete and nonsexual, history-correct personal-wound ownership; forbid H1 recurring pull through the documented correction. Love does not make her medically omnipotent. |

### areelu.trickster.report.prison

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| wait | “The Commander waited at the top of the stairs for an hour, and then another, while the torchlight below moved from cell to cell and stopped. When she came up at last, there was dust on he…” | 91/K | Keep prison memory and the living witness; no intimacy reward for her captivity or demonstration of a lost craft. |
| cell_mortal | “She reads the marks to the end. "The calculation was right. I cannot supply its power now. A century of the Abyss had grown through my craft. When your cauldron pulled it out, it brought …” | 91/K | Keep prison memory and the living witness; no intimacy reward for her captivity or demonstration of a lost craft. |

### areelu.trickster.report.cult

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| deal_witch_after | “The others went. She shut the door and leaned on it, and for a moment she looked every one of her years. "I could have taught them," she said. "It would have been easy. It is always easy,…” | 91/K | Keep her independent amoral counter-move and return indoors; witness request buys no romantic flag or forgiveness. |

### areelu.trickster.report.incursion

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| end | “Entry, the seventh summer: "Incursion from the Wound. Repelled. Losses within tolerance. Observer's contribution not recorded, by the observer's request." Beneath it, in the laughing hand…” | 87/H | Keep earned admiration after actual casualties; show her returning alive to answer the Commander. Do not hide the price behind a notebook epigram. |

### areelu.trickster.report.dagger

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| keep | “"Very well," she said, and did not argue, which was worse than arguing. Three nights later the Commander woke to find her sitting on the end of the bed in the dark, with the dagger across…” | 89/H | Preserve the unsettling bedroom intrusion as a custody dispute; sheath stays closed, no threat recast as foreplay. She returns the blade, not proof of consent. |

### areelu.trickster.report.lady

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| date | “The bird turns one grey eye on the Commander. "The Lady does not negotiate dates," it said. "She keeps them. That is what is being bought: that she keeps this one." It considered Areelu a…” | 86/H | Use contested records and actual retrieval labor; her fear of losing the Commander gives the bargain stakes, not divine-proof leverage or a free household future. |
| refuse | “"Keep them for what?" said Areelu. "For the day she sends for me, and I stand in front of her with a hundred years of clauses, and win, and you are already in her garden?" She did not loo…” | 86/H | Use contested records and actual retrieval labor; her fear of losing the Commander gives the bargain stakes, not divine-proof leverage or a free household future. |

### areelu.trickster.report.visitors

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| daeran | “Daeran arrived with two bottles of wine and no apology, and looked at the Architect of the Worldwound across the Commander's kitchen table with open, delighted interest, as if at a rare a…” | 91/K | Daeran's hand-kiss is courtly social contact between lucid people; preserve her sharp return invitation and independent interests. No implied affair, jealousy stance or drunken incapacitated sex. |
| daeran_after | “They drank both bottles and a third, and he told her things about Mendev's inquisition that the Commander had not known, and she told him things about the Abyss that made him go quiet for…” | 91/K | Daeran's hand-kiss is courtly social contact between lucid people; preserve her sharp return invitation and independent interests. No implied affair, jealousy stance or drunken incapacitated sex. |
| shut | “The Commander closed the door on the curious, and after a while they stopped coming. "You did that for me," said Areelu, not looking up. "Do not. I have been stared at by better people th…” | 91/K | Daeran's hand-kiss is courtly social contact between lucid people; preserve her sharp return invitation and independent interests. No implied affair, jealousy stance or drunken incapacitated sex. |

### areelu.trickster.report.name

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| start | “In the ninth winter she said a name in her sleep. It was not the Commander's name. It was short, and old, and Sarkorian, and she said it the way people say a name they have said ten thous…” | 92/K | Preserve shared sleep, her hard hand-grip and refusal of appropriation; grief is not foreplay. Keep child name out of later sexual dialogue. |
| ask | “She sits up and pulls the blanket around her shoulders. "You know whose name it is. You heard it while I slept. That does not make it yours." She looks at the Commander now. "My {mf\|son\…” | 92/K | Preserve shared sleep, her hard hand-grip and refusal of appropriation; grief is not foreplay. Keep child name out of later sexual dialogue. |
| nothing | “The Commander said nothing. After a long time she lay down again, with her back to the Commander, very straight. Near dawn her hand found the Commander's in the dark, and held it, hard, t…” | 95/K | Keep hard hand-holding before dawn. Remove later access to her private notebook if it contradicts actual room terms; no sexual expansion of grief. |
| back | “The Commander said the name back to her, softly, once. She went white to the lips. For a moment the Commander saw in her face exactly what the hunters must have seen, a hundred years ago,…” | 92/K | Preserve shared sleep, her hard hand-grip and refusal of appropriation; grief is not foreplay. Keep child name out of later sexual dialogue. |
| end | “The name does not appear anywhere in the report. Scholars who have searched for it have found only a single place, in the ninth winter, where a word has been written and scraped away so t…” | 92/K | Preserve shared sleep, her hard hand-grip and refusal of appropriation; grief is not foreplay. Keep child name out of later sexual dialogue. |

### areelu.trickster.report.promise

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| confront | “She saw it on the table and did not pretend. "Yes," she said. "Every morning. I read it every morning, and every morning I put it away." Then: "Do not look at me as if I had forgotten. Yo…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| why | “"Because of the promise." She said it at once, as if she had been waiting nine years for somebody to ask. "I held my child at the door and I promised that the world would not stay as it w…” | 92/K | Keep the frightening unresolved extraction threat as villainous conflict; never eroticize the child link or cast involuntary soul harm as love. |
| back | “The Commander returns the notebook to its hiding place. That evening Areelu lays it on the table. A fine hair hangs from the binding, its ends no longer joined. "You opened it. And put it…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| burn_mortal | “The Commander burned it in the kitchen grate, page by page, as a century of her notes had once burned after Threshold. She watched without moving. "You understand," she said, when it was …” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| burn_witch | “The Commander burned it in the kitchen grate, page by page, as she had once burned a century of notes to pay her stake. She watched without moving, and the fire in the grate burned violet…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| burned | “Letters came for a while: from Nex, and from Geb, and once from somewhere that was not on any map. Each was a single line of observation about the Commander, sent from very far away, and …” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| burned_mortal | “The last of the letters came in a hand so unsteady that the Commander did not recognise it at first: an old woman's hand, spotted with ink, pressing too hard. It said only, "Still correct…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| burned_witch | “The last of the letters came up out of the ground, one winter night, through the floor of the Commander's study, written in frost on the inside of a window that faced nowhere. "Still corr…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| join | “"Together." She said the word as if testing whether it would bear weight, and found that it would not. "No. You would make it a joke, and the Lady would laugh, and I would lose {mf\|him\|…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| filed | “She spent the rest of her years on it. What she built, and what she bargained, and what it cost her, the report does not say; those pages are missing, and whoever took them out did it wit…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| keep | “The Commander left the notebook on the table between them, open, and did not touch it. "You are a fool," said Areelu Vorlesh. "You will wake one morning and wonder whether today is the da…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| kept | “She read the method every morning for the rest of her life, and every morning she put it away. She never explained it, and the report never records a reason. It records only the date of e…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| afterword | “Inside the report's back cover, the Commander writes beneath a line she left blank: "I did not know whether we would survive Threshold. I wanted enough time to find out who I had wagered …” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| aw_line | “There is one more line beneath it, added later, in the same laughing hand: "Neither. Told you so." And beneath that, in her small neat hand, her answer: "Result: neither. Experiment conti…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |
| aw_leave | “The Commander left the cover as it was. Nobody has added anything since. Scholars who have handled the report say that the back cover is worn smooth in one place, as if someone had rested…” | 89/H | Set piece 6: keep the threat, hand-taking and daily decision physically concrete but nonsexual; separate child research from desire. Carry keep/file/burn and show returns only where company continues. |

### areelu.trickster.report.afterword

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| start | “The report ends where it ends. But on the inside of its back cover, in a hand that is not hers, someone has written a note of their own, and she did not cross it out. "For the record, sin…” | 83/H | Replace observer/subject sentiment and false universal Iz recollection with actual chosen company; preserve ending identity. No late free reconciliation or first-night recall without it. |
| line | “There is one more line beneath it, added later, in the same laughing hand: "Neither. Told you so." And beneath that, in her small neat hand, the last thing she ever wrote in any of her no…” | 83/H | Replace observer/subject sentiment and false universal Iz recollection with actual chosen company; preserve ending identity. No late free reconciliation or first-night recall without it. |
| leave | “The Commander left the cover as it was. Nobody has added anything since. Scholars who have handled the report say that the back cover is worn smooth in one place, as if someone had rested…” | 83/H | Replace observer/subject sentiment and false universal Iz recollection with actual chosen company; preserve ending identity. No late free reconciliation or first-night recall without it. |

### areelu.trickster.finale.prior_lien

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| end | “"You burned." Areelu wrote it at the top of a clean page, and underlined it. "The Lady of Graves had the prior lien. She always does; I have spent a century reading her books and I have n…” | 91/K | Memorial only: preserve her loss without living Commander intimacy; jar remembrance depends on actual accepted company. |
| end/Paragraphs[0] | “She kept it in a jar of her own design, in a room nobody else was allowed to enter, and on the day each year that the Commander had first offered her the bet she did not open the room at …” | 91/K | Memorial only: preserve her loss without living Commander intimacy; jar remembrance depends on actual accepted company. |
| end/Paragraphs[1] | “She did not thank anyone. Nobody who knew her expected her to. But the report she wrote afterwards, which is long, and precise, and entirely about a wound, ends with a single line that is…” | 91/K | Memorial only: preserve her loss without living Commander intimacy; jar remembrance depends on actual accepted company. |

### areelu.trickster.finale.lien_bottled

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| end | “"You burned." Areelu wrote it at the top of a clean page, and underlined it, and then, below it, in smaller letters: "And did not stay burned." "The Lady of Graves had the prior lien. She…” | 86/H | Set piece 4: H2 only, actual commitment; corked flask stays on washstand. Her anxiety becomes appetite and morning return; no first-night repeat or wrist bottle. |
| end/Paragraphs[0] | “She did not go back to a laboratory. She took the rooms across the hall from the Commander's instead, with a fresh notebook and a lamp she kept burning later than anyone in the house, and…” | 86/H | Set piece 4: H2 only, actual commitment; corked flask stays on washstand. Her anxiety becomes appetite and morning return; no first-night repeat or wrist bottle. |
| end/Paragraphs[1] | “The flask stays with the Commander, corked, its contents undisturbed. Once a month she asks the Commander to hold it toward the lamp. She lays two fingers against the glass long enough to…” | 86/H | Set piece 4: H2 only, actual commitment; corked flask stays on washstand. Her anxiety becomes appetite and morning return; no first-night repeat or wrist bottle. |
| across | “She comes across the hall with a lamp and leaves it on the washstand. "The scar. Show me." The Commander loosens the shirt. She pushes it from both shoulders and lays her palm over the cl…” | 84/S | Retain forceful kiss/undressing; set the flask on the washstand first. Accepted approach enters BOTTLE, stop enters old stopped node. |
| morning | “At dawn she is across the hall, writing. When the Commander passes the door, she catches the wrist bearing the flask, feels the warmth beneath it and lets go. "Still here. I would like yo…” | 84/H | Remove wrist-bearing flask. Show her reluctant bodily closeness before going back across the hall, and a chosen return; fear of another death is specific to H2. |
| stopped | “She went very still. Then she sat back on her heels, and took her hand away, and looked at it. "It was not a measurement," she said. "That is what I cannot forgive you for making me say."…” | 82/H | She resents being reduced to measurement, leaves, and later returns with a fresh invitation. Preserve refusal; no act implied by later knocking. |
| stands | “The report on the wound was long and precise and entirely about the wound. She sent a copy to the Commander's door, bound, with an invoice for the binding.” | 86/H | Set piece 4: H2 only, actual commitment; corked flask stays on washstand. Her anxiety becomes appetite and morning return; no first-night repeat or wrist bottle. |

### areelu.trickster.finale.ascended

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| end | “They had ascended together. In the first entry of her new report, Areelu wrote both names. That night she closed the notebook and looked at the Commander. "I have recorded what the crysta…” | 92/K | Set piece 4: preserve equal power and her frank invitation; morning actually postpones work, refusal remains distinct. Never call ascension mortal recovery. |
| asc_night | “She takes your hand from the notebook and places it at the fastening of her gown. When you undo it, she steps close enough for the loosened cloth to brush your skin. "Look at me." Her mou…” | 87/S | Keep undressing and frank pursuit; accepted approach enters ASCENT, old stopped branch remains. Godhood supplies no compulsory yes. |
| asc_morning | “In the morning her gown lies over your discarded shirt. She reaches for the notebook, then leaves it closed and draws your hand back beneath the blanket. "Stay. I have work waiting. I pre…” | 94/K | Keep her drawing the hand beneath the blanket and postponing work; no added explicit morning slot needed. |
| asc_stopped | “She settles beside you and pulls the blanket over both of you. "Very well. Stay here." In the morning she retrieves the notebook, then moves the lamp so you can read the new heading besid…” | 92/K | Keep shared blanket without implied consummation and her notebook ownership; distinguish this quieter accepted company from the completed night. |

### areelu.trickster.finale.not_burned

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| end | “"You did not burn." Areelu wrote it at the top of a clean page, and did not underline it, because she was not yet certain it was true. "The lock took the key, exactly as designed. I measu…” | 86/H | Set piece 4: true Iomedae return, no flask. Outside intervention unsettles her; morning shows chosen return, and refusal cannot imply a completed night. |
| nb_across | “She comes to the Commander's rooms with a lamp and a notebook. Both go on the floor, the notebook closed. "Where the wound was. Show me." She takes the loosened shirt from the Commander's…” | 85/S | Keep kiss and assertive approach; accurate scarless/changed-skin history, no research-created desire. Accepted approach enters BRIDGE, old stop stays. |
| nb_morning | “In the morning the notebook is still closed on the floor. She picks it up, then stops at the door. "I will come back tonight. If that patch of skin changes before then, send for me." She …” | 86/H | Keep promised return, but show morning physical contact and her irritation at what she could not explain; accurate appointment/rescue variant, no flask. |
| nb_stopped | “She went still, and took her hand away, and looked at it as though it belonged to a colleague who had disappointed her. "It was not an experiment," she said. "I would not have said so if …” | 82/H | Remove disappointed-colleague simile; express her wounded pride through withdrawal and later fresh invitation. No refusal punishment or automatic reconciliation. |

### areelu.trickster.afterlogue.spared

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| line | “"I was defeated. The victor spared my life, and then did something I had not predicted: kept it. Not as a boon, and not as charity, but the way one keeps a wager that has not been settled…” | 80/H | Retrospective chosen company must fit keep/file/burn; remove lifelong roof/hallway assertion after departure. Native judgment remains and altered fate applies only on current Trickster. |

### areelu.trickster.afterlogue.mortal

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| line | “"I was defeated, and the one I had tried to transform made a joke of my death and collected my power instead. I lived the rest of my days as a mortal woman under {mf\|his\|her} roof, with…” | 80/H | Retrospective chosen company must fit keep/file/burn; remove lifelong roof/hallway assertion after departure. Native judgment remains and altered fate applies only on current Trickster. |

### areelu.lastcall.page

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| page | “I will record, since I am obliged to record everything, that the wager was settled. Whoever burned at Threshold was to pay. I have gone over the terms many times since, looking for the fl…” | 75/H | Coordinator correction: intact hands, actual encounter memory, personal wound received not Worldwound ceded, and flask only in its earned history. Call-in debt buys no love or free arrival. |
| page/Paragraphs[0] | “At the rift the Commander called in our wager, and told me to take notes. I did. They are appended. They are very thorough.” | 75/H | Coordinator correction: intact hands, actual encounter memory, personal wound received not Worldwound ceded, and flask only in its earned history. Call-in debt buys no love or free arrival. |
| page/Paragraphs[1] | “I ceded the Wound. I have not regretted it, which I record here because I promised to regret nothing, and I keep my promises when they are also my conclusions.” | 75/H | Coordinator correction: intact hands, actual encounter memory, personal wound received not Worldwound ceded, and flask only in its earned history. Call-in debt buys no love or free arrival. |
| page/Paragraphs[2] | “The flask is mine. I made it. The Commander carries it. I have not tried to take it back, and I would like whoever reads this to understand how much that restraint costs me.” | 75/H | Coordinator correction: intact hands, actual encounter memory, personal wound received not Worldwound ceded, and flask only in its earned history. Call-in debt buys no love or free arrival. |

### areelu.early.courtesy_freed

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| silent | “She tilts her head and watches you say nothing, the way a collector watches a specimen that has not yet decided to move. Then she studies you, and smiles.” | 91/K | Recognition only: keep mask recognition unsensual; no invented touch or attraction. |
| offered | “"That's what someone would say who wanted me to think it was curiosity." The smile does not change at all.” | 91/K | Recognition only: keep mask recognition unsensual; no invented touch or attraction. |

### areelu.early.courtesy_refused

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| silent | “She tilts her head and watches you say nothing, the way a collector watches a specimen that has not yet decided to move. Then she studies you, and smiles.” | 91/K | Recognition only: keep mask recognition unsensual; no invented touch or attraction. |
| offered | “"Now I have two things to weigh: what you did, and what you would like me to believe about it." She sounds delighted, and looks nothing of the kind.” | 91/K | Recognition only: keep mask recognition unsensual; no invented touch or attraction. |

### areelu.lastcall.call

| Node / paragraph | Existing passage (one-line excerpt) | Rating / action | Situation-level treatment |
|---|---|---|---|
| call | “Across the rift, Areelu Vorlesh folds her one hand over the wrist that has none, and watches you the way she has watched you since Iz: as a result she has not finished recording.” | 75/H | Coordinator correction: intact hands, actual encounter memory, personal wound received not Worldwound ceded, and flask only in its earned history. Call-in debt buys no love or free arrival. |

Initial inventory: 179 individually quoted nodes/paragraphs. Boundary rows deliberately include nonsexual hand contact, vulnerability and social reactions so that the heat pass does not accidentally sexualize them.

### Additional class-sweep anchors

The read-only second sweep below adds missed refusal, settlement and treatment siblings. Each scene ID is repeated because these rows span hosts. Pure scenery matches were reviewed separately: hunters/scarecrow's robe, crossroads/rift's sleeping creature and buy_witch's eye contact, prison/cell's stone bed, and visitors/nenio_after's Commander asleep in a chair contain no intimate action and need no heat change.

| Scene ID | Node / paragraph | Existing passage | Rating / action | Situation-level treatment |
|---|---|---|---|---|
| areelu.trickster.wager.raised | afraid | “You cannot be calculated. That is the whole of my objection, Commander, and it is enough. The answer is no.” | 94/K | Keep the repeated refusal and blood-stained wrist nonsexual. No taunt or test turns her no into a yes. |
| areelu.trickster.wager.at_threshold | worse | “Because you came late, and I have never rewarded lateness. Because I am bleeding and you are not.” | 91/K | Preserve harsh late settlement, not romantic debt; her medical condition does not imply incapacity in every conversation but precludes immediate bed staging. |
| areelu.trickster.finale.rewrite | end/Paragraphs[2] | “She collected it the same night, with a silver probe, and it never closed again for anyone but her.” | 84/H | Actual wound collection/treatment, no explicit slot. Make survival work concrete; reconcile H1 and the actual price without making her sexual access the cure. |
| areelu.trickster.report.wound | take | “You think I bet on your wound so that I could cut it out of you in your sickbed, like a thief?” | 91/K | Preserve treatment versus ownership distinction; split unconditional cession from conditional original bet. No sexual sickbed or denial of Pharasma's prior soul claim. |
| areelu.trickster.finale.report_stands | end/Paragraphs[1] | “She lived, and she paid her stake to the last page, in front of the Commander, in a single night. Then she left.” | 88/H | This night is settlement, not sex. Actual payment matches the term/burn history; no company or later household after a refused raise. |
| areelu.trickster.finale.report_stands | end/Paragraphs[2] | “Ask me again some year when you are not holding one, and I will tell you no again, and we will both know I considered it.” | 95/K | Retain her considered refusal and the original exit. Do not turn this coda into free reunion or an intimacy hook. |

Final inventory: **185 individual nodes/paragraphs**. The remaining nonintimate scenes, including native crystal/cauldron/ascension operations, stake-only/death settlements and former-half-demon afterlogue, were read for presence and body-state continuity; no extra intimate scene is implied by their names or procedural hand gestures.
