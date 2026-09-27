# Eliandra Trickster opening development report

## Status

This is a 3,164-word authored opening experiment, not a complete romance route.

The new source is unregistered and has not been independently reviewed or approved for integration.

It does not meet the project requirement of at least 21,000 meaningful words for a complete individual route.

No score is assigned to this draft, and no content is ready for in-game testing.

The draft proposes an adult, reciprocal attraction, but it does not assume Eliandra welcomes the Commander, change her duties, or commit her to romance.

## Canon checked

Evidence was inspected in the local game-dialogue extracts `reference/canon-review/candidate-inventory-dialogue.json` and `reference/canon-review/candidate-extra-mentions.json`, the official candidate summary in `reference/canon-review/additional-candidate-table.md`, and the extracted etude manifest in `reference/expansion/etudes.json`.

The requested `reference/story-review/Areelu-concept-evidence.txt` was also checked for its Pulura references, including the Inheritor's account of Eliandra and Katair's self-sacrifice and Eliandra's reflection on Sarkoris's suspicion of arcane magic.

These are checked local source extracts; this task did not independently unpack or decode the game's original `.jbp` archives.

| Canon evidence | Source record | How the draft uses it |
| --- | --- | --- |
| Eliandra is high priestess of Pulura and describes the Commander as the first new face she has seen during the vigil. | `World/Dialogs/c3/Pulura_C3/Pulura_C3_main/ElyandraRanger_Intro/Cue_0001.jbp`, GUID `0bd02c57a78fd7f4e8b5b379d29280ec`. | Establishes first contact and her measured warmth toward a rare visitor. |
| Katair is leader of the holy guards, and the Hand describes a hundred years of voluntary isolation shared by Eliandra, Katair, and their comrades. | `ElyandraRanger_Intro/Cue_0002.jbp`, GUID `3fcae78bc3948ab4c8c8de778013099c`; `Cue_0003.jbp`, GUID `c0dd70f8eb05b8a4fb13342b5507958a`. | Keeps Katair a trusted fellow leader and refuses to recast their century together as a marriage. |
| Eliandra says isolation makes love, jealousy, discord, quarrels, and breakups a real community risk. | `Elyandra_main/Cue_0002.jbp`, GUID `c9f74d937a185d543a06273cdd21ca30`. | Supplies the central policy conflict and the Trickster's reversible trial proposal. |
| Eliandra may change her policy or retain it because of old wounds and feared chaos. | `Elyandra_main/Cue_0010.jbp`, GUID `dde53ed7a465f5a4c8062f7e82cb1ead; Cue_0011.jbp`, GUID `6692c6d1de7b1404cbd87079739a3a4e`. | The opening requires exactly one positively verified outcome and presents distinct dialogue for each. |
| The Herald says Eliandra discovered her gift at thirteen, served as healer and guide, and never married or had a family. | `HeraldPulura/Cue_0009.jbp`, GUID `24d719b48b3195949b3d96a5afb5721b`. | Grounds her long service and her uncertainty about a private life without claiming she regrets her calling. |
| Chapter 3's extracted Pulura-area etudes include an Eliandra default-actor entry. | `World/Etudes/Common/WrathOfTheRighteous/Chapter03_Extra/Chapter03_AreasDefault/PuluraFall/Pulura_NPC_DefaultActors/Pulura_NPC_Eliandra_DefaultActor.jbp`, GUID `a048f51d45b5268488cb32c383465115`. | Supports placing this opening in Chapter 3 while the Commander can still meet her at the shrine. A static etude entry alone does not prove runtime availability for every save. |
| The Hand reacts to the Echo of Deskari taking Eliandra from Pulura's Fall. | `HeraldChapel/Cue_0004.jbp`, GUID `45876b95070de8a43b4e2eb88bf7381d`. | Sets the hard chronology boundary after this Chapter 3 opening. |
| The Angel has a Chapter 4 rescue conversation with Eliandra. | `World/Dialogs/c4/Mythic_Angel/EliandraSaved/Cue_0001.jbp`, GUID `75eca543e0150f74b927fbd6694a90cb`. | Treated as Angel-specific evidence, not a universal post-capture actor source. |
| A Chapter 5 Pulura-shrine scene reports Eliandra alive and rescued from the Echo, then presents her thanking the Commander for saving the shrine. | `World/Dialogs/c5/PuluraFallsC5/PuluraLeaderSaved/Answer_0028.jbp`, GUID `fd419afa29e9cf146807aa3d91c3332e`; `Cue_0001.jbp`, GUID `860edc351f25b624296a572aa1f6c48f`. | Identifies a separate future post-rescue continuation point, subject to verifying its actual actor and quest-state conditions. It is not used to justify the Chapter 3 scene. |
| Eliandra says the community spent one hundred years studying the Worldwound and describes the Echo's attempt to exploit that research. | `PuluraLeaderSaved/Cue_0025.jbp`, GUID `53d10d142f76b964cb7e14ee305a642b`; `Cue_0031.jbp`, GUID `c12de8773867e9d49a4fdfedd804b8a7`. | Confirms that Chapter 5's rescued Eliandra has an independent quest-centered continuation opportunity. |
| The Inheritor recognizes that Eliandra and Katair helped protect Pulura's Fall through self-sacrifice. | `World/Dialogs/c3/Mythic_Angel/Targona/Cue_0014.jbp`, GUID `a528614125b07714db52d9004f36d448`. | Reinforces their joint duty without inventing a romantic bond between them. |

The candidate table likewise identifies Eliandra as a new-route candidate and explicitly warns that the reviewed evidence does not establish that she and Katair are spouses.

The canon excerpts establish no romance with the Commander.

The trial, private audience, attraction, evening invitation, and all custom states below are authored alternate developments.

## Opening design

The proposed scene occurs in Chapter 3 at Pulura's Fall, after a future source-bound reader confirms the native relationship-policy result and after Eliandra herself has invited the private audience.

The Trickster's authored intervention is a reversible one-week test of the rule, designed to reveal both the safety the rule was meant to protect and the costs of restricting the community's relationships.

People may remain silent, no partner must be named, and the community can retain the rule after the trial.

This creates a Trickster-specific opportunity through wit and political craft without presenting fourth-wall knowledge or a magical override of fate, duty, or consent.

The script gives Eliandra separate follow-up dialogue if she changed the rule and if she retained it.

The retained-rule branch cannot be reframed as coyness or a request to be overruled.

A Knowledge: World check at DC 25 tests whether the Commander can design a neutral record that accounts for the harms on both sides.

Success offers Eliandra a concrete draft to revise, while failure leaves the question unresolved and gives the player a respectful recovery choice.

Neither check outcome increases attraction or removes the need for her independent invitation.

The opening develops mature chemistry through explicitly stated adult interest, attentive observation, Eliandra's own admission that she has wondered what a kiss would feel like, and an optional, bounded hour together after her duties.

Her interest is not framed as payment for rescue, service, or policy reform.

Refusal, withdrawal, coercive flattery, demanding a kiss, or attempting to manipulate her closes the private route while keeping the temple's public quest help separate.

Katair remains an ally and co-leader, and neither his absence nor Eliandra's care for him is used as a jealousy device.

## State and chronology contract

`eliandra.native.rule_reformed_verified` and `eliandra.native.rule_retained_verified` are proposed mod-owned witness flags, not native etudes.

A future dialogue-history reader must positively identify exactly one native result by its cited cue GUID.

If both outcomes appear, neither is observed, or the witness cannot distinguish them, the scene must remain unavailable.

The scene additionally requires the Trickster path, confirmed Chapter 3 Pulura contact, a living and physically present Eliandra actor, and a separate native-history-backed invitation from Eliandra.

No such reader, actor validator, or invitation producer is implemented by this manuscript.

The scene is limited to Chapter 3 because that is the supported pre-abduction Pulura contact window used here.

The Chapter 4 Angel rescue does not supply other mythic paths with contact.

The Chapter 5 PuluraLeaderSaved scene is a credible later contact point in canon, but its quest-state and actor bindings need their own verification before a continuation can use it.

Other nine path routes, the complete Trickster route, all later relationship-state transitions, and game delivery are explicitly open.

The relationship metadata keeps `eliandra.trickster.romance_committed` unset throughout this opening.

Only the explicit answer welcoming another private conversation writes `eliandra.trickster.private_conversation_welcomed`.

That state means one more conversation, not romance, exclusivity, sexual consent, or a ToyBox setting.

## Structural checks

The opening contains one scene, 35 unique nodes, 97 choices, and 3,164 words of node text.

The word count includes spoken text and authored narration and excludes choice labels and development documentation.

The Python module imported successfully, serialized its scene to JSON, and passed `python -m py_compile`.

Running `python -m storylines.eliandra_trickster_opening` passed the local graph check for unique IDs, valid destinations, 35 reachable nodes, check-success and check-failure edges, and balanced narrative tags.

Additional assertions confirmed that the source IDs are populated, the two native decision flags are the required exclusive entry group, and no choice sets a romance-committed flag.

`git diff --check -- storylines/eliandra_trickster_opening.py` passed, and the source contains no em dash.

These checks do not register or compile the scene into the mod, verify Unity runtime conditions, confirm that a save can deliver the actor, test ToyBox compatibility, or constitute an independent quality review.

## Art and remaining route work

No art was created for this opening.

Any eventual portrait or scene art should preserve Eliandra's recognizable aasimar and priestess design, her dignified presence, and mature attractiveness without making beauty a substitute for characterization.

The complete route still needs at least 21,000 meaningful words across the selected playthrough, the user's ten-path access design, quest-linked progression, refusal and failure consequences, end states, source-backed actor delivery, ToyBox review, headless integration tests, an independent multi-rubric quality review above 90 in every required dimension, and manual in-game verification.

The proposed evening is only an opening beat and is not counted as a complete romance or as evidence that the full route can be completed in game.

## Exact source hash

SHA-256: `E5A0E454F476848269042CE101DF3C12A009B49497130A179642590AE408757B`.
