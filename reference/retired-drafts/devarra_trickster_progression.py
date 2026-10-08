"""Unregistered authored continuation for Devarra's Trickster experiment.

This follows the proposed Storyteller Tower opening only. The quest, gates,
custom flags, skill checks, and any continued actor presence are proposals,
not implemented game behavior.
"""

from collections import deque
from copy import deepcopy

from story_format import c, n, scene


SAVED = "devarra.brood.saved_verified"
LOST = "devarra.brood.lost_verified"
SAVED_CUE = "devarra.native_saved_brood_cue_seen"
LOST_CUE = "devarra.native_lost_clutch_cue_seen"
OPEN = "devarra.trickster.open"
REFUSED = "devarra.trickster.progression_refused"
TRUST = "devarra.trickster.record_trust"
PRIDE = "devarra.trickster.pride_respected"
MISTRUST = "devarra.trickster.record_mistrust"
WORLD_TRIED = "devarra.trickster.world_check_attempted"
PERCEPTION_TRIED = "devarra.trickster.perception_check_attempted"
WITNESS_TRIED = "devarra.trickster.witness_check_attempted"
ARCANA_TRIED = "devarra.trickster.arcana_check_attempted"
RECORD_LIMITED = "devarra.trickster.record_access_limited"
EVIDENCE_APPENDIX = "devarra.trickster.evidence_appendix_access"
PRIDE_NOTE = "devarra.trickster.devarra_annotation_access"
INVITED = "devarra.trickster.second_meeting_invited"
ROMANCE = "devarra.trickster.reciprocal_interest"
CASE_DONE = "devarra.trickster.slate_case_closed"
CASE_CHECK = "devarra.trickster.slate_inspection_attempted"
MEAL_DONE = "devarra.trickster.meal_scene_complete"
MEAL_ROMANCE_END = "devarra.trickster.first_date_complete"
LETTER_READ = "devarra.trickster.second_envelope_opened"
PLAN_READY = "devarra.trickster.doublehour_prepared"
PLAN_PUBLIC = "devarra.trickster.public_plan"
PLAN_PRIVATE = "devarra.trickster.private_plan"
FATE_CHECK = "devarra.trickster.doublehour_check_attempted"
MEETING_PERCEPTION = "devarra.trickster.bridge_perception_attempted"
MEETING_DIPLOMACY = "devarra.trickster.bridge_persuasion_attempted"
FATE_HELD = "devarra.trickster.doublehour_held"
FATE_BROKE = "devarra.trickster.doublehour_broke"
MESSENGER_SAFE = "devarra.trickster.messenger_safe"
MESSENGER_USED = "devarra.trickster.messenger_used"
LEAD_FOUND = "devarra.trickster.cistern_lead_found"
BUYER_BURNED = "devarra.trickster.lead_burned"
EXCHANGE_DONE = "devarra.trickster.exchange_complete"
CONSEQUENCE_DONE = "devarra.trickster.consequence_complete"
NEXT_FIRE = "devarra.trickster.next_fire_invited"
AFTER_FIRE_DONE = "devarra.trickster.after_fire_complete"
FALSE_FOLIO_READY = "devarra.trickster.false_folio_ready"

CONTRACT = {
    "status": "unregistered authored progression draft; no producer, actor continuation, or runtime condition exists",
    "entry": "Requires the separate proposed opening's devarra.trickster.open flag and one positively verified native history/cue pair. Neither requirement currently has a registered producer.",
    "canon": [
        "DLC1 Tower Cue_27 (8c53478782244b90a37f727f7b814318) presents Devarra saying demons captured her clutch and forced her to fight; its native condition recognizes DragonEggsReleased (4ba6fd446353825459f469fe5973fd87) or the completed egg project (4aa538f07bd542f7a013b90464577d67).",
        "DLC1 Tower Cue_0006 (d368680393304b5ba324dd5a517140ed) is the fallback account that her clutch was pillaged and her offspring died before birth. Do not treat it as proof that all histories lost the eggs.",
        "Main-campaign death uses RedDragonDead (581521b398fb9dd4eb52bbfffb3b5c43) and RedDragonKilledInIvorySanctum (056ba61e04cca104a9c95ac2d4658c67). DLC Devarra_dead (d713e8b772484376a7da810c37ab7922) is not a stand-alone main-campaign death predicate.",
    ],
    "authored_additions": [
        "A Tower-side evidence task reconstructing who used the clutch as leverage. It deliberately does not name an egg recipient, claim Nidalynn received Devarra's eggs, or claim to identify where any surviving egg went.",
        "The offered archive, testimony, evidence checks, private audience, attraction, and relationship flag are wholly new fiction and have no native hooks.",
        "A delayed encounter about an illicit copy of the sealed account and a separate consensual meal scene extend the relationship after the evidence work; both are authored additions with no native hooks.",
        "Saved brood and lost clutch are separate, mutually exclusive entry histories. Mercy, restoration, gratitude, and investigation success never set romance.",
        "The collector Vey, his teacher Serevin, the cistern, the lime kilns, the prisoner rescue, the receipt trap and the ruined watchtower are authored developments. Neither the shard nor the lamps establish a native resurrection mechanism.",
        "The lower-vault departure apparatus, copied nest sketch, targeting map, divided-power bargain and western ledge proposal are authored fiction. Destroying the collector network protects access already assumed; it does not implement initial resurrection or claim new facts about the clutch.",
        "Retreat forfeits the kiln cart's departure; the delayed return follows its permanent quarry destination and cannot recover Serevin or her ledger. The western house, Mareth, Oren, Talvren, drainage dispute, partnership choices and supplementary recollections are authored developments, not registered world changes or native campaign endings.",
    ],
    "paths": "Trickster-only proposal in this draft. Two unregistered retrospective partnership recollections do not implement native ending support. Other mythic path gates, the selected-content floor, main-campaign resurrection, actor delivery, art, ToyBox runtime behavior and in-game play remain unimplemented or unverified.",
    "design_rule": "Checks govern evidence quality or the Commander's access to an argument, never Devarra's attraction or consent. Failure continues into an honest, consequential path.",
}


def page(key, speaker, text, *choices):
    return n(key, speaker, text, *choices, portrait="Devarra")


SCENE = scene(
    "devarra.trickster.evidence_and_terms",
    "Ashes have witnesses",
    "Devarra",
    5,
    "return_to_tower",
    [
        page("return_to_tower", "Narrator", '''{n}You return to the Storyteller's tower with the answer Devarra demanded: not a name invented to fill a silence, but an index of the things the tower can still prove. Her wing is folded away from the bronze door. The invitation is not warm. It is not a summons either.{/n}

{n}A narrow table has been moved into the circular room. Three blank folios wait beside a bowl of charcoal. Devarra stands over them with the stillness of a judge who has not decided whether the court is worth holding.{/n}

"You said you would look for the hands that carried the eggs, the route, and a witness. Did you bring those, or did you bring another performance about fate?"''',
            c("Show the sources and let her inspect them before you explain.", "lay_out_sources"),
            c("Admit you found no reliable witness and ask whether she wants to stop.", "no_witness"),
            c("Say the Trickster can make any record say what it needs to say.", "coercion", flags=(REFUSED,))),
        page("lay_out_sources", "Commander", '''{n}You lay down only what you can authenticate: a copy of the contract that sent hunters to the Ivory Sanctum, an inventory of marks found on seized equipment, and a statement from a survivor whose account can be checked against the tower's older record. There is no list of the rescued eggs' later keepers. There is no hidden page naming a recipient. You tell her both absences before she has to ask.{/n}

"These can establish how the clutch became leverage. They cannot tell us where every egg went after it was carried to safety. I will not turn a gap in the archive into a convenient answer."''',
            c("Ask her to decide which source deserves attention first.", "choose_source"),
            c("Offer to read the testimony aloud, including what makes you look bad.", "read_statement"),
            c("Ask whether she wants the papers destroyed instead.", "destroy_option")),
        page("no_witness", "Devarra", '''"Then you have nothing to bring me except the fact that you returned." The answer comes fast enough to have been waiting behind her teeth.

{n}Her claws close around the edge of the table. The wood complains. You do not tell her to calm down, and you do not remind her that the tower offered a meeting. This was her invitation to speak, and it can end without becoming a debt.{/n}

"Do you want me to search longer, or do you want the matter closed?"''',
            c("Ask for one more attempt, with a fixed limit and no promise of success.", "limited_search"),
            c("Offer the blank folios to her and accept that the evidence may be gone.", "archive_without_witness"),
            c("Ask her to let you use fate to fill the gap.", "coercion", flags=(REFUSED,))),
        page("limited_search", "Commander", '''"One more search. I will name its limits: the old contract, the tower's surviving inventory, and a single witness who will not be bought by either of us. If those yield nothing, I stop. I won't keep turning your loss into an excuse to find you again."''',
            c("Use Knowledge (World) to compare the contract's dates and seals. DC 28.", flags=(WORLD_TRIED,), forbids=(WORLD_TRIED,), check=dict(Skill="SkillKnowledgeWorld", DC=28, Success="contract_success", Failure="contract_failure", CommanderOnly=True)),
            c("Ask Devarra which mark she recognizes, then accept her correction.", "dragon_eye"),
            c("End the search and offer no further meeting.", "end_no_pressure", flags=(REFUSED,))),
        page("archive_without_witness", "Devarra", '''"An honest empty page may be worth more than a thousand well-dressed lies." She taps the folio once, leaving a scorch at its corner.

"Do not write that this makes the clutch whole. If the young survived in the history I remember, they are still their own lives. If they did not, nothing you write here brings them back. The record is about the people who made eggs into a weapon, not a memorial that claims to repair me."''',
            c("Ask if she will choose what may be preserved.", "archive_terms"),
            c("Say you can leave the archive blank and depart.", "end_no_pressure", flags=(REFUSED,))),
        page("choose_source", "Devarra", '''"Start with the contract. The witness has reasons to hate the people who held the clutch, and hatred can sharpen a memory or bend it. The inventory may show whose hands touched the chain of events without telling us what those hands intended. A paper has no virtue, but it is less likely to flatter you."''',
            c("Examine the dates and compare the marks against the inventory. Lore (World) DC 28.", flags=(WORLD_TRIED,), forbids=(WORLD_TRIED,), check=dict(Skill="SkillKnowledgeWorld", DC=28, Success="contract_success", Failure="contract_failure", CommanderOnly=True)),
            c("Invite Devarra to perform the physical inspection while you take notes.", "dragon_eye"),
            c("Read the witness statement first, without concealing its uncertainty.", "read_statement")),
        page("contract_success", "Narrator", '''{n}The contract's seal is genuine, but the date beside its final authorization was added later. You find the difference because the same clerk used a hooked stroke in the older inventory. It is not proof of who ordered the change. It is proof that someone altered the trail after the seizure.{/n}

{n}You mark the disputed line in charcoal instead of circling it in triumph. Devarra looks at the folio, then at your hand. Her expression says she noticed that small choice.{/n}''',
            c("Show the discrepancy and state exactly what it does not prove.", "present_discrepancy", flags=(TRUST,)),
            c("Use the discrepancy to demand a private meeting as your reward.", "coercion", flags=(REFUSED,))),
        page("contract_failure", "Narrator", '''{n}The seal and date resist your reading. You cannot tell whether the altered line predates the seizure or was copied afterward. Devarra recognizes the mistake before you do. Her claw stops your hand before it smears the ink.{/n}

"Do not make the paper confess because you are embarrassed. Tell me what you know, then tell me what you do not."''',
            c("Name the uncertainty plainly and ask her to check the physical marks.", "dragon_eye"),
            c("Set the contract aside and read the witness statement instead.", "read_statement"),
            c("Pretend the failed reading is enough to accuse a target.", "false_accusation", flags=(MISTRUST,))),
        page("dragon_eye", "Devarra", '''{n}She takes the page between two talons and turns it toward the light. Her attention is clinical: pressure, ink, the dragged edge of a seal. A thin line of smoke escapes one nostril as she studies the marks.{/n}

"This stamp was handled by someone wearing a ring. That could be the clerk, a guard, a courier, or a person trying to make the mark look official. It does not tell us whose order this was." Her gaze lifts to yours. "You were about to make it tell you that, weren't you?"''',
            c("Admit the temptation and keep the interpretation narrow.", "present_discrepancy", flags=(PRIDE,)),
            c("Ask her to show you how she distinguishes evidence from a guess.", "teach_method"),
            c("Say that certainty matters more than the truth in a war.", "false_accusation", flags=(MISTRUST,))),
        page("present_discrepancy", "Commander", '''"Someone changed a date. The record cannot identify the hand or tell us whether that person knew what the demons had done. We can preserve the discrepancy and search for corroboration. I won't name a culprit until the evidence supports one."''',
            c("Offer to hear the witness under terms Devarra sets.", "witness_terms"),
            c("Ask whether she wants the names in the public record withheld.", "privacy_terms"),
            c("Put the contract away and let her decide whether to continue.", "archive_terms")),
        page("false_accusation", "Devarra", '''"No." The word is quiet. The fire is not.

{n}Heat rolls across the table without touching the folios. The ring-shaped mark on the paper darkens. Devarra looks at you as though measuring the distance between an error and a choice.{/n}

"You have no name. You want a villain because then you can strike something and call the sound justice. I know vengeance. Do not mistake that for permission to spend mine."''',
            c("Withdraw the accusation, record the uncertainty, and accept the damaged evidence.", "repair_record", flags=(MISTRUST,)),
            c("Stand by the accusation and leave her out of the inquiry.", "end_refused", flags=(REFUSED,))),
        page("repair_record", "Commander", '''"I wanted an answer more than I wanted a true one. I withdraw the accusation. The record stays damaged, and I will not ask you to pretend I handled it well."''',
            c("Correct the record and end the inquiry for today.", "repair_resolution"),
            c("Leave the damaged folio with her and ask for no reassurance.", "repair_resolution")),
        page("repair_resolution", "Devarra", '''"You corrected it because it was wrong. That does not restore the confidence you spent, and it does not make me responsible for repairing it." She checks that the accusation is gone, then keeps the folio on her side of the table. "The witness is finished for today. I will decide whether I want another inquiry."''',
            c("Accept that the next decision belongs to her and end the meeting.", "end_open"),
            c("Leave the corrected record and ask nothing more of her.", "end_no_pressure")),
        page("read_statement", "Commander", '''{n}The witness's statement does not make a clean story. It describes a route through hostile territory, then corrects itself: one turn may have been a second journey remembered out of order. The writer admits fear and hatred. No line claims knowledge of where the eggs were taken after their rescue. You read that part twice so it cannot become a footnote.{/n}

"This is an account of coercion and movement, not a map to your family. I can preserve it as testimony, but it needs another witness before anyone calls it settled."''',
            c("Ask Devarra what she would need before hearing the witness.", "witness_terms"),
            c("Use Diplomacy to ask the witness for a second statement without pressure. DC 30.", flags=(WITNESS_TRIED,), forbids=(WITNESS_TRIED,), check=dict(Skill="SkillPersuasion", DC=30, Success="witness_success", Failure="witness_failure", CommanderOnly=True)),
            c("Let the witness's statement stand alone as uncertain.", "archive_terms")),
        page("witness_success", "Narrator", '''{n}You state the limits before the witness speaks: no one will trade testimony for pardon, shelter, or a meeting with Devarra. The witness changes one detail and keeps another. The route's first landmark is corroborated by the inventory; the second remains uncertain. A new statement that admits what it cannot prove is more useful than a rehearsed confession.{/n}

{n}Devarra does not praise your charm. She does look at you differently when you refuse to use it as a leash.{/n}''',
            c("Offer both statements and the uncertainty to Devarra for her judgment.", "weigh_evidence", flags=(TRUST,)),
            c("Ask permission before preserving the witness's name.", "privacy_terms")),
        page("witness_failure", "Narrator", '''{n}Your questions close the witness down. They hear a promise of safety as a promise of reward and decide you are trying to purchase their account. They will not speak again today.{/n}

{n}The mistake costs you the corroboration. Devarra does not turn this into a test you can retry until she likes the result.{/n}

"You made the witness think their words were currency. If you want to continue, you will have to accept that you lost the cleanest chance to hear them."''',
            c("Accept the failure and preserve the first statement with its limits.", "archive_terms", flags=(MISTRUST,)),
            c("Ask Devarra to arrange another witness herself.", "pride_test"),
            c("Try to compel the witness with Trickster magic.", "coercion", flags=(REFUSED,))),
        page("teach_method", "Devarra", '''"You do not distinguish them by being clever. You ask what else would have to be true if your guess were right. You look for a fact that could prove you wrong. Then you let it." She places the contract beside the inventory. "I have been wrong. I have been lied to. Those are not the same experience, and neither makes every next answer mine to choose."''',
            c("Use Perception to compare the wear on the seal with the inventory copy. DC 27.", flags=(PERCEPTION_TRIED,), forbids=(PERCEPTION_TRIED,), check=dict(Skill="SkillPerception", DC=27, Success="mark_success", Failure="mark_failure", CommanderOnly=True)),
            c("Ask her to check your reasoning without taking the page from her.", "mark_failure"),
            c("Tell her you already know how she thinks.", "pride_test")),
        page("mark_success", "Commander", '''{n}You find the hooked stroke repeated on the inventory, but the pressure is different. It could be the same hand writing in haste, or another hand copying a familiar mark. You record both readings and refuse to select one merely because the first is more satisfying.{/n}

"The mark can help us test a later claim. It cannot tell us whose fingers held the pen."''',
            c("Let Devarra decide whether that is enough evidence to proceed.", "weigh_evidence", flags=(TRUST,)),
            c("Ask what she wants preserved for a later inquiry.", "privacy_terms")),
        page("mark_failure", "Devarra", '''The marks will not resolve into a story. You can keep searching, but the more time you spend over the same marks, the more likely you are to begin seeing what you hoped to find.

"Stop here. A failed search is information about the search. It is not proof that the person you suspect did it."''',
            c("Stop and write down the uncertainty.", "weigh_evidence", flags=(MISTRUST,)),
            c("Ignore her warning and accuse the witness.", "false_accusation", flags=(MISTRUST,))),
        page("witness_terms", "Devarra", '''"Before the witness hears my name, there are terms. They are not a bargain for me. They are a limit on what you are allowed to make this inquiry do." She counts them on one talon. "No pardon for testimony. No private threat. No promise of my attention. No story that calls a person a liar because their memory has holes."''',
            c("Agree and repeat the terms back exactly.", "privacy_terms", flags=(PRIDE,)),
            c("Invite the witness to review the statement from the far side of the open door.", "witness_presence"),
            c("Offer to keep Devarra's name out of the record unless she asks otherwise.", "privacy_terms"),
            c("Reject the limits and demand the witness's name.", "end_refused", flags=(REFUSED,))),
        page("witness_presence", "Narrator", '''{n}You leave the bronze door open. The witness waits in the outer passage, close enough to see the folios and far enough away to leave without crossing Devarra's shadow. Their face is turned partly aside. They have already said they will not identify themselves to the archive, and you repeat that the name is not needed to preserve the account.{/n}

{n}Devarra remains by the table. She does not loom over the witness or pretend that her presence is neutral. She asks whether they want her out of sight. The witness looks at her, then at you, and says they would rather see the dragon than wonder what was hidden behind the door.{/n}

"I remember the route in pieces," the witness says. "I remember what it felt like to be told the eggs mattered more than the people forced to carry them. I do not remember every turn. I will not swear that my fear gave me a perfect map."''',
            c("Ask which detail they remember most clearly, then let them stop there.", "witness_detail"),
            c("Ask them to correct the statement themselves without defending your copy.", "witness_detail"),
            c("Ask Devarra to question them for you.", "witness_boundary")),
        page("witness_detail", "Commander", '''"The first mark on the road was a split stone. I know because I cut my hand on it. The turn after that, I cannot tell you. There were two walls, maybe three. A guard shouted in a language I didn't know. I remember the sound of the eggshells shifting when the basket changed hands. I cannot tell you who carried them after we reached the next place."''',
            c("Record the split stone as a remembered detail and leave the unknown turn blank.", "witness_boundary", flags=(TRUST,)),
            c("Ask permission to compare the mark with the inventory later.", "witness_boundary"),
            c("Press for the next turn because a complete map would help Devarra.", "witness_pressure")),
        page("witness_pressure", "Devarra", '''"Enough." Devarra's voice cuts through the question. The witness has stepped backward. You see it only after she says it: they are no longer looking at the paper. They are watching the door.

"You are asking for a map because you want to help me. That does not make the answer yours to take." She does not move toward the witness. Her anger is aimed at the space you have made, not at the frightened person standing in it. "They said what they remember. You can keep that, or you can stop pretending their uncertainty is a refusal to cooperate."''',
            c("Apologize, close the interview, and preserve only the volunteered detail.", "witness_boundary", flags=(MISTRUST,)),
            c("Ask the witness to leave and accept the lost chance for corroboration.", "witness_boundary", flags=(MISTRUST,)),
            c("Tell Devarra she has no right to interrupt your interview.", "end_refused", flags=(REFUSED,))),
        page("witness_boundary", "Devarra", '''The witness chooses to stay for one more question, then holds up a hand before you can ask it. "Do not make me say the same thing twice so the sentence sounds more certain. If the record says I gave you a route, it lies. I gave you a stone, a sound, and what I thought the movement meant. That last part is a guess."''',
            c("Write down the distinction between memory and inference.", "weigh_evidence"),
            c("Ask whether the witness wants their testimony withdrawn from the archive.", "archive_terms"),
            c("Tell them the record needs certainty more than their consent.", "end_refused", flags=(REFUSED,))),
        page("privacy_terms", "Commander", '''"The record can name the institutions and acts it can prove. It can omit private names unless they are necessary to prevent another harm and you agree that the evidence supports publishing them. You can review the account before it leaves this room. The witness can withdraw their own name. Neither choice changes the facts we keep."''',
            c("Ask Devarra whether she wants the record public, sealed, or destroyed.", "record_choice"),
            c("Tell her you will preserve her right to stop the inquiry.", "record_choice", flags=(PRIDE,)),
            c("Ask what vengeance would mean to her now, without proposing a target.", "vengeance_question"),
            c("Say the archive belongs to the Commander now.", "end_refused", flags=(REFUSED,))),
        page("archive_terms", "Devarra", '''"I will decide what happens to the account. Not because the evidence is mine to alter, but because the story is about what was done to me and to my clutch. The facts can be preserved without making them public. The witness can keep their name. I can keep mine out of it. You may still leave this room without asking me to make that decision comfortable for you."''',
            c("Offer her the sealed, private record with no use without her consent.", "record_choice"),
            c("Offer to destroy the copy and let her keep the original.", "record_choice"),
            c("End the meeting without creating a record.", "end_no_pressure")),
        page("destroy_option", "Devarra", '''"If I ask you to burn it, you burn it. If I ask you to keep it, you keep it under my terms. Do not make destruction another gesture you can perform for applause." She watches the charcoal bowl. "I want to know whether the record can be used to stop someone from turning a clutch into leverage again. I do not know yet whether I want to read it after that."''',
            c("Offer a sealed copy under her control, with no use without her assent.", "record_choice"),
            c("Offer destruction now and leave the decision to her.", "record_choice"),
            c("Tell her you will decide once you know what is useful.", "end_refused", flags=(REFUSED,))),
        page("weigh_evidence", "Devarra", '''She studies the folios without asking you to narrate them. The contract shows an altered date. The statement gives a route but admits one uncertain turn. The inventory connects one mark without identifying its maker. None of it tells you where the eggs went after their rescue. None of it makes the dead unborn children less dead in the history she has named.

"There is enough here to describe how a person can be made into a hostage through what they love. There is not enough to punish a particular hand. What do you want this record to do?"''',
            c("Create a sealed warning about methods, not an unsupported accusation.", "record_choice", flags=(TRUST,)),
            c("Preserve the evidence privately for another witness.", "record_choice"),
            c("Destroy it if that is what she chooses.", "record_choice")),
        page("pride_test", "Devarra", '''"You want me to arrange your recovery after you failed to listen. That is a peculiar way to prove you can hear a no." Her mouth bends, not quite a smile. "You may ask for advice. You may not make my help the price of my company."''',
            c("Apologize and accept that she may refuse to help.", "privacy_terms", flags=(PRIDE, PRIDE_NOTE)),
            c("Ask one narrow question about what a dragon would consider a fair record.", "archive_terms"),
            c("Tell her that she owes you a chance to try again.", "end_refused", flags=(REFUSED,))),
        page("record_choice", "Devarra", '''"I choose a sealed account, held here until I decide whether to release it. It will say what the evidence shows: someone altered a date, a witness remembers a route imperfectly, and the clutch was used as leverage. It will not pretend to know where every egg went. It will not call mercy a debt or loss a lesson for the Commander."''',
            c("Accept her wording, make the record, and ask for no reward.", "sealed_record", flags=(TRUST,)),
            c("Ask whether she wants you to sit with her after the work is done.", "after_record_invitation"),
            c("Ask whether she wants revenge, justice, or neither from this inquiry.", "vengeance_question"),
            c("Insist that a public accusation would be more satisfying.", "end_refused", flags=(REFUSED,))),
        page("vengeance_question", "Devarra", '''"You ask that as if the choices came in separate bowls." A spark runs along one horn. "I want the people who made my clutch a weapon to understand what it cost. I want no one to try it again. I want some of them afraid. I want some of them dead. I also know that wanting does not make every act wise, and that rage can make a poor map."''',
            c("Say that you will help identify the people responsible before choosing a response.", "vengeance_terms"),
            c("Offer to destroy the records and leave the guilty unexamined.", "vengeance_terms"),
            c("Promise to punish a particular person despite lacking a supported name.", "false_accusation", flags=(MISTRUST,))),
        page("vengeance_terms", "Devarra", '''"I have no name to give you. The ledger has a false date; the witness has a broken route; the inventory has a mark without a hand. If you promise me a throat, you are promising to invent one." Her tail makes a hard line through the ash. "But if you find someone who is still using hostages, I will not ask you to persuade them with a pamphlet. I want the threat stopped. I want the choice to be mine when the evidence is real."''',
            c("Use Knowledge (Arcana) to separate a current magical trace from old residue. DC 31.", flags=(ARCANA_TRIED,), forbids=(ARCANA_TRIED,), check=dict(Skill="SkillKnowledgeArcana", DC=31, Success="trace_success", Failure="trace_failure", CommanderOnly=True)),
            c("Tell her the inquiry ends at the facts already verified.", "sealed_record"),
            c("Say you will not let her choose how far the punishment goes.", "end_refused", flags=(REFUSED,))),
        page("trace_success", "Narrator", '''{n}The mark has been handled more recently than the rest of the page, but the ink carries no reliable spell signature. You can establish that someone revisited the record. You cannot establish that the same person ordered the seizure, that the trace belongs to a demon, or that anyone remains nearby. Devarra watches you cross out the conclusion you were tempted to write.{/n}

"A thread to follow, then. Not a name. We can look for a present danger without pretending the past has become simple."''',
            c("Record the trace as an unverified lead and wait for corroboration.", "sealed_record", flags=(TRUST,)),
            c("Ask her to set the next inquiry's limits and choose whether to join it.", "after_record_invitation")),
        page("trace_failure", "Devarra", '''{n}You cannot separate the old residue from the later handling. The mark may be ordinary ink, or it may have passed through magic that left no trace you can read. The answer is not hidden in the failure; the failure is the answer available today.{/n}

"I am still angry. I am not less angry because you failed to find me a target. We stop before the need for a target starts making one up."''',
            c("Accept the limit and keep the account sealed.", "sealed_record", flags=(PRIDE,)),
            c("Tell her any future search is hers to request.", "sealed_record"),
            c("Claim your power can make the absent evidence irrelevant.", "coercion", flags=(REFUSED,))),
        page("sealed_record", "Narrator", '''{n}You write the account in her words where they are testimony and in yours where they are inference. The distinction takes longer than the ink. Devarra interrupts twice, once to remove a claim you had overstated and once to add a detail she wants preserved. You do not turn either correction into a joke.{/n}

{n}When the seal cools, she keeps it. The table between you no longer looks like an altar to a lost answer. It looks like work that can be resumed if she decides it should be.{/n}''',
            c("Ask whether the work is enough for today.", "after_record_invitation"),
            c("Offer to leave before the silence asks anything of her.", "end_no_pressure")),
        page("after_record_invitation", "Devarra", '''"For today, yes." She rolls one shoulder, and the old scar beneath the wing catches the firelight. "I asked you back because I wanted to know whether you would bring a name or a record. You brought the record. That is not the same as earning my trust. It is a start that does not insult my judgment."''',
            c("Ask whether she would choose a second meeting after the evidence rests.", "private_audience"),
            c("Say you would like to speak again, but accept her refusal.", "private_audience"),
            c("Leave the next move entirely to her.", "end_open")),
        page("private_audience", "Commander", '''"There is something I have not said because I did not want to smuggle it into the evidence. I want your company. I want to know what you choose when no one is making you fight, no egg is being held over you, and I am not offering a useful document in exchange. I am attracted to you. You do not owe me a reply."''',
            c("Wait without moving nearer.", "chemistry_answer"),
            c("Clarify that she can decline without losing the sealed record or future aid.", "chemistry_answer"),
            c("Use a Trickster fate rewrite to make the answer favorable.", "coercion", flags=(REFUSED,))),
        page("chemistry_answer", "Devarra", '''A low sound rolls in her throat. It is not a growl, though it could become one. Her gaze travels over you without apology, pauses at your mouth, and returns to your eyes.

"You have a dangerous habit of making an offer that leaves me room to refuse. I find that more interesting than your usual tricks." She steps closer by a measured pace, then stops before the gap belongs to either of you. "I am attracted to the mind that knew when not to finish a sentence. I have not decided what I want to do with that."''',
            c("Ask whether you may touch her face, and wait for a spoken answer.", "touch_request"),
            c("Tell her the attraction is mutual and leave her distance intact.", "mutual_interest", flags=(ROMANCE,)),
            c("Ask her to decide whether there will be another meeting.", "end_open")),
        page("touch_request", "Devarra", '''"My face is not a prize for asking beautifully." Her eyes hold yours. The test in the words is real; so is the heat close enough to feel against your skin. "I am considering it because I want to. If I say no, you stop. If I say yes, you still stop the moment I ask. Can you hear both halves?"''',
            c("Say yes, and keep your hands where she can see them.", "touch_consent"),
            c("Say you would rather she initiate any touch.", "mutual_interest", flags=(ROMANCE,)),
            c("Treat the question as a boundary and end the private audience.", "end_open")),
        page("touch_consent", "Commander", '''"Yes. Both halves." You do not reach. Devarra studies you, then tips her head forward until the warm ridge above her eye rests lightly against your palm. Her scales are smooth in some places and rough where old battles have marked them. She lets the contact last for one breath, then withdraws by her own choice.

"That is enough." She says it without shame or apology. You lower your hand at once.''',
            c("Thank her and ask what she wants next.", "mutual_interest", flags=(ROMANCE,)),
            c("Say nothing and give her the room back.", "end_open")),
        page("mutual_interest", "Devarra", '''"If this becomes anything, it will be because we both keep choosing it. Do not make the Tower's impossible timing into destiny. Do not call my anger foreplay because it makes a better song. And do not make the children I lost or the eggs I remember into a price I paid for your attention."''',
            c("Agree: her history stays hers, and each meeting remains optional.", "relationship_terms", flags=(ROMANCE,)),
            c("Ask whether she prefers to speak again in private or among witnesses.", "relationship_terms", flags=(ROMANCE,)),
            c("Say you wanted conquest, not a choice that could be withdrawn.", "end_refused", flags=(REFUSED,))),
        page("relationship_terms", "Devarra", '''"Then the next meeting is mine to request. You can say no. I can change my mind after I request it. If you use your power to make a path easier, it may open a door or move a body; it cannot write my answer. The sealed record remains sealed whether I want you tomorrow or never again."''',
            c("Accept the terms and leave the Tower without claiming a promise.", "end_interest", flags=(INVITED, ROMANCE)),
            c("Ask if she wants to make a concrete second meeting now.", "schedule_meeting", flags=(ROMANCE,)),
            c("Say that a Trickster can decide better than she can.", "coercion", flags=(REFUSED,))),
        page("schedule_meeting", "Devarra", '''She looks toward the bronze door, then back at you. "Not tonight. There is a difference between wanting to see you again and consenting to spend every hour proving it. I will ask when I have chosen the place and the hour. If you are busy, you may decline without turning it into a test."''',
            c("Accept, and let her be the one to send the next invitation.", "end_interest", flags=(INVITED, ROMANCE)),
            c("Say that you would rather leave the future undecided.", "end_open")),
        page("coercion", "Devarra", '''The tower's shadows bend at your command. Devarra's eyes flare, and the bronze latch snaps shut between you. For one instant every trick you could make is visible in the room: a false memory, a forced word, a convenient version of her desire.

"You asked whether I would choose you. Then you reached for the answer." Her voice drops. "No. My answer is no. Not because you failed a test. Because I refuse to be another thing you rewrite when it inconveniences you."''',
            c("Release the distortion, leave immediately, and accept the refusal as final.", "end_refused", flags=(REFUSED,))),
        page("end_no_pressure", "Narrator", '''{n}You gather nothing from the table except your own papers. Devarra keeps the sealed record and the right to decide whether the inquiry continues. You leave without asking her to console you for the work's limits.{/n}

{n}The eggs' histories remain separate. The record does not claim a rescue it cannot prove, and it does not turn grief into proof of a romance. Whatever your next meeting might be, it cannot be purchased by the hours spent here.{/n}'''),
        page("end_open", "Narrator", '''{n}You leave the Tower with no promise and no claim. Devarra's answer, if there is one, remains hers to give in another scene that has not yet been written. The sealed account is still hers to open or keep closed.{/n}

{n}You do not turn one meeting into a route merely by naming it. You can be welcome today and refused tomorrow. She can be interested without being ready, or decide the interest has passed. That uncertainty is not a puzzle for your power to solve.{/n}'''),
        page("end_interest", "Narrator", '''{n}Devarra keeps the sealed account. She has chosen the next invitation, not a permanent bond, a confession, or a promise to ignore what happened between you in other histories. Your interest is mutual for this moment because both of you named it without a threat or price.{/n}

{n}A later scene would still have to earn its own place. Her anger can return. Your choices can make her wary. She can withdraw her invitation, and the route must honor it. The Tower's strange chronology does not erase those consequences.{/n}'''),
        page("end_refused", "Narrator", '''{n}The exchange ends on Devarra's terms. She has refused the inquiry, the private audience, or the use of fate as leverage. No hidden flag records her as secretly won over. No later scene may reinterpret this refusal as flirtation.{/n}

{n}A future Trickster repair could be authored only if she independently chose to reopen contact. It would need to address what you did and allow her to keep the refusal. This draft contains no such producer and grants you no second attempt.{/n}'''),
    ],
    requires=("trickster", OPEN, "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED,),
    delay=0,
    last=5,
    optional=True,
    Relationship="devarra.trickster",
    ManualOnly=True,
    Remote=False,
    PhysicalPresenceRequired=True,
    ContactUnit="Devarra",
)


SCENE["RequiresAnyGroups"] = [(SAVED, LOST), (SAVED_CUE, LOST_CUE)]
SCENE["Forbids"].append("devarra.trickster.progression_complete")


FOLLOWUP_SCENE = scene(
    "devarra.trickster.the_echoing_slate",
    "The echoing slate",
    "Devarra",
    5,
    "followup_arrival",
    [
        page("followup_arrival", "Narrator", '''{n}The letter arrives in a hand that is not Devarra's. Its words are spare: the sealed account was copied, the copy is moving through the old service passages beneath the Tower, and she wants you at the west stair before dawn. It ends with a line in her own clawed script: Come because you choose to. Bring no audience.{/n}

{n}You find her beside a narrow window. The dawn paints copper along the edge of one horn, then disappears when a cloud passes. She has not brought the folio. That is deliberate. The problem is the new copy, not the record she chose to keep.{/n}

"Someone thinks a story about my clutch can be sold. I want to know who, and I want the account back. I have not decided what happens to the person carrying it."''',
            c("Ask what she needs from you before you choose a plan.", "set_terms"),
            c("Offer to find the carrier and bring them here alive.", "shared_plan"),
            c("Promise to make the copy disappear by whatever means are easiest.", "hard_plan")),
        page("set_terms", "Devarra", '''"First: no one touches the sealed original. Second: the copy is not proof of who ordered the old seizure. Third: if the carrier is being forced, they leave alive. Fourth: do not make a spectacle of saving me from a danger I have not asked you to face." She watches to see whether you hear the last term as well as the first three.

The passage below has two exits. One opens onto a public stair used by scribes and servants. The other leads to a disused cistern where the letter says the exchange will happen. There is time to check the route, but not to inspect every stone twice.''',
            c("Agree to the terms, then inspect the cistern threshold for a fresh ward. DC 29.", flags=(CASE_CHECK,), forbids=(CASE_CHECK,), check=dict(Skill="SkillPerception", DC=29, Success="ward_found", Failure="ward_missed", CommanderOnly=True)),
            c("Let Devarra select the approach and follow her lead.", "shared_plan"),
            c("Tell her the terms are useful only if you retain the right to act alone.", "hard_plan")),
        page("shared_plan", "Devarra", '''She studies your face for the first hint that you will take her answer as permission to command the room. Finding none, she taps one talon against the stone.

"We go through the public stair. I will be visible. You stay where the carrier can see that the exit is not blocked. If they run, you do not chase them into the cistern. If someone else comes out, I will decide whether to follow." Her mouth tilts by a fraction. "You may have an opinion. You may even be right. We will find that out when there is something real to disagree about."''',
            c("Ask her what signal she wants if the carrier is not alone.", "approach"),
            c("Say you trust her to call the retreat.", "approach")),
        page("hard_plan", "Devarra", '''"No." She does not raise her voice. The word lands with enough weight to stop your next sentence.

"You do not get to invoke the Trickster as if it were a second commander in this room. If the copy is there, we take it. If the carrier is a threat, I will answer that threat. You may decide whether you can work beside that. You may not decide that your power makes my judgment decorative." She waits, and leaves the choice with you.''',
            c("Withdraw the promise and agree to coordinate with her.", "approach"),
            c("Insist that she accept your plan or lose your help.", "case_refused", flags=(REFUSED,))),
        page("ward_found", "Commander", '''{n}The scratch beside the threshold is too regular to be a crack. A thin line of magic runs under the dust and loops back on itself. It is a warning ward, not a trap: someone wanted to know when the cistern door opened, not kill whoever crossed it.{/n}

You show Devarra where the line begins and where it ends. She crouches beside it, careful not to touch the chalk. "Good. We know they expect company. We do not know whether they expect me."''',
            c("Leave the ward intact and use the public stair as planned.", "approach"),
            c("Disarm the alert before either of you enters. DC 30 Arcana.", flags=("devarra.trickster.slate_arcana_attempted",), forbids=("devarra.trickster.slate_arcana_attempted",), check=dict(Skill="SkillKnowledgeArcana", DC=30, Success="ward_disarmed", Failure="ward_triggered", CommanderOnly=True))),
        page("ward_missed", "Narrator", '''{n}The dust disguises the ward's line. Your boot breaks the chalk when you step toward the cistern. A small click answers from beyond the door, followed by the scrape of someone moving a chair.{/n}

Devarra does not blame you for a failed reading. She does look at the door, then at the public stair. "We can still choose. A mistake is not a command to keep going the same way."''',
            c("Take the public stair and let the carrier see both of you arrive.", "approach"),
            c("Use the warning to demand a surrender from the other side.", "approach")),
        page("ward_disarmed", "Commander", '''The glow thins under your fingers and goes dark without a flare. You have removed the warning, not learned who placed it or what they intended. Devarra waits until you say that distinction aloud.

"Fine. We know the door will not announce us. We do not know whether the person behind it is afraid, armed, or both."''',
            c("Enter together and keep the public stair clear behind you.", "approach"),
            c("Let Devarra enter first after she chooses the pace.", "approach")),
        page("ward_triggered", "Narrator", '''{n}The ward folds in on itself before you can lift the second strand. A bell rings once beneath the stone, then stops. You cannot tell who heard it.{/n}

Devarra's eyes narrow. "We have spent surprise. That is all. Do not turn one lost advantage into a reason to gamble with the carrier's life."''',
            c("Abandon the cistern and wait at the public stair.", "approach"),
            c("Call out that the exit is open and no one needs to fight.", "approach")),
        page("approach", "Narrator", '''{n}The carrier is younger than the voice that negotiated the exchange. A human courier, perhaps thirty, stands beside a stone basin with a flat slate wrapped in oilcloth. A second figure keeps to the far arch. Devarra does not charge. She moves into the open where both strangers can see her and stops beyond striking distance.{/n}

"You have a copy of an account that belongs to me. Put it down. Tell me who asked you to carry it. No one has to be hurt before I know what you chose."''',
            c("Ask the courier to set the slate down and step away from it.", "courier_answer"),
            c("Offer the courier a clear exit in exchange for the copy and the buyer's name.", "courier_answer"),
            c("Use Trickster magic to collapse the far arch and trap both figures.", "dangerous_turn")),
        page("courier_answer", "Courier", '''The courier looks at Devarra, not you. "I was paid to move a copy. I did not know whose eggs it was about until I read the first page. The other one told me it would be worth more if you came in person." They glance at the arch, then at the open stair. Their fingers remain on the oilcloth.

Devarra's tail draws one slow line through the dust. "That is a useful fact. It is not yet a name, and it does not give me the right to burn you for taking the job."''',
            c("Let the courier give the slate to Devarra and leave by the open stair.", "slate_recovered"),
            c("Ask who recruited them, then accept that they may not know.", "slate_recovered"),
            c("Demand the name and promise safety only after they give it.", "courier_pressure")),
        page("courier_pressure", "Devarra", '''The courier's grip tightens. Devarra steps between your voice and the stair, not between the courier and freedom.

"No. You offered them an exit, then tied it to an answer they may not possess." Her eyes meet yours. There is anger in them, but not surprise. "We can take the copy without making their fear our instrument. If you want a confession more than a fact, say so plainly."''',
            c("Apologize, separate the slate from the question, and let them go after it is secured.", "slate_recovered"),
            c("Tell Devarra that the courier can leave after answering.", "dangerous_turn")),
        page("dangerous_turn", "Narrator", '''{n}Your magic bends the cistern's shadow. The far figure draws a knife. Devarra moves before your trick finishes, catches the wrist, and wrenches the weapon free. She does not strike again. The courier drops the slate and backs toward the open stair.{/n}

"That was the difference between stopping a threat and deciding what everyone else will do next." Devarra releases the attacker only when they let the knife fall. "If you can still hear me, help secure the copy. If not, leave."''',
            c("Release the distortion and help her bind the attacker without punishment.", "slate_recovered"),
            c("Keep the distortion in place and order her to finish the attacker.", "case_refused", flags=(REFUSED,))),
        page("slate_recovered", "Narrator", '''{n}Devarra unwraps the slate herself. The copy is incomplete: the testimony's first page and the inventory mark are there, but the disputed date is not. Someone wanted the account's most painful details without its cautions. She reads the first line, then turns the slate facedown.{/n}

The courier leaves through the stair once the slate is safe. If there is a name behind the payment, neither of you has it yet. Devarra does not pretend the missing name makes the danger harmless. She also does not turn the courier into a culprit because a better villain would make the ending easier.''',
            c("Ask what she wants done with the incomplete copy.", "disposition"),
            c("Offer to keep it as evidence and let her decide whether to pursue the buyer.", "disposition")),
        page("disposition", "Devarra", '''"We keep the slate beside the original and mark every difference. If someone comes looking for the rest, we will know what they believe is missing. We do not publish it. We do not promise revenge. If I decide to pursue the buyer, I decide after we know more than a courier's fear and a payment with no name." She presses the oilcloth flat, then passes it to you to hold while she seals the case.

Her claws brush your palm. Neither of you moves away at once. She is the first to break contact, but not with haste. "You let me choose the pace in there. That matters more than making the clever move. I have not decided what else it means."''',
            c("Tell her you want another meeting even if the answer stays uncertain.", "followup_interest", flags=(ROMANCE,)),
            c("Ask whether she would prefer the next meeting to be about something besides danger.", "followup_interest", flags=(ROMANCE,)),
            c("Say you will wait for her to request any further meeting.", "followup_open")),
        page("followup_interest", "Devarra", '''"Then let this be the first honest thing we do after the danger: we stop calling every hour together an emergency." A dry smile touches her mouth and vanishes. "I want a meal somewhere the walls are not listening. I want to know whether you can make me laugh without turning it into a strategy. And I want the option to leave when I have had enough."''',
            c("Accept the invitation and let her choose the place.", "case_complete", flags=(CASE_DONE, INVITED, ROMANCE)),
            c("Suggest a place, while leaving the choice and the hour to her.", "case_complete", flags=(CASE_DONE, INVITED, ROMANCE))),
        page("followup_open", "Devarra", '''"Good. I may ask. I may not. Do not turn either possibility into a debt." She takes the slate back and tucks it under one wing. "If I ask, it will be because I want the meeting. If I do not, the record still stays sealed and the courier still walks free."''',
            c("Accept the uncertainty and close the case together.", "case_complete", flags=(CASE_DONE, INVITED)),
            c("Ask her to tell you if she ever changes her mind.", "case_complete", flags=(CASE_DONE, INVITED))),
        page("case_refused", "Narrator", '''{n}Devarra takes the slate and leaves the cistern first. The courier's route stays open. She does not mistake your power for an answer she owes you, and she does not let the sealed record become collateral for your apology.{/n}

The inquiry ends. A later repair would need her freely chosen invitation; this draft supplies no such invitation after the refusal.''',
            c("End the route here.", flags=(REFUSED, CASE_DONE))),
        page("case_complete", "Narrator", '''{n}You leave with the incomplete copy sealed beside Devarra's original. The courier has not been made a hostage to your curiosity, and the unknown buyer remains unknown. There may be another investigation if Devarra chooses it, but the route does not need another crisis to justify the time she has offered you.{/n}

{n}Her invitation to meet away from the Tower is not a promise of love, sex, or permanence. It is one concrete choice, made by her, that you can accept or decline without changing what the evidence says.{/n}'''),
    ],
    requires=("trickster", INVITED, "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED, CASE_DONE),
    delay=72,
    last=5,
    optional=True,
    Relationship="devarra.trickster",
    ManualOnly=True,
    Remote=False,
    PhysicalPresenceRequired=True,
    ContactUnit="Devarra",
)


QUIET_SCENE = scene(
    "devarra.trickster.a_table_without_witnesses",
    "A table without witnesses",
    "Devarra",
    5,
    "meal_arrival",
    [
        page("meal_arrival", "Narrator", '''{n}The Tower's west gallery has no windows, but the stone remembers the afternoon sun. Devarra chose it for the meal because the ceiling is high enough for her to sit without folding herself into a corner. A long plank table rests on trestles. Someone has laid out roasted meat, bitter greens, black bread, and a small dish of salt. Nothing is arranged like an offering.{/n}

{n}She waits near the far end, not behind the table. You see the thought in the choice: the room is private, but the path to the door stays clear. When she notices you studying it, one gold eye narrows.{/n}

"I said I wanted to know whether you could make me laugh without turning it into a tactic. I did not promise to laugh. Sit where you like."''',
            c("Take the seat that leaves her the clearest path to the door.", "table_terms"),
            c("Ask whether she wants the meal served before you sit.", "table_terms"),
            c("Tell her that choosing the room already counts as a tactical victory.", "tactical_joke")),
        page("tactical_joke", "Devarra", '''A low chuff moves through her chest. It could be the beginning of a laugh, but she refuses to let you claim it. "If you put that in your report, I will deny it under oath." The edge of her mouth shifts as she settles onto the stone bench.

"You make a joke and wait to see whether it lands. That is different from arranging the room so I have to reward you for telling it." She nods toward the food. "Come on. Before the bread becomes a historical artifact."''',
            c("Join her and leave the subject where she set it.", "table_terms"),
            c("Ask whether she prefers to begin with the meal or with a question.", "table_terms")),
        page("table_terms", "Devarra", '''The first few minutes are quiet. Devarra eats slowly, tearing the bread into pieces with one claw and dipping them into the salt. She does not need the food, perhaps, but she has chosen it. You do not ask her to explain the gesture.

"I asked for an ordinary evening because every conversation lately has had a witness, a record, or a door someone might break through. Ordinary is not the same as easy. I do not know what to do with a person who can make almost anything happen and has started asking first."''',
            c("Tell her you are still learning the difference between asking and steering.", "answer_honest"),
            c("Say that power is useful only if she keeps choosing what to do with it.", "answer_honest"),
            c("Tell her that you have always known what she wanted.", "answer_claim")),
        page("answer_claim", "Devarra", '''"No, you have not." Her answer is immediate, and the gold in her eyes turns bright as a coin held over flame. "You knew what would make a scene. You knew what would make me angry. You guessed what might make me stay. Those are not the same as knowing me."

She sets down the bread and waits. There is no spectacle in the correction. It is worse than that: a clear opening to admit you were wrong, or to turn the mistake into another contest.''',
            c("Withdraw the claim and ask what she would rather you understand.", "answer_honest"),
            c("Insist that being the Commander means you can read anyone eventually.", "meal_refused", flags=(REFUSED,))),
        page("answer_honest", "Commander", '''"I was good at finding the answer that moved a room. Sometimes I called that understanding. I do not want your attention badly enough to pretend those are the same thing now." You leave the bread between you rather than reaching across the table.

Devarra watches your hands, then your face. "That is the first honest answer tonight. Do not make it the last by polishing it until it shines." She shifts her weight, and the old scar under the edge of her wing draws tight. "There is something I want to ask you. You can answer or not. I will not demand a confession just because I gave one."''',
            c("Invite her to ask, and promise nothing beyond an honest answer.", "commander_cost"),
            c("Ask whether she would rather discuss the scar or the eggs.", "devarra_choice"),
            c("Tell her that you would rather hear what she wants from you now.", "desire_terms")),
        page("commander_cost", "Devarra", '''"When you use fate to make something possible, what do you tell yourself about the cost?" Her voice has lost its teasing edge. "Not the cost to the world. Not the cost to the people who had no vote. The cost to you. What do you have to believe about yourself to keep doing it?"

She does not lean closer. The question asks for a part of you that a courtship cannot claim by right. She is giving you room to decline, and she is also making it clear she will notice whether you hide behind a joke.''',
            c("Admit that sometimes you call it play so you do not have to call it fear.", "shared_vulnerability"),
            c("Say that you choose the cost when the alternative is worse.", "shared_vulnerability"),
            c("Refuse the question and ask her to leave the past alone.", "meal_open")),
        page("shared_vulnerability", "Commander", '''You tell her about the moments when the world bends and your own certainty bends with it. You can make a way out of a trap, then find yourself wondering whether the person who walked through it was still the person who entered. You do not make the fear sound noble. You do not call it proof that you deserve admiration.

Devarra lets the silence last. "I know what it is to survive something and then be told survival proves you wanted it." Her gaze drops to the scar. "I will not tell you that every choice is clean. I will tell you that choosing matters, even when the choices are ugly."''',
            c("Ask what she chooses when anger is the truest thing she feels.", "anger_and_desire"),
            c("Tell her you do not want to make a virtue of what happened to her.", "devarra_choice")),
        page("anger_and_desire", "Devarra", '''"Sometimes I choose to stay angry. Anger keeps the loss from being turned into a lesson someone else can own. Sometimes I choose to act on it. Sometimes I choose to eat supper and talk to a person who hurt me, because the hurt is not the only thing that exists between us." Her voice lowers, rough and warm against the stone.

She does not ask you to heal her, forgive her, or make the anger disappear. The heat she carries is close enough to change the air. You notice it; she notices you noticing. Her expression holds the question without granting you an answer.''',
            c("Say that you are attracted to her and let her decide whether to answer.", "desire_terms", flags=(ROMANCE,)),
            c("Tell her the anger is hers, and you will not claim it as an invitation.", "devarra_choice")),
        page("devarra_choice", "Devarra", '''"Then let me choose the next thing." She moves around the end of the table, not quickly, and stops where you can see the offered distance. Her scales catch the low light in dark red and bronze. The old seam beneath her wing is rougher than the unmarked plates. None of it makes her less beautiful to you, and you do not turn that thought into an argument she has to answer.

"I want you to know I can want you and still be angry with you. I can be angry and still decide to stay for supper. I can change either answer tomorrow."''',
            c("Tell her the attraction is yours to carry, and ask what she wants next.", "desire_terms", flags=(ROMANCE,)),
            c("Say you would rather leave the relationship unnamed tonight.", "meal_open"),
            c("Tell her anger proves she already belongs to you.", "meal_refused", flags=(REFUSED,))),
        page("desire_terms", "Devarra", '''She studies you for a long breath. "I want to know what your desire sounds like when it is not trying to win." The question is intimate, but it is not permission to touch her. Her gaze stays on yours, then moves once to your mouth and back.

"Tell me what you want. Leave me room to say it is too much, too soon, or not for me. If that ruins the evening, then the evening was a performance."''',
            c("Say you want another meal, a kiss if she wants one, and no claim over her future.", "kiss_choice", flags=(ROMANCE,)),
            c("Say you want only to keep talking until she is ready to leave.", "meal_open"),
            c("Say you want her to stop thinking and let you decide.", "meal_refused", flags=(REFUSED,))),
        page("kiss_choice", "Devarra", '''"A kiss is a thing I can choose now. It is not a signature under every promise you might make later." She lowers her head until the ridge over her muzzle is near your shoulder. The scales there are smooth and warm. She does not close the last distance.

"You can ask. I can say yes or no. If I say yes, I can still stop. If either of us changes their mind, the answer changes. Speak carefully, Commander. I am listening to the words you use when there is something you want."''',
            c("Ask whether she wants to kiss you, and wait without reaching.", "kiss_answer", flags=(ROMANCE,)),
            c("Tell her you are content to let her initiate if she chooses.", "kiss_answer", flags=(ROMANCE,)),
            c("Treat the offered closeness as consent to take what you want.", "meal_refused", flags=(REFUSED,))),
        page("kiss_answer", "Devarra", '''"I do." Her answer is quiet. She closes the distance herself, pressing the warm bridge of her muzzle to your cheek and holding there for one slow breath. Her exhale carries the faint scent of smoke and bitter greens. She withdraws first, but her eyes remain on yours.

"That was a kiss. It was mine to give. It is all I have decided tonight." She settles beside the table again, leaving a little less distance than before. The meal has gone cold. Neither of you seems to mind.''',
            c("Thank her and ask whether she wants the evening to end here.", "meal_terms", flags=(ROMANCE,)),
            c("Ask what she wants to talk about now, without assuming the answer.", "meal_terms", flags=(ROMANCE,))),
        page("meal_terms", "Devarra", '''"We finish the bread. We talk about something that is not my clutch, your mythic path, or the number of people you have outmaneuvered this week." The smile comes back, sharper now that she has decided to show it. "Then I walk you to the arch. At the threshold I decide whether there is another kiss. You do not ask twice if I say no the first time."''',
            c("Agree, and let her set the pace for the rest of the night.", "meal_end_romance", flags=(ROMANCE,)),
            c("Ask her to choose the subject and accept whatever answer she gives.", "meal_end_romance", flags=(ROMANCE,))),
        page("meal_open", "Narrator", '''{n}The evening closes without a promise. Devarra keeps the room and the rest of the meal. You leave the arch clear. She is not less real because you did not get an answer tonight, and you are not owed a second chance for having asked once.{/n}''',
            c("Close the scene without treating uncertainty as a hidden promise.", flags=("devarra.trickster.meal_scene_complete",))),
        page("meal_refused", "Narrator", '''{n}The invitation ends. Devarra says she will not repeat herself, and you leave before the room turns her refusal into another debate. The route stays closed. No later scene may read the meal's closeness as a secret yes.{/n}''',
            c("Accept the refusal and close the scene.", flags=("devarra.trickster.meal_scene_complete",))),
        page("meal_end_romance", "Narrator", '''{n}Devarra walks you to the arch as she chose. She pauses there, looking down at you with the same hard attention she brought to the first meeting, though there is warmth in it now. She gives you one brief kiss, then withdraws with a smile that belongs to her alone.{/n}

{n}The invitation was a date because you both treated it as one. The kiss was a kiss because she chose it. Neither is a vow, and neither cancels the anger or history that made the evening difficult. There is more between you now, but it has to survive another day of choices.{/n}''',
            c("Let the evening end on her terms.", flags=(MEAL_DONE, MEAL_ROMANCE_END))),
    ],
    requires=("trickster", CASE_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED, "devarra.trickster.meal_scene_complete"),
    delay=24,
    last=5,
    optional=True,
    Relationship="devarra.trickster",
    ManualOnly=True,
    Remote=False,
    PhysicalPresenceRequired=True,
    ContactUnit="Devarra",
)


AFTER_MEAL_SCENE = scene(
    "devarra.trickster.the_second_envelope",
    "A letter that arrived twice",
    "Devarra",
    5,
    "second_envelope",
    [
        page("second_envelope", "Narrator", '''{n}Three days after the meal, Devarra sends no invitation. She sends a time and a place: the east gallery of the Storyteller's tower, before the next watch changes. When you arrive, she is waiting beside a narrow stone table. An envelope lies between her claws. Its seal is made from the same dark wax used to close the incomplete slate copy, though the mark pressed into it is unfamiliar.{/n}

"The messenger left before I could ask a question. He said the person who paid for the slate wants the original account. He also said that the buyer can prove where the eggs went." Her eyes hold yours. "The last claim may be bait. The first one is a threat. I want to answer it on my terms."''',
            c("Ask what she wants the encounter to accomplish before you offer a plan.", "saved_history", requires=(SAVED, SAVED_CUE)),
            c("Ask which part of the offer she intends to test first.", "lost_history", requires=(LOST, LOST_CUE)),
            c("Say you can make the buyer appear before her if she lets you take control.", "wrong_opening", flags=(MISTRUST,))),
        page("saved_history", "Devarra", '''"The eggs survived in the history I remember. They were not returned to me as property. Someone carried living creatures away from that slaughter. Whoever they were, I will not let a buyer sell their names to the next enemy who wants a hostage." Her tail curls around the table leg, metal scraping stone. "If the messenger speaks truth, he has a route and a witness. I want to know whether the buyer is trying to sell me a map or frighten those who made the rescue possible."''',
            c("Treat the rescue as a fact she may defend, not a debt you can spend.", "read_letter"),
            c("Offer to put the list of rescuers in her hands before the meeting.", "read_letter"),
            c("Call the eggs her leverage and watch how she reacts.", "wrong_opening", flags=(MISTRUST,))),
        page("lost_history", "Devarra", '''"The clutch was taken. My offspring died before birth." Her voice is flat, the words placed as carefully as a blade laid on a table. "Do not turn that loss into a riddle with a pleasing answer. If the buyer claims to know where the eggs went, the claim is bait until it is proven. I want the name behind it because someone is selling a wound they did not earn." Her nostrils flare. Smoke threads past one fang, then stops. "I want the choice of what to do when the liar is in front of me."''',
            c("Keep the loss out of the price of the meeting and ask what outcome she wants.", "read_letter"),
            c("Tell her the lie itself may be worth using against its author.", "read_letter"),
            c("Say the truth about her clutch is less important than a useful trap.", "wrong_opening", flags=(MISTRUST,))),
        page("wrong_opening", "Devarra", '''The answer is a short laugh without warmth. "You came here to tell me what you can do. I came here to decide what I want." She folds one wing between you and the door. There is room to leave, but no path through the sentence you just chose.

"The meal did not buy you the right to arrange my enemies, my memory, or my body. If you want to stay in this room, speak to me as the woman who chose to invite you, not as a lock you think your magic can pick."''',
            c("Own the mistake and accept that she may close the matter.", "repair_opening"),
            c("Tell her she owes you a chance to explain.", "closed_meeting", flags=(REFUSED,))),
        page("repair_opening", "Commander", '''"I wanted the advantage before I knew the terms. That is old habit, and it was a poor one." You set your hands on your side of the table. "You decide whether I get another sentence. If you do, I will listen first."''',
            c("Let her choose whether to continue.", "invitation_terms"),
            c("Ask one direct question: does she want the envelope opened?", "read_letter")),
        page("closed_meeting", "Narrator", '''{n}Devarra takes the envelope and the original account. She does not raise her voice or strike the table. The absence of both is more final than anger would have been.{/n}

"You can leave now. The date was real. It is over." You go without another argument. The message remains unanswered, the buyer's threat remains active, and this conversation gives you no permission to turn the evening into a promise you can collect later.''',
            c("Leave and accept that she has closed the meeting.", flags=(REFUSED,))),
        page("invitation_terms", "Devarra", '''"I invited you because you amuse me when you are not trying to arrange the room around my answer." Her eyes narrow, the corners of her mouth barely moving. "Do not look pleased. Amusement is a reason to keep someone near for an hour, not a treaty." She nudges the envelope toward you with one claw. "Open it if you want. The first thing we decide is whether its claim is evidence or a hook. The second is what we do with the hand holding it."''',
            c("Open it at the torn edge and read the message as written.", "read_letter"),
            c("Ask her to break the seal herself and tell you what she sees.", "read_letter")),
        page("read_letter", "Commander", '''You open the envelope at the torn edge. There is no signature. The note asks Devarra to bring the sealed original to the arch under the old east bridge at midnight. It promises "the truth of the clutch" and warns that the buyer will send the archive's location to the crusaders if she refuses.

Devarra reads it once. "He wants the original because it can prove what the copy cannot. He wants me alone because he thinks the difference between a dragon and a woman is that one can be cornered." She glances at you. "I will go. You may come if you can keep a plan from becoming a cage."''',
            c("Ask her to choose which risk she is willing to take before you plan around it.", "devarra_terms"),
            c("Point out that the threat gives you a narrow, useful deadline.", "clock_terms"),
            c("Tell her the buyer's first mistake was assuming she would arrive alone.", "clock_terms")),
        page("devarra_terms", "Devarra", '''"The original stays with me. The witness stays free to leave. No one gets dragged to a question room because you are curious, and no one gets named publicly because the name would make our story cleaner." She settles the envelope beside her claw. "If the buyer has a real lead about my clutch, I will hear the evidence. If he has a lie, I will decide whether to burn it or make him carry it home. You can offer a clever way to catch him. You cannot choose what I do with him."''',
            c("Ask whether she wants a public meeting with witnesses and a record of every claim.", "public_plan"),
            c("Offer a private exchange that uses a false copy as bait, not the original.", "private_plan"),
            c("Suggest letting the buyer think the threat worked, then taking him alive.", "private_plan")),
        page("clock_terms", "Devarra", '''"Midnight is three hours away. The threat is useful because it tells us when he expects me to feel alone." She taps the note with one claw. "The location is an old bridge. There are three exits, no easy cover, and enough ruined stone to hide a dozen people badly. We could arrive early, bring a witness, or make his chosen hour mean something else." Her gaze sharpens. "That last idea is why I agreed to meet a Trickster. Give me a plan with a price I can see."''',
            c("Tell her to bring a witness and make the exchange visible.", "public_plan", flags=(PLAN_PUBLIC,)),
            c("Use the tower's broken hour to make the meeting arrive twice.", "trickster_plan", flags=(PLAN_PRIVATE,)),
            c("Threaten the messenger until he gives you the buyer's name.", "predatory_plan", flags=(PLAN_PRIVATE,))),
        page("public_plan", "Commander", '''"We answer the threat openly. I can notify the crusaders that someone is trying to sell a witness's location, bring a neutral recorder, and keep the original sealed. If the buyer brought evidence, it goes on the table where everyone can see it. If he brought a lie, it will have to survive more than our anger."''',
            c("Ask Devarra to decide who may witness the exchange.", "witness_choice", flags=(PLAN_PUBLIC,)),
            c("Offer to reveal the threat before midnight, even if the buyer runs.", "witness_choice", flags=(PLAN_PUBLIC,))),
        page("private_plan", "Devarra", '''"A false copy can draw him out. My original stays beneath my wing. If he asks for the sealed account, I will give him a folio with a deliberate flaw and watch whether he corrects it." She considers the note, then your face. "I do not want a spell that makes him confess. I want a room where the wrong person cannot hide behind the right paper."''',
            c("Make the copy, mark its flaw, and keep the original out of reach.", "trickster_plan", flags=(PLAN_PRIVATE,)),
            c("Let her write the flaw herself and follow her lead.", "trickster_plan", flags=(PLAN_PRIVATE,))),
        page("predatory_plan", "Devarra", '''"That is not the same as making a witness answer." She lifts her head until her horns cut across the lantern light. "If the messenger carries a threat, we may stop him from delivering another. If he carries a fear, we do not turn it into a confession for our convenience." Her mouth curls. "You are allowed to be ruthless. You are not allowed to call it clever when you cannot tell who is holding the knife."''',
            c("Keep the pressure on the employer, not the courier, and accept the public cost.", "public_plan", flags=(PLAN_PUBLIC,)),
            c("Use the courier as bait without telling him, and accept Devarra's judgment afterward.", "trickster_plan", flags=(PLAN_PRIVATE,))),
        page("witness_choice", "Devarra", '''"A witness who has met the courier once. Not a crusader with an arrest order and not someone who thinks I am a prize to be escorted." She looks toward the arch. "I can ask the Tower's keeper to observe from the upper landing. If he refuses, we do not replace him with an illusion and call that consent to testify."''',
            c("Invite the keeper to observe and let the courier know he may refuse to speak.", "plan_check", flags=(PLAN_PUBLIC,)),
            c("Keep the witness outside the bridge and read the buyer's response first.", "plan_check", flags=(PLAN_PUBLIC,))),
        page("trickster_plan", "Commander", '''"The tower has already made one evening feel like two. At the bridge, I can fold a single minute across itself. The courier will see the meeting begin, then see it begin again from the other side of the arch. Nobody will lose a memory, and nobody will be made to answer twice. We use the overlap to learn whether the courier carried the note or wrote it."''',
            c("Ask Devarra to name what would make the trick unacceptable to her.", "plan_check", flags=(PLAN_PRIVATE,)),
            c("Tell her the second minute will be yours to spend, and the exposure is the price.", "plan_check", flags=(PLAN_PRIVATE,))),
        page("plan_check", "Narrator", '''{n}Before leaving the Tower, you and Devarra prepare a false folio.
She copies the harmless inventory entries, then reverses the seal's lower stroke.
Anyone who has handled the stolen account should notice the flaw; an ordinary messenger has no reason to notice it.
She slides the original beneath her wing and gives you the copy.
Even if the exchange stays public and the hour remains untouched, the bait is ready.{/n}

{n}You measure the distance from the bridge to the Tower's old seam in the world. The echo will be brief. If you make it too wide, the two versions of the meeting will touch and the courier may see both plans at once. If you make it too narrow, the minute will close before Devarra can read what the courier does with the false folio.{/n}

This is a Trickster's arrangement of timing, not a command over anyone's thoughts. It has one attempt. The tower will not give the same minute back because you disliked its answer.''',
            c("Use Knowledge (Arcana) to anchor the repeated minute to the bridge's east arch. DC 33.", flags=(FATE_CHECK,), forbids=(FATE_CHECK,), check=dict(Skill="SkillKnowledgeArcana", DC=33, Success="hour_held", Failure="hour_broke", CommanderOnly=True)),
            c("Have Devarra choose the meeting time without altering it.", "hour_ordinary"),
            c("Set the overlap without testing the seam and accept that it may show.", "hour_broke", flags=(FATE_CHECK,))),
        page("hour_held", "Narrator", '''{n}The seam catches. For one impossible minute, the bridge holds the instant before the courier arrives and the instant after he leaves. They overlap without becoming the same moment. The tower's bells ring once, then seem to remember that they have already rung.{/n}

You cannot keep the trick hidden. Anyone close enough to see the bridge will know that its hour stuttered, and the buyer may realize that the meeting was planned around his message. The minute is yours now, but only once.''',
            c("Tell Devarra exactly what the trick will reveal and what it will expose.", "plan_locked", flags=(FATE_HELD,)),
            c("Let her decide whether the risk is worth the opening.", "plan_locked", flags=(FATE_HELD,))),
        page("hour_broke", "Narrator", '''{n}The minute splits crookedly. The east arch repeats, but the rest of the bridge does not. You glimpse the courier on both sides of the same stone and then the echo snaps shut. He has not been trapped or changed. He has seen enough to know that someone reached into the hour before he arrived.{/n}

The trick has failed as a secret. It has succeeded as a warning: the buyer will know that the meeting is no longer under his control. Devarra studies you, then smiles without showing a fang. "Now we find out what he does when he knows we can surprise him."''',
            c("Own the visible failure and make a plan that can survive being seen.", "plan_locked", flags=(FATE_BROKE,)),
            c("Ask Devarra whether she wants to cancel the meeting or use the warning.", "plan_locked", flags=(FATE_BROKE,))),
        page("hour_ordinary", "Devarra", '''"No broken minute. The courier can arrive once, and he can see me waiting exactly where he expects." She chooses the place on the plan with one claw. "You will still have the copy, the exits, and the chance to decide whether to tell the truth. My reason for inviting you does not depend on making the world stutter."''',
            c("Keep the straightforward plan and let the courier choose whether to talk.", "plan_locked", flags=(PLAN_PUBLIC,)),
            c("Keep the false copy and refuse to use magic on the courier.", "plan_locked", flags=(PLAN_PRIVATE,))),
        page("plan_locked", "Devarra", '''"Then we have a plan. It can be good, ugly, or both. If it works, I still choose what I do with the answer. If it fails, I still choose what I do with you." Her talon slides the original account into a leather case. "I will meet you at the bridge before midnight. Come with your own face and your own answer. I have seen what your jokes can do when they arrive before you."''',
            c("Agree to meet her at the bridge and keep the arrangement you chose.", "plan_complete", flags=(PLAN_READY, LETTER_READ, FALSE_FOLIO_READY)),
            c("Tell her you will bring a joke sharp enough to deserve the risk.", "plan_complete", flags=(PLAN_READY, LETTER_READ))),
        page("plan_complete", "Narrator", '''{n}Devarra leaves with the original account under her wing and the false copy in your hands. The sealed page is still hers. The hour belongs to neither of you, but you have both chosen where to stand when it arrives.{/n}''',
            c("Close the plan and prepare for midnight.", flags=(LETTER_READ, PLAN_READY, FALSE_FOLIO_READY))),
    ],
    requires=("trickster", MEAL_DONE, MEAL_ROMANCE_END, ROMANCE, CASE_DONE, "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED, LETTER_READ),
    delay=72,
    last=5,
    optional=True,
)


EXCHANGE_SCENE = scene(
    "devarra.trickster.the_hour_under_the_bridge",
    "The hour under the bridge",
    "Devarra",
    5,
    "bridge_arrival",
    [
        page("bridge_arrival", "Narrator", '''{n}The bridge is older than the road it crosses. Its central arch has sunk into the black water, and the stones on the north side still bear scorch marks from a battle nobody in the nearby village remembers clearly. Devarra waits on the high span with the original secured under her wing and the false folio in one foreclaw. The night makes her red scales nearly black.{/n}

She looks at your hands, then at your face. "You came with the same answer you gave me at the Tower. Good. I dislike plans that become different when the dark arrives." The courier has not yet appeared. Somewhere below the bridge, water strikes a stone. Devarra listens, waiting to hear whether you have changed its rhythm.''',
            c("Tell her the minute held and let her decide whether to use the opening.", "held_minute", requires=(FATE_HELD,)),
            c("Tell her the minute broke and admit that the meeting may be exposed.", "broken_minute", requires=(FATE_BROKE,)),
            c("Tell her you chose not to bend the hour and will follow her plan.", "plain_minute", forbids=(FATE_HELD, FATE_BROKE))),
        page("held_minute", "Devarra", '''"I can feel it between the stones. The same drop strikes twice, though the second sound arrives before the first has finished." She watches the water instead of you. "That is the price you named. The buyer may know we prepared, but the courier still has to decide whether to walk across this bridge." Her gaze returns. "I will not waste the moment by pretending it makes us invisible. If he sees the trick, I want him to see me choosing to stay."''',
            c("Keep the doubled minute visible and let Devarra control the first question.", "courier_arrives", flags=(FATE_HELD,)),
            c("Use the echo to move the witness to the far end before the courier arrives.", "witness_move", flags=(FATE_HELD,))),
        page("broken_minute", "Devarra", '''"I can feel the seam closing. The water keeps one rhythm now." She snorts smoke into the dark. "The courier saw enough to know this is a trap. That may mean he is frightened, or it may mean he will bring help. I will still meet him. I refuse to let an imperfect trick decide that I cannot face an imperfect answer." Her claw closes around the false folio. "We can tell the witness what happened, or keep the rest of the plan and accept that it may turn public before we are ready."''',
            c("Warn the witness and prepare to make the exchange public.", "witness_move", flags=(FATE_BROKE, PLAN_PUBLIC)),
            c("Keep the false folio ready and let Devarra read the courier's first move.", "courier_arrives", flags=(FATE_BROKE, PLAN_PRIVATE))),
        page("plain_minute", "Devarra", '''"Then there is only one of us playing with the hour." A smile cuts across her muzzle. "I can work with that. The rest of the plan is already a lie in the buyer's favor. He thinks the original will be here. He thinks I will arrive without anyone to contradict him. Let him keep both mistakes until they cost him something."''',
            c("Keep the witness visible and let Devarra speak first.", "witness_move", flags=(PLAN_PUBLIC,)),
            c("Keep the witness out of sight while Devarra tests the false folio.", "courier_arrives", flags=(PLAN_PRIVATE,))),
        page("witness_move", "Commander", '''You signal the observer to move from the bridge approach to the old tollhouse. The witness can still see the span, but no courier can mistake them for a guard or a target. You do not tell them to stay if they want to leave. The choice costs time, and the opening minute narrows.

Devarra watches you make the signal. "A witness is not a lantern you set where it helps the story." Her voice softens by a fraction. "Now the buyer will have to choose whether the record matters more than the chance to make me angry."''',
            c("Ask the witness to leave if the exchange turns violent.", "courier_arrives"),
            c("Tell the witness to remain until Devarra has heard the offer.", "courier_arrives")),
        page("courier_arrives", "Narrator", '''{n}A small figure steps onto the bridge from the east bank. The courier carries no weapon you can see. A leather satchel hangs from one shoulder, and the strap has been repaired with thread the same dark red as the wax on the letter. He stops well short of Devarra and puts the satchel on the stones between you.{/n}

"The original," he says. "Then the location." He looks at Devarra, not at the Commander. "My employer says he can prove where the clutch went. I was told the account was yours to keep, but the route makes the claim worthless if you cannot see it." He produces a narrow strip of parchment and holds it up without crossing the space between you.''',
            c("Ask him to set the parchment down before anyone discusses the eggs.", "parchment_terms"),
            c("Tell him Devarra will hear evidence, but the original is not for sale.", "parchment_terms"),
            c("Order him to kneel and explain why he thought a threat would work.", "hard_entry")),
        page("hard_entry", "Devarra", '''"You may kneel if you choose to. You may also keep your feet and answer the question." Her tone is almost bored. "Do not confuse my patience with permission to order my meeting for me." The courier's hand has gone to the satchel strap. It is not yet a weapon; you cannot know whether he is afraid, reaching for the parchment, or preparing to run.

Devarra's eyes meet yours for a heartbeat. She does not tell you what to do. The answer you give now will decide whether the courier remains a witness or becomes part of the threat you came to stop.''',
            c("Drop your hand, give him room, and ask what he knows about the buyer.", "parchment_terms"),
            c("Keep pressure on him and make clear that running will have a cost.", "parchment_terms", flags=(MESSENGER_USED,))),
        page("parchment_terms", "Devarra", '''Devarra does not take the strip. "Read it aloud. If it names a place, we will decide whether to go there. If it names a person, you will tell us how you know. If it names an egg or one of the people who carried it, the account stays sealed until I understand why you brought that name here." She taps the false folio against the stone.

The courier reads the strip. It is a route through three settlements and a final mark beside a dry cistern. No name appears. The last mark is the same hooked stroke as the altered date in the contract, but the hand could be a copyist's. The courier says the person who sent him promised the mark would make Devarra recognize the location.''',
            c("Use Perception to compare the fresh stroke with the damaged contract. DC 32.", flags=(MEETING_PERCEPTION,), forbids=(MEETING_PERCEPTION,), check=dict(Skill="SkillPerception", DC=32, Success="mark_matched", Failure="mark_unreadable", CommanderOnly=True)),
            c("Ask the courier who gave him the strip and let him answer in his own order.", "courier_account"),
            c("Tell Devarra the repeated mark is enough to treat the cistern as a lead.", "courier_account")),
        page("mark_matched", "Commander", '''The hooked stroke shares the same odd break at its end as the alteration in the contract. It is a match in form, not a signature. The courier cannot tell whether the same hand wrote both marks or whether someone copied the first one to make a trail look certain.

You lay the strip beside the false folio. Devarra studies the pairing without touching either. "A place to look. Not a name to condemn." Below the bridge, water carries a broken reed out of sight. The mark has given you a place to look. Devarra keeps watching the courier, who has yet to explain why his employer wanted her alone.''',
            c("Give her the strip and tell her exactly what the match proves and cannot prove.", "courier_account"),
            c("Ask whether she wants to follow the cistern lead tonight.", "courier_account")),
        page("mark_unreadable", "Narrator", '''{n}The mark has been folded through its middle. The paper's crease has crushed the hook into a small dark knot. You cannot compare it cleanly with the contract. The courier watches your face and guesses the answer before you say it.{/n}

"Then the route may be nothing," he says. "Or the mark may have been damaged on purpose." Devarra's claw opens above the paper, showing the thin edge of each talon. "You have one honest answer. Do not make a guess sound like certainty because the hour is running out."''',
            c("Say the mark is inconclusive and ask for his account instead.", "courier_account"),
            c("Accuse him of destroying the only proof and accept the risk of being wrong.", "courier_account", flags=(MISTRUST,))),
        page("courier_account", "Commander", '''"Who gave you the note?" You keep your voice level. The courier glances at the north bank, then at Devarra's shadow covering the center of the bridge. He says he was paid to deliver a message and collect the sealed account. He never met the buyer. The instructions came through two people, each one using a different name.

He admits that the threat about sending the archive's location to the crusaders was written for him to repeat. He does not know whether the threat is real. He has carried other messages for the same chain, but this is the first one addressed to a dragon.''',
            c("Ask Diplomacy who held the message before him, without promising safety you cannot guarantee. DC 30.", flags=(MEETING_DIPLOMACY,), forbids=(MEETING_DIPLOMACY,), check=dict(Skill="SkillPersuasion", DC=30, Success="account_opened", Failure="account_closed", CommanderOnly=True)),
            c("Ask Devarra whether she wants to question him or end the exchange.", "devarra_decides"),
            c("Offer him a safe route away if he stops carrying the threat.", "devarra_decides", flags=(MESSENGER_SAFE,))),
        page("account_opened", "Narrator", '''{n}You do not offer pardon or payment. You ask for the one fact he can verify: who handed him the envelope. The courier gives a description of a woman in a grey travel cloak and a voice with a coastal accent. It is not enough to identify her, but it can be checked against the next message in the chain.{/n}

He looks relieved and ashamed at once. "I thought the buyer wanted the page. I didn't know the threat would go to a witness's home." He lets the satchel fall from his shoulder. "If I leave now, I cannot tell you another thing."''',
            c("Let him leave, then record his account without his name unless he agrees.", "safe_exchange", flags=(MESSENGER_SAFE,)),
            c("Ask him to wait beside the witness while Devarra decides what to do.", "devarra_decides", flags=(MESSENGER_SAFE,))),
        page("account_closed", "Narrator", '''{n}The courier's shoulders rise. He gives you a name, then retracts it and says he does not know whether it was the person's real one. You have no way to test the answer on this bridge. The longer you press, the more he looks at the gap between Devarra and the water.{/n}

The reply has cost the chance to learn who passed the envelope. He has not named the buyer, and he has not given you a route beyond the mark. A failed question is not a reason to invent a confession.''',
            c("Stop questioning him and let Devarra choose the next move.", "devarra_decides"),
            c("Tell him the buyer can no longer protect him from the threat he delivered.", "devarra_decides", flags=(MESSENGER_USED,))),
        page("devarra_decides", "Devarra", '''"The courier carried a threat. He did not write it, and we have no proof he knew whose home it named." She walks one slow step toward him. The courier does not move. "He also carried the route to a place where the person behind this may have kept a copy of my record. I want that lead. I will not pretend those facts cancel each other out."''',
            c("Offer the witness and the courier a public statement, then follow the cistern lead openly.", "safe_exchange", flags=(MESSENGER_SAFE, PLAN_PUBLIC)),
            c("Use the courier as the visible bait while you and Devarra take the hidden route.", "risky_exchange", flags=(MESSENGER_USED, PLAN_PRIVATE)),
            c("Burn the strip, keep the original, and let the unknown buyer wonder what you learned.", "burned_exchange", flags=(EXCHANGE_DONE,))),
        page("safe_exchange", "Devarra", '''"You can leave," she tells the courier. "If you want to speak later, send a message to the Tower without a name on it. If you want to forget this bridge, I will not follow you." The words give him a way out. They do not make the night harmless. He takes the satchel and leaves by the eastern bank, where the observer can see him go.

Devarra watches until he is gone. "The cistern is real. The mark may be a lure, but someone wants us to find it or wants us to think we have. I will decide at the Tower whether to follow it. You did not make the decision for me."''',
            c("Preserve the strip and the false folio together as evidence.", flags=(MESSENGER_SAFE, EXCHANGE_DONE, LEAD_FOUND)),
            c("Give the strip to the witness and let them decide whether to record it.", flags=(MESSENGER_SAFE, EXCHANGE_DONE, LEAD_FOUND))),
        page("risky_exchange", "Narrator", '''{n}The courier looks from you to Devarra. He knows the offer is a trap now. Devarra does not promise him safety or tell him that he owes you cooperation. He takes the route east with the false folio visible in the satchel, and you follow along the riverbank while Devarra keeps to the high stones.{/n}

The second messenger never appears. The courier reaches a deserted storehouse, leaves the satchel by its door, and continues alone. Inside the satchel is a scrap of the original account, burned through the center. The buyer has learned that the copy can be used as bait. The lead survives, but the secret does not.''',
            c("Keep the burned scrap and return the courier to the road unharmed.", flags=(MESSENGER_USED, EXCHANGE_DONE, LEAD_FOUND)),
            c("Let the courier go and keep the storehouse location for the next search.", flags=(MESSENGER_USED, EXCHANGE_DONE, LEAD_FOUND))),
        page("burned_exchange", "Narrator", '''{n}Devarra folds the strip once, then burns it in her palm. The false folio remains untouched. The fire consumes the route before the buyer can know whether you believed it.{/n}

"I have enough enemies who know where my history began. I will not drag a witness into another chase because an unknown person used a threat to make a sale." She leaves the bridge by the north road. The original account is still under her wing. The buyer will know you refused the trade, and the next approach will not come with a map.''',
            c("Accept that she has ended the exchange and return with her.", flags=(EXCHANGE_DONE, MESSENGER_SAFE, BUYER_BURNED))),
    ],
    requires=("trickster", PLAN_READY, LETTER_READ, FALSE_FOLIO_READY, MEAL_ROMANCE_END, ROMANCE, CASE_DONE, "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED, EXCHANGE_DONE),
    delay=0,
    last=5,
    optional=True,
)


CISTERN_TRIED = "devarra.trickster.cistern_latch_attempted"
ANCHOR_KEPT = "devarra.trickster.anchor_kept"
ANCHOR_PAID = "devarra.trickster.anchor_paid"
BUYER_SPARED = "devarra.trickster.buyer_spared"
BUYER_KILLED = "devarra.trickster.buyer_killed"
BUYER_SERVES = "devarra.trickster.buyer_in_service"

CISTERN_SCENE = scene(
    "devarra.trickster.a_dragon_out_of_place", "A dragon out of place",
    "Devarra", 5, "ash_at_dawn",
    [
        page("ash_at_dawn", "Narrator", '''{n}At dawn, something falls out of Devarra's shadow.
It strikes the gallery floor with a sound like a coin and unfolds into a beetle made from hammered copper.
Its legs work furiously, although Devarra has already pinned it beneath a talon.{/n}

"That was inside my wing."

{n}The stones under her forefeet redden.
For an instant you see the far wall through the edge of her folded wing.
Then it is solid again.{/n}

"You saw. Good. I would hate to explain this twice."

{n}She lifts the beetle. A thread as fine as spider silk stretches from its mouth into her shadow.
When she pulls, a piece of the gallery seems to come with it.
Beyond that displaced stone there is a dark room, an iron wheel, and a man pulling on the other end.{/n}''',
            c("Follow the cistern directions before he can finish winding that wheel.", "known_road", requires=(LEAD_FOUND,)),
            c("We burned his directions. Fortunately, he has attached himself to the evidence.", "burned_road", requires=(BUYER_BURNED,))),
        page("known_road", "Devarra", '''"So that is what his map was worth."
She closes her claw around the beetle, crushing two legs. The thread sings.
"He gave us a destination so we would never ask how he meant to keep us there."

You compare the cistern mark with the fleeting shape of the room beyond her wing.
The same hooked stroke has been cut into the wheel's rim.

"Leave the folios," she says. "We have something that screams when we squeeze it. That should be easier to follow."

She takes the road on foot, wings pressed tight against her sides.
Twice she stumbles without touching an obstacle.
The second time you offer your arm. She catches it hard enough to bruise, steadies herself, and lets go.
"Walk faster. Sympathy has short legs."''', c("Take the lower road.", "wheel_room")),
        page("burned_road", "Commander", '''"He was very careful to destroy the trail," you say, watching the thread draw a straight line through a solid wall. "Then he tied it to his waist."

Devarra bares her teeth. "Perhaps he wants us to follow."

"Then we must disappoint him when we arrive."

Following the thread costs most of the morning.
A culvert collapses beneath your boots, and Devarra has to claw it open while the thread tightens around her shadow.
By the time you find the dry cistern, daylight shines through her wingtips.
Burning the map denied the buyer his neat little exchange. It also cost you the hours he needed to turn his machine.''', c("Climb down ahead of her.", "wheel_room")),
        page("wheel_room", "Narrator", '''{n}The wheel once raised buckets; now it winds black thread around a shard of glazed stone.
Copper beetles swarm over its axle.
Their maker has climbed onto the far platform with a crossbow.
He wears an expensive coat backwards to keep its embroidered front clean.{/n}

"Stay there. I can send her back."

Devarra stops. "Back where?"

"Where she belongs. There are rules."

"Then you should have brought one tall enough to hide behind."

{n}The man retreats. The wheel turns by itself.
You recognize the pattern of the Tower's broken masonry on the shard.
Someone has stolen a fragment of the place that held her and taught it to pull.{/n}''',
            c("What do you think a dragon is worth alive?", "buyer_offer"),
            c("[Good] Give us the wheel, and you can leave breathing.", "buyer_offer"),
            c("[Evil] Keep winding. Every turn is another finger you will miss.", "buyer_offer")),
        page("buyer_offer", "Devarra", '''"Look at me when you put a price on me."

He does. His aim slips.
He calls himself Vey, a dealer in recovered curiosities.
The clutch's history was a lure. He has no eggs, no list of keepers, no secret account of a survivor.
He bought the copied folio because it named a dead dragon who had been seen walking, and he wanted the trick that made her possible.

"You wanted a specimen."

"An investment. I could have found patrons."

She moves closer. The thread draws blood where it crosses her shadow, although no flesh touches it.
"Commander. He has mistaken the restraint in this room for weakness. Correct him while I decide how much of the room I need to keep."

Behind Vey, the last empty spoke approaches the axle.''', c("Examine the Tower stone.", "latch")),
        page("latch", "Commander", '''The shard remembers a doorway.
Vey's device insists that Devarra is still passing through it, however far she walks.
The wheel keeps asking the same question: has she left yet?

A possibility presents itself. If the machine wants a departure, you might give it one it can never finish counting.
Vey sees your expression.
"Don't touch that."

"An excellent salesman's instinct. Alas, you began by showing me how it works."

You need to slip the beetle's jaws into the last spoke and send its thread back through the wheel.
Miss the opening, and the shard will have to be broken while it still has its teeth in Devarra.''',
            c("[Trickery 34] Make the returning thread register as another departure.", flags=(CISTERN_TRIED,), forbids=(CISTERN_TRIED,), check=dict(Skill="SkillThievery", DC=34, Success="wheel_caught", Failure="wheel_bites", CommanderOnly=True)),
            c("Break the shard together.", "wheel_bites")),
        page("wheel_caught", "Narrator", '''{n}The beetle bites its own thread.
The wheel spins, searching for the end of a departure that keeps departing.
A copper leg flies past Vey's ear. He drops the crossbow.
Devarra becomes solid with a crash of claws against stone.{/n}

"How long?"

"Until something leaves twice. I recommend we each leave once and disagree with anyone who keeps count."

She drives a talon into the axle.
The Tower shard drops into your palm, warm but inert.
"Keep that. If another man tries to put me in a box, I want something of his to put in it first."

{n}The shard still carries the shape of its doorway.
It may help you discover who taught Vey his trade.{/n}''',
            c("Pocket the shard.", "history_answer", flags=(ANCHOR_KEPT,))),
        page("wheel_bites", "Narrator", '''{n}The final spoke turns.
Devarra drives the wheel off its bolts.
You seize the shard before it falls through the black gap beneath the axle.
For a moment you are holding a doorway closed with your bare hand.
Something on the other side pushes back.{/n}

"Now."

Her jaws close around the stone.
It breaks. Your hand comes free, scored with a white scar from thumb to wrist.
Devarra strikes the wall hard enough to split its bricks.

{n}The gap closes.
You have no intact stone to examine.
Devarra unfolds her wings, testing each joint, and rises without help.{/n}

"A clumsy escape," she says, looking at your hand. "I prefer you clumsy to absent. Do not cultivate the habit."''',
            c("Bind the cut.", "history_answer", flags=(ANCHOR_PAID,))),
        page("history_answer", "Narrator", '''{n}Vey retreats behind the bucket rack.
Devarra hooks it aside.
There is very little room left for him to retreat.{/n}''',
            c("Hear her answer about her surviving brood.", "saved_answer", requires=(SAVED, SAVED_CUE)),
            c("Stand with her while she answers his lie about her dead clutch.", "lost_answer", requires=(LOST, LOST_CUE))),
        page("saved_answer", "Devarra", '''"My young escaped one set of chains. You meant to fasten another around their mother and call it gratitude."

Vey tries to speak. Furnace light washes over his face.
"If you ever learn where they went, forget it. If a buyer asks you for the name, forget the buyer."

She looks back at you.
"He has a teacher. He may have customers. I want them frightened before they become ambitious."

She has not asked him to take her to the eggs.
You cannot tell whether she fears another lie or has chosen to leave their safety undisturbed.
Her tail sweeps the broken axle off the platform.
"Well? You were full of promises on the way down."''', c("Consider his fate.", "judgment")),
        page("lost_answer", "Devarra", '''"Say what you told the messenger."

Vey stammers that it was only a way to arrange a meeting.
"The words."

"The truth of the clutch."

The flame behind her teeth goes white.
"There. Now you know how they sound in this room."

You have seen her angry before. This is quieter.
She rests her foreclaw on his platform; the wood smokes beneath it.
She is remembering lives that never reached the air, and Vey is looking for a price that might make her forget them.

"I could spend an hour on him. Perhaps two. Tell me why I should spend it elsewhere."

She turns her head enough to see you.
She wants an answer, and she has left you room to give one she dislikes.''', c("Give her an answer.", "judgment")),
        page("judgment", "Narrator", '''{n}Vey's crossbow lies under Devarra's foot.
He watches you, having discovered whose words might still change what happens next.{/n}''',
            c("[Good] He leaves his tools and tells us his teacher's name. Then he lives.", "mercy_cost", flags=(BUYER_SPARED,)),
            c("[Evil] Let him work for us. His patrons can discover what they bought when you collect.", "service_cost", flags=(BUYER_SERVES,)),
            c("He tried to cage you. I will hear his teacher's name; then I will not stop you.", "blood_cost", flags=(BUYER_KILLED,))),
        page("mercy_cost", "Devarra", '''"A generous offer. Spending my patience must be very pleasant."

She withdraws her foot from the crossbow and snaps its stock.
"He lives because I want to watch you keep him out of trouble. Remember whose amusement he owes his breath to."

Vey gives you a name, Serevin, and describes a woman with silver teeth who buys chipped magical stone.
They are to meet outside the old lime kilns in six days.

Devarra takes his embroidered coat.
"Leave. Explain to your friends why you are cold."

After he climbs out, she turns on you.
"If he sells another cage, you will help me find him. You have bought him a morning. Do not expect me to admire the purchase."''', c("I will answer for letting him go.", "return_fire")),
        page("service_cost", "Devarra", '''"That is almost worthy of the insult."

She lowers her head until Vey has to lean back.
"Attend your next meeting. Boast that your wheel worked. Ask your teacher what a living dragon is worth. When she names a sum, laugh."

You take his account book and lockbox key.
He gives you Serevin's name and the meeting at the lime kilns before you ask twice.

Devarra lets him climb the ladder.
"If he runs, we follow the money. If he stays, we follow his teacher."

She studies you with frank interest.
"There is a mean streak beneath the laughter. I wondered how long you would keep making it apologize."

Her approval does nothing to sweeten the bargain. You have taken a frightened man into your service, and he will have reasons to betray you.''',
            c("Fear alone makes poor servants. We should give him a reason to survive her.", "return_fire")),
        page("blood_cost", "Narrator", '''{n}Vey gives the name Serevin and the meeting at the lime kilns.
He gets as far as describing her silver teeth before Devarra moves.
You turn away from the sudden heat.
When you look back, the bucket rack is burning.{/n}

"She will know something went wrong when he fails to come. We have six days to decide what she sees instead."

There is no triumph in her voice. Nor is there regret.
She steps toward the ladder shaft, wings scraping soot from the walls.
At its foot she waits.
"Do you wish I had made it easier to watch?"

{n}The man was beaten and unarmed.
You heard him speak, and you stood aside.{/n}''',
            c("No. But I will remember what happened here.", "return_fire"),
            c("He gambled with a dragon's life. He lost.", "return_fire")),
        page("return_fire", "Narrator", '''{n}You reach the Tower after sundown.
Devarra leaves the machine outside, where its smell will not trouble her rest.
An old furnace warms the chamber beyond the gallery.
She folds herself beside it and watches you find a place on the bench.{/n}

"You are staring at my shadow."

It rests against the wall, whole.
"I preferred it attached."

"So did I. Come closer."

{n}She runs a careful claw over your knuckles, searching for injuries she did not ask about in the cistern.
Her touch is hot and surprisingly light.{/n}

She turns your hand toward the light. The lamplight finds every crease.''',
            c("Show her the uninjured hand and the shard you brought back.", "return_kept", requires=(ANCHOR_KEPT,), forbids=(ANCHOR_PAID,)),
            c("Let her inspect the cut the doorway left.", "return_paid", requires=(ANCHOR_PAID,), forbids=(ANCHOR_KEPT,))),
        page("return_kept", "Devarra", '''"You looked pleased when the wheel began counting itself."

"It finally had an occupation suited to its abilities."

She laughs and takes the inert stone from your palm, weighing it with one claw.
"You made his own device too busy to obey him. I approve. Next time, try it before I begin disappearing."

"I would have preferred that as well."

She returns the shard. Her claws linger against your fingers.
"Keep it out of other collectors' hands. I prefer to flirt with someone who can remain in the room."''',
            c("I have never been safe with you. That may be part of the attraction.", "near_fire"),
            c("I want your company tonight, but I am not ready for more.", "quiet_fire")),
        page("return_paid", "Devarra", '''The cut has bled through its binding. Devarra catches your wrist before you can fold your hand shut.
"You might have mentioned that."

"You were insulting the axle. I did not want to interrupt."

She brings the water jug closer with her tail and waits while you loosen the cloth.
The wound is shallow; the white line beside it is colder than the rest of your skin.
When you rinse it, the cold recedes.

"We should have broken his wheel sooner," she says.

"And missed his description of its market value?"

The laugh takes her by surprise. She steadies the jug until you have finished binding your hand, then lays her claw beside it.
"You came back with me. That is a result I intend to keep."''',
            c("I have never been safe with you. That may be part of the attraction.", "near_fire"),
            c("I want your company tonight, but I am not ready for more.", "quiet_fire")),
        page("near_fire", "Devarra", '''"Then your judgment is as poor as I hoped."

She draws your hand against the warm scales beneath her jaw.
You feel her pulse, slow and strong.
For a while she lets you learn the pressure she likes, eyes narrowed to bright slits.
Then she brushes her mouth against your palm.

"I want you here tonight. There is no buyer outside that door. No witness waiting for us to say something wise. We could waste an entire evening."

Her gaze settles on your mouth.
"I have been told you excel at that."

{n}The joke has impatience under it.
She waits with your hand still resting against her throat.{/n}''',
            c("Stay beside her and return the offered kiss.", "night_kept"),
            c("Stay, but keep the evening quiet.", "quiet_fire")),
        page("night_kept", "Narrator", '''{n}She meets you carefully, then less carefully when you lean closer.
Her laugh warms your cheek.
There is no audience for the look she gives you afterward, and no useful thing to do with it.
You stay.

Later, the furnace settles with a sigh.
Devarra draws one wing around the bench, shutting out the draught.
You listen to the Tower creak and feel her breathing slow beside you.
She does not move away when you lay your hand over hers.
The machinery in the courtyard can wait for daylight.{/n}''',
            c("Spend the night together.", flags=(CONSEQUENCE_DONE, NEXT_FIRE, AFTER_FIRE_DONE))),
        page("quiet_fire", "Devarra", '''"Then sit. I have no intention of spending the evening listening to you explain why."

She pushes a cushion toward your end of the bench.
After a while she begins describing the exact faults in Vey's machine.
Her account becomes increasingly insulting.
You contribute improvements to the insults, and she rejects most of them.

"You are tired. Tomorrow you may try again."

She leaves her hand near yours.
When you take it, she does not interrupt her account of the crooked axle.''',
            c("Stay until the furnace burns low.", flags=(CONSEQUENCE_DONE, NEXT_FIRE, AFTER_FIRE_DONE))),
    ],
    requires=("trickster", EXCHANGE_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED, CONSEQUENCE_DONE), delay=12, last=5, optional=True,
    RequiresAnyGroups=[(SAVED, LOST), (SAVED_CUE, LOST_CUE)],
)



KILN_TRIED = "devarra.trickster.kiln_approach_attempted"
KILN_LOCK_KNOWN = "devarra.trickster.kiln_lock_known"
KILN_LOCK_UNKNOWN = "devarra.trickster.kiln_lock_unknown"
KILN_TRICK_TRIED = "devarra.trickster.kiln_contract_attempted"
KILN_PRISONERS_FREE = "devarra.trickster.kiln_prisoners_free"
KILN_LEDGER_TAKEN = "devarra.trickster.kiln_ledger_taken"
KILN_SEREVIN_HELD = "devarra.trickster.serevin_held"
KILN_SEREVIN_ESCAPED = "devarra.trickster.serevin_escaped"
KILN_DONE = "devarra.trickster.kiln_complete"
KILN_RETREATED = "devarra.trickster.kiln_retreat"
KILN_RETRY_CLOSED = "devarra.trickster.kiln_retry_closed"
KILN_INTIMACY = "devarra.trickster.kiln_evening_close"

LIME_KILN_SCENE = scene(
    "devarra.trickster.the_price_of_an_empty_cage", "The price of an empty cage",
    "Devarra", 5, "kiln_appointment",
    [
        page("kiln_appointment", "Narrator", '''{n}The lime kilns stand beyond an orchard that has not borne fruit in years.
White dust fills the ruts. It records every wheel that approaches and every foot that leaves.
Someone has swept the path to the largest kiln, then forgotten to sweep the broom marks.
Devarra examines them with a disdainful curl of her lip.{/n}

"I hope she paid Vey very little for his education."

{n}The appointed bell has not sounded yet.
At the top of the kiln, a woman in a grey coat is hanging red glass lamps beneath a loading beam.
Sunlight flashes from her silver teeth when she bites through a length of thread.
Devarra draws her wings close and moves behind the broken orchard wall.
She could announce herself with fire. For the moment, she is willing to see what your arrangements have brought.{/n}''',
            c("Look for Vey. You let him go with his life.", "vey_spared", requires=(BUYER_SPARED,), forbids=(BUYER_SERVES, BUYER_KILLED)),
            c("Check whether your reluctant agent has arrived.", "vey_serves", requires=(BUYER_SERVES,), forbids=(BUYER_SPARED, BUYER_KILLED)),
            c("Study the meeting place Vey will never reach.", "vey_absent", requires=(BUYER_KILLED,), forbids=(BUYER_SPARED, BUYER_SERVES))),
        page("vey_spared", "Commander", '''Vey waits behind the orchard wall in a coat that is too short for him.
He sees Devarra and immediately looks at you.
"I told her the wheel broke. I did not tell her you were coming."

"An unusually promising distinction," Devarra says. "Continue."

He has brought no weapon and no device. He has also brought the written offer Serevin sent him after his failure.
It promises twice his old fee for a live demonstration and says nothing about compensating an injury.
He wants you to understand why he returned.

"You gave me a morning. I should like another one."

Devarra reads the offer over your shoulder.
"And you hoped the Commander would buy it again."

"Yes."

She seems almost pleased by the honest answer.
Vey tells you that the red lamps detect a creature passing beneath them. The lamps will count a dragon as a delivery if anyone carrying Serevin's marked paper presents her at the beam.
He refuses to carry it himself. He has seen what the wheel did, and there are three lamps instead of one.

You send him down the road before Serevin can see him from the kiln.
Devarra watches him leave.
"Mercy has produced one useful piece of information. Do not become insufferable about it."''',
            c("Take the offer and examine the loading beam.", "kiln_survey", flags=("devarra.trickster.vey_warning_received",))),
        page("vey_serves", "Devarra", '''Vey arrives carrying a sample case and wearing a smile that fails when he sees her.
"I told her the wheel worked. She doubled the fee."

"You laughed?"

"As instructed. She doubled it again."

Devarra turns a slow, delighted look on you.
"We should employ more people who are frightened of two employers at once."

Vey opens the case. Inside lies a receipt bearing the same red-lamp mark as the kiln's loading beam.
Serevin has written that anything delivered beneath that mark becomes hers upon acknowledgement.
The price is to be discussed afterward.

"She intended to pay me whatever I could persuade her to pay once she had the dragon," he says.

"You are learning," Devarra replies.

He asks for a share of whatever you recover, and for his account book back if he survives the meeting.
His fear has given him a reason to obey you. It has also given him a reason to make himself worth more alive than dead.
Devarra lets you answer him. Her interest is plainly in which kind of employer you choose to be.''',
            c("Promise the book and a tenth of the recovered money. He has earned a reason to survive.", "kiln_survey", flags=("devarra.trickster.vey_share_promised",)),
            c("The book stays with us. His payment is leaving the kiln alive.", "kiln_survey", flags=("devarra.trickster.vey_debt_enforced",))),
        page("vey_absent", "Narrator", '''{n}Serevin lights the first red lamp, although the sun is still above the loading beam.
She waits for Vey until the bell strikes.
Then she takes a crossbow from under the bench and turns its winding handle.{/n}

"She knows something failed," Devarra says. "She does not yet know how completely."

{n}There will be no agent to approach her with a harmless case, no frightened craftsman to describe the lamps.
Devarra killed the man who could have done either.
A strip of paper bearing the same red mark as the beam has been nailed to a post beside the road.
From the shelter of the orchard wall, you can read only the large word at its top: RECEIPT.{/n}

"I would still kill him," she says. "If that is the question you are preparing."

"I was preparing a question about the lamps."

"Better. We may find an answer to that one."

{n}You wait until Serevin walks around the kiln to check the rear gate, then cross the road and pull the receipt from its nail.
The terms are short. Anything delivered beneath her red mark becomes hers when she acknowledges it.
She has left no amount beside the price.
You return to the wall before she comes back, carrying the paper and a little more respect for what Vey was willing to enter.{/n}''',
            c("Show Devarra the receipt.", "kiln_survey", flags=("devarra.trickster.vey_absence_exposed",))),
        page("kiln_survey", "Commander", '''Beyond the loading beam, a row of shallow stone cells has been cut into the cold kiln.
Two people sit inside one of them, chained at the wrists to a copper rail.
A pair of discarded quarry picks rests outside the door.
Serevin has found laborers to test whether her lamps can keep a living delivery from walking out again.

Devarra's tail stops moving.
"No more talk of merchandise. Find the catch."

The lamps burn without consuming oil. A thin red reflection passes from each one to the rail inside the cell, then to the receipt in your hand.
There must be a point where Serevin's mark turns passage into possession.
If you can identify it, you may be able to give her exactly what she is expecting, in a form she will regret accepting.''',
            c("Ask how her bargain with Vey differs from the copper rail.", "kiln_employment", requires=(BUYER_SERVES,)),
            c("Use the intact Tower shard to read the lamps' doorway pattern.", "shard_survey", requires=(ANCHOR_KEPT,), forbids=(ANCHOR_PAID, BUYER_SERVES)),
            c("The shard is gone. Follow the physical work instead.", "stone_survey", requires=(ANCHOR_PAID,), forbids=(ANCHOR_KEPT, BUYER_SERVES))),
        page("kiln_employment", "Devarra", '''"A bargain can be broken," she says. "You have made breaking yours expensive. That rail has removed the question."

She looks toward Vey, who has kept well back from the lamps.
"If you mean to tell me both arrangements are generous, save your breath. We have made use of a frightened man. I never asked you to pretend otherwise."

Her gaze returns to the cell.
"Now find the catch. We can admire your employment practices afterward."''',
            c("Use the intact shard.", "shard_survey", requires=(ANCHOR_KEPT,), forbids=(ANCHOR_PAID,)),
            c("Study the physical latch.", "stone_survey", requires=(ANCHOR_PAID,), forbids=(ANCHOR_KEPT,))),
        page("shard_survey", "Devarra", '''You turn the shard toward the red glass.
Its glazed face darkens until the three lamps appear in it as three open doors.
Behind two is empty stone. Behind the third, Serevin's own shadow is drawing a bolt.

Devarra keeps her body behind the orchard wall.
"If that thing begins pulling, I break it."

"An incentive to finish promptly."

"You are discovering the advantages of working with me."

The shard gives you the connection. It does not tell you which mark controls it.
Serevin has learned from Vey's wheel: the door is no longer asking whether a captive has left. It asks whether its owner has accepted delivery.''',
            c("[Knowledge: Arcana 33] Identify the mark that turns Serevin's acknowledgement into the lock.", flags=(KILN_TRIED,), forbids=(KILN_TRIED,), check=dict(Skill="SkillKnowledgeArcana", DC=33, Success="lock_known", Failure="lock_unclear", CommanderOnly=True))),
        page("stone_survey", "Commander", '''Without the shard, the red light is only light.
You circle the outside of the wall while Devarra watches the loading beam.
White dust has settled into every crack except a narrow groove running from the rear gate toward Serevin's bench.
Something has been drawn through it often enough to leave the stone clean.

The cold line across your hand aches when you touch the groove.
Whatever answered from the other side of Vey's doorway has left you an unpleasant sensitivity to its relatives.
You withdraw your hand before the ache can become an answer.

A copper latch beneath the bench carries the same mark as the receipt.
You can study its scratches from here, or retreat before Serevin returns from checking her lamps.''',
            c("[Perception 33] Read the wear on the latch and work out which motion accepts delivery.", flags=(KILN_TRIED,), forbids=(KILN_TRIED,), check=dict(Skill="SkillPerception", DC=33, Success="lock_known", Failure="lock_unclear", CommanderOnly=True)),
            c("Retreat and watch, risking the cart's departure rather than attempting the latch now.", "kiln_retreat")),
        page("kiln_retreat", "Narrator", '''{n}You withdraw behind the orchard wall and take Devarra with you.
No latch is touched, and no attempt has been spent trying to read it.
Serevin checks the road, then begins packing the lamps' oil cases for transport.
She still needs the quarry cart to move the prisoners. The ruts leading from the quarry are empty.{/n}

"An hour at most," Devarra says. "Watch where she puts her hands. I will watch the road."

{n}You leave the near wall and settle in the higher orchard, beyond the red light.
The meeting is over for now. Another approach will have to be deliberate.{/n}''',
            c("Withdraw from this attempt. Be prepared to follow the workers after the cart leaves.", flags=(KILN_RETREATED,))),
        page("lock_known", "Commander", '''You find the trick in the receipt's blank price.
Serevin does not need to pay. She needs only to say that she accepts what has been brought under the beam.
The latch follows her voice; the lamps establish where the delivery stands.

"A very profitable contract," you tell Devarra. "Especially if one brings the owner to the goods."

Her gaze moves from the receipt to the beam.
"Explain the amusing part before you reach it."

You show her how the lower stroke can be folded through its own acknowledgement.
If Serevin steps beneath the beam holding the receipt and says that she accepts it, she will identify herself as both the owner taking delivery and the thing delivered.
Your power can make that contradiction hold long enough to break her command of the lamps.
It will need her exact words and her actual position. A forgery of her voice will not be enough.

Devarra's smile shows every tooth.
"Bring her a convincing price."''', c("Approach the loading beam.", "serevin_offer", flags=(KILN_LOCK_KNOWN,))),
        page("lock_unclear", "Narrator", '''{n}The reflection vanishes as Serevin turns the third lamp.
You have the receipt and a suspicion about its blank price, but no reliable way to tell which acknowledgement closes the latch.
Guessing would put you beneath the beam while she held the answer.{/n}

"Then we do it without the clever version," Devarra says.

{n}She studies the rail in the cell.
Fire could open it, if she spent her first breath on the lock instead of Serevin.
The woman would have time to reach the rear gate.
Alternatively, you could take the ledger from her bench and pursue her while the prisoners stayed behind the rail.
Neither plan preserves everything you came for.{/n}

"I can chase a woman or melt copper," Devarra says. "Choose which you intend to help me do."''',
            c("Approach with the receipt and keep her attention away from the cell.", "serevin_offer", flags=(KILN_LOCK_UNKNOWN,))),
        page("serevin_offer", "Devarra", '''Serevin sees you first and raises the crossbow.
Then Devarra steps out from behind the orchard wall.
The weapon lowers by a finger's width.

"You have brought her," Serevin says.

"I came," Devarra replies. "Practice the distinction."

The silver teeth show in a practiced smile.
Serevin names three wealthy patrons and a figure large enough to buy the orchard, the road and the village beyond them.
She has room for a partner who understands what an exceptional creature is worth.

Devarra moves one forefoot forward.
The dust begins to bake into a crust beneath it.
"I understood the offer before you finished. You may stop making it."

Serevin's free hand reaches toward the latch under her bench.
Inside the cell, one of the quarry workers starts to stand, then sinks back when the copper rail brightens.
You have her attention and perhaps another sentence before she decides that a failed sale should become a demonstration.''',
            c("[Trickster] The fee is your receipt. Step beneath the beam and accept delivery, if you mean to pay what you promised.", "receipt_trap", requires=(KILN_LOCK_KNOWN,)),
            c("[Good] Devarra, open the cell. Let the collector run if that is the price.", "free_workers"),
            c("[Evil] Take the ledger and cut off her retreat. The workers can wait until she has answered.", "seize_ledger")),
        page("receipt_trap", "Commander", '''You hold the receipt where Serevin can read her own signature.
"No coin was named. You promised to accept the delivery. I am offering the only thing here whose ownership is not in dispute."

"Paper."

"Your paper. Your mark. Your word. Unless one of those has become worthless since you wrote it."

She glances at Devarra, who has stopped just outside the red light.
Serevin presses a copper ring against the bench. A red spark circles her wrist and returns to the lamps.
"The handler is exempt," she says. "I tested that before I ever hired Vey."
She steps beneath the beam because it puts the lamps between her and Devarra, and keeps you within reach of the latch.
Her safeguard works on the owner named by the receipt. You intend to make that same owner the delivery, a contradiction her ordinary tests never supplied.
Serevin keeps her ring against the marked wood while she reaches out with her other hand.

"I accept it."

You fold the lower stroke toward her waiting hand.
For an instant the red lamps illuminate the wrong side of every object in the yard.
Serevin has accepted a document that now describes the person accepting it as its delivery.
Your power has to hold both readings together while she is still speaking.
If you lose the moment, Devarra will have to break the cell's rail before Serevin closes the door on everyone.''',
            c("[Knowledge: World 35] Keep her acknowledgement attached to both readings of the receipt.", flags=(KILN_TRICK_TRIED,), forbids=(KILN_TRICK_TRIED,), check=dict(Skill="SkillKnowledgeWorld", DC=35, Success="receipt_held", Failure="receipt_lost", CommanderOnly=True))),
        page("receipt_held", "Narrator", '''{n}The lamps turn inward.
Serevin's shadow rises to meet her wrists and holds them against the loading beam.
The crossbow falls.
Inside the kiln, the copper rail opens its locks with a succession of small, offended clicks.{/n}

"That is not what I accepted."

"You should insist on a more precise contract," you tell her.

{n}Devarra walks beneath the extinguished lamp and lowers her head until Serevin can see her reflected in both gold eyes.{/n}

"Is this the part of the demonstration where I am supposed to admire the workmanship?"

{n}The quarry workers leave the cell.
You take Serevin's ledger from the bench before either has a chance to use it as kindling.
The first page lists payments for chipped stone from several places where the Worldwound's old magic lingers.
Beside one ruined watchtower, a black mark has been drawn twice.{/n}''',
            c("Keep her for questioning and let the workers leave.", "captured_terms", flags=(KILN_PRISONERS_FREE, KILN_LEDGER_TAKEN, KILN_SEREVIN_HELD))),
        page("receipt_lost", "Narrator", '''{n}The second reading tears away from the first.
Serevin lets go of the receipt before the red light can close around her wrists.
The latch slams down.{/n}

"Devarra!"

{n}Her fire takes the copper rail before the cell's stone door has fallen halfway.
The workers crawl through the gap.
You drag the slower one clear while Devarra braces the door with a foreclaw.
Beyond the yard, the rear gate bangs open.
Serevin has her ledger beneath one arm and a considerable head start.{/n}

"I heard enough of that contract," Devarra says through her teeth.
"Move. This door is irritating me."''',
            c("Get everyone beyond the beam before she lets the door fall.", "escaped_terms", flags=(KILN_PRISONERS_FREE, KILN_SEREVIN_ESCAPED, "devarra.trickster.kiln_paradox_failed"))),
        page("free_workers", "Narrator", '''{n}You throw the receipt into Serevin's face.
It buys less than a heartbeat, which is all Devarra needs to turn toward the cell.
The copper rail runs bright and falls apart in a shower of white sparks.
The workers stumble into the yard.{/n}

{n}Serevin reaches for her ledger.
You could still reach her before she gets to the rear gate, if you stop helping the man whose wrists have burned against the rail.
You keep your hand beneath his arm.
She takes the book and runs.{/n}

Devarra tears the nearest lamp from its hook.
"A collector should leave something behind."
She crushes the red glass between her claws and looks down the road after Serevin.
"I will remember which way she went."''',
            c("Get the workers into the shade and check their burns.", "escaped_terms", flags=(KILN_PRISONERS_FREE, KILN_SEREVIN_ESCAPED))),
        page("seize_ledger", "Commander", '''You go for the bench while Devarra blocks the rear gate.
Serevin loses the book when you kick its lower shelf into her legs.
She rolls beneath the loading beam, reaching for the latch.
Devarra's tail strikes the ground between her fingers and the copper handle.

"You should have taken the generous offer," she says.

The workers shout from inside the cell.
Serevin has tightened the rail around their wrists, hoping their cries will make you leave her an opening.
You keep the ledger out of her reach.
Devarra pins her sleeve to the ground with a talon until she tells you which lamp releases the lock.

It takes longer than it should have.
When the rail finally opens, one worker cannot close his hand.
His companion looks at the book beneath your arm and then looks away.

Devarra sees the glance.
"You wanted the names," she says to you. "Now we have them. Decide what you intend to do with the price before you ask me to call it necessary."

She has helped you take Serevin. She has not volunteered to excuse the choice for you.''',
            c("Take Serevin alive, with the ledger. Pay for the workers' care afterward.", "captured_terms", flags=(KILN_PRISONERS_FREE, KILN_LEDGER_TAKEN, KILN_SEREVIN_HELD, "devarra.trickster.workers_hurt_for_ledger"))),
        page("captured_terms", "Devarra", '''Serevin sits against the orchard wall with her hands bound by her own copper wire.
Without her smile, the silver teeth look like repairs.
She gives you the watchtower's location after Devarra asks whether its doors are larger than the cistern's.
The double mark means a purchase already paid for and a second purchase still expected.
Someone is buying the same stone twice.

"Where is the stone now?"

"Under the tower. The lower vault. I was going there after this."

You ask how the lower door opens. Serevin gives the order for turning its copper plate, then repeats it while you write it in the ledger.
Devarra keeps one claw beside the page until the two accounts match.

Devarra presses the toe of one claw into the margin of the ledger.
"Then we shall spare you the inconvenience."

You arrange a guard from the nearby quarry to take Serevin into custody with a copy of the workers' account.
The original book stays with you.
Devarra watches the wire around the collector's wrists.
"I would have preferred a shorter conversation. But she will be available if the book lies. That has some value."''',
            c("Keep the ledger and the lower-vault appointment.", "kiln_departure", flags=("devarra.trickster.lower_vault_location",))),
        page("escaped_terms", "Commander", '''The quarry workers know which road Serevin took, but she had a horse beyond the orchard.
By the time you reach the gate, there is only white dust moving over the hoofprints.
You have neither the ledger nor the collector.

One of the workers calls you back.
He helped load a cart with chipped stone three mornings ago.
It went north to a ruined watchtower, and the driver paid him twice, once to load the cart and once to forget its destination.
He has decided the second payment was insufficient.

Devarra asks him to draw the tower's mark in the dust.
He draws two black strokes with a burned finger.
You copy them before the wind can erase either.

"She will warn whoever buys from her," Devarra says.
"We may find an empty room and a trap."

"Then we shall be very suspicious of its hospitality."

She gives you a look that is almost a smile.
"Bring something useful besides that."''',
            c("Take the worker's directions, knowing Serevin will arrive first.", "kiln_departure", flags=("devarra.trickster.lower_vault_location", "devarra.trickster.lower_vault_warned"))),
        page("kiln_departure", "Narrator", '''{n}You leave the lamps broken on the loading beam.
The workers take the road to the quarry, where there are clean bandages and people who will recognize them.
Devarra waits until they are beyond the orchard before letting out the breath she has been holding.
It scorches a black line through the white dust.{/n}

"Every collector believes his cage will be different."

{n}She looks at the dark outline of her own claws, as if the sight still needs confirming after the cistern.
You stand beside her without offering a lesson about survival.
The lamps are broken. She is here.
For the moment, those facts are enough to argue with the fear.{/n}

"When we return," she says, "I want an evening in which nobody asks me to demonstrate anything."

"I had prepared a very persuasive speech about supper."

"Burn it. Bring supper."

{n}She starts toward the road, then pauses until you catch up.{/n}''',
            c("Settle the share and return the account book you promised Vey.", "vey_paid", requires=(BUYER_SERVES, "devarra.trickster.vey_share_promised")),
            c("Remind Vey what you still hold over him.", "vey_bound", requires=(BUYER_SERVES, "devarra.trickster.vey_debt_enforced")),
            c("Tell her what you would like from the evening before making another joke.", "kiln_evening", forbids=(BUYER_SERVES,)),
            c("Stay with her, but ask for a quiet meal and separate rooms tonight.", "kiln_quiet", forbids=(BUYER_SERVES,))),
        page("vey_paid", "Commander", '''Vey waits beyond the orchard with the empty sample case.
He has kept himself out of the red light and out of Devarra's way, which she considers two unusually intelligent decisions.

You return the account book taken at the cistern.
There was no recovered money to divide; the kiln held prisoners and records, not a cash box.
Vey turns the book over, checking that its spine has not been opened.

"Then I am finished?"

"With us," you tell him. "If you decide to build another wheel, expect another visit."

Before leaving, he describes the safety catches his supplier charged for and never fitted.
The copper return counters have empty slots where the catches should be.
It is the last useful thing he can offer you, and he offers it after receiving his book.

He leaves without trying to make his relief look dignified.
Devarra watches him until he is well down the road.
"A useful servant released before he became resentful enough to be inventive. That may prove cheaper than the alternative."

"Almost a compliment."

"I am waiting to see whether he is intelligent enough to keep walking."''',
            c("Leave Vey to his own road and speak to her about the evening.", "kiln_evening", flags=("devarra.trickster.vey_released",)),
            c("Leave Vey to his own road and ask for a quiet supper.", "kiln_quiet", flags=("devarra.trickster.vey_released",))),
        page("vey_bound", "Devarra", '''Vey waits beyond the orchard with his sample case clasped against his chest.
You keep the account book.
He is to send word of anyone asking after chipped stone, old doorways or a collector with silver teeth.
When he asks how long, you tell him that depends on how useful the messages are.

Devarra lets him walk three paces before calling him back.
"If you intend to sell us to someone, ask for enough that I will respect the attempt."

He says he would never consider it.
She bares her teeth until he stops speaking.

After he has gone, she looks at the book under your arm.
"That buys obedience for a while. He will spend the interval looking for something to hold over you."

"Then he should become a very observant man."

"So should you." Her claw taps the book once. "I like your mean streak. I will not let it excuse stupidity."''',
            c("Keep the account book and speak to her about the evening.", "kiln_evening", flags=("devarra.trickster.vey_obligation_continues",)),
            c("Keep the account book and ask for a quiet supper.", "kiln_quiet", flags=("devarra.trickster.vey_obligation_continues",))),
        page("kiln_evening", "Devarra", '''"Your company," you say. "The pleasure of hearing you insult something that is not trying to kill us. Another kiss, if the evening is going well."

"A modest list. Suspiciously modest."

"You may negotiate."

"I intend to."

At the Tower, she makes you carry the food to the gallery instead of the old furnace room.
The windows face the dark orchard hills. No red lamps hang above them.
She eats before she asks about the ruined watchtower, and dismisses your first attempt to spread the copied mark beside the plates.

"Tomorrow. I asked for an evening."

You put it away.
She draws closer after the meal, keeping the edge of one wing between the two of you and the open window.
Her cheek brushes your temple.

"There," she says. "Something I wanted without a practical reason. Do not make me regret admitting it."

You turn toward her. She meets the movement, her mouth warm against your cheek, then waits until you lean into her before continuing.
The next joke goes unspoken.
Outside, the Tower's bell counts the hour correctly for once.''',
            c("Stay with her and leave the investigation for morning.", flags=(KILN_DONE, KILN_INTIMACY))),
        page("kiln_quiet", "Devarra", '''"Good. I was beginning to suspect you slept only when ambushed."

She insists on the gallery table, where the windows open onto a stretch of dark hills.
You eat while she describes the sort of hoard Vey's sample case would have deserved.
It is a brief list and none of its contents would be valuable to anyone but a dragon with an excellent memory for insults.

When the plates are empty, she takes the copied watchtower mark before you can unfold it.
"Tomorrow. You asked for a quiet evening. I accepted. Try not to become tiresome about your own proposal."

At the door, she nudges your shoulder with the side of her muzzle.
She could block the doorway without moving anything but a wing.
Instead she leaves it open and watches until you turn at the stair.

"Sleep, Commander. If the next collector makes a mistake, I want you awake enough to enjoy it."''',
            c("Say good night and return to your own room.", flags=(KILN_DONE,))),
    ],
    requires=("trickster", CONSEQUENCE_DONE, AFTER_FIRE_DONE, NEXT_FIRE, ROMANCE,
              "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED, KILN_DONE, KILN_RETREATED), delay=144, last=5, optional=True,
    Relationship="devarra.trickster", ManualOnly=True, Remote=False,
    PhysicalPresenceRequired=True, ContactUnit="Devarra",
)

VAULT_DONE = "devarra.trickster.vault_complete"
VAULT_TRIED = "devarra.trickster.vault_address_attempted"
VAULT_MAP_KEPT = "devarra.trickster.vault_map_kept"
VAULT_MAP_BURNED = "devarra.trickster.vault_map_burned"
VAULT_EXPOSED = "devarra.trickster.vault_departure_exposed"
VAULT_SHARED_POWER = "devarra.trickster.vault_shared_power"
VAULT_AFTER_DONE = "devarra.trickster.vault_evening_complete"

LOWER_VAULT_SCENE = scene(
    "devarra.trickster.the_door_that_owed_a_debt", "The door that owed a debt",
    "Devarra", 5, "vault_road",
    [
        page("vault_road", "Narrator", '''{n}The ruined watchtower stands above a stream whose banks are streaked green.
Its upper floor has fallen into the stairwell. The door at ground level is new, clean oak fitted to stone that has weathered for centuries.
Devarra stops where the stream crosses the road and lowers her head to the water.{/n}

"Copper. Hot copper. Something below that tower has begun emptying itself."

{n}The next settlement lies downstream.
From here you can see its waterwheel turning between the trees.
Nobody is waiting at the tower to sell you a dragon or explain a price.
There is only the new door, a plume of warm air from the old arrow slit, and the road you chose at the kiln.{/n}''',
            c("Serevin escaped. Assume she has warned the vault.", "vault_warned", requires=(KILN_SEREVIN_ESCAPED,), forbids=(KILN_SEREVIN_HELD,)),
            c("Use the ledger taken with Serevin to identify the lower entrance.", "vault_unwarned", requires=(KILN_SEREVIN_HELD, KILN_LEDGER_TAKEN), forbids=(KILN_SEREVIN_ESCAPED,))),
        page("vault_warned", "Commander", '''A horse has crossed the stream ahead of you.
Its tracks climb toward the tower, then turn sharply east.
Serevin came here and left again.

The new door is open. Its lock has been pulled out from the inside, leaving a neat square hole and a heap of filings.
Below the threshold, a copper pipe pulses like a vein.

Devarra sniffs the warm air.
"She has left the machinery to kill its own witnesses. Sensible. Irritating."

You find a list of outgoing carts nailed inside the doorframe.
Every destination has been scraped away.
The vault is no longer a place you can enter unnoticed and examine at leisure.
Its operators are gone, its records are being destroyed, and the hot runoff will reach the waterwheel before evening.

"Next time," Devarra says, "I would like to argue about the woman before we let her escape."

"You were occupied with the prisoners."

"I remember. I am describing a preference, not asking you to improve the memory."''',
            c("Follow the pipe into the vault.", "vault_fate")),
        page("vault_unwarned", "Devarra", '''The ledger's double mark matches the lower door.
You turn the locking plate in the order Serevin supplied. Inside, a bell gives one muted note.

"Would she have told you how to silence that?" Devarra asks.

"We did not get as far as courteous entry."

"A gap in your education."

The narrow room beyond the door is empty.
A meal has dried beside a stack of cart receipts. The operators left before the kiln meeting, expecting Serevin to bring the next shipment.
They have left their accounts and the apparatus running.

The ledger identifies the warm pipe as a discharge channel.
When its copper reservoir fills, excess heat drains into the stream.
You have time to locate the reservoir before it fails, provided you resist the temptation to read every interesting page first.

Devarra glances at the receipts.
"I am willing to be offended by them afterward. That is a considerable concession."''',
            c("Mark the discharge wheel in the ledger and descend.", "vault_fate")),
        page("vault_fate", "Narrator", '''{n}The first landing holds a carpenter's bench and several unfinished copper housings.
One bears the same maker's cut as Vey's beetle.
The people who supplied him worked here.
His part in this has followed you into a room he never described.{/n}''',
            c("Remember the warning he brought after you spared him.", "vault_spared", requires=(BUYER_SPARED,)),
            c("Compare the housings with the account book you still hold over him.", "vault_bound", requires=(BUYER_SERVES, "devarra.trickster.vey_obligation_continues")),
            c("Use the description Vey gave before you released him from service.", "vault_released", requires=(BUYER_SERVES, "devarra.trickster.vey_released")),
            c("Examine the maker's cut without its dead owner's help.", "vault_dead", requires=(BUYER_KILLED,))),
        page("vault_spared", "Commander", '''Vey warned that the lamps measured passage beneath them.
Here, narrow copper bands cross the floor at ankle height.
You step over the first and hear a click from inside the housing.
It has counted something despite your careful footwork.

Devarra lifts her tail before it touches the next band.
"He told you what he knew. Someone here knew more."

You set a loose board over the remaining bands and cross it.
There is no further click.
The man you spared bought you a suspicion, enough to stop you striding into the rest of the apparatus as though it were ordinary plumbing.
It did not buy a complete map.
Devarra waits until you have braced the board before putting her weight on it.''',
            c("Hold the board while she crosses.", "vault_reservoir")),
        page("vault_bound", "Devarra", '''The account book names the housings as return counters.
Vey has drawn a small correction beside the price of each: the maker had charged him for a safety catch that was never fitted.

"An honest grievance," she says. "How unusual to find one of his."

You wedge the counters open with pieces of their own packing wood.
Devarra watches you put the book away.

"When we leave, tell him you used it. Let him wonder which of his secrets are still worth selling."

"You enjoy this arrangement."

"I enjoy seeing whether you are clever enough to keep it. There is a difference."

The counters stop moving.
The book has paid for a little of the danger you accepted by keeping its owner frightened of you.''',
            c("Take the passage while the counters are stopped.", "vault_reservoir")),
        page("vault_released", "Commander", '''Before leaving the orchard, Vey described the safety catches he had paid for and never received.
You remember because Devarra laughed at the price.
The copper housings have empty slots exactly where his catches should have fitted.

You cut wedges from the packing wood and jam them into those slots.
One counter clicks against the wedge, then gives up.

"We might have learned that with the book," Devarra says.

"We learned it while giving the book back."

"Yes. You will be tiresome about that for some time."

She steps over the stopped mechanism and waits for you on the far side.
The information outlasted your power over its owner.
Whether that makes the next bargain easier remains to be discovered.''',
            c("Follow her across.", "vault_reservoir")),
        page("vault_dead", "Narrator", '''{n}The maker's cut tells you whose work this resembles, and very little about what it does.
Devarra studies the copper bands crossing the floor.
Then she hooks one housing up from its bolts and tears out the little wheel inside.{/n}

"We could have asked Vey," you say.

"We could have asked him many things. We killed him instead."

{n}She holds the ruined housing while you disconnect its neighbors.
It is slower than opening a catch, and one wheel cuts your glove before it stops.
Devarra has not changed her opinion of the man.
She has also not pretended that killing him left you every advantage you might have had.{/n}''',
            c("Finish disconnecting the wheels.", "vault_reservoir")),
        page("vault_reservoir", "Narrator", '''{n}Below the last landing lies a copper basin as wide as a cottage.
Black glass plates hang over it on iron arms, each etched with a doorway and a number.
Every few breaths, one plate flashes and a line of hot copper runs into the basin.
The discharge pipe leads from its lowest point to the stream outside.{/n}

Devarra follows the hanging plates with her eyes.
"Those are not places. They are departures."

{n}You find the Tower's fractured threshold on the nearest plate.
Beside it is a tracing of her wing, flattened into a measurement.
The apparatus has been buying copies of her passage through that threshold and selling devices that can call it unfinished.
Other plates carry shapes you do not recognize.
Their backs list buyers in a cramped cipher. Devarra begins reading one name, then stops when the basin groans again.
None holds a soul. They record movements, then teach doors to dispute that those movements ever ended.{/n}

"A man sees me walk through a doorway," she says, "and decides there must be a way to charge for letting me leave."

{n}The basin gives a deep metallic groan.
You have found the source of the collectors' device.
You have also found a machine that will empty its waste into someone else's drinking water when it breaks.{/n}''',
            c("Examine the plate with her wing.", "vault_history")),
        page("vault_history", "Commander", '''The back of the Tower plate carries dimensions copied from an older sketch of Devarra's lair.
Small oval marks sit beneath the outline of a larger body.
They are measurements, not an account of where any egg was taken.
There is no new history here that can replace the one she remembers.

Devarra sees the marks as you turn the plate.
Her foreclaw closes on the edge before you can put it down.''',
            c("Let her decide what remains of the sketch of her surviving brood.", "vault_saved", requires=(SAVED, SAVED_CUE)),
            c("Wait while she looks at the marks for her lost clutch.", "vault_lost", requires=(LOST, LOST_CUE))),
        page("vault_saved", "Devarra", '''"They measured the nest."

She turns the plate toward the furnace glow.
The little ovals have no names beneath them.
"They did not know which egg was which. They did not need to. To men like these, anything small enough to carry is sufficiently alike."

You ask whether she wants the sketch kept.
"No. I know the shape of my own nest. I would prefer that the next buyer did not."

With one careful stroke she scrapes the ovals out of the glass.
She leaves the threshold measurement untouched.
Her brood's survival does not make her patient with the people who imagined a second use for its captivity.

"Now," she says, "tell me how we finish leaving that Tower."''',
            c("Turn to the doorway's active sequence.", "vault_method")),
        page("vault_lost", "Devarra", '''"I remember making room for the last one."

She says it so quietly that you nearly miss it beneath the basin's groan.
Her claw rests beside the smallest oval.

You do not tell her the sketch has preserved anything she lost.
She has spent enough time with people who wanted drawings to count as possessions.

"I thought the ledge was too narrow. I moved the stones myself."

She scratches through each oval, slowly, leaving the larger outline and the threshold intact.
"There. He can no longer sell the shape of it."

For a moment she leans against your shoulder, heavy and hot.
Then she lifts her head.
"We have a machine to break. If you have found an elegant way to do it, this would be an excellent time to become unbearable."''',
            c("Show her the sequence that keeps disputing her departure.", "vault_method")),
        page("vault_method", "Commander", '''The plates all feed one question into the basin: who has left without paying?
The answer returns along the copper bands and refreshes each disputed doorway.
You sketch the return line in your notebook before approaching it. Those few strokes would help identify another such apparatus, but cannot reconstruct its targeting map.
You could destroy the plates and let Devarra vent the basin through the empty tower, ending the call at its source.
That would leave very little to study.

Or you could give the basin its own question back with a different debtor.
Every plate is a doorway through which its copy has already passed.
If the machine accepts itself as the departing customer, it must collect its own entire output before it may send another call.

Devarra studies the plates.
"The wheel again."

"The wheel was a small dishonest shop. This is its bank."

"Then rob it thoroughly."

She points out a difficulty before you reach for the nearest plate.
The reservoir is already hot enough to burst. If you lose control of the return, she must vent it immediately.
The plates will shatter, and every buyer still connected to them will know where the last call began.''',
            c("Use the shard to identify the correct return line.", "vault_shard", requires=(ANCHOR_KEPT,), forbids=(ANCHOR_PAID,)),
            c("Use the cold scar to locate the call before it reaches her.", "vault_scar", requires=(ANCHOR_PAID,), forbids=(ANCHOR_KEPT,)),
            c("[Good] Burn the plates and vent the heat here. The people downstream have waited long enough.", "vault_burn")),
        page("vault_shard", "Devarra", '''The shard shows the Tower plate as an open door.
You tilt it until the copper basin appears on the other side.
For an instant, every hanging plate turns toward its own reflection.

"There," Devarra says. "Keep them looking."

She slides her claw beneath the Tower plate and holds it steady while you draw the return in its dark surface.
The preserved shard has given you a view of the connection.
It cannot hold the weight of the whole basin; that will have to be your part of the work.

"If it starts pulling you through," she says, "I tear this out. I have no intention of arguing with a doorway about which of us gets you back."

You tell her that sounds almost affectionate.
"Then finish before I reconsider the phrasing."''',
            c("[Knowledge: Arcana 35] Make the apparatus recognize itself as the debtor.", flags=(VAULT_TRIED,), forbids=(VAULT_TRIED,), check=dict(Skill="SkillKnowledgeArcana", DC=35, Success="vault_caught", Failure="vault_burst", CommanderOnly=True))),
        page("vault_scar", "Commander", '''You put your palm against the copper rim.
The scar goes cold, then colder, until you cannot feel the tips of your fingers.
The call passes through the reservoir toward the Tower plate.
You follow its course in the deadened skin and mark the return with chalk.

Devarra watches your face.
"How long?"

"Long enough if you keep talking. I will want my hand back to stop you."

"A poor threat. You have failed to stop me with both."

She holds the plate above the line you have marked.
The scar has found the connection, at the price of putting your hand against it again.
It has not given you a second chance if you mistake the direction of the return.
Devarra draws a breath and keeps it ready.''',
            c("[Knowledge: Arcana 35] Send the claim back to the apparatus that issued it.", flags=(VAULT_TRIED,), forbids=(VAULT_TRIED,), check=dict(Skill="SkillKnowledgeArcana", DC=35, Success="vault_caught", Failure="vault_burst", CommanderOnly=True))),
        page("vault_caught", "Narrator", '''{n}The basin demands payment.
Every plate points at the basin.
The copper rises in a bright ring, finds itself owed the same ring, and settles back into the trough.
One hanging doorway after another goes dark.{/n}

Devarra steps away from the Tower plate.
Her shadow stays attached to her feet.

"You have bankrupted a machine."

"It had been extending itself considerable credit."

{n}The discharge pipe cools.
You close its valve and leave the basin turning its demand inward.
The diagrams survive, although their active calls have ceased.
This has ended the collectors' hold on her departure from the Tower.
The other plates fall silent too, leaving their recorded doorways cold and dark.{/n}

"What do you intend to do with the plates?" she asks.
Her gaze rests on the doorways you have not identified.
She has already seen their value.''',
            c("Destroy the targeting lines. Keep only what explains how to stop another device.", "vault_scrub", flags=(VAULT_MAP_BURNED,)),
            c("[Evil] Keep the map. The next person who tries to bind you may find his own doors answering us.", "vault_bargain")),
        page("vault_burn", "Narrator", '''{n}Devarra bites through the nearest iron arm.
Its plate strikes the floor and breaks into black grit.
You pull the other plates from their brackets while she turns toward the stairwell.
The copper basin starts to boil.{/n}

"Behind me."

{n}You take shelter beneath her folded wing.
Her fire runs up the discharge shaft, through the empty tower and out into the sky.
The masonry shakes. The basin's excess heat follows the path she has opened, away from the stream.
When the roar stops, there is no doorway left in any plate.{/n}

"A great deal of valuable work," she says, looking at the ruins.

"That was an objection you could have made earlier."

"I made my choice. I am reserving the right to dislike the cost."

{n}The stream will need to be checked before the settlement uses it again.
The mechanism that was heating it is finished.{/n}''',
            c("Close the discharge valve and warn the settlement about the water.", "vault_exit", flags=(VAULT_MAP_BURNED,))),
        page("vault_burst", "Narrator", '''{n}The return catches the wrong plate.
For an instant the basin calls every marked doorway at once.
Somewhere far beyond this room, something answers with a sound like an enormous bolt being drawn.{/n}

Devarra knocks you beneath the stair and tears the Tower plate loose.
Her next breath opens the discharge shaft through the roof.
The basin vents upward in a pillar of white heat.

{n}When you can see again, the plates lie shattered around their bent arms.
The stream's pipe has gone cold.
You have ended the call, but every connected buyer had one last clear indication of where you were standing.{/n}

"That," Devarra says, "was the expensive answer."

You reach for the broken chalk.
She pins it beneath a talon.
"No. There is nothing here to try again. Take your hands and the rest of yourself upstairs. I would like to count them before anyone follows that noise."''',
            c("Leave the broken apparatus and prepare for whoever heard it.", "vault_exit", flags=(VAULT_MAP_BURNED, VAULT_EXPOSED))),
        page("vault_scrub", "Devarra", '''"You want the defense and none of the advantage."

"I want the advantage of not keeping a list of people someone else can hunt."

She makes an impatient sound, then lifts the first plate into the light.
"These two strokes locate the subject. That one records the movement. Destroy the first two and you may keep the explanation you asked for."

You work through the plates together.
She corrects you when you nearly remove a harmless coordinate and misses no opportunity to mention the value you are scraping away.
When the last targeting line is gone, she examines her own plate once more.

"I could have kept one."

"I know."

"Good. I would dislike having restraint mistaken for a lack of imagination."

She drops the scrapings into the empty discharge channel.''',
            c("Take the defensive notes and leave the targeting map destroyed.", "vault_exit")),
        page("vault_bargain", "Devarra", '''"Answering us," she repeats. "You have reached the division of the spoils without inviting me to it."

"I am inviting you now."

"Then hear my price. My plate is destroyed. No copy of my passage, no harmless little exception for emergencies. I keep the names we decipher. You keep the method that makes the calls turn back. Neither of us uses the other half without the other knowing."

You point out that she would own the only readable list.
She points out that you would own the only working trick.

"An uncomfortable arrangement," you say.

"For someone who hoped to leave with everything."

She places her foreclaw across the Tower plate.
"I will share a weapon. I will not agree to become part of its ammunition. If you dislike the bargain, we can break the plates and leave poorer."

There is no apology in the offer.
She wants the power badly enough to negotiate for it, and remains prepared to destroy it rather than put her own leash in your hand.''',
            c("Accept the divided control. Break her plate and take the remaining map together.", "vault_exit", flags=(VAULT_SHARED_POWER, VAULT_MAP_KEPT)),
            c("The division is too dangerous. Scrape away the targeting lines instead.", "vault_scrub", flags=(VAULT_MAP_BURNED, "devarra.trickster.vault_power_declined")),
            c("Insist that her plate stays intact. You will decide when it is needed.", "vault_breakup")),
        page("vault_breakup", "Devarra", '''She breaks the Tower plate beneath her claw.
Then she breaks the plate beside it.
You have time to step back before she sweeps the rest into the empty basin.

"There. Your emergency is over."

She takes the stairs without waiting for you.
When you follow, she is already beyond the broken door.
"I wanted a dangerous man," she says. "I did not ask for another collector."

The passage out remains clear. She leaves you to use it alone.''',
            c("Leave with the relationship ended.", flags=(VAULT_DONE, VAULT_MAP_BURNED, REFUSED))),
        page("vault_exit", "Narrator", '''{n}Outside, the stream no longer gives off steam.
You send a warning downstream before anyone mistakes cooler water for clean water.
Devarra watches the messenger take the lower road, then turns toward the Tower.
Its broken threshold no longer shows through the edges of her wings.{/n}

"They will invent another device," she says.

"Then we will find another objection to its design."

She lowers her head until you are looking directly into her eyes.
"I would like our next discovery to involve a room we chose to enter."

{n}She starts walking before you can answer.
This time, when you catch up, she makes room beside her.{/n}''',
            c("Return with her, carrying the consequences of the vault.", flags=(VAULT_DONE,))),
    ],
    requires=("trickster", KILN_DONE, "devarra.trickster.lower_vault_location", ROMANCE,
              "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED, VAULT_DONE), delay=24, last=5, optional=True,
)

VAULT_AFTER_SCENE = scene(
    "devarra.trickster.a_room_of_her_choosing", "A room of her choosing",
    "Devarra", 5, "chosen_room",
    [
        page("chosen_room", "Narrator", '''{n}Two days after the vault, Devarra asks you to come to the Tower's roof.
The broken stair opens onto a wide platform where rain has collected in the grooves between the stones.
She has cleared the fallen masonry into an untidy wall along the northern edge.
A brazier burns behind it, sheltered from the wind.{/n}

"A room without a door," she says. "For tonight, I find that appealing."

{n}There are two cups beside the brazier, one of them large enough to serve as a washbasin.
She notices you looking.{/n}

"If you make a joke about the measure, I shall choose your next cup myself."

"I was admiring the invitation."

"A prudent beginning. We shall see whether it lasts."

{n}The diagrams from the vault are nowhere in sight.
Before you can sit, she asks one question about the work you brought back.{/n}''',
            c("Discuss the weapon you agreed to share.", "roof_power", requires=(VAULT_SHARED_POWER, VAULT_MAP_KEPT)),
            c("Discuss destroying the targeting map.", "roof_burned", requires=(VAULT_MAP_BURNED,), forbids=(VAULT_MAP_KEPT,))),
        page("roof_power", "Devarra", '''"I have deciphered the first name."

She does not tell you what it is.
Instead she lays a blank scrap of paper beside your cup.
"A buyer who ordered three doorways and paid for only two. I suspect he will be less pleased to discover that somebody remembers the debt."

You ask what she wants to do with him.
"Find out what he bought. If it was a cage, break it. If he has something I want, persuade him that the price of keeping it has risen."

"And if I object?"

"Then we argue. You have the method; I have the address. The inconvenience was part of the bargain."

She watches you consider it.
The power you kept has already become a disagreement with a particular victim at its far end.
It will not remain an attractive idea merely because you have not used it yet.''',
            c("[Evil] Find out what he fears losing. We can discuss the price before we approach him.", "roof_agenda", flags=("devarra.trickster.map_extortion_intent",)),
            c("No threats until we know what he bought. I will help free captives, not collect tribute.", "roof_agenda", flags=("devarra.trickster.map_investigation_limit",))),
        page("roof_burned", "Devarra", '''"I have remembered part of the first name."

She lets you look at her for a moment before showing you the empty paper.
"The rest is gone. I considered whether that should please me. It does not."

You say you did not expect her to enjoy the loss.
"You sometimes expect an argument to end because you have made a good point. I am warning you that this one may recur."

She pushes the paper into the brazier.
The flame takes it without changing color.
"I will not rebuild a targeting plate from a half-remembered name. If I meet the man, I may ask him an unpleasant question. Those are different ambitions."

The defensive notes remain with your supplies below.
You kept a way to recognize the apparatus; you did not keep a list of strangers to threaten.
Devarra looks at the ashes with regret and leaves them there.''',
            c("I would expect you to ask the question. I will judge the answer when we have one.", "roof_agenda"),
            c("And I will keep arguing when I think you are wrong.", "roof_agenda")),
        page("roof_agenda", "Narrator", '''{n}A bell rings below the roof.
Devarra listens until its last note fades, then looks toward the eastern road.{/n}''',
            c("The vault broadcast our position. Keep a watch on that road.", "roof_exposed", requires=(VAULT_EXPOSED,)),
            c("The vault ended without a final broadcast. Let the watch do its ordinary work.", "roof_unexposed", forbids=(VAULT_EXPOSED,))),
        page("roof_exposed", "Devarra", '''"The keeper found a copper washer on the road this morning. No cart had passed."

She drops it beside your cup.
It is cold, without a mark you recognize.
It might be rubbish. It might be the first little piece of something coming to see who called from the vault.

"I asked him to put another watch at the lower stair. He complained about the hour. I told him I would complain more loudly if he declined."

You stand to inspect the road.
She catches your sleeve with the blunt side of one claw.
"After you finish that cup. I asked for the watch so we could sit here. Do not waste someone else's lost sleep by duplicating it."

You settle back.
The cost of the failed return is still approaching through an uncertain dark.
Tonight she has chosen a guard and an open roof instead of pretending that the danger never followed you home.''',
            c("Finish the cup while the watch holds the stair.", "roof_future")),
        page("roof_unexposed", "Devarra", '''"No new device has tried to climb out of my shadow. I am enjoying the novelty."

She turns one wing toward the brazier.
Its shadow moves with it, solid from shoulder to tip.
You had begun checking without thinking. Now you notice that you have stopped.

"You may ask," she says.

"Whether you are still here?"

"Whether I mean to stay. You have looked at the road three times."

You admit that you wondered where she would go when the investigation no longer supplied an invitation.
She moves your cup closer to the brazier before it cools.
"That is a better question than whether the magic will allow it. Ask it properly."''',
            c("What do you want to build when we are no longer following collectors?", "roof_future")),
        page("roof_future", "Devarra", '''"A place with a high western ledge. Stone that does not crumble when I land. A roof I can leave without asking someone to open a door."

She considers you.
"And room for someone foolish enough to visit when there is no treasure to steal."

You tell her there would be treasure.
"Better. I was concerned you might become sentimental."

The place she describes is not the old nest.
She wants no copy of the ledge she lost, no carefully arranged proof that it can be made the same again.
She names a broad ruin above the western road that she has seen from the Tower.
Its stone would suit her. Its owner, if it has one, has made no effort to keep the roof standing.

"I want to see it before I decide," she says. "I would like you to come."

The invitation has none of the collector's urgency.
She could make the inspection alone.
She is asking whether you want a place in something she intends to choose for herself.''',
            c("[Good] I will come. We find out who owns it before you begin moving the walls.", "roof_disagreement", flags=("devarra.trickster.home_claim_inquiry",)),
            c("[Evil] A ruin above my road would benefit from a dragon. Let us see whose claim is stronger.", "roof_disagreement", flags=("devarra.trickster.home_claim_challenge",)),
            c("I want to visit you. I am not ready to plan a shared home.", "roof_visits", flags=("devarra.trickster.home_visits_only",))),
        page("roof_disagreement", "Devarra", '''"You have mistaken an invitation to inspect a ledge for a request to join your crusade's estates."

"You mentioned a roof. I considered the neighbors."

"I will consider them too. They may provide interesting conversation."

You tell her you intend to be present for the first of those conversations.
She bares a little tooth, then lets the expression become a smile.
"Good. Bring whatever you think entitles you to an opinion. I shall bring myself."

There is an argument waiting on the western road about ownership, neighbors and the use of force.
Affection has not made either of you concede it in advance.
For now, she has accepted your company on the inspection and left the rest unsettled.

"You understand," she adds, "that a place of my own would not be an instruction to follow me there every night?"

"I might occasionally wish to be invited."

"You have become demanding."''',
            c("Only where I have reason to expect you might enjoy it.", "roof_desire", flags=("devarra.trickster.home_inspection_planned",)),
            c("Tonight I would enjoy finishing the wine and returning to my own room.", "roof_goodnight", flags=("devarra.trickster.home_inspection_planned",))),
        page("roof_visits", "Devarra", '''"I invited you to see a ruin. You have already declined to furnish it."

Her amusement is unkind enough to make you laugh.
"You were looking a long way ahead."

"I can look a long way without deciding to fly there."

She nudges your cup with hers.
The smaller vessel rings against the metal rim.
"Visit when you want to. I will tell you when I do not want a visitor. That arrangement has survived more difficult creatures than either of us."

You ask whether you are welcome on the ledge inspection.
"Yes. Provided you do not spend it explaining why you have brought no curtains."

She leaves the future at that, with room for two separate lives to reach the same roof.''',
            c("Then I will come for the view, and for you.", "roof_desire", flags=("devarra.trickster.home_inspection_planned",)),
            c("Agree to the inspection, and keep tonight quiet.", "roof_goodnight", flags=("devarra.trickster.home_inspection_planned",))),
        page("roof_desire", "Devarra", '''"For me," she repeats.

She draws closer, enough that you can feel the heat of her without touching.
The mockery has gone from her voice.
"I have been feared by people who wished to own me and admired by people who imagined they could afford the price. You are beginning to become inconveniently different."

You ask whether that is a complaint.
"Several. I shall explain them when I have decided which one is least flattering to you."

Her gaze falls to your mouth.
The night has grown cold beyond the brazier, and you have no practical reason to remain outside.
She has made no move toward the stairs.

"Stay a little longer," she says.
This time the words carry no investigation, no wounded hand, no question about a door that might take her away.
They carry her impatience to discover what you will do with a plain invitation.''',
            c("Move closer and ask for the kiss you have both been postponing.", "roof_kiss"),
            c("Stay beside the brazier without touching tonight.", "roof_still"),
            c("Say good night. You want to leave now.", "roof_goodnight")),
        page("roof_kiss", "Narrator", '''{n}She meets you before you can make the request sound ceremonious.
You feel her breath warm your cheek, then her mouth beside yours.
When you move a hand toward her neck, she guides it to the place beneath her jaw where the scales are smallest.
The low sound she makes is pleased, impatient, and entirely her own.{/n}

"There," she says. "You can occasionally stop talking without becoming dull."

{n}You answer with another kiss.
She lets the brazier burn down while you stay close beneath her wing.
The ruin on the western road remains a plan, the plates remain dealt with as you chose, and the argument about ownership waits for another day.
For this hour, she has found something she wants to keep near without fastening anything around it.{/n}''',
            c("Stay until the embers fade, then arrange the ledge inspection.", flags=(VAULT_AFTER_DONE, "devarra.trickster.roof_intimacy_chosen"))),
        page("roof_still", "Devarra", '''She settles on her side of the brazier.
"Then tell me something I would not discover by threatening a collector."

You tell her about a place you once wanted to live, before the crusade made every comfortable room feel temporary.
She asks about the view first and the defenses second.
When you describe the people nearby, she interrupts only to ask which one would object most loudly to a dragon on the roof.

The conversation lasts until the brazier is almost out.
She does not reach across it or offer a new bargain for the touch you declined.
At the stair, she reminds you to bring a warm cloak on the western road.
"I have no intention of shortening an inspection because you forgot what wind does."''',
            c("Say good night and keep the inspection date.", flags=(VAULT_AFTER_DONE, "devarra.trickster.roof_quiet_chosen"))),
        page("roof_goodnight", "Narrator", '''{n}You put down the cup and stand.
Devarra shifts her wing away from the stair.
No farewell kiss or last request waits in the opening.{/n}

"The western road," she says. "When we have agreed on the day."

{n}You answer from the top step, then go down alone.
She remains on the roof with the last of the wine and a place she means to inspect.{/n}''',
            c("Return to your own room.", flags=(VAULT_AFTER_DONE, "devarra.trickster.roof_departure_chosen"))),
    ],
    requires=("trickster", VAULT_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"),
    forbids=(REFUSED, VAULT_AFTER_DONE), delay=48, last=5, optional=True,
)

LEDGE_INSPECTED = "devarra.trickster.ledge_inspected"
LEDGE_CLAIM_HEARD = "devarra.trickster.ledge_claim_heard"
LEDGE_STORM_ENDED = "devarra.trickster.ledge_storm_ended"
LEDGE_SETTLED = "devarra.trickster.ledge_settled"
PARTNERSHIP_DONE = "devarra.trickster.partnership_chosen"

WESTERN_LEDGE_SCENE = scene(
    "devarra.trickster.the_house_above_the_road", "The house above the road", "Devarra", 5, "ledge_arrival", [
        page("ledge_arrival", "Narrator", '''{n}The western ruin looks less empty when you reach it.
A woman has hung blankets over its broken parapet. Three goats stand beneath them, eating the corner of a proclamation. Devarra watches their progress with approval.
The woman puts down her washing basket. She looks at you, then at the dragon whose shadow has covered her roof.{/n}
"If you came about the tax, it is eating the third paragraph."
"I came about the ledge," Devarra says.
"Then you are the more expensive problem."
{n}Her name is Mareth. She tends the lower rooms for families who work the road's drainage channels. The house belonged to a minor lord who left when the war reached the district. His agent still sends demands for payment. Nobody has seen a repair paid for with the money.
Devarra walks past her and examines the western face. Her claws find solid stone beneath the fallen tiles. For the first time since the Tower, you see her looking at a place without checking how it might take something from her.
Then Mareth steps between her and the lower door.{/n}
"People sleep beneath that wall. Decide where you put your weight before deciding whose house it is."
{n}Devarra looks down at her. Mareth's basket trembles against her knee, but she does not move it aside.{/n}
"A sensible order," Devarra says. "You should give it to whoever neglected the stone."
"I would, if he ever brought himself instead of a letter."''',
            c("We agreed to investigate the ownership. Ask to see the agent's demand.", "ledge_inquiry", requires=("devarra.trickster.home_claim_inquiry",)),
            c("We agreed to test the claim. Ask who will defend it in person.", "ledge_challenge", requires=("devarra.trickster.home_claim_challenge",)),
            c("You came as her guest, not a prospective householder. Ask what she wants to examine first.", "ledge_guest", requires=("devarra.trickster.home_visits_only",))),
        page("ledge_inquiry", "Commander", '''Mareth brings a folded demand from behind a loose stone. The lord's agent, Talvren, claims rent for the upper rooms as well as the cellar, although the upper rooms have lacked a roof for years.
You ask whether the families agreed to those terms. Mareth says they agreed to mend the road in exchange for lodging. Talvren began calling the lodging a tenancy after the first bridge repair was finished.
"He owns the stone," she says. "Apparently that means he also owns whatever he remembers asking us to do."
Devarra noses the paper toward you.
"You wished to find an owner. Does the discovery improve the place?"
"It tells us which claim must be answered."
"I had already noticed the woman standing in the doorway."
She is not mocking Mareth. The mockery is for a distinction which gives an absent claimant more weight than the person keeping the roof from falling.
You ask for the earlier letter about the road. Mareth says Talvren took it back to correct an error. She has a witness, but no copy.''',
            c("Hear the witness and inspect the work before offering anything.", "ledge_bearing", flags=("devarra.trickster.ledge_tenancy_question",))),
        page("ledge_challenge", "Devarra", '''"Let him come," she says. "I would enjoy hearing why his neglect deserves a better roof than my presence."
Mareth does not look relieved.
"Will we owe you afterward?"
Devarra turns toward her. "That depends upon what you ask of me."
"At present, nothing. I am asking you not to fall through the ceiling."
For a moment you expect the answer to offend her. Instead she looks at the low lintel, then at you.
"A negotiation in which somebody has identified the immediate expense. We should invite her to more of ours."
Mareth asks whether she should send for Talvren. Devarra bares the tips of her teeth and asks whether he usually brings soldiers to inspect his drains.
"We discover whether he considers the house worth repairing or merely worth taking," you answer.
"An excellent distinction. It may become clearer if I remain where he can see me."
Mareth asks that she remain somewhere the foundations can bear her. You begin there.''',
            c("Inspect the western stone before testing the absent owner's courage.", "ledge_bearing", flags=("devarra.trickster.ledge_force_question",))),
        page("ledge_guest", "Devarra", '''"The ledge," she says. "I have already explained why I came."
"And the people beneath it?"
"Have explained why it is not yet mine to land on carelessly."
Mareth listens to the exchange with the concentration of somebody deciding which part of a dangerous visit can become useful. She offers to show you where water enters the lower rooms.
Devarra follows. Her folded wing brushes the washing line, and one blanket slips into the mud. She catches it with a claw before the goats can reach it.
For an instant she looks offended by the ridiculous object hanging from her talon.
"A place of my own," she says. "I had imagined fewer negotiations with laundry."
"You can still leave."
"I can. I would first like to know whether the stone is worth the inconvenience."
She hands the blanket to Mareth without offering to warm it with a breath that would leave nothing to fold. You take the basket because your hands are better suited to carrying it.
Mareth points out the path to the western retaining wall. Devarra asks how much of it has fallen since the last rain.''',
            c("Follow the inspection as her chosen companion.", "ledge_bearing", flags=("devarra.trickster.ledge_guest_present",))),
        page("ledge_bearing", "Narrator", '''{n}The western ledge is sound. The retaining wall below it is not.
A drain has been blocked with dressed stone taken from the upper rooms. Rain collects behind the wall and pushes against the mortar. Mareth has been sending people out with buckets after every storm. Her last request for help returned with a new fee for occupying the cellar.
Devarra puts one forefoot against the ledge and tests it. The stone holds. Below, a little thread of mud slides through a crack.{/n}
"Somebody moved the drain," she says.
{n}A narrow culvert leads toward a mill on Talvren's side of the road. Its stone is newer than the blocked opening. The house has become a reservoir somebody else empties when he wants water.
You do not yet know whether Talvren ordered that work or merely benefits from it. Mareth names the mason who protested. His name is Oren. He lives at the lower bend and will not approach the house while its owner is discussed.
Devarra looks from the culvert to the cellar door.{/n}
"I could break the new wall."
"The water would go somewhere."
"I have observed that habit of water."
"So should the person living where it goes."
{n}She exhales through her nostrils, a warm impatient gust which sends the nearest goat backward. Then she steps away from the cracked stone.{/n}
"Find your mason. I would like to know exactly how much of this inconvenience deserves to be broken."
{n}Before leaving, she asks Mareth which part of the ledge no one uses. Mareth points to the western end. Devarra scratches a single shallow mark there, small beside her claw.{/n}
"A claim?" you ask.
"A place to stand while I decide. If I wanted the first, you would hear it."''',
            c("Arrange to hear Oren and Talvren, with the occupied cellar named plainly.", flags=(LEDGE_INSPECTED,))),
    ], requires=("trickster", VAULT_AFTER_DONE, "devarra.trickster.home_inspection_planned", ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED, LEDGE_INSPECTED), delay=24, last=5, optional=True)

LEDGE_CLAIM_SCENE = scene(
    "devarra.trickster.the_man_who_owned_the_rain", "The man who owned the rain", "Devarra", 5, "rain_hearing", [
        page("rain_hearing", "Narrator", '''{n}Talvren arrives with two guards, a tube of rolled papers and a servant carrying his chair.
Devarra is lying beside the ledge when he sees her. He stops far enough away that the servant must decide whether to put the chair down in the road.
Mareth watches from the lower doorway. Oren has come after all, carrying a mason's hammer whose handle is polished by one thumb.{/n}
"The property is not available for military requisition," Talvren says.
"Then it should stop falling on civilians," you answer.
"An emotional description of ordinary disrepair."
Devarra lifts her head.
"I have been called emotional about broken stone. Usually by people beneath it."
{n}Talvren asks whether she is speaking for the Commander. She says she is speaking for herself. He looks toward you as though the correction has made the meeting less lawful.
His papers describe the redirected water as a mill right inherited with the estate. The house's tenants must maintain the passage beneath its western wall. A second document says they have failed to do so, entitling the estate to seize their tools and winter provisions.
Oren turns his hammer slowly in his hands. The drain was blocked on Talvren's orders. He can show you where the fresh stone joins the old culvert, but he has no authority to decide what the papers mean.{/n}''',
            c("[Knowledge: World 34] Compare the mill right with the tenants' actual maintenance duty.", flags=("devarra.trickster.rain_read_attempted",), forbids=("devarra.trickster.rain_read_attempted",), check=dict(Skill="SkillKnowledgeWorld", DC=34, Success="rain_clause", Failure="rain_uncertain", CommanderOnly=True)),
            c("[Evil] His papers are useful. Keep him here until he offers terms worth leaving with.", "rain_pressure"),
            c("[Trickster] He claims the rain when it is useful. Ask him to receive everything his claim brings.", "rain_bargain", requires=("trickster",))),
        page("rain_clause", "Commander", '''The mill right permits a channel across the estate. It does not permit a reservoir behind an occupied wall. Talvren has joined two different obligations and made the resulting danger look like a debt owed by the people below it.
You lay the pages apart.
"Your channel may cross their work. It may not prevent them from completing it and then charge them for the failure."
Talvren begins explaining that the distinction requires a magistrate. You ask which magistrate authorized the new stone. He changes the subject to the cost of his journey.
Devarra watches him discover that a written threat can become a collection of separate sentences.
"Keep reading," she says. "I had not expected the entertainment to improve."
The papers give Mareth a defense against the demand for her tools. They do not repair the wall. Talvren still owns access to the mill channel, and opening it without preparation could destroy Oren's workshop downstream.
You have won a point which will matter after the water has been given somewhere safe to go.''',
            c("Keep the defense and ask Oren what will actually divert the water.", "rain_work", flags=("devarra.trickster.rain_claim_defeated",))),
        page("rain_uncertain", "Narrator", '''{n}The older document measures the channel from a boundary stone which has been moved. Your confident reading puts the mill on the wrong side of it. Talvren notices before you can complete the accusation.
His pleasure is more irritating than his correction. Devarra lets him finish, then asks whether the stone moved because the water had learned to read.{/n}
"The danger remains," she says. "You have established that the Commander misread a boundary. I suggest you not mistake that for a sound wall."
{n}You withdraw the failed argument. Mareth cannot use it to resist the demand for her tools. You can still protect the occupied house while the claim is examined, but doing so will be an overt exercise of authority rather than a victory extracted from Talvren's papers.
He will tell people about the distinction. He is already rehearsing the story for his guards.{/n}
"Let him tell it," you say. "I will be named in the order. Mareth will not be fined for obeying me."
{n}Devarra moves her tail so that Talvren must take a longer path back to his chair. She does not pretend your mistake has made him correct about everything else.{/n}''',
            c("Take responsibility for protecting the tenants while the claim is unresolved.", "rain_work", flags=("devarra.trickster.rain_claim_contested",))),
        page("rain_pressure", "Devarra", '''"You heard him," she tells Talvren. "I would choose a shorter explanation."
You have not threatened his life. You have placed a dragon between him and the road, and neither of you pretends that the difference makes him comfortable.
Talvren offers to suspend the fee. You ask who will pay the mason. He offers the tenants a future reduction. Devarra asks whether he would like to pay for her next breath in future promises.
He produces a purse.
Mareth does not thank you. She asks whether the purse creates another debt. You tell Talvren to state the answer where his guards can hear it. He says the repair is the estate's expense.
The pressure obtains money quickly. It does not settle the underlying right. Talvren will have a story about coercion, and this time it will contain a truth he did not have to invent.
Devarra seems satisfied by the distinction.
"You wanted him to be afraid," she says to you quietly. "You need not ask me to call it a lesson in generosity."''',
            c("Keep his payment and own the coercion used to obtain it.", "rain_work", flags=("devarra.trickster.rain_payment_forced",))),
        page("rain_bargain", "Commander", '''You ask Talvren to name everything the mill right entitles him to receive. He lists the channel's flow, its seasonal increase and the material carried along it.
"Including the stones which obstruct it?"
"Obstructions must be removed by the tenants."
"Then you accept delivery once they are removed."
He glances at Devarra. She has become very still, which is the wrong reassurance to take from a dragon.
"At the mill," he says.
You mark his receiving yard on Oren's sketch. The obstructing blocks came from this estate, the yard belongs to it, and Talvren has just requested that the obstruction be brought there. A narrow mythic adjustment can make the final distance of that delivery shorter, provided the stones are first loosened and the yard kept empty.
It cannot empty a reservoir into somebody's occupied workshop without harming them. You tell Oren exactly what still needs to be done by hand.
Talvren realizes which part of his answer you kept. He tries to withdraw it. You have not completed the magic, and you could permit that withdrawal.
Instead you offer a choice: open the unused yard and accept the stones, or pay for the work which will place them elsewhere. He chooses the yard.
Devarra waits until his servant begins moving the chair before she laughs.''',
            c("Prepare the named empty yard and the stones; do not attempt an unprepared delivery.", "rain_work", flags=("devarra.trickster.rain_delivery_prepared",))),
        page("rain_work", "Narrator", '''{n}Oren needs the outlet cleared from the far side before the blocked drain is opened. Otherwise the water will hit the workshop's outer wall. He can do the cutting with two helpers, but someone must hold the house's western retaining stones while the pressure changes.
Devarra studies the crack. She could brace it. She could also choose a ledge which did not require serving as part of the foundations.{/n}
"You may still decide this place costs too much," you tell her.
"I am deciding that already. Your permission has arrived late."
"Then why stay?"
{n}She looks up at the ledge. The shallow mark she made is visible against the pale stone.{/n}
"Because I disliked being told where I could stand long before anyone tried to make a romance out of it. Because that woman remained in her doorway. Because I want to discover whether the view is worth hearing you explain how pleased you are with our decisions."
"I could keep the last explanation brief."
"I shall consider it part of your contribution."
{n}Mareth begins moving bedding out of the western cellar. She does not wait for a final argument about who deserves to give the order. Talvren remains while Oren marks the work, then leaves his servant to witness it and takes his guards down the road.
Oren gathers the tools while Mareth calls the last household out of the cellar. Beyond the hill, the weather front has swallowed the highest trees.{/n}''',
            c("Prepare the repair and clear the cellar before testing the wall.", flags=(LEDGE_CLAIM_HEARD,))),
    ], requires=("trickster", LEDGE_INSPECTED, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED, LEDGE_CLAIM_HEARD), delay=12, last=5, optional=True)

LEDGE_STORM_SCENE = scene(
    "devarra.trickster.the_weight_of_the_wall", "The weight of the wall", "Devarra", 5, "storm_work", [
        page("storm_work", "Narrator", '''{n}The rain begins before the last bedding is carried out.
Oren has opened the far outlet. Water already runs through it in a thin brown stream, but the blocked house drain still holds most of the pressure behind the retaining wall.
Devarra stands beneath the ledge with her shoulder against the cracked stone. Rain runs down the ridges of her neck and hisses where her scales are hottest. She looks less like part of the building than an argument the building is losing.{/n}
"You have ten sound courses above me," she says. "I would prefer to finish the evening with the same number."
{n}The cellar is empty. Mareth counts the people gathered beneath the eastern arch and makes them answer by name. Nobody will have to be fetched from bed after the first stone moves.
Oren asks you to help loosen the blocked drain. Talvren's servant, Iven, has stayed to witness the work. He is an adult man with a careful hand and a great dislike of being asked whose side he is on. He has brought a lantern and placed it where Oren can use it.
The first block comes free. Devarra shifts her weight. A crack opens above her shoulder, and for a moment you can see darkness through the wall.{/n}
"Do not stop because you have discovered why we began," she says.
{n}Oren works the next stone. The water behind it is pressing hard enough to make the tool shiver. You must choose how the prepared outlet will receive the obstruction before another block is moved.{/n}''',
            c("Use the prepared delivery to Talvren's empty yard.", "storm_delivery", requires=("devarra.trickster.rain_delivery_prepared",)),
            c("Take the blocks out by hand and keep the water in Oren's channel.", "storm_hands")),
        page("storm_delivery", "Commander", '''You have the receiving yard, the named stones and the owner's answer. You still need to bring the three together without letting the reservoir become part of the delivery.
Oren has marked each block with chalk. You trace the same marks over his sketch of the empty yard, then turn the page until the drawn wall faces the real one. Your power catches at the coincidence.
It would be easy to include the pressure behind the stones. The resulting arrival would demolish the yard and much of the mill. You hold the smaller definition instead: the obstructions, loosened for removal, arriving where their owner agreed to receive them.
Devarra watches the marks from beneath the wall.
"If the clever answer starts taking the house, use your hands. I am already using the rest of me."
You promise to stop before the distinction is lost. She does not praise you for making the promise. She expects you to remember it when the magic becomes interesting.''',
            c("[Knowledge: Arcana 35] Hold the prepared delivery to the marked stones alone.", flags=("devarra.trickster.rain_turn_attempted",), forbids=("devarra.trickster.rain_turn_attempted",), check=dict(Skill="SkillKnowledgeArcana", DC=35, Success="storm_sent", Failure="storm_slip", CommanderOnly=True))),
        page("storm_sent", "Narrator", '''{n}The marked blocks vanish one at a time. Each leaves behind a square of moving water and a brief smell of wet chalk.
Far down the slope, stone strikes stone in Talvren's empty receiving yard. The mill's lamp remains lit. The workshop remains standing. Iven counts each impact while Oren pulls the last loose fragment from the drain.
The water follows the cleared channel, finding the outlet Oren opened before you began.{/n}
"There," Devarra says. "A delivery whose price I enjoyed."
{n}The wall settles against her shoulder as the pressure falls. She keeps holding it while Oren drives the first brace into place. The successful trick has removed the obstruction, not rebuilt the damaged courses above it.
You can already imagine the story Talvren will tell about the stones appearing in his yard. Iven says he heard the permission and will write the same words he heard, even if his employer dislikes the sentence.
Mareth thanks him. He asks her to wait until the ink is dry before deciding how brave he has been.{/n}''',
            c("Brace the drained wall before asking Devarra to move.", "storm_braces", flags=("devarra.trickster.rain_delivery_held",))),
        page("storm_slip", "Narrator", '''{n}The second mark begins to include the water behind it. You feel the definition widen, hungry for the easier answer.
You break the connection before it takes the reservoir.
One block has reached the yard. The rest fall outward into the channel at your feet, burying Oren's tool beneath them. Devarra drives her shoulder harder against the wall. The stone above her cracks with a sound you feel in your teeth.{/n}
"Hands," she says. "Now."
{n}You and Oren drag the fallen blocks aside. Mareth passes down a second tool. Iven leaves his account unfinished and holds the lantern over the water until you can see the channel again.
The abandoned trick costs time and a broken tool. Devarra has to hold the shifting wall while you pay both costs by ordinary work. She does not call that proof you should never have tried it. She does ask you to save the explanation for a moment when it cannot interrupt your lifting.{/n}''',
            c("Clear the channel by hand and finish the braces.", "storm_braces", flags=("devarra.trickster.rain_delivery_failed",))),
        page("storm_hands", "Commander", '''You tie ropes around the loosened blocks and bring them out one at a time. Oren directs the pull from beside the channel. Iven and two road workers take the rope's far end.
The first block turns in the mud, nearly taking your boot with it. Devarra pins it with a foreclaw without shifting her shoulder from the wall.
"You may find the route around that stone more convenient than the route beneath it."
"A discovery I was making."
"You looked excessively committed to the experiment."
The water rises over your ankles, then drops when Oren opens the final channel. It takes the chalk from your trousers and the heat from your hands. You cannot make the work elegant by describing it afterward.
Mareth counts the ropes as they come back. Every worker who went down into the cut comes out of it. You leave the removed blocks beside the empty yard for their owner to discuss when the rain stops.
Devarra remains under the ledge while Oren fits the first brace. She has acquired a view of the underside she did not request.''',
            c("Help secure the wall before she releases it.", "storm_braces", flags=("devarra.trickster.rain_handwork",))),
        page("storm_braces", "Devarra", '''"Is the wood supposed to make that noise?"
Oren listens to the brace, then asks her to ease her shoulder away by the width of his thumb. She tells him to put the thumb somewhere she can see it.
The brace takes the load. A little mortar falls. The wall holds.
Devarra steps away slowly, her wing half-open for balance. There is a pale scrape along the scales of her shoulder where the stone moved against them. She looks at it with irritation, then looks at Oren.
"If it falls after this, I shall regard the house as having lied to me."
"I will repair it before it gets the opportunity."
She considers the answer. "That is the most agreeable thing anybody has said about ownership today."
You ask whether she wants the scrape cleaned. She turns the shoulder toward you, plainly consenting to that small practical care. It is not an invitation to decide what the rest of the night must contain.
You wash the grit from between the scales with clean water Mareth brought from the eastern cistern. Devarra watches the damaged wall rather than your hands.
"You asked before touching," she says.
"You can be difficult about surprises."
"Only the badly chosen ones."
Her humor returns by degrees. Oren marks the courses that need replacing. The house is safe for the night; it is not repaired forever. Mareth will keep the western cellar empty until he has completed the work.
Iven finishes his account with rainwater spreading the last line. He writes it again instead of guessing which words Talvren might prefer.
When you leave, Devarra pauses at the shallow mark she made on the ledge. She enlarges it with a second stroke.
"Still deciding?" you ask.
"I have discovered an expense. I am adjusting the offer."''',
            c("Return when the immediate danger has become a repair someone can finish.", flags=(LEDGE_STORM_ENDED,))),
    ], requires=("trickster", LEDGE_CLAIM_HEARD, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED, LEDGE_STORM_ENDED), delay=0, last=5, optional=True)

LEDGE_SETTLEMENT_SCENE = scene(
    "devarra.trickster.a_roof_is_not_a_rein", "A roof is not a rein", "Devarra", 5, "roof_account", [
        page("roof_account", "Narrator", '''{n}When you return to the ledge, the house smells of wet lime and new-cut wood.
Oren is replacing the damaged courses. Mareth has moved the washing line to the eastern wall. The goats have eaten the rest of the proclamation and begun an argument with its string.
Talvren has sent a new document. This one bears the absent lord's authority to settle the disputed lodging and mill access. Iven brought it and remained to hear the answer.
The offer grants Devarra the western platform and the upper rooms for as long as she protects the road. The lower households keep their lodging at the old terms. Talvren retains the mill, with the drainage outlet restored.
The fine print defines protection to include any campaign the lord may declare necessary beyond the road.{/n}
"He has finally found a roof he hopes I will wear around my neck," Devarra says.
{n}She lays one claw beside the sentence without tearing it. She wants you to read what she objects to before she removes it.
Mareth asks whether refusing the offer will cost the families their cellar. Iven says the two provisions can be separated if the lord's agent agrees. Talvren has not agreed yet.
Devarra looks from the lower doorway to the document. It would be easy to make her desire for the ledge into a duty to accept the rest.
She has noticed that possibility too.{/n}''',
            c("How much authority does he still have to demand terms?", "settlement_strong", requires=("devarra.trickster.rain_claim_defeated",)),
            c("Our failed reading left his claim disputed. Name the cost of resolving it.", "settlement_disputed", requires=("devarra.trickster.rain_claim_contested",)),
            c("He paid because we frightened him. Expect the new terms to be retaliation.", "settlement_coerced", requires=("devarra.trickster.rain_payment_forced",)),
            c("He accepted the prepared delivery. What did its result leave us to argue about?", "settlement_delivery", requires=("devarra.trickster.rain_delivery_prepared",))),
        page("settlement_strong", "Commander", '''Mareth can show that the repair answered a hazard the estate had no right to create. Talvren cannot make his earlier obstruction disappear by offering to forgive the people harmed by it.
Iven has included that conclusion in the copied account. He has not said the Commander now owns the estate. The distinction irritates Devarra less than you expected.
"You obtained a useful answer," she says. "Do not spoil it by pretending it contains every other answer you wanted."
You propose separating the cellar agreement before discussing the platform. Talvren will lose the immediate threat of eviction, but retain the chance to negotiate a dragon's presence above his road. Iven believes that is enough to bring him back to the table.
Mareth asks for her copy before any new discussion begins. She has learned to dislike promises which become available after somebody else finishes a more interesting bargain.''',
            c("Separate the tenants' lodging from the offer made to Devarra.", "settlement_choice")),
        page("settlement_disputed", "Devarra", '''"He can demand a hearing. You can prevent him from evicting them while it is held. Neither fact repairs the first mistake."
Iven has brought a second copy of the older boundary description. The moved stone explains your bad reading. It also shows that the mill right predates Talvren's obstruction. The estate has a legitimate channel to maintain and no legitimate reason to store its water behind sleeping people.
Settling those claims will require an independent survey. You authorize it in your own name, accepting its cost instead of requiring Mareth to pay for the correction. No money changes hands in this conversation; the promised survey remains work to arrange.
Devarra reads the commitment, then pushes it toward Iven.
"There. An error with an owner. I have met many people who become remarkably homeless when that question arises."
Mareth keeps the temporary protection while the survey is pending. Devarra's offer can be considered separately. Talvren will not be allowed to turn her refusal into a punishment for the people in the cellar.''',
            c("Keep the survey obligation and separate her decision from the tenants' safety.", "settlement_choice", flags=("devarra.trickster.survey_owed",))),
        page("settlement_coerced", "Commander", '''Talvren's complaint describes the dragon between him and the road. It omits the occupied cellar and the blocked drain.
You require Iven to keep both facts in the account. The coercion happened. So did the danger used to excuse collecting another fee.
Devarra listens while you dictate the reply. She seems pleased until you say that she will not be sent to intimidate every petitioner whose answer inconveniences you.
"Sent," she repeats.
You correct yourself. "Asked. And occasionally refused."
"More promising."
You will have to answer the complaint through the crusade's ordinary channels. For now the lodging provision is separated, and Talvren's payment remains the repair expense he named before witnesses. Neither you nor Devarra obtains a standing right to seize other estates merely because this threat worked.
She tells you she would still use the threat again. You answer that you would still expect to be named beside it. The disagreement is about its next use, not an attempt to invent a gentler past.''',
            c("Stand by the intervention without treating it as ownership of her future choices.", "settlement_choice", flags=("devarra.trickster.coercion_complaint_open",))),
        page("settlement_delivery", "Narrator", '''{n}Iven records both the named delivery and the work performed by hand. Talvren accepted an empty receiving yard, not a ruined mill. The mill remains standing.
The account gives Oren and the people on the ropes their part in the work. Your proposed shortcut has not become a substitute for describing what actually cleared the channel. Everyone can now argue in a dry room, which does not entitle Talvren to call the repair effortless.
The owner's attempt to turn the repair into a claim on Devarra's service is a new proposal. No earlier permission contains it.{/n}
"He believes I will prefer a roof to another argument," she says.
"Would you?"
"A better roof. A shorter argument. He has supplied neither."
{n}You send back a division of the terms: lodging and drainage settled on their own account, the platform discussed only after the service clause is removed. Iven says Talvren will complain about the lost opportunity.
Devarra replies that he is welcome to include it among the stones he asked to receive.{/n}''',
            c("Treat her presence as a new choice, not the final installment of his bargain.", "settlement_choice")),
        page("settlement_choice", "Devarra", '''"I will defend a place because I choose to keep it. I will not let an absent man's definition of necessity choose my enemies."
She gives you two acceptable answers. The service clause can be removed and the platform bought through a fixed agreement which neither party can enlarge by inventing a new war. Or she can reject the ledge and find somewhere else, leaving the repaired house to its people and the estate to its arguments.
She is also willing to claim the platform by force if you intend to stand beside that decision. It would create an enemy with a recognizable grievance. She does not dismiss that consequence merely because she is large enough to survive his first complaint.
"I have asked what you advise," she says. "I have not asked you to choose which leash I should find most comfortable."
You ask whether the view is worth another enemy.
"Possibly. It is also worth learning what you consider an acceptable way to want something."
Mareth has withdrawn to the eastern yard. The question is finally not being asked over a household whose lodging depends on giving the right romantic answer.''',
            c("Seek the fixed agreement. A chosen home deserves terms you can actually keep.", "settlement_buy", flags=("devarra.trickster.home_fixed_terms",)),
            c("[Evil] Claim it openly. I will stand beside the dispute instead of calling it charity.", "settlement_take", flags=("devarra.trickster.home_taken",)),
            c("Leave it. I want your company more than I want this place to prove something.", "settlement_leave", flags=("devarra.trickster.home_declined",))),
        page("settlement_buy", "Narrator", '''{n}The answer goes back with Iven. When the agreement returns, the service clause has been struck out. The platform has a fixed price and a fixed boundary. Devarra examines both, then demands that access from the air be stated without requiring the use of Talvren's road.
He has found a way to be paid for stone he neglected. She has found a place whose terms no longer require pretending she is somebody's soldier. Neither considers the other grateful enough.
The lower households keep the lodging settlement. Oren asks for three more lengths of timber before he will call the western rooms dry. Devarra adds them beneath the price and makes Iven carry the amended copy back.{/n}
"A purchase," Devarra says. "An expensive way to avoid hearing myself described as a generous invader."
"Was it worth it?"
"Ask after the first sunset. I intend to be difficult until then."''',
            c("Keep the agreement and the ordinary work it leaves to do.", flags=(LEDGE_SETTLED,))),
        page("settlement_take", "Devarra", '''She stands on the platform and burns the service clause from its copy. The rest remains legible in your hand.
"I claim the upper stone. Not the people beneath it. If Talvren wishes to discuss the distinction, he knows where I will be."
You add your own name to the notice. Mareth's lodging remains settled on its separate terms; her household has not become a garrison. Iven takes the notice with an expression which suggests he will describe both signatures accurately.
Devarra watches him go.
"He will bring somebody more important."
"Or somebody less willing to discuss it."
"Then we shall discover which advantage he believed the new person supplied."
She wants the platform and has taken the risk that comes with taking it. Your place beside her is not an excuse for the act and not a guarantee that every future demand will receive the same answer.
The ownership dispute remains live beyond this inspection. You have chosen to inhabit it openly.''',
            c("Stand by the claim without declaring its enemies or consequences finished.", flags=(LEDGE_SETTLED,))),
        page("settlement_leave", "Narrator", '''{n}Devarra looks along the western ledge one last time. Then she scrapes away the shallow mark she made there.
It takes two strokes. She does not hurry the second.{/n}
"I liked the view."
"I know."
"You need not make refusing it sound like a victory. I am allowed to dislike something I have chosen."
{n}The house keeps its repaired drain and the work still being done on its wall. Mareth asks whether Devarra will return. She answers that she may visit, and that a visit is not a claim made quietly.
On the road, she walks more slowly than usual. You match her pace without supplying an improved version of the afternoon.
When she finally speaks, she asks which other hills you know. It is not forgiveness for having an opinion. It is the next question she wishes to share.{/n}''',
            c("Leave the house repaired and the search for a home still open.", flags=(LEDGE_SETTLED,))),
    ], requires=("trickster", LEDGE_STORM_ENDED, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED, LEDGE_SETTLED), delay=24, last=5, optional=True)

PARTNERSHIP_SCENE = scene(
    "devarra.trickster.what_she_comes_back_for", "What she comes back for", "Devarra", 5, "return_choice", [
        page("return_choice", "Narrator", '''{n}Devarra finds you at the Tower's outer stair. She has brought no plate, letter or copied doorway.
There is a strip of pale stone caught between two scales on her shoulder. She has failed to remove it because she cannot quite reach the place without scraping herself against the wall. When you notice, she turns that shoulder toward you with an expression which discourages comment.
You work the fragment loose. It falls into your palm, an unimpressive remnant of the house which caused so much discussion.{/n}
"Keep it if you require a trophy," she says.
"I was considering throwing it away."
"An encouraging instinct."
{n}You drop it beside the stair. She watches until your hand is empty.
The western decisions have left practical work behind them. Some of it belongs to Oren and Mareth. Some belongs to Talvren. She has come to ask which part of the future belongs to the two of you by choice, when nobody is using a locked door or a failing wall to arrange the meeting.{/n}
"I will not be another appointment you make because you dislike disappointing people," she says. "I would prefer an occasional refusal to a lifetime of being treated as a duty you perform handsomely."
"You have seen me perform duties less handsomely."
"Yes. It has made this question more interesting."''',
            c("You kept the platform under fixed terms. What do you want it to contain?", "return_owned", requires=("devarra.trickster.home_fixed_terms",)),
            c("You took the platform with a live dispute attached. What do you expect from me?", "return_claimed", requires=("devarra.trickster.home_taken",)),
            c("You left the platform. What are you still looking for?", "return_roaming", requires=("devarra.trickster.home_declined",))),
        page("return_owned", "Devarra", '''"A dry place to land. Enough empty stone that no one asks me to fold a wing for the comfort of a chair. A place for books which are not evidence."
"You intend to read them?"
"I intend to choose whether I do. You have a remarkably narrow understanding of possession."
She asks whether you would keep something there. Not a seal of authority, not an order giving guards access, and not a gift whose price would make refusing it into another negotiation. An object which could be left because you expected to return.
You say that you would, if she wanted it.
"I have just asked. Do not make me perform the invitation twice because the first was insufficiently flattering."
You choose a plain cup, small enough that it will be recognizably yours among the things she can lift without care. She promises neither that it will always be waiting nor that every visit will find her there. It is a place for an ordinary expectation, with room left for either of you to have a life beyond the ledge.''',
            c("Leave room for a return without turning it into a requirement.", "return_power")),
        page("return_claimed", "Devarra", '''"Honesty about the next messenger. You need not agree that I should burn his papers merely because you signed the first notice."
"You need not agree that I should answer him alone."
"I had no intention of agreeing to that."
She is pleased by the argument before it has acquired an adversary. Then she becomes more serious.
"Do not use the people beneath the ledge to win it. They have had enough owners discovering how useful their fear can be. If we defend a claim we made by force, we defend our own act."
You ask whether that is restraint or pride.
"You may enjoy both without making them the same thing."
The ownership dispute has not disappeared. She expects you to stand beside the act you supported, answer the claims it creates and still refuse a later cruelty if it goes beyond what you will choose. She will argue with that refusal. She would be disappointed if you needed her permission to make it.
You tell her that the arrangement sounds exhausting.
"Then consider how much duller your excuses would become with someone easily impressed."''',
            c("Stand beside the choice without surrendering the right to oppose another one.", "return_power")),
        page("return_roaming", "Devarra", '''"A place I can want without being told what wanting it obliges me to become."
"That may exclude more houses than their owners expect."
"They will survive the disappointment."
She has begun looking north of the western road. There are higher ridges, less useful to a mill and harder for a tax collector to reach with a chair. She has not chosen one. She would like you to accompany her on some of the inspections, and to admit when you would rather remain somewhere warm.
You ask whether she wants a household with you or a visitor she enjoys.
"I want you to stop presenting the second as though it were a smaller answer. I have had plenty of people who wanted to remain wherever my treasure happened to be. I have become selective about the people I invite to arrive."
You let that distinction settle. Her wandering is not a failure to choose you, and your duties do not become a failure to follow her unless either of you decides to use them as an excuse for saying something else.
She suggests that the next journey contain no property dispute. You both recognize the optimism in the proposal.''',
            c("Keep the possibility of separate roads meeting by choice.", "return_power")),
        page("return_power", "Narrator", '''{n}Before she asks for your answer, Devarra returns to the dangerous thing you brought out of the vault.{/n}''',
            c("You kept divided control of the map. State what has and has not been agreed about using it.", "return_weapon", requires=(VAULT_SHARED_POWER, VAULT_MAP_KEPT)),
            c("The targeting map is gone. Do not make a substitute for it out of the relationship.", "return_unarmed", requires=(VAULT_MAP_BURNED,), forbids=(VAULT_MAP_KEPT,))),
        page("return_weapon", "Devarra", '''"The names remain with me. The method remains with you. I have not made a call behind your back. I could not make the agreed one without asking."
She has deciphered another purchase: a buyer who commissioned a doorway to a room whose owner had never agreed to sell it. The record does not establish whether the device was delivered. It is a reason to investigate, not proof that you have found another captive.
"And if he has something you want?" you ask.
"Then I may still want it. We have not solved my appetite by dividing a weapon."
You tell her the point of the division was to require another conversation before either of you turned desire into a threat. She agrees with the purpose and plainly dislikes how often it may inconvenience her.
The buyer's name is a beginning. His latest purchase is still somewhere east of the river, and the account gives no address.
She puts the unread names away. Tonight's answer will not be purchased with one of them.''',
            c("Keep the divided power and the need to decide its next use together.", "return_answer")),
        page("return_unarmed", "Devarra", '''"I could ask you to remember which names you saw."
"You could."
"You would become very solemn, and I would have to listen to the argument again. I am deciding to spare myself."
She has kept the defensive explanation. If another device begins tugging at her shadow, it may help you recognize the mechanism before a collector has arranged a demonstration. It cannot let either of you summon the strangers whose targeting lines were destroyed.
The loss remains real. So does her capacity to seek power somewhere else.
"Do not congratulate yourself too extravagantly," she says. "I have not promised to become uninterested in the advantage. I agreed to destroy this one."
You answer that you would distrust a sudden lack of interest more than another argument.
She seems pleased by the answer, then irritated that she is pleased. The expression makes you want to kiss her. You keep listening instead, because wanting the next moment does not require taking this one from her.''',
            c("Remember the actual restraint she chose, without inventing a different woman.", "return_answer")),
        page("return_answer", "Devarra", '''"I want a lover who can leave my room and still come back with an answer I dislike. I want company which is not frightened into remaining and not grateful enough to mistake me for a reward."
Her gaze does not leave yours.
"I am not asking you to empty your life of other people. If another lover needs your time, say that. If two promises conflict, tell me before deciding that the dragon will endure the insult more conveniently. I will give you the same answer about my absences."
"You expect arguments."
"I have been paying attention."
She watches a pair of crows quarrel over the stair. One retreats to the roof, carrying what the other wanted. Devarra waits until it has landed before looking back at you.
The question is whether you want to share decisions which are larger than the next investigation.
She waits without approaching. If you refuse, she will retain the knowledge and possessions that were actually hers. She will not reopen the collectors' apparatus to teach you what you have lost.''',
            c("I want to build a partnership with you, and keep choosing how we share it.", "return_partners", flags=("devarra.trickster.chosen_partnership",)),
            c("I want you in my life without a shared household. Let us keep choosing the visits.", "return_visitors", flags=("devarra.trickster.chosen_separate_lives",)),
            c("I cannot offer that future. End the courtship here without undoing what we did.", "return_end")),
        page("return_partners", "Narrator", '''{n}Devarra takes a step toward you, then stops close enough that you feel the warmth rising from her scales.
She has heard the answer. She has not decided that hearing it makes every other question unnecessary.{/n}
"Then begin with something small," she says. "Tell me when you next want to see me without waiting for a crisis to make the invitation respectable."
{n}You name an evening you can actually keep free. She changes it because she intends to fly west that day. You settle on the following one without making the adjustment into a test of devotion.
There will be larger arguments. Tonight, the first shared plan is an ordinary meeting neither of you had to disguise as work.{/n}''', c("Keep the appointment, then choose how to leave tonight.", "return_farewell", flags=(PARTNERSHIP_DONE,))),
        page("return_visitors", "Devarra", '''"You have made the answer sound less dangerous than it will be. A visitor can still become important enough to be missed."
"I was not offering to be unimportant."
"Good. I should have found that very difficult to believe."
She asks for an invitation when your duties allow one, and the right to decline it without turning each absence into a judgment on the relationship. You ask for the same.
There is no household to establish merely to prove that this answer is serious. There are two people who want to meet again and enough history between them to know that wanting will sometimes be inconvenient.
She names the next evening she expects to be near the Tower. You agree to meet if the campaign permits, and to send a plain answer if it does not.''', c("Keep the separate lives and the deliberate invitations between them.", "return_farewell", flags=(PARTNERSHIP_DONE,))),
        page("return_farewell", "Narrator", '''{n}The outer stair has grown cold. Devarra shifts one wing to shelter you from the wind, leaving the passage open.
She asks whether you intend to remain a little longer. There is no hidden task inside the question.{/n}''',
            c("Ask for a kiss and stay beside her for a while.", "return_close"),
            c("Stay and talk without touching tonight.", "return_quiet"),
            c("Say good night and return to your duties.", "return_depart")),
        page("return_close", "Narrator", '''{n}She bends her head to meet you. Your hand rests beneath her jaw, where she has shown you she likes it, and her breath warms your fingers.
The kiss ends before either of you makes a promise about the length of the night. She stays near. You tell her the first utterly ordinary thing you hope will happen tomorrow, and she improves it with a suggestion sufficiently outrageous to make you laugh.
For a while the Tower is a place where the two of you are standing, rather than the place from which somebody might take her away.{/n}''', c("Leave when you choose, with the next invitation already made.")),
        page("return_quiet", "Devarra", '''She keeps the wing where it is and asks what you thought of the goat eating the proclamation.
You tell her it understood the document better than its author. She suggests that the creature might be profitably employed in the next property dispute.
The conversation moves to the view, then to places neither of you has seen. She does not use the quiet choice as an invitation to ask again for touch.
When you finally leave, she reminds you of the agreed meeting and asks you to bring a story which contains no collectors.''', c("Keep the quiet company and say good night.")),
        page("return_depart", "Narrator", '''{n}She draws the wing aside.
"Then go before you invent a reason to apologize. I asked because I wanted an answer."
You give her the next invitation once more, with its actual limits, and take the stair. She remains long enough that you can turn and see her watching the road beyond you.
Nothing has been withdrawn because you chose to leave tonight.{/n}''', c("Return to your duties.")),
        page("return_end", "Devarra", '''She looks beyond you for a moment, toward the piece of pale stone beside the stair.
"Then that is the answer. I shall dislike it without improving it on your behalf."
The home decision stands. The tenants keep the settlement. The targeting plates remain destroyed or divided as you actually chose; any dangerous shared property will require a separate practical settlement before use, not a romantic claim on your return.
She does not invite a farewell kiss. You do not take one.
"We did useful things," she says. "Do not make them lies because we have reached the end of something else."
She steps away from the stair, leaving it open. You go down alone.''', c("End the courtship without erasing its consequences.", flags=(REFUSED,))),
    ], requires=("trickster", LEDGE_SETTLED, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED, PARTNERSHIP_DONE), delay=24, last=5, optional=True)

APPOINTMENT_DONE = "devarra.trickster.appointment_kept"
EAST_BUYER_HEARD = "devarra.trickster.east_buyer_heard"
EAST_STORE_DONE = "devarra.trickster.east_store_answered"
EAST_ACCOUNT_DONE = "devarra.trickster.east_account_settled"
EAST_CLAIM_PUBLIC = "devarra.trickster.east_claim_public"
EAST_CLAIM_BOUGHT = "devarra.trickster.east_claim_bought"
EAST_DOOR_BROKEN = "devarra.trickster.east_door_broken"
EAST_DOOR_KEPT = "devarra.trickster.east_door_kept"
EAST_CHECK_TRIED = "devarra.trickster.east_boundary_tried"
EAST_CHECK_FAILED = "devarra.trickster.east_boundary_failed"

APPOINTMENT_SCENE = scene(
    "devarra.trickster.an_evening_without_an_alibi", "An evening without an alibi", "Devarra", 5, "appointment", [
        page("appointment", "Narrator", '''{n}Devarra keeps the appointment at a ruined vineyard above the western road. The vines are dead, but the low walls have survived, holding the day's warmth in their stones. Somebody has repaired one length with bricks from a house whose windows were once painted blue.
You arrive carrying supper and a story with no collectors in it. She has brought a length of faded silk large enough to shade a market stall. One end is caught beneath her claw.{/n}
"A tablecloth?" you ask.
"A wager."
{n}She opens the silk across the courtyard. It depicts a coast crowded with little cities. Each city has been embroidered in a different hand. Some have towers finer than needles; others look as though the maker grew bored after completing the harbor.
Devarra has covered the names with flat stones.{/n}
"You claim to have traveled. Tell me which of these places you would enter without an army."
"I did not claim to travel wisely."
"That makes the game more promising."
{n}You put the food on the wall. She moves one stone an inch, concealing more of a coastline. When you notice, she looks pleased rather than ashamed.
There is no messenger waiting at the gate. The nearest sound is a cricket beneath the broken press, repeating itself with the confidence of an orator who cannot be interrupted.{/n}''',
            c("Choose the harbor. A city is easier to understand where it has to unload its lies.", "harbor"),
            c("Choose the hill fortress. Why does it expect trouble from the sea?", "fortress")),
        page("harbor", "Devarra", '''"It expects trouble from the road. The harbor is where it sends the people who notice."
She moves the stone. The embroidered name has been picked out and sewn in again with darker thread. Devarra remembers the city before its ruler changed the name.
"It was already an ugly name. At least the old one had earned it."
"You visited?"
"I was discouraged from landing. I found another place from which to disagree."
She describes slate roofs, an unfinished tower and a yellow ship whose captain tried to conceal it beneath a sail. She remembers a woman ringing a bell with both hands and a watch officer running in the wrong direction.
When you ask what brought her there, she looks down at the silk.
"A man who believed distance made a promise smaller. He discovered that wings are useful for measuring such things."
"Did you collect?"
"Most of it. I have learned to be suspicious of people who consider a tale unfinished until every loss has been repaid."''', c("Ask about the ship she remembered more clearly than the debtor.", "sail")),
        page("fortress", "Devarra", '''"It expects trouble from its own lower town. The gate faces inland so that the garrison can collect its supper without crossing the market."
She moves the stone. The towers on the cloth are larger than the hill beneath them.
"A flattering portrait," you say.
"The mason paid for it. He meant to persuade the ruler to finish the work."
"Did it work?"
"They finished one tower. It fell into the kitchens."
She remembers a yellow ship below the fortress, moored where a siege engineer thought the siege engines could protect it. Her opinion of the engineer is brief and unkind.
You ask whether she always studies a city by deciding how she would attack it.
"Frequently. Do you always enter one by deciding whom you ought to help?"
"Not always."
"Then we both possess interests which might survive an evening's disapproval."
She removes the next stone before you can choose it. The same yellow ship has been sewn into another harbor farther along the coast.''', c("Ask why the ship appears twice.", "sail")),
        page("sail", "Devarra", '''"The woman who made the cloth had a brother aboard. She added him wherever she hoped he would arrive."
"You asked her?"
"I bought it from her. She wished me to understand why the work was inaccurate before I complained."
The ship appears a third time, hidden behind a fold. There is no dragon over any of its harbors. Devarra has kept that omission as carefully as the rest.
"Did he arrive?"
"She had no letter. I have no better ending to offer."
You lean close enough to distinguish two shades of yellow thread. The last ship is less finely stitched than the first. Devarra watches your hand stop short of touching the worn sail.
"You have brought the expression you wear over evidence. I was hoping to defeat it with supper."
"Then uncover the names. I am finished pretending to know the coast."
"You surrender beautifully when there is food involved."
You eat while she tells you which cities she would refuse to visit again. One smells of spoiled fish. Another contains a bell she dislikes. A third disappointed her by rebuilding a particularly handsome roof after she had made her opinion of its owner clear.
You object to that last reason. She asks whether your objection improves the roof.
The cricket stops. You both look toward the press, absurdly attentive to the loss of so small a noise.''',
            c("Tell her the harmless story you brought, including the part in which you looked foolish.", "story"),
            c("Tell her about an ambition you seldom admit because it sounds selfish.", "ambition")),
        page("story", "Narrator", '''{n}You tell her about losing an argument to someone who had misunderstood half of it, then discovering that the other half was sufficient. Devarra interrupts to improve your opponent's insults.
By the end she is laughing, a low sound that makes a loose tile rattle on the press. You ask whether she must shake the building to express amusement.{/n}
"Would you prefer a discreet squeak?"
"I would prefer the roof to survive my finest anecdote."
"Then choose a better roof next time."
{n}She has said next time without disguising it. You let her finish laughing before pointing that out. Her gaze sharpens; then she nudges one of the stones against your hand.{/n}
"Keep that until you can identify one city without asking me for its history. I shall expect evidence of study."
{n}It is a flat piece of blue-painted brick. You put it beside your plate. The wager has acquired a future without either of you promising to travel its whole coast.{/n}''', c("Keep the brick and the invitation to another contest.", "evening_end")),
        page("ambition", "Commander", '''"I would like to walk into a room and want something before deciding what wanting it will make people ask of me."
Devarra studies you across the cloth.
"You would find that freedom less innocent than you imagine."
"I did not say I wanted to be innocent."
"No. You did not."
She pushes a piece of blue-painted brick toward you, worn smooth on the back.
"Choose a city you want to see. Then learn enough to dislike part of it. You may still want to go. That is when the preference becomes worth hearing."
"Is this how you choose company?"
"Among other tests. You have survived several without noticing."
You tell her this is an intolerable confession to make over somebody else's supper. She asks whether you intended to eat all of it, and takes the answer before you have finished laughing.
The brick remains beside your plate. You decide not to ask whether it was taken from one of the cities she disliked.''', c("Keep the brick and choose a city to learn about.", "evening_end")),
        page("evening_end", "Narrator", '''{n}When the light has gone, Devarra folds the coast with surprising care. She leaves the last yellow ship outside the first fold, then covers it with the next.
You gather the plates. The last hour has passed without either of you asking for a report. You almost spoil it by mentioning that.
Instead you ask when she wants the cloth brought out again.{/n}
"When you have learned the names. Or when you have become impatient enough to invent convincing ones."
"You would know."
"That is the part I expect to enjoy."
{n}She carries the folded silk while you take the basket. At the gate she waits for you to find the road in the dark. Her wing blocks the wind until you have done so.
The blue brick knocks against a plate with each step. You move it into your pocket, where it stays warm a little longer.{/n}''', c("Return from the evening with the next wager still open.", flags=(APPOINTMENT_DONE,))),
    ], requires=("trickster", PARTNERSHIP_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED,), delay=24, last=5, optional=True)

EAST_BUYER_SCENE = scene(
    "devarra.trickster.the_buyer_at_the_western_gate", "The buyer at the western gate", "Devarra", 5, "buyer_arrival", [
        page("buyer_arrival", "Narrator", '''{n}Iven waits outside the Tower with a man whose cloak is too fine for the road and too wet to conceal that fact. The stranger has refused a seat. He keeps looking at the upper landing as though Devarra might come through the door in a form better suited to his expectations.
She does not oblige him.{/n}
"Adrast," he says, before anyone asks. "I hold a store on the eastern river. Your recent interference has made it difficult to insure."
"I have interfered with several things recently," Devarra answers. "Tell me which one has become less profitable."
{n}He places a lead token on the stair. Its face bears the impressed shape of a scale. The pattern is close enough to Devarra's that you look at her before touching it.
She lowers her head. A thin curl of smoke passes over the lead without melting it.{/n}
"Not mine."
"It was supplied as proof of protection," Adrast says.
"Then somebody sold you a very small dragon."
{n}Iven explains why he brought the man here. Talvren's mill has received a demand for payment to keep its eastern deliveries untouched. The seal matches Adrast's token. Both documents claim that the western ledge is the seat from which the protection is granted.
Devarra looks at you. Her interest has become unpleasantly precise.{/n}''',
            c("The fixed purchase gave no one a right to sell protection in her name.", "buyer_owned", requires=("devarra.trickster.home_fixed_terms",)),
            c("We claimed the platform. We did not authorize someone else to collect from it.", "buyer_taken", requires=("devarra.trickster.home_taken",)),
            c("She left the platform. Someone is trading on a claim she refused.", "buyer_left", requires=("devarra.trickster.home_declined",))),
        page("buyer_owned", "Devarra", '''"I paid for a place to land. It appears somebody has sold the shadow I would cast over it."
Adrast produces a copy of the agreement. It contains the boundary and price, but not the struck-out service clause. Somebody has copied the rejected version as a promise to protect the entire road.
Iven recognizes Talvren's clerk's habit of copying the seal before the final signature arrives.
"That clerk will tell us who requested it," you say.
"Eventually," Devarra answers. "First this man will tell us why he brought a false scale to a dragon."''', c("Ask Adrast what he actually bought.", "buyer_history")),
        page("buyer_taken", "Devarra", '''"I claimed stone. I did not invite every thief within walking distance to call himself my steward."
Adrast has a copy of the notice you allowed to stand. Beside it is another hand's addition, offering protection for eastern stores that pay a quarterly tribute. The addition borrows your threat without your signature.
Iven looks at you rather than at her.
"People heard that force settled the platform. They will believe force is collecting the next payment."
"Then we will have to be particular about whose force it is," Devarra says.
She does not ask him to withdraw the uncomfortable observation.''', c("Ask Adrast what he actually bought.", "buyer_history")),
        page("buyer_left", "Devarra", '''"I refused the platform. I should have charged for the disappointment. It appears to be the only part of the visit nobody has found a way to sell."
Adrast has a copy of the old service offer, made before her refusal. Somebody has copied its heading and omitted the reply. The lower households are named as beneficiaries of protection they never requested.
Mareth has denied the claim to two carters. Neither believed a woman at a washing line could contradict a dragon's arrangements.
"They may find me easier to hear," Devarra says.
"That will not make Mareth wrong."
"No. It will make the next carter more attentive."''', c("Ask Adrast what he actually bought.", "buyer_history")),
        page("buyer_history", "Adrast", '''"Access. A door through which I could bring goods without paying the bridge toll. The protection was added when I asked what would happen if the owner on the other side complained."
Devarra glances at you. The word door has acquired an unwelcome familiarity.
Adrast says the mechanism arrived before the trouble at the kilns. It stands in his riverside store, facing a wall. He has used it twice. Both times, he entered a room already holding goods he expected to receive.
He did not ask who else used that room. He paid the seller to make that question unnecessary.
"And now?" you ask.
"Now the other owner has found a way to close it. My paid freight is behind it."
"Your freight," Devarra repeats.
"Purchased freight."
"Then your receipts will be fascinating."
Adrast asks whether she intends to seize the store. She looks at his cloak, then at the lead scale.
"I have not yet decided whether it contains anything I want. You may find that uncertainty more uncomfortable than an answer."
He gives you the address. He wants his goods and believes your interest in the false protection will help him get them.''',
            c("Compare his supplier's mark with the kept targeting account.", "buyer_map", requires=(VAULT_MAP_KEPT, VAULT_SHARED_POWER)),
            c("The targeting account is gone. Ask for the delivery docket and the carter.", "buyer_docket", requires=(VAULT_MAP_BURNED,), forbids=(VAULT_MAP_KEPT,))),
        page("buyer_map", "Narrator", '''{n}Devarra brings the names; you bring the part explaining how the marks were assigned. Neither part opens a passage on its own. Together they identify the supplier's mark beside Adrast's purchase.
The entry describes a fixed receiving room. Its owner is named Lethra, with an address at an old bridge house farther downriver. Adrast's payment buys a route into her store. There is no witness to her acceptance beneath it.
Devarra reads the absence twice.{/n}
"You wanted somebody else's room. You have been remarkably careless about whose name could make it yours."
{n}Adrast begins to explain the convenience of the arrangement. She stops him by moving the token closer to his hand.{/n}
"Begin with what you told the woman who owned the wall."''', c("Make him bring the original purchase and identify the receiving room.", "buyer_decision")),
        page("buyer_docket", "Narrator", '''{n}The targeting names cannot answer you. Adrast sends for his docket, and Iven brings the carter who delivered the mechanism.
The carter remembers a bridge house because its owner made him unload outside. Her name is Lethra. She allowed the seller to measure a damaged wall, then refused installation when he asked for the key to her inner room.
Adrast says that disagreement was never mentioned to him.{/n}
"You paid to stop asking," you tell him.
"I paid to avoid a toll."
"A more flattering sentence. Keep the docket beside it."
{n}Finding the address has cost an extra journey and given Adrast time to send a message ahead of you. Iven saw his clerk take the eastern road. The store will know you are coming.{/n}''', c("Keep the warning in mind and make him bring the original purchase.", "buyer_decision")),
        page("buyer_decision", "Devarra", '''"We can take the false protection apart in public. Make him name the seller and post the denial where he has been selling its advantage."
"His creditors will withdraw," Iven says.
"Some of them. The intelligent ones will ask what he still owns."
Adrast's mouth tightens. A public dispute could cost him the goods waiting on the river, even if he persuades someone to reopen the passage.
Devarra has another proposal. Buy the claim against the seller at the price of its doubtful recovery, obtain the papers, and make Adrast pay for witnessed restitution before anyone helps move his legitimate freight. She would gain a debt and a reason to question its author.
"And Lethra?" you ask.
"Gets to tell us what entered her house before we decide how much he has left to sell. I have begun to dislike the frequency with which people describe a room without mentioning its occupant."
She waits. Adrast watches you with the dislike of a man discovering that his useful rescuers may have their own appetite.''',
            c("[Good] Publish the denial. Let everyone he charged know what he was selling.", "buyer_end", flags=(EAST_CLAIM_PUBLIC,)),
            c("[Evil] Buy the evidence cheaply. Make his legitimate freight answer for the loss, and keep the debt that survives examination.", "buyer_end", flags=(EAST_CLAIM_BOUGHT,))),
        page("buyer_end", "Narrator", '''{n}Adrast agrees to bring his keys. He objects to Iven bringing a second witness, then withdraws the objection when Devarra asks which inventory he expects to improve in private.
You leave the lead token on the stair until he turns to go. Devarra stops him with one claw resting beside it.{/n}
"Take your dragon. I have no use for one that fits in your pocket."
{n}He picks it up by the edge. When he has gone, she asks whether you think Talvren arranged the claim.
You answer that he may merely have supplied a paper somebody wanted.{/n}
"You have become irritatingly patient with people who annoy me."
"You have supplied a crowded field for practice."
{n}She smiles without softening the question. You promise to ask it at the eastern store, where an answer might be worth more than the pleasure of guessing.{/n}''', c("Visit the eastern store with the keys, papers and a second witness.", flags=(EAST_BUYER_HEARD,))),
    ], requires=("trickster", APPOINTMENT_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED,), delay=24, last=5, optional=True)

EAST_STORE_SCENE = scene(
    "devarra.trickster.a_door_without_permission", "A door without permission", "Devarra", 5, "store", [
        page("store", "Narrator", '''{n}Lethra reaches the warehouse before Adrast. She has brought a broken length of doorpost, tied behind a handcart. The grooves cut across it mark the heights of children who have since grown tall enough to help her drag it here.
Adrast complains that she should have waited for his mason. She lays the wood across his doorstep.
Devarra cannot enter the loading room without taking its lintel with her. She remains outside, looking through the broad opening while Iven checks the keys against the inventory. Haren, the porter, lights three lamps. He will not approach the frame until Lethra does.
The apparatus occupies the room's far wall. Its brass teeth are smaller than the vault's, but the returning catch is unmistakable. Somebody has built a cheap copy and dispensed with the counterweight. Beyond its upright stones you can see a narrow passage, an overturned stool and the corner of a kitchen hearth.{/n}
"My hearth," Lethra says. "He knocked once. I refused him. The next morning his flour came through my wall."
{n}Adrast says he paid for a doorway. Devarra's eye narrows.{/n}
"You appear to have purchased a woman's kitchen. Did you expect the rest of her house to arrive by installments?"
"The seller said the receiving site was vacant."
"You heard her refuse."
{n}His answer is lost beneath the frame's creak. Lethra has barred her passage with an oak beam. The apparatus keeps drawing it toward the warehouse. The doorpost broke first; the lintel will follow.{/n}''', c("Clear the loading room and inspect the return catch.", "store_catch")),
        page("store_catch", "Commander", '''The frame borrows the distance between two fixed walls. It cannot choose a new destination while its return catch is engaged. Breaking the catch under strain would release that distance through Lethra's kitchen.
Haren produces the seller's instructions. They advise the owner to keep the receiving doorway clear. Nothing describes what to do when the receiving doorway belongs to someone else.
"An omission with a fine commercial future," Devarra says.
You ask Haren how often he used it. Twice, he says. The second load came back wet because Lethra poured washwater over the sacks. Adrast had called it damage to goods in transit.
"And the linen?" Lethra asks.
Haren looks toward a stack behind the lamps. Adrast says that was held against the ruined flour. Lethra had paid for it before the doorway arrived.
Devarra could reach the stack with one claw. She does not. She asks you whether a merchant's power to invent debts is a custom you intend to defend.
"I intend to distinguish his theft from the goods we still need to move out of danger."
"A distinction he has found profitable. Do hurry."
You have Haren mark the sacks he actually carried. Iven records his answer in front of Adrast. Lethra's linen goes onto her cart, and the flour remains in the yard until its condition can be examined. The room empties. There is finally space to see the stone sockets beneath the frame.''', c("Prepare a safe receiving space for the released distance.", "store_plan")),
        page("store_plan", "Devarra", '''"The loading arch is the same width."
{n}She has measured it with her foreclaw while you worked. The space beyond is open ground. You mark the arch with chalk, then compare the catch's stroke against the marks in the seller's instructions. The prepared arch could take the final release if you persuade the apparatus that its journey ended before it began.
It would be a small lie told at the right joint. It would also be a dangerous one if the catch moved before the mark held.
The other method is slower: brace both walls, unwind the axle a fraction at a time and remove the teeth under load. Haren knows where the lifting timbers are kept. Lethra's sons can carry them home while you work from this side.
Devarra rests her claw against the axle's housing.{/n}
"I can hold that. I cannot hold your chalk if you make it promise something foolish."
"A distinction my officers seldom appreciate."
"They are small. Perhaps your foolishness obscures the view."
{n}She waits until everyone has left the receiving passage. Lethra calls through the frame to confirm it. Only then does Devarra put her weight against the iron.{/n}''',
            c("[Trickster, Knowledge: Arcana 35] Make the final delivery arrive at the prepared loading arch.", flags=(EAST_CHECK_TRIED,), forbids=(EAST_CHECK_TRIED,), check=dict(Skill="SkillKnowledgeArcana", DC=35, Success="store_turned", Failure="store_failed", CommanderOnly=True)),
            c("Brace both walls and dismantle the loaded axle by hand.", "store_manual")),
        page("store_turned", "Narrator", '''{n}The chalk line brightens. For a moment the loading arch stands inside the distant kitchen, its empty yard visible where the hearth should be. Then the apparatus completes a journey of no distance at all.
The oak beam drops on Lethra's side. Dust falls around it. Her sons wait until she has inspected the lintel before they move it; neither trusts the sudden silence.
Devarra lifts her claw. The axle turns freely once, then stops.{/n}
"You persuaded a door it had already gone through itself."
"It had very little experience of doors."
"I shall remember that defense when you try it on me."
{n}Lethra calls through the fading opening that she wants the brass strip bearing her address. You remove it before the frame closes. Its scratches are shallow enough to have been made in an afternoon. Repairing the damage to her home will take longer.{/n}''', c("Decide what survives of the apparatus.", "store_parts")),
        page("store_failed", "Narrator", '''{n}The chalk darkens before the catch finishes its stroke. One of the cheap brass teeth snaps. Devarra forces the axle against its housing while you pull your hand clear.
A stone falls from the far lintel into the empty passage. Lethra curses, then calls the names of both her sons. Both answer from outside.
The catch cannot be turned again. You scrape away the false mark and send Haren for the timbers. Devarra has stopped smiling.{/n}
"Your door believed you for half a sentence. I suggest you spend the rest lifting."
{n}You spend the afternoon fitting braces under Lethra's lintel before the axle can be unwound. Iven adds the fallen stone to the repair account. Adrast protests that the stone fell after you arrived; Lethra asks which part of her house he would have preferred to lose before then.
With the weight supported, Haren removes the teeth one by one. The opening shrinks until you can no longer see the hearth. Devarra keeps her claw on the housing until the last tooth lies on the floor.{/n}''', c("Record the extra damage and examine the dismantled parts.", "store_parts", flags=(EAST_CHECK_FAILED,))),
        page("store_manual", "Narrator", '''{n}The work takes the afternoon. Haren brings lifting timbers; Lethra directs her sons from the far side. Every quarter turn of the axle is answered by a shout from her passage. You stop whenever the sound changes.
Devarra holds the housing still. After the first hour she asks whether all your domestic visits involve supporting buildings. You tell her she chose a city with old stonework.
"I chose interesting company. The masonry was concealed from me."
Adrast attempts to leave for a meal. She moves her tail across the gate and asks him to bring one for everybody.
When he returns, Haren eats beside the dismantled teeth. Lethra accepts bread through the narrowing opening without thanking its owner. The final tooth comes free just before dusk. Her kitchen disappears; a plain stone wall stands where the hearth had been.
Devarra withdraws her claw slowly. The housing stays still. She stretches each joint, watching you count the people who entered the room against those now standing outside.{/n}''', c("Examine the dismantled parts.", "store_parts")),
        page("store_parts", "Devarra", '''"I want the frame."
{n}Lethra holds out her hand for the address strip. You give it to her. She asks Devarra what she means to do with a machine built to enter an unwilling person's house.{/n}
"Discover how it was made. Then decide."
"That is what he said."
{n}She points at Adrast. Devarra lowers her head until the merchant steps back.{/n}
"He wanted to avoid a toll. Do not confuse the size of his ambition with mine."
"The hole in my wall was large enough."
{n}For a moment nobody moves. Devarra's anger shows in the slow spreading of her claws. Lethra does not withdraw her hand.
You take the strip with her permission and lay it on the hearth shovel. Devarra melts it with a narrow breath. When the brass cools there is no address left to read.
The frame can be broken, or divided so neither of you possesses a working apparatus. Its joints would still teach you something. Devarra plainly prefers that. She also knows you have already seen what the complete device was used to do.{/n}''',
            c("[Good] Break the frame. We have learned enough from the house it damaged.", "store_destroy"),
            c("Keep the outer sections. I keep the axle and catch. We examine them together before either attempts to rebuild it.", "store_keep")),
        page("store_destroy", "Narrator", '''{n}Devarra snaps the first upright with enough force to split the paving beneath it. She leaves the second for you and the porter's hammer.
When the pieces are too small to carry a joined inscription, she picks up the ordinary iron chain which secured the housing to its stone socket.{/n}
"You have an expensive taste in lessons."
"You may charge Adrast for the paving."
"I was speaking of what we could have learned. Do not spend a joke pretending you failed to hear me."
{n}You meet her gaze. She coils the chain around one claw and turns toward the gate. Lethra follows with her cart. The warehouse wall remains stubbornly ordinary behind you.{/n}''', c("Leave the destroyed apparatus and return with the repair account.", flags=(EAST_STORE_DONE, EAST_DOOR_BROKEN,))),
        page("store_keep", "Narrator", '''{n}Devarra carries the two outer sections into the yard. You wrap the axle and catch separately. Lethra inspects the empty sockets, then asks Haren to witness that nothing remains joined.
"If that thing comes through my wall again, I will not ask which of you owns the missing piece."
"Sensible," Devarra says. "You should also move the hearth away from that lintel until the mason finishes."
Lethra accepts the second remark without forgiving the first.
Outside, Devarra waits while you secure the axle. She would like it in her possession; she makes no effort to hide that. She asks whether you intend to keep it in a bedroom.
"Would that improve your interest in visiting?"
"It would complicate the evening."
She lifts the sections without joining them. You follow her through the gate with the only catch that fits their teeth.{/n}''', c("Keep the apparatus divided and settle the damage it caused.", flags=(EAST_STORE_DONE, EAST_DOOR_KEPT,))),
    ], requires=("trickster", EAST_BUYER_HEARD, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED,), delay=24, last=5, optional=True)

EAST_ACCOUNT_SCENE = scene(
    "devarra.trickster.the_price_of_an_address", "The price of an address", "Devarra", 5, "account", [
        page("account", "Narrator", '''{n}Iven brings the account to the vineyard. Adrast has returned the linen and paid for lamp oil wasted during the dismantling. He has also offered three sacks of flour toward the repairs. The baker who examined them found damp meal at the bottom of each.
Lethra refused the sacks. Iven sold Adrast's spare wagon instead, with his signature beneath the sale. The proceeds will pay the mason; the merchant must now hire his own cartage.
Devarra listens from the broken terrace. She has stretched the embroidered cloth over a dry patch of stone. It leaves room for your papers without placing them on the little yellow ship.{/n}
"A man who sold distance has become short of wheels. I approve of the account so far."
{n}Iven sets down a second paper. Talvren's clerk admits sending the unsigned western offer to Adrast. He wanted the merchant to believe the mill enjoyed a dragon's favor and would remain a safe customer. He denies inventing the payment demand. The added hand does not match his.
Talvren has dismissed him. That may satisfy the mill owner; it does not prove who wrote the demand. Iven will keep the originals while the witnesses can still recognize them.{/n}''',
            c("Read the published denial and the claims that followed it.", "account_public", requires=(EAST_CLAIM_PUBLIC,)),
            c("Examine the debt purchased from Adrast.", "account_bought", requires=(EAST_CLAIM_BOUGHT,))),
        page("account_public", "Commander", '''The denial reached the bridge before Adrast did. Two shopkeepers have brought tokens like his; one paid, the other refused. Neither can identify the seller beyond a coat and a missing finger.
Publishing the fraud has stopped further payments at those shops. It has also frightened a lender who believed Adrast possessed a legitimate protected road. He wants his loan repaid at once. There will be less money to divide among the people already cheated.
Devarra reads the copied description, then asks why the lender should come before the woman whose wall fell.
"He should not. Iven is keeping the wagon sale separate."
"And when he hires men to seize the rest?"
"Then they will have to explain which debt entitles them to Lethra's repair money. In front of witnesses."
"You propose to bore armed men into retreat."
"I propose to give them a cheaper enemy than me."
She considers that answer with more pleasure than the promise of a hearing. Iven takes the description back to compare it with the bridge toll records. Nobody has yet found the seller, and the unpaid shopkeeper will not recover money merely because his complaint has been heard.''', c("Ask about the cost of dismantling the door.", "account_damage")),
        page("account_bought", "Commander", '''Adrast has signed over his claim against the seller after the repair money was set aside. The paper names a receiving agent beyond the river. It contains no guarantee that the agent has assets worth taking, or that he will admit his master's name.
Devarra studies the address with immediate interest. She proposes arriving before word of the warehouse reaches it.
"You would leave the witnesses here and fly east?"
"Yes. A debtor who has time to pack is generally less interesting."
"And if the agent was cheated too?"
"Then he will be particularly eager to introduce us to the person responsible."
You tell her that the claim purchases a chance to collect, not ownership of everybody who handled the paper. She replies that you have become fond of defining the limits of profitable objects.
"I prefer knowing what I bought before I threaten someone with it."
That makes her laugh. She asks Iven to copy the address, then leaves the original beside your hand. She means to pursue it. You have given her a reason to expect company, and neither of you mistakes that expectation for an innocent excursion.''', c("Ask about the cost of dismantling the door.", "account_damage")),
        page("account_damage", "Narrator", '''{n}Iven turns to the mason's estimate. Devarra watches the changing position of your hand on the table. The afternoon at the warehouse is close enough that both of you remember where it had been when the axle moved.{/n}''',
            c("Include the stone lost when the prepared turn failed.", "account_failed", requires=(EAST_CHECK_FAILED,)),
            c("Confirm that the supported lintel needs repair even though it held during dismantling.", "account_held", forbids=(EAST_CHECK_FAILED,))),
        page("account_failed", "Commander", '''You add your acknowledgment beside the fallen stone. Adrast created the danger, but your failed turn made that part of the damage worse. Iven separates the extra work from the original repair before leaving.
Devarra waits until he is out of earshot.
"You came close to leaving fingers in that catch."
"You held it."
"That is an answer to a different question."
You flex your hand. She follows the motion, then looks away toward the empty loading road. She does not ask you to become careful enough never to attempt anything worth attempting. She asks that next time you move your hand before the machine begins to believe you.
"I had intended to keep it."
"Then show better taste in where you put it."''', c("Put the papers aside.", "account_remainder")),
        page("account_held", "Devarra", '''"The mason charges more than the man who made the doorway."
"The doorway's maker did not include the cost of a house."
"Perhaps I should have eaten him before he developed his trade."
"We have not found him yet."
"A defect in the afternoon."
You lay the estimate beside Iven's other papers. Devarra watches him descend the path with them. The porter will show the mason where the braces stood; Lethra has insisted on remaining while the work is done. Neither of them has agreed to another experiment.
Devarra rolls her shoulder and stretches the foreleg which held the axle. You ask if it aches. She says she has held heavier things for less interesting company, and refuses to elaborate until you offer a better supper.''', c("Put the papers aside.", "account_remainder")),
        page("account_remainder", "Narrator", '''{n}A gust lifts the corner of the embroidered cloth. Devarra catches it before the yellow ship folds beneath the stone. You take the blue-painted brick from your pocket and set it beside the edge.
She looks from the brick to you.{/n}
"You kept that."
"You have not told me the city's name."
"I had wondered whether you would ask again."
{n}She gives you the name, slowly enough to hear how it was spoken by someone who had seen the harbor from above. You repeat it badly. She corrects you with evident pleasure, then describes a street whose houses have their doors on the roofs because the lower rooms flood each spring.
You ask whether the embroidered ship ever reached it. She shakes her head. She still does not know. This time you ask what she saw there herself.
The answer begins with a portrait painter who insisted that a dragon should pay for the whole wall, and grows into an argument about whether a likeness should flatter its subject. She claims she wanted accuracy. You ask how many windows he painted into the ruined building behind her. Her laughter startles the birds below the terrace.{/n}''',
            c("I would like to see the painting. Preferably before you quarrel with its owner.", "account_close"),
            c("Tell me which ruler owned the city. I want to know whether visiting you will require conquering it.", "account_ambition")),
        page("account_ambition", "Devarra", '''"You would conquer a city to improve the arrangements for a visit?"
"I asked whether it would be necessary."
"It rarely is. People undertake it for the other pleasures."
She names the ruler she remembers, then admits that mortal succession may have changed the answer. You would need a ship, current news and a reason for the harbor master to believe you were arriving as a guest. The crusade has given your name uses you cannot leave behind merely by traveling.
"And you?" you ask.
"I would arrive from above. I have given my name the same difficulty."
For a while you discuss the city as two dangerous visitors might: its defenses, its grudges, what either of you would be tempted to take. When she turns back to the painted ship, she says she would rather discover whether the painter's descendants kept the wall than spend the first afternoon defending herself to you over a burning harbor.
"Then we begin with the painting," you say.
"We begin by asking whether the owner still possesses a roof."''', c("Stay to hear the rest of the story.", "account_close")),
        page("account_close", "Narrator", '''{n}The brick holds the cloth while Devarra reaches for the supper basket. She opens it herself. You have learned to leave the wrapping loose enough for a claw, and she has learned which loaf you will resent losing before you have tasted it.
She takes that loaf first and divides it on the clean stone.
The eastern address remains with Iven's copy; the city remains beyond a sea neither of you will cross tonight. Devarra has no intention of becoming content with the smallness of this terrace. You can see it in the way her gaze follows the road beyond the vines.
Then she asks whether you mean to eat your half before it cools. You sit beside the cloth. The ship's embroidered sails catch the last light, and she resumes the story at the place where you interrupted it.{/n}''', c("Spend the remaining evening together.", flags=(EAST_ACCOUNT_DONE,))),
    ], requires=("trickster", EAST_STORE_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED,), delay=24, last=5, optional=True)

EAST_AGENT_DONE = "devarra.trickster.east_agent_answered"
EAST_SETTLEMENT_DONE = "devarra.trickster.east_claim_settled"
LAST_INVITATION_DONE = "devarra.trickster.last_invitation_kept"
EAST_RESTITUTION = "devarra.trickster.east_restitution_chosen"
EAST_REVENUE = "devarra.trickster.east_revenue_chosen"

EAST_AGENT_SCENE = scene(
    "devarra.trickster.the_man_who_sold_her_shadow", "The man who sold her shadow", "Devarra", 5, "agent_road", [
        page("agent_road", "Narrator", '''{n}The receiving agent has rented the upper floor of a countinghouse built against the bridge approach. His name is Rulven. A painted board advertises freight guarantees, witnessed transfers and discreet introductions. Someone has recently scraped the word protection from the bottom.
Iven found him through the bridge's toll register. Rulven had paid to carry an empty frame across, then claimed the return fee because the mechanism would make the bridge unnecessary. The keeper remembered the boast more clearly than the signature.
Devarra lands on the open embankment. The bridge watch sounds a horn. You wait while its sergeant comes down, counts the people beside you and asks whether the city is under attack.
Devarra looks at the countinghouse.{/n}
"Not yet."
{n}You identify the business and ask the sergeant to keep the roadway clear. He leaves two guards by the tollhouse. Neither moves close enough to pretend he could arrest her.
Rulven watches from an upper window. He has had time to hear about the warehouse. He has also had time to decide which papers to display on his desk. He comes downstairs carrying them, dressed for an appearance before someone less dangerous.{/n}''',
            c("Show him the public complaints and ask him to name the protection he sold.", "agent_public", requires=(EAST_CLAIM_PUBLIC,)),
            c("Show him the assigned debt and ask what stands behind his guarantee.", "agent_bought", requires=(EAST_CLAIM_BOUGHT,))),
        page("agent_public", "Rulven", '''"I sold an introduction. Adrast wanted a supplier. I gave him a name. The supplier made representations which I repeated in good faith."
{n}He says it with the care of a man who has paid to learn where a sentence becomes an admission. Iven puts the lead token beside his papers.{/n}
"And these?"
"A supplier's mark."
"My mark," Devarra says.
"An approximation of a dragon's scale. No individual was named."
{n}You read the sentence naming the western ledge. Rulven looks toward the bridge watch. The sergeant has remained where you asked him to stand.{/n}
"There may have been an unfortunate inference."
"Yes," you say. "You inferred that she would never read it."
{n}The shopkeeper who paid follows Iven down the embankment. Rulven recognizes her and loses some of his composure. She asks for her money. He explains that the actual supplier has left the district. She asks which part of her payment Rulven kept.
For the first time, he gives you a number instead of a description of his profession.{/n}''', c("Examine what can actually be recovered.", "agent_assets")),
        page("agent_bought", "Rulven", '''"Adrast has assigned you a disputed claim. I dispute it."
"You guaranteed delivery," you say.
"The mechanism was delivered."
"A useful mechanism."
"Those are different words."
{n}Devarra lowers one claw onto the painted board. Its frame cracks without breaking through.{/n}
"I can guarantee that your introduction will be useful. You will meet the person whose name you sold. She will have questions."
{n}Rulven stops examining the assignment. He says he can return his commission if the remaining claim is withdrawn. You ask why he expects you to buy Adrast's loss and then sell it back for less than its cost.
He names the actual supplier. Iven already has that name. Rulven adds that the supplier has left the district with the money which ought to answer for the installation.
Devarra's claw presses farther into the board.{/n}
"Then we have found the man who accepted money to introduce thieves. I am impatient to discover the price of his next introduction."
{n}You place the assigned guarantee beside his offer. He looks at the smaller sum for a long moment before agreeing to show you his security account.{/n}''', c("Examine what can actually be recovered.", "agent_assets")),
        page("agent_assets", "Narrator", '''{n}The account names a warehouse bond held by the tollhouse, and a consignment of finished brass fittings. Iven has asked the keeper for the transfer dates. Those dates matter more than the impressive sum written at the top of Rulven's page.
The keeper compares the notice of the warehouse inquiry with Rulven's instructions to release his security. One reached the tollhouse before the other. The order has made a difference you can now count.{/n}''',
            c("Compare the dates after the docket investigation gave Adrast time to send his warning.", "agent_warned", requires=(VAULT_MAP_BURNED,)),
            c("Compare the dates against the earlier identification made from the divided targeting account.", "agent_held", requires=(VAULT_MAP_KEPT, VAULT_SHARED_POWER))),
        page("agent_warned", "Commander", '''Rulven released the bond on the morning Adrast's clerk arrived. He called the payment a refund to the supplier. By the time the warehouse's second witness notified the tollhouse of the disputed installation, the money had been carried out with a departing caravan.
The keeper has a signed release. It names a recipient, not a bag of money anybody here can seize. Finding the recipient would mean following the caravan beyond the river settlements.
Devarra reads the date, then looks at you. Burning the targeting names protected the people named in them. It also left you dependent on a man who used the delay to warn his associate.
"I can catch a caravan," she says.
"Which one? The keeper records the carrier who took the money, not the wagons he joined afterward."
She knows the difference. Her tail lashes across the bare earth anyway.
Rulven begins to explain that the transfer was lawful. You stop him before Devarra answers. The brass consignment remains in his name. Its sale could pay the known complaints, but not all the debt Adrast signed over or all the claims still arriving.
You have recovered a smaller fund and a longer pursuit. Rulven cannot be made to possess the missing money by frightening him hard enough.''', c("Keep the release as evidence. Settle what remains here before deciding whether to pursue the carrier.", "agent_scale")),
        page("agent_held", "Commander", '''The second witness reached the tollhouse with the named receiving room while the bond was still held. The keeper suspended its release pending the installation dispute. Rulven's instruction to return it to the supplier arrived after the suspension.
Rulven argues that you had no right to interfere in a private transfer. Iven asks whether he would like the keeper to explain why a disputed freight guarantee has security attached to it.
Devarra studies the signatures. You brought the method from the vault account; she brought the targeting names. That unpleasant knowledge let you identify Lethra without giving Adrast an extra journey in which to rearrange the money.
"There," she says. "Something useful which did not improve by being burned."
"Something dangerous which happened to name the person we needed."
"You may preserve the objection. I intend to preserve the money."
The keeper will release it only against a witnessed settlement. It is not a chest waiting for Devarra's claw. Together with the brass consignment it should cover the known complaints and leave a disputed balance for the guarantee's holder.
Rulven asks whether cooperation will end the matter. Devarra tells him they have not yet reached the part she considers personal.''', c("Keep the bond suspended until the witnessed settlement is ready.", "agent_scale")),
        page("agent_scale", "Devarra", '''"Who took the impression?"
{n}Rulven glances at the token. He says the pattern came from a cast sold with the delivery frames. Its maker described it as an old dragon's scale, found beside an abandoned road. He did not meet that dragon.
She asks again. This time he brings out a wrapped clay plate. The surface repeats a familiar ridge, but part of the edge has been made with a tool. The token was pressed from this master, not against her body.
You see the difference only after she turns it toward the light. What you first took for the pattern of a scar is a clean groove cut to make the cast easier to lift.{/n}
"He made the damage prettier," she says. "A small vanity. I shall remember it."
{n}Rulven offers you the plate as part of the settlement. Devarra refuses to let him exchange the instrument of a theft for forgiveness of it. She wants the maker's instructions as well.
The instructions mention the frames. Their brass sockets carried the same little pattern, intended to make the owner's token answer when the apparatus was used. It was a way of recognizing connected devices. Rulven sold it as recognition by a dragon.
His supplier's trick was cleverer than his explanation. Devarra looks annoyed to have discovered that about a man she intends to punish.{/n}''', c("Take the plate and instructions to examine against what survived the warehouse.", "agent_depart")),
        page("agent_depart", "Narrator", '''{n}Rulven signs an undertaking to leave the fittings with the tollhouse until the claims are heard. The sergeant sends a guard with Iven to watch them weighed. Rulven keeps his countinghouse and the freedom to complain about you to anyone willing to listen.
Devarra would prefer to bring him along. You tell her he has more reason to appear at the settlement while his goods are held than while he believes the settlement will end in her mouth.
She asks whether that is your entire argument. You say it is the part likely to interest him.
Rulven reaches for the painted board after you turn away. Devarra puts her claw through the last intact letter of protection.{/n}
"A correction," she says. "Do not charge the carpenter to the complainants."
{n}On the road back she asks whether you enjoyed that. You admit that some of it pleased you more than a judge would find reassuring.
Her expression brightens.{/n}
"Then the afternoon was not entirely wasted on arithmetic."''', c("Bring the actual security, missing funds and false mark into the settlement.", flags=(EAST_AGENT_DONE,))),
    ], requires=("trickster", EAST_ACCOUNT_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED,), delay=24, last=5, optional=True)

EAST_SETTLEMENT_SCENE = scene(
    "devarra.trickster.the_price_she_names", "The price she names", "Devarra", 5, "price_arrival", [
        page("price_arrival", "Narrator", '''{n}Iven chooses the tollhouse courtyard because Devarra can stand in it without breaking anything which the disputed money would have to replace. The claimants sit beneath an awning. Rulven remains in its shadow until she asks whether he has become difficult to recognize in daylight.
Lethra brings a short account from the mason. Her new lintel is in place. She does not bring the old doorpost. Her sons have taken its marked length inside, where the house's repairs cannot turn it into firewood.
The fittings have been weighed. The keeper has checked the metal beneath their polished surfaces and found enough brass to justify a buyer's offer. Rulven argues for waiting until the price improves. The shopkeeper asks whether he waited for a favorable day when he took her payment.
Devarra leaves that argument to Iven. She has brought the clay master and wants to know what you intend to do with its promise of recognition.
She sets the plate beside the supplier's instructions. The little groove runs across the edge of every illustrated socket. She asks what the warehouse has left you with to compare against it.{/n}''',
            c("Examine the surviving fastening chain. The apparatus itself was destroyed.", "price_broken", requires=(EAST_DOOR_BROKEN,)),
            c("Bring your axle and catch beside Devarra's outer sections, without joining them.", "price_kept", requires=(EAST_DOOR_KEPT,))),
        page("price_broken", "Commander", '''The chain has ordinary wear at the point where it held the housing. It supplies no hidden inscription and no way to reconstruct the apparatus. The clay pattern is clearer evidence than the iron.
Devarra lays the chain beside it. She had hoped to compare the inscription on a complete socket with the supplier's instructions. Your decision at the warehouse has made that impossible.
"You were entitled to dislike the machine," she says. "You are not entitled to tell me nothing valuable went with it."
You do not. The drawing describes how the recognition mark was repeated, but not how its charge was set. A second frame might be recognized by the same token. You cannot make this dead clay tell you whether any others remain.
Rulven notices the limit and tries to withdraw his earlier admission. Devarra tips the plate until its tool-cut groove catches the light. The shopkeeper's token bears the same flaw. So does Adrast's.
You put the matching impressions before the witnesses. They prove these tokens came from the same master. They do not prove that every device named in the instructions was built.
Devarra lets you make that distinction, though she does not enjoy letting a potentially useful lead die on the table. She tells Rulven that his testimony about the supplier will be copied before he leaves. If another frame appears, she expects to know who introduced its buyer.
He asks how long she means to remember his name.
"You should arrange your remaining business on the assumption that I have no difficulty with names."''', c("Record the proved fraud and the investigation which cannot be completed from the broken parts.", "price_claims")),
        page("price_kept", "Commander", '''The socket on Devarra's outer section bears the same tool-cut groove as the clay master. Your catch has a shallow seat for it. You can compare them without fitting the axle or giving the frame a receiving wall.
The instructions describe a recognition charge. With the parts separate, you lay the false token in the socket. It gives a faint answering warmth. You remove it and try an unmarked coin. Nothing happens.
Rulven says that proves the protection worked. Devarra puts one real claw beside the warmed token.
"Did it ask me anything?"
"It recognized the mark."
"Then you sold the company of a machine which could recognize itself. My participation was invented for the price."
The witnesses see the difference. The trick was never a dragon watching the road. It was a copied sign making a buyer feel answered.
Devarra wants to test whether the token can locate another matching frame. The instructions require the axle to be fitted before the charge can reach beyond the socket. She looks at the wrapped piece beside your hand.
You remind her where you are standing. A courtyard full of witnesses is no place to discover what a machine might regard as its next destination.
She dislikes the delay. She also looks at the awning, at Lethra, and finally at the bridge arch behind them. The axle remains wrapped.
She removes the token herself and gives you the socket's measurements to copy. You have preserved a possible investigation without pretending it is finished. She tells you she will expect an empty testing ground and a real answer to her proposal later.''', c("Keep the pieces separate and record the demonstrated false protection.", "price_claims")),
        page("price_claims", "Narrator", '''{n}The keeper lays out the claims. The mason has been paid from Adrast's wagon sale. The shopkeeper wants the protection fee returned. Adrast wants the difference between a delivered contraption and the useful passage Rulven guaranteed.
Devarra names a claim of her own: payment for the use of her identity. Rulven protests that no court agreed to it. She answers that no dragon agreed to the use.
Iven will record a voluntary settlement, not declare that whatever a dragon demands has become law. She could take the fittings anyway. She makes certain he knows it, then turns toward you.
The known victims could be paid first, leaving the rest in question. Or Rulven could surrender his remaining commission and accept a secured debt to you and Devarra after those claims are paid. That would give her a continuing interest in his business and a means of demanding news of the supplier. Rulven dislikes both arrangements. He dislikes her standing beside his goods more.
You ask why he should stay in business at all. He answers that people still need goods carried across the river, and that someone who has been made expensive to cheat may become cheaper to employ.
It is the first argument he has made that Devarra considers worth hearing.{/n}''',
            c("[Good] Pay the proved victims first. Take no personal payment for her name, and leave future claims to the witnesses.", "price_restitution", flags=(EAST_RESTITUTION,)),
            c("[Evil] Pay the proved victims, then secure the remaining debt against his commissions. Make him profitable to watch.", "price_revenue", flags=(EAST_REVENUE,))),
        page("price_restitution", "Devarra", '''"You are generous with something which was stolen from me."
"I am asking you what you intend to recover. Money from people already waiting to be repaid, or a name they will believe when you speak?"
"I could take both."
"You could. Then the next seller would only have to describe the payment accurately."
She turns toward the awning. The shopkeeper has stopped pretending not to listen. Devarra asks her how much of the fee she would have paid if the dragon herself had demanded it.
"Whatever kept my children alive," the woman says.
Devarra studies her, then Rulven. She does not call the answer courage or ask to be thanked for hearing it.
"You sold a fear you had not earned. I will not have it mistaken for a debt I collected."
She strikes her claim from Iven's sheet with the point of one claw. The parchment tears. Iven copies the remaining sums onto another page.
Later, while the claimants sign, she tells you she has not agreed never to take tribute.
"I heard the distinction."
"Good. I disliked the thought of needing to make it with a demonstration."''', c("Witness the repayments without taking a personal share.", "price_end")),
        page("price_revenue", "Devarra", '''"Now there is an apology with a future."
Rulven asks for a ceiling. He will sign for the stated loss and an agreed share of his commissions until it is paid. He will not sign away everything he might ever earn. A man with nothing left to lose is difficult to keep in a countinghouse.
You accept a stated sum, require copies of the freight accounts and make false entries grounds for calling the remaining debt at once. Iven reads it aloud. Devarra interrupts to add the supplier's introductions to the required reports.
Rulven objects that he cannot report introductions he has not made. She tells him to begin with that useful sentence whenever he considers making another.
The victims are paid before the first commission becomes yours. The arrangement leaves Rulven working under a threat he has good reason to believe. Devarra makes no effort to dress that in gentler language.
When he asks which of you will collect, she looks at you.
"We shall compare his accounts. Separately, on occasion. He deserves the pleasure of wondering how often we speak."
You agree. Iven writes the collection terms, and Rulven discovers that your interest in keeping him alive has become rather less comforting than he expected.''', c("Witness the secured debt and accept responsibility for collecting what it actually says.", "price_end")),
        page("price_end", "Narrator", '''{n}The keeper will distribute only money he holds and the proceeds of the weighed fittings. Every claimant receives a copy of the sums, including what remains unpaid. Nobody mistakes an entry against the absent supplier for coins already returned.
The clay master is broken before the witnesses. Each surviving token has its false scale scored through. Rulven gives the watch the supplier's last description and agrees to surrender any matching master still in his possession.
Devarra keeps one defaced token. She says it will remind her how cheaply people have tried to acquire a dragon.
On the road away from the bridge, you ask whether she thinks the price was the mistake.{/n}
"The presumption was the mistake. The price insulted it."
{n}She turns the lead between two claws, then drops it into the pouch holding the copied accounts. She is finished standing before an audience for today.
You mention the vineyard. She shakes her head.{/n}
"Somewhere higher. I have spent too long looking at roofs which somebody else should repair. Bring something you will still want to eat after the climb."''', c("Arrange the next meeting above the bridge road.", flags=(EAST_SETTLEMENT_DONE,))),
    ], requires=("trickster", EAST_AGENT_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED,), delay=24, last=5, optional=True)

LAST_INVITATION_SCENE = scene(
    "devarra.trickster.a_place_above_the_road", "A place above the road", "Devarra", 5, "height", [
        page("height", "Narrator", '''{n}The path ends on a bare shelf above the river bend. Devarra has chosen a place from which the bridge looks small enough to hold between two claws. The countinghouse roof is visible beyond it. She notices where you look and tells you she did not choose the view as a threat.
You ask whether she wants that statement witnessed.
Her laughter follows you up the last stones. She has brought the coast cloth, weighted with flat pieces of shale. You put the blue brick beside its yellow ship.
The food has survived the climb. Your dignity fares less well when the basket catches in a thorn bush and requires an operation which she watches with unhelpful attention. By the time you sit, she has named the bush's victory and proposed terms for its surrender.
For a while neither of you mentions the bridge. You tell her which of the embroidered cities you have found on a map. One has a different name now. She dislikes the new name on first hearing and asks who had the authority to make it uglier.{/n}''',
            c("Tell her what you learned, then ask how she means to spend the days you are absent.", "height_future")),
        page("height_future", "Devarra", '''"West, first. There is a ridge I have not seen since the roads below it carried different banners. I want to know whether the wind still strikes its northern face hard enough to make the ravens fly sideways."
"A matter of strategic importance."
"To the ravens."
{n}She spreads one wing to catch the evening air. There is power in the movement which no talk over a disputed account can make domestic. You imagine the distance she could cross while you sit through a single council meeting.
She asks what keeps you in Drezen when every report offers another place where you might be needed. You tell her there are people whose work becomes impossible if the Commander disappears whenever the next problem looks more interesting.
She does not flatter the answer. She asks whether you have learned to distinguish their need from your pleasure in being needed.
You give her the silence that question deserves. She lets you keep it long enough to become uncomfortable, then nudges the basket toward you.{/n}
"Eat. I did not ask you to solve yourself before supper."
{n}You ask when she will return. She studies you before answering.{/n}''',
            c("We chose a partnership. Tell me when to expect word, even if you decide to remain west.", "height_partners", requires=("devarra.trickster.chosen_partnership",)),
            c("We chose separate lives. Give me an invitation when you know where you want the next meeting.", "height_visitors", requires=("devarra.trickster.chosen_separate_lives",))),
        page("height_partners", "Commander", '''She proposes sending word with a caravan crossing the northern ford. You point out that a changed road or a dead horse could turn a missed message into weeks of uncertainty.
"You wish me to appoint a herald?"
"I wish you to tell me whether an unanswered message means you want no answer."
Her gaze sharpens. She has used silence that way before. You have commanded people who would rather pretend not to understand an unwelcome question.
She says she will leave a mark at the ridge's old watch post if she changes her plan. You will arrange for a messenger to look when the road is passable. No messenger will climb into her resting place or demand that she return.
You offer the same courtesy when duty draws you away from Drezen. She asks whether your officers will believe a message intended for her can be delivered without first improving its political meaning.
"They will receive unusually short instructions."
"Then give them mine as well. I would enjoy seeing how a clerk arranges the sentence 'Do not follow me unless I ask.'"
You settle where the messages will go, then put the particulars aside. The agreement has required neither of you to promise that departure will cease to matter.
She asks whether you wanted a date for her return. You say yes.
"Then I shall give you one before I leave. If I change it, you will hear why."
The answer costs her more than the joke did. You hear that too.''', c("Accept her word and offer your own.", "height_history")),
        page("height_visitors", "Commander", '''She proposes a meeting after she has seen the western ridge. There is a ruined beacon above the northern ford. She will leave a message with the keeper's household if she wants company on the return journey.
You tell her not to make the household responsible for knowing where you are. She suggests they send the message to Drezen and let the Commander demonstrate the usefulness of having so many people who read for him.
"They will ask whether it is urgent."
"Tell them I will be displeased if the answer is late. They understand that sort of importance."
You ask how long she would wait at the beacon. Until the third sunset after the message reaches Drezen, she says, if the messenger comes back with confirmation. Without confirmation she will choose another evening instead of teaching herself to resent an absence you never agreed to.
You say you might refuse an invitation because you want something else that evening. She studies you, then says she might find that insulting.
"Would you rather I invented a war council?"
"I would rather you made the other evening worth my curiosity. I did not choose you because I expected agreeable answers."
You smile. She warns you that an honest disappointment remains a disappointment, even when you have phrased it attractively.
The arrangement leaves both of you free to go. It also gives the next meeting a place and a reason to arrive, which is more than either would have obtained by pretending not to care.''', c("Accept the invitation without promising every evening that follows it.", "height_history")),
        page("height_history", "Narrator", '''{n}The last light moves across her foreleg. A scar near the joint catches it differently from the scales around it. You remember the prettified groove on Rulven's clay plate and understand why it offended her.
The false mark borrowed damage without knowing how it had been made. You have learned enough of her history to know that ignorance can be profitable, and that knowing more does not grant you possession of the telling.
She follows your glance, then looks toward the west.{/n}''',
            c("Ask what she wants the surviving brood to hear about this journey, if she chooses to tell them.", "height_saved", requires=(SAVED, SAVED_CUE), forbids=(LOST, LOST_CUE)),
            c("Stay with her while the conversation reaches the loss neither of you can turn into a different history.", "height_lost", requires=(LOST, LOST_CUE), forbids=(SAVED, SAVED_CUE))),
        page("height_saved", "Devarra", '''"That I found people selling my protection and charged them dearly for the education."
"That is not the whole story."
"It is the part likely to discourage imitation."
You ask whether your appearance improves it. She says that depends on whether the telling requires a competent accomplice or an example of how much trouble mortals can make while trying to be useful.
Her amusement fades only slightly when she speaks of the brood. They have their own appetites and mistakes ahead of them. She has no wish to teach them that survival entitles anyone to borrow her judgment indefinitely.
"And if they dislike me?"
"Then you will discover whether you can be interesting to someone who has not agreed to indulge you."
"A familiar beginning."
That earns a slow smile. She does not promise an introduction tonight, or turn the evening into an examination you have already passed. You have asked about people whose survival matters to her. She has answered without making them witnesses to your courtship.''', c("Let their future remain theirs and return to the evening you share.", "height_want")),
        page("height_lost", "Devarra", '''"I do not intend to make the western journey an anniversary."
You had not asked her to. She knows it, and lets the unnecessary sharpness stand for a moment before drawing her wing closer.
The river below has become a strip of reflected sky. She watches it while you sit beside the cloth. There is no useful correction to offer about the brood. You have heard what happened. The view does not make it kinder.
After a while she says she dislikes discovering how often other people expect loss to explain the whole of her.
"They find an answer and stop looking," you say.
"You have a talent for continuing to look after being warned."
"It has supplied several of my better evenings."
She turns back to you. The remark does not make her smile immediately, but she reaches for the basket and asks whether you brought the sharp cheese again.
You did. You pass it without asking her to finish a thought she has chosen to leave where it is. When she resumes the story of the western ridge, she begins with the ravens, furious at a wind they cannot intimidate.''', c("Listen to the story she chooses to tell.", "height_want")),
        page("height_want", "Devarra", '''"What do you want when you look at me?"
{n}The question arrives without the shelter of a joke. She watches your face, not your hand. The cloth stirs beside you.{/n}
"You have wanted information. You have wanted my strength at an inconvenient piece of iron. You have wanted me to leave things unburned which would have looked better afterward. I am asking about the moment before you discover a use."
{n}There is no answer she will supply for you. She has spent too long watching other people pretend their appetite belonged to somebody else's need.{/n}''',
            c("I want the woman who asks whether I can bear an answer she knows I may dislike. I also want another evening before the next argument.", "height_company"),
            c("I want someone whose ambition makes mine feel worth confessing. I want you beside me when we choose what neither of us could take alone.", "height_ambition")),
        page("height_company", "Commander", '''She tells you she is likely to disappoint any wish that she become less demanding with affection. You answer that you have already met the alternative. People who wanted nothing from you sometimes meant they wanted nothing you would notice missing.
"You think I announce my thefts?"
"You have an unusually clear opinion of what should have been yours."
She laughs, then asks whether you intend to spend the next evening praising the honesty of her worst impulses. You say you intend to hear more about the cities, and perhaps to tell a better story than the one which endangered the vineyard roof.
"There was nothing wrong with the story. Your opponent had excellent judgment."
"You improved the insults."
"An act of generosity you continue to undervalue."
Her head lowers a little, bringing her voice nearer. She says she wants you to return because you wish to, and because there are things she would rather hear from you than from a messenger. She gives no example. For once, you do not demand one to make the answer easier to keep.''', c("Stay near her until the last light leaves the river.", "height_end")),
        page("height_ambition", "Commander", '''"You make an attractive offer. You have left the division of the spoils tactfully vague."
"I expected you to object to the first proposal."
"I object to several which you have not made yet. It will save time if you begin with that knowledge."
You tell her the danger is part of what draws you. She studies you without rewarding the confession immediately. Many people admire dangerous things while expecting to remain exempt from them.
"I am not asking you to become harmless," you say.
"Then do not mistake my wanting you here for a promise that you will always like the view."
You look toward the city. You have brought it victories and burdens which cannot be separated merely because you prefer one account of yourself. Devarra follows your gaze.
"I would like to see what you choose when you have finished telling everybody what they expect to hear," she says.
You answer that she will have to remain close enough to argue about it. Her smile is slow and quite without innocence. She tells you she has already made arrangements for another meeting.''', c("Stay with her and let the next argument wait its turn.", "height_end")),
        page("height_end", "Narrator", '''{n}Devarra folds one wing against the windward edge of the shelf. She leaves room for you beside the cloth. You move closer, without crossing the space she has kept for herself.
Below, a cart reaches the bridge. The watch opens the road, and the little light travels through. For tonight the people in it owe neither of you a performance.
She asks for the blue brick while she folds the cloth. You hand it over. She puts it back in your palm after the ship is covered.{/n}
"You have learned one city's name. There are others."
"I had suspected the wager was unfair."
"You accepted it remarkably quickly."
{n}The path will be dark when you descend. You know where its worst stones are now. She knows you will still catch the basket on something if she makes you laugh at the wrong moment.
She waits until you have lifted it before beginning another story.{/n}''', c("Keep the next invitation and leave the height together.", flags=(LAST_INVITATION_DONE,))),
    ], requires=("trickster", EAST_SETTLEMENT_DONE, ROMANCE, "devarra.actor_confirmed", "devarra.history_read"), forbids=(REFUSED,), delay=24, last=5, optional=True)

PARTNERSHIP_ENDINGS = (
    scene("devarra.trickster.recollection_partnership", "The view they argued over", "Epilogue", 0, "memory", [
        page("memory", "Narrator", '''{n}The account of the western house named a blocked drain, a disputed channel and the people whose rooms had almost vanished beneath the repair. It did not name the evening the Commander and Devarra arranged afterward.
That appointment belonged to a different account. They had discovered that a dragon could want a place of her own without offering herself as its garrison, and that the Commander could stand beside her without agreeing to every use of her power.
Their choice of partnership did not decide the crusade's ending. It did not restore a lost clutch or change the truth of the brood that had survived. It gave them a next invitation made without a collector, a wounded hand or a failing wall to excuse it.
Devarra had changed its date because she intended to fly west. The Commander had accepted the change. In a history crowded with vows, threats and impossible bargains, it was an ordinary adjustment worth remembering.
Whatever the larger histories recorded, that evening had not been a rescue offered in exchange for love. She had named what she wanted, heard an answer and asked for an evening of her own.{/n}''')], requires=(PARTNERSHIP_DONE, EAST_ACCOUNT_DONE, LAST_INVITATION_DONE, "devarra.trickster.chosen_partnership"), forbids=(REFUSED,), last=99, optional=True, Relationship="devarra.trickster", Remote=True),
    scene("devarra.trickster.recollection_visits", "The road left open", "Epilogue", 0, "memory", [
        page("memory", "Narrator", '''{n}They had not chosen a household merely to make the relationship easier to describe. Devarra wanted room to fly where she intended; the Commander had a campaign which did not become smaller because somebody waited beyond its reports.
They had chosen invitations instead. The first named an evening, a place and the possibility that duty might require a different answer. Neither called that possibility indifference. Both knew how much easier a command would have been to misunderstand as devotion.
The ledge, the drain and the collector's apparatus remained part of what they had actually done. Her brood's history remained its own truth. Their affection had not purchased another version of it.
The later fate of the crusade belonged to larger decisions. Before those decisions, there had been a dragon beside an outer stair, saying that a visitor could become important enough to be missed, and a Commander refusing to make separate lives a promise of being unimportant.
She had left the road open. It was the only sort of return she had asked him to choose.{/n}''')], requires=(PARTNERSHIP_DONE, EAST_ACCOUNT_DONE, LAST_INVITATION_DONE, "devarra.trickster.chosen_separate_lives"), forbids=(REFUSED,), last=99, optional=True, Relationship="devarra.trickster", Remote=True),
)

def kiln_retry_scene():
    """The cart's deadline is lost on retreat; later play follows its destination."""
    nodes = {node["Id"]: node for node in LIME_KILN_SCENE["Nodes"]}
    reached, pending = set(), ["kiln_departure"]
    while pending:
        key = pending.pop()
        if key in reached:
            continue
        reached.add(key)
        for choice in nodes[key]["Choices"]:
            check = choice.get("Check") or {}
            for target in (choice.get("Next"), check.get("Success"), check.get("Failure")):
                if target:
                    pending.append(target)
    continued = [deepcopy(node) for node in LIME_KILN_SCENE["Nodes"] if node["Id"] in reached]
    for node in continued:
        if node["Id"] == "kiln_departure":
            node["Text"] = '''{n}The workers leave the sorting shed with their tools and the surviving copies of their wages. You escort them to the quarry's free settlement, where people recognize their names.
The kiln meeting cannot be recovered. Serevin has gone with her ledger, and the extra labor she extracted will remain part of this account.
One worker describes a ruined watchtower north of the orchard. He delivered chipped stone there before his imprisonment and remembers its double mark. You copy it from his drawing, without pretending it tells you what Serevin has already done there.{/n}
"She has had time to warn them," Devarra says. "We shall have to disappoint a prepared audience."
{n}You return by the orchard to settle the arrangements left behind. Nothing useful has been captured in your absence.
The lamps at the original kiln are gone. Devarra studies the empty beam, then turns away.{/n}
"An evening without machinery," she says. "I should like to discover whether you remember what those are for."'''
    arrival = page("kiln_return", "Narrator",
        '''{n}The cart left when the hour ended. Watching from the higher orchard bought no second opening: Serevin loaded the prisoners, dismantled the lamps and rode away with her ledger.
Whenever you return to the kiln, that departure is already behind you. The empty beam offers nothing to inspect. Devarra tears the receipt from its nail and lets the wind take it.{/n}
"A demonstration we missed. I propose we decline to miss the people."
{n}The quarry pays for deliveries through a weighhouse on the northern road. Its keeper can be questioned even after the ruts have dried. Finding the destination will take another investigation, not another attempt at the vanished latch.{/n}''',
        c("Find where the cart delivered the workers. Accept that Serevin and her ledger are gone.", "stone_survey"),
        c("Leave the rescue unfinished. Do not follow the cart's destination.", flags=(KILN_RETRY_CLOSED,)))
    pursuit = [
        page("stone_survey", "Commander", '''The weighhouse keeper remembers the cart because its driver disputed the weight of two living passengers.
He has a delivery copy but refuses to give it away. Serevin still buys stone here. Devarra looks at the flimsy roof until the keeper stops explaining how valuable a customer she is.
You can compare the copy to the board of regular deliveries, identifying the destination without taking his only defense against an unpaid fee. If you fail to distinguish the marks, you will have to visit the listed sheds one by one.
The weighhouse clerk has entered the workers against the quarry foreman's name. Their sleeping shed stands beside the cutting face; the cart returned empty before dawn.''',
             c("[Perception 33] Match the delivery mark to the sorting shed.", flags=(KILN_TRIED,), forbids=(KILN_TRIED,), check=dict(Skill="SkillPerception", DC=33, Success="quarry_found", Failure="quarry_search", CommanderOnly=True))),
        page("quarry_found", "Narrator", '''{n}The keeper has reversed the copied mark, as people do when writing what they see on the far side of a hanging board. You turn the paper over against the light and find the matching shed.
Its overseer owns no red lamps. He has ordinary locks, four hired guards and a written claim that the workers were sold to him. Devarra reads the claim from outside the window.{/n}
"I have found the fault in your purchase," she tells him. "You expected me to discuss its price."
{n}The guards decide that their wages did not include a dragon. You open the workers' manacles with the key the overseer supplies. Their wrists are raw from the journey. Neither has been kept safe by your earlier caution.{/n}''',
             c("Free the workers and take their account of the destination north of the orchard.", "kiln_departure", flags=(KILN_PRISONERS_FREE, KILN_SEREVIN_ESCAPED, "devarra.trickster.lower_vault_location", "devarra.trickster.lower_vault_warned", "devarra.trickster.kiln_departure_missed"))),
        page("quarry_search", "Narrator", '''{n}You mistake the copied mark for the neighboring shed's. Its owner sends a runner ahead while insisting that you have accused an honest man. By the time you reach the correct yard, the overseer has barred its doors.
Devarra removes a section of roof. He pulls one worker beneath his arm and puts a knife against the man's side. You climb through the opening while she keeps his attention on the teeth above him.
He cuts the worker before you wrench the knife away. The wound can be treated. It cannot be made into something that happened because you arrived elegantly.{/n}
"Carry him," Devarra says. "You can tell me how much you dislike my temper after we find someone with clean needles."
{n}The other worker has the keys. He opens his own manacle before helping you lift his companion. Serevin is not here, and the overseer knows only where he bought them.{/n}''',
             c("Free both workers and obtain care before returning to the investigation.", "kiln_departure", flags=(KILN_PRISONERS_FREE, KILN_SEREVIN_ESCAPED, "devarra.trickster.lower_vault_location", "devarra.trickster.lower_vault_warned", "devarra.trickster.kiln_departure_missed", "devarra.trickster.quarry_rescue_injury"))),
    ]
    return scene("devarra.trickster.the_last_kiln_approach", "The last kiln approach", "Devarra", 5,
                 "kiln_return", [arrival, *pursuit, *continued],
                 requires=(*LIME_KILN_SCENE["Requires"], KILN_RETREATED, ANCHOR_PAID),
                 forbids=(REFUSED, KILN_DONE, KILN_TRIED, KILN_RETRY_CLOSED, ANCHOR_KEPT),
                 delay=1, last=5, optional=True)


KILN_RETRY_SCENE = kiln_retry_scene()
# The delayed return follows a missed departure and shares only the settlement.
_SCENE_TEMPLATES = (SCENE, FOLLOWUP_SCENE, QUIET_SCENE, AFTER_MEAL_SCENE,
                    EXCHANGE_SCENE, CISTERN_SCENE, LIME_KILN_SCENE,
                    LOWER_VAULT_SCENE, VAULT_AFTER_SCENE, WESTERN_LEDGE_SCENE,
                    LEDGE_CLAIM_SCENE, LEDGE_STORM_SCENE, LEDGE_SETTLEMENT_SCENE,
                    PARTNERSHIP_SCENE, APPOINTMENT_SCENE, EAST_BUYER_SCENE,
                    EAST_STORE_SCENE, EAST_ACCOUNT_SCENE, EAST_AGENT_SCENE,
                    EAST_SETTLEMENT_SCENE, LAST_INVITATION_SCENE)
_DELIVERY_TEMPLATES = (*_SCENE_TEMPLATES[:7], KILN_RETRY_SCENE, *_SCENE_TEMPLATES[7:], *PARTNERSHIP_ENDINGS)

def history_variant(template, saved):
    result = deepcopy(template)
    matching = (SAVED, SAVED_CUE) if saved else (LOST, LOST_CUE)
    opposite = (LOST, LOST_CUE) if saved else (SAVED, SAVED_CUE)
    result["Id"] += ".saved_brood" if saved else ".lost_clutch"
    # Runtime uses Nodes[0] as its start page; Entry is the interaction label.
    result["Entry"] = template["Title"]
    result["Requires"] = list(dict.fromkeys((*result["Requires"], *matching)))
    result["Forbids"] = list(dict.fromkeys((*result["Forbids"], *opposite, "devarra.trickster.closed")))
    result.pop("RequiresAnyGroups", None)
    ending = result["Owner"].endswith("Epilogue")
    result.update(Relationship="devarra.trickster", ManualOnly=not ending, Remote=ending)
    if not ending:
        result.update(PhysicalPresenceRequired=True, ContactUnit="Devarra")
    return result

SCENES = [history_variant(template, saved)
          for template in _DELIVERY_TEMPLATES for saved in (True, False)]


def reachable_nodes(current_scene):
    nodes = {node["Id"]: node for node in current_scene["Nodes"]}
    assert len(nodes) == len(current_scene["Nodes"]), "duplicate node id"
    seen = {current_scene["Entry"]}
    queue = deque(seen)
    while queue:
        node_id = queue.popleft()
        for choice in nodes[node_id]["Choices"]:
            check = choice.get("Check") or {}
            for target in (choice.get("Next"), check.get("Success"), check.get("Failure")):
                if target is None:
                    continue
                assert target in nodes, (node_id, target)
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
    return nodes, seen


def validate():
    results = {}
    attempt_flags = {WORLD_TRIED, PERCEPTION_TRIED, WITNESS_TRIED, ARCANA_TRIED, CASE_CHECK, "devarra.trickster.slate_arcana_attempted", FATE_CHECK, MEETING_PERCEPTION, MEETING_DIPLOMACY, CISTERN_TRIED, KILN_TRIED, KILN_TRICK_TRIED, VAULT_TRIED, "devarra.trickster.rain_read_attempted", "devarra.trickster.rain_turn_attempted", EAST_CHECK_TRIED}
    for current_scene in _DELIVERY_TEMPLATES:
        assert current_scene["Nodes"][0]["Id"] == current_scene["Entry"]
        nodes, reached = reachable_nodes(current_scene)
        assert reached == set(nodes), sorted(set(nodes) - reached)
        for node in nodes.values():
            assert node["Text"].count("{n}") == node["Text"].count("{/n}"), node["Id"]
            for choice in node["Choices"]:
                check = choice.get("Check")
                if check:
                    assert check["Success"] in nodes and check["Failure"] in nodes
                    assert check["DC"] >= 10 and check["CommanderOnly"] is True
                    flags = set(choice["Set"]) & attempt_flags
                    assert len(flags) == 1 and flags.issubset(choice["Forbids"]), node["Id"]
        results[current_scene["Id"]] = (nodes, reached)
        # Check every edge, including alternatives omitted from a selected playthrough.
        visiting, finished = set(), set()
        def visit(node_id):
            assert node_id not in visiting, (current_scene["Id"], "cycle", node_id)
            if node_id in finished:
                return
            visiting.add(node_id)
            for choice in nodes[node_id]["Choices"]:
                check = choice.get("Check") or {}
                for target in (choice.get("Next"), check.get("Success"), check.get("Failure")):
                    if target:
                        visit(target)
            visiting.remove(node_id)
            finished.add(node_id)
        visit(current_scene["Entry"])
    assert SCENE["RequiresAnyGroups"] == [(SAVED, LOST), (SAVED_CUE, LOST_CUE)]
    assert TRUST not in SCENE["Requires"] and ROMANCE not in SCENE["Requires"]
    assert not any("Nidalynn" in node["Text"] for node in results[SCENE["Id"]][0].values())
    assert sum(bool(choice.get("Check")) for scene_nodes, _ in results.values() for node in scene_nodes.values() for choice in node["Choices"]) >= 7
    return results[SCENE["Id"]]


def _allowed(item, flags):
    return (set(item.get("Requires", ())) <= flags
            and not set(item.get("Forbids", ())) & flags
            and all(set(group) & flags for group in item.get("RequiresAnyGroups", ())))


def validate_history_delivery():
    """Only one matching native pair may deliver any progression scene."""
    from itertools import combinations
    history_flags = (SAVED, LOST, SAVED_CUE, LOST_CUE)
    assert len({item["Id"] for item in SCENES}) == len(SCENES) == 2 * len(_DELIVERY_TEMPLATES)
    assert not {item["Id"] for item in SCENES} & {item["Id"] for item in _SCENE_TEMPLATES}
    for template in _DELIVERY_TEMPLATES:
        variants = [item for item in SCENES if item["Id"].startswith(template["Id"] + ".")]
        assert len(variants) == 2
        for size in range(5):
            for combination in combinations(history_flags, size):
                flags = set(template["Requires"]) | set(combination)
                count = sum(_allowed(item, flags) for item in variants)
                expected = set(combination) in ({SAVED, SAVED_CUE}, {LOST, LOST_CUE})
                assert count == int(expected), (template["Id"], combination, count)


def validate_branch_staging():
    """Walk repaired shared passages with the states that previously contradicted them."""
    def follow(current, path, flags):
        nodes = {node["Id"]: node for node in current["Nodes"]}
        for here, target in zip(path, path[1:]):
            choices = [choice for choice in nodes[here]["Choices"] if _allowed(choice, flags)
                       and (choice.get("Next") == target
                            or target in (choice.get("Check") or {}).values())]
            assert choices, (here, target)
            flags |= set(choices[0]["Set"])
        return flags

    initial = set(AFTER_MEAL_SCENE["Requires"]) | {SAVED, SAVED_CUE}
    ordinary = follow(AFTER_MEAL_SCENE,
        ("second_envelope", "saved_history", "read_letter", "clock_terms", "public_plan",
         "witness_choice", "plan_check", "hour_ordinary", "plan_locked", "plan_complete"), initial)
    assert FALSE_FOLIO_READY in ordinary and not {FATE_HELD, FATE_BROKE} & ordinary
    assert _allowed(EXCHANGE_SCENE, ordinary)
    nodes = {node["Id"]: node for node in EXCHANGE_SCENE["Nodes"]}
    assert [choice["Next"] for choice in nodes["bridge_arrival"]["Choices"]
            if _allowed(choice, ordinary)] == ["plain_minute"]
    follow(EXCHANGE_SCENE, ("bridge_arrival", "plain_minute", "courier_arrives",
                           "parchment_terms", "mark_matched"), ordinary)
    assert "repeated minute" not in nodes["mark_matched"]["Text"]
    for fate, target in ((FATE_HELD, "held_minute"), (FATE_BROKE, "broken_minute")):
        flags = ordinary | {fate}
        assert [choice["Next"] for choice in nodes["bridge_arrival"]["Choices"]
                if _allowed(choice, flags)] == [target]

    nodes = {node["Id"]: node for node in CISTERN_SCENE["Nodes"]}
    for anchor, target in ((ANCHOR_KEPT, "return_kept"), (ANCHOR_PAID, "return_paid")):
        assert [choice["Next"] for choice in nodes["return_fire"]["Choices"]
                if _allowed(choice, {anchor})] == [target]
    assert not any(_allowed(choice, {ANCHOR_KEPT, ANCHOR_PAID})
                   for choice in nodes["return_fire"]["Choices"])
    assert "wheel turned against him" not in nodes["return_fire"]["Text"]


def validate_continuation_paths():
    """Carry valid states through the continuation and its one optional retry."""
    from functools import lru_cache
    import re
    def words(text):
        plain = " ".join(re.sub(r"\{[^}]*\}|<[^>]*>", "", text).split())
        return len(re.findall(r"\b[^\W_]+(?:['?][^\W_]+)*\b", plain))

    totals = {}
    for saved in (True, False):
        templates = (AFTER_MEAL_SCENE, EXCHANGE_SCENE, CISTERN_SCENE, LIME_KILN_SCENE, KILN_RETRY_SCENE, LOWER_VAULT_SCENE, VAULT_AFTER_SCENE, WESTERN_LEDGE_SCENE, LEDGE_CLAIM_SCENE, LEDGE_STORM_SCENE, LEDGE_SETTLEMENT_SCENE, PARTNERSHIP_SCENE)
        sequence = [history_variant(item, saved) for item in templates]
        history = (SAVED, SAVED_CUE) if saved else (LOST, LOST_CUE)
        retained = {REFUSED, CONSEQUENCE_DONE, KILN_DONE, BUYER_SPARED, BUYER_KILLED,
                    BUYER_SERVES, ANCHOR_KEPT, ANCHOR_PAID, KILN_SEREVIN_HELD,
                    KILN_SEREVIN_ESCAPED, KILN_PRISONERS_FREE, KILN_LEDGER_TAKEN,
                    "devarra.trickster.vey_released", "devarra.trickster.vey_obligation_continues", VAULT_DONE, VAULT_AFTER_DONE, VAULT_MAP_BURNED, VAULT_MAP_KEPT, LEDGE_INSPECTED, LEDGE_CLAIM_HEARD, LEDGE_STORM_ENDED, LEDGE_SETTLED, PARTNERSHIP_DONE, "devarra.trickster.chosen_partnership", "devarra.trickster.chosen_separate_lives"}
        outcome_flags = set(retained)
        for current in sequence:
            for item in [current] + [choice for node in current["Nodes"] for choice in node["Choices"]]:
                retained.update(item.get("Requires", ()))
                retained.update(item.get("Forbids", ()))
        states = {frozenset(sequence[0]["Requires"]): 0}
        for current_index, current in enumerate(sequence):
            nodes = {node["Id"]: node for node in current["Nodes"]}
            @lru_cache(None)
            def walk(node_id, flags):
                node = nodes[node_id]
                choices = [choice for choice in node["Choices"] if _allowed(choice, flags)]
                assert choices, (current["Id"], node_id, "dead end")
                outputs = {}
                for choice in choices:
                    if choice.get("Abort"):
                        continue
                    updated = frozenset((flags | set(choice["Set"])) & retained)
                    length = words(node["Text"]) + words(choice["Text"])
                    check = choice.get("Check")
                    targets = [check["Success"], check["Failure"]] if check else [choice.get("Next")]
                    for target in targets:
                        results = walk(target, updated) if target else {updated: 0}
                        for final, remainder in results.items():
                            outputs[final] = max(outputs.get(final, 0), length + remainder)
                return outputs
            outputs = {}
            for flags, count in states.items():
                if current["Id"].startswith(KILN_RETRY_SCENE["Id"]) and KILN_DONE in flags:
                    outputs[flags] = max(outputs.get(flags, 0), count)
                elif _allowed(current, flags):
                    for final, length in walk(current["Nodes"][0]["Id"], flags).items():
                        outputs[final] = max(outputs.get(final, 0), count + length)
            assert outputs, current["Id"]
            future = set(outcome_flags)
            for later in sequence[current_index + 1:]:
                for item in [later] + [choice for node in later["Nodes"] for choice in node["Choices"]]:
                    future.update(item.get("Requires", ()))
                    future.update(item.get("Forbids", ()))
            states = {}
            for flags, length in outputs.items():
                projected = frozenset(flags & future)
                states[projected] = max(states.get(projected, 0), length)
        states = {flags: count for flags, count in states.items() if REFUSED not in flags}
        assert states
        assert all({CONSEQUENCE_DONE, KILN_DONE, KILN_PRISONERS_FREE, VAULT_DONE, VAULT_AFTER_DONE, PARTNERSHIP_DONE} <= flags for flags in states)
        assert all(len({"devarra.trickster.chosen_partnership", "devarra.trickster.chosen_separate_lives"} & flags) == 1 for flags in states)
        assert all(len({VAULT_MAP_BURNED, VAULT_MAP_KEPT} & flags) == 1 for flags in states)
        assert all(len({BUYER_SPARED, BUYER_KILLED, BUYER_SERVES} & flags) == 1 for flags in states)
        assert all(len({ANCHOR_KEPT, ANCHOR_PAID} & flags) == 1 for flags in states)
        assert all(len({KILN_SEREVIN_HELD, KILN_SEREVIN_ESCAPED} & flags) == 1 for flags in states)
        assert all((KILN_LEDGER_TAKEN in flags) == (KILN_SEREVIN_HELD in flags) for flags in states)
        for flags in states:
            obligations = {"devarra.trickster.vey_released", "devarra.trickster.vey_obligation_continues"} & flags
            assert len(obligations) == int(BUYER_SERVES in flags)
        # Both shard outcomes and all collector fates must carry through to either kiln result.
        for fate in (BUYER_SPARED, BUYER_KILLED, BUYER_SERVES):
            for anchor in (ANCHOR_KEPT, ANCHOR_PAID):
                for result in (KILN_SEREVIN_HELD, KILN_SEREVIN_ESCAPED):
                    assert any({fate, anchor, result} <= flags for flags in states), (history, fate, anchor, result)
        totals[history[0]] = max(states.values())
    return totals


def validate_vault_and_retry():
    """Exercise the selected retreat and outcome menus with their actual flags."""
    kiln = {node["Id"]: node for node in LIME_KILN_SCENE["Nodes"]}
    retry = {node["Id"]: node for node in KILN_RETRY_SCENE["Nodes"]}
    assert LIME_KILN_SCENE["DelayHours"] == 6 * 24
    for template in _DELIVERY_TEMPLATES:
        for saved in (True, False):
            variant = history_variant(template, saved)
            assert variant["Nodes"][0]["Id"] == template["Entry"]
            assert variant["Entry"] == template["Title"]
    for fate in (BUYER_SPARED, BUYER_KILLED, BUYER_SERVES):
        available = [choice["Next"] for choice in kiln["kiln_survey"]["Choices"]
                     if _allowed(choice, {fate, ANCHOR_PAID})]
        assert available == (["kiln_employment"] if fate == BUYER_SERVES else ["stone_survey"])
    assert "discussing employment" not in kiln["kiln_survey"]["Text"]
    assert "handler is exempt" in kiln["receipt_trap"]["Text"]

    flags = set(LIME_KILN_SCENE["Requires"]) | {SAVED, SAVED_CUE, BUYER_SPARED, ANCHOR_PAID}
    retreat = next(choice for choice in kiln["stone_survey"]["Choices"]
                   if choice["Next"] == "kiln_retreat")
    assert _allowed(retreat, flags)
    flags.update(retreat["Set"])
    flags.update(kiln["kiln_retreat"]["Choices"][0]["Set"])
    assert KILN_TRIED not in flags and KILN_RETREATED in flags
    assert not _allowed(LIME_KILN_SCENE, flags)
    assert _allowed(KILN_RETRY_SCENE, flags) and KILN_RETRY_SCENE["DelayHours"] == 1
    attempt = retry["stone_survey"]["Choices"][0]
    assert _allowed(attempt, flags)
    flags.update(attempt["Set"])
    assert KILN_TRIED in flags and not _allowed(attempt, flags)
    assert not _allowed(KILN_RETRY_SCENE, flags)
    assert "kiln_retreat" not in retry
    assert "The cart left when the hour ended" in retry["kiln_return"]["Text"]
    assert "receipt_trap" not in retry and "captured_terms" not in retry
    for result in ("quarry_found", "quarry_search"):
        effects = set(retry[result]["Choices"][0]["Set"])
        assert {KILN_PRISONERS_FREE, KILN_SEREVIN_ESCAPED, "devarra.trickster.kiln_departure_missed"} <= effects
        assert not {KILN_LEDGER_TAKEN, KILN_SEREVIN_HELD} & effects

    vault = {node["Id"]: node for node in LOWER_VAULT_SCENE["Nodes"]}
    for fate, target in ((KILN_SEREVIN_HELD, "vault_unwarned"), (KILN_SEREVIN_ESCAPED, "vault_warned")):
        flags = {fate, KILN_LEDGER_TAKEN} if fate == KILN_SEREVIN_HELD else {fate}
        assert [choice["Next"] for choice in vault["vault_road"]["Choices"] if _allowed(choice, flags)] == [target]
    bargain = vault["vault_bargain"]["Choices"]
    assert {VAULT_MAP_KEPT, VAULT_SHARED_POWER} <= set(bargain[0]["Set"])
    assert VAULT_MAP_BURNED in bargain[1]["Set"] and VAULT_MAP_KEPT not in bargain[1]["Set"]
    assert REFUSED in vault["vault_breakup"]["Choices"][0]["Set"]
    roof = {node["Id"]: node for node in VAULT_AFTER_SCENE["Nodes"]}
    for flags, target in (({VAULT_MAP_KEPT, VAULT_SHARED_POWER}, "roof_power"), ({VAULT_MAP_BURNED}, "roof_burned")):
        assert [choice["Next"] for choice in roof["chosen_room"]["Choices"] if _allowed(choice, flags)] == [target]
    # Quiet or departing answers terminate without crossing the kiss page.
    for selected in roof["roof_desire"]["Choices"][1:]:
        pending, reached = [selected["Next"]], set()
        while pending:
            key = pending.pop()
            if key in reached:
                continue
            reached.add(key)
            pending.extend(choice["Next"] for choice in roof[key]["Choices"] if choice["Next"])
        assert "roof_kiss" not in reached
        assert reached <= {"roof_still", "roof_goodnight"}


def longest_path_words(current_scene, target=None):
    import re
    from functools import lru_cache

    nodes = {node["Id"]: node for node in current_scene["Nodes"]}
    count_words = lambda text: len(re.findall(r"\b[\w'-]+\b", re.sub(r"\{/?n\}", " ", text)))

    @lru_cache(maxsize=None)
    def visit(node_id):
        node = nodes[node_id]
        if target is not None and node_id == target:
            return count_words(node["Text"])
        options = []
        for choice in node["Choices"]:
            check = choice.get("Check") or {}
            targets = [value for value in (choice.get("Next"), check.get("Success"), check.get("Failure")) if value]
            continuations = [visit(value) for value in targets if target is None or visit(value) >= 0]
            if not targets:
                continuations = [0] if target is None else []
            options.extend(count_words(choice["Text"]) + value for value in continuations)
        if not options and target is not None:
            return -1
        return count_words(node["Text"]) + max(options, default=0)

    return visit(current_scene["Entry"])


def selected_completed_word_bounds():
    """Count opening, compatible selected visits and exactly one eligible coda."""
    import runpy
    from functools import lru_cache
    from storylines import devarra_trickster_opening as opening
    word = lru_cache(None)(runpy.run_path("tools/measure-story-content.py")["words"])
    totals = {}
    for saved in (True, False):
        pair = {SAVED, SAVED_CUE} if saved else {LOST, LOST_CUE}
        delivered = [item for item in SCENES if pair <= set(item["Requires"])]
        sequence = [opening.SAVED_SCENE if saved else opening.LOST_SCENE] + [item for item in delivered if item["Owner"] != "Epilogue"]
        endings = [item for item in delivered if item["Owner"] == "Epilogue"]
        live = [set() for _ in range(len(sequence) + 1)]
        for ending in endings:
            live[-1].update(ending["Requires"])
            live[-1].update(ending["Forbids"])
        for index in reversed(range(len(sequence))):
            live[index] = live[index + 1] | {REFUSED, "devarra.trickster.closed"}
            for item in [sequence[index]] + [choice for node in sequence[index]["Nodes"] for choice in node["Choices"]]:
                live[index].update(item.get("Requires", ()))
                live[index].update(item.get("Forbids", ()))
                for group in item.get("RequiresAnyGroups", ()):
                    live[index].update(group)
        states = {frozenset(sequence[0]["Requires"]): (0, 0)}
        for index, current in enumerate(sequence):
            nodes = {node["Id"]: node for node in current["Nodes"]}
            future = live[index + 1]
            @lru_cache(None)
            def walk(key, flags):
                node, outputs = nodes[key], {}
                for choice in node["Choices"]:
                    if choice["Abort"] or not _allowed(choice, flags):
                        continue
                    updated = frozenset((flags | set(choice["Set"])) & live[index])
                    if {REFUSED, "devarra.trickster.closed"} & updated:
                        continue
                    check = choice.get("Check")
                    targets = [check["Success"], check["Failure"]] if check else [choice["Next"]]
                    for target in targets:
                        outcomes = walk(target, updated) if target else {updated & future: (0, 0)}
                        for final, (low, high) in outcomes.items():
                            amount = word(node["Text"]) + word(choice["Text"])
                            old = outputs.get(final, (10**9, 0))
                            outputs[final] = (min(old[0], low + amount), max(old[1], high + amount))
                return outputs
            updated_states = {}
            for flags, (low, high) in states.items():
                if current["Id"].startswith(KILN_RETRY_SCENE["Id"]) and KILN_DONE in flags:
                    outcomes = {flags & future: (0, 0)}
                else:
                    outcomes = walk(current["Nodes"][0]["Id"], flags) if _allowed(current, flags) else {}
                for final, (extra_low, extra_high) in outcomes.items():
                    old = updated_states.get(final, (10**9, 0))
                    updated_states[final] = (min(old[0], low + extra_low), max(old[1], high + extra_high))
            states = updated_states
            assert states, current["Id"]
        completed = []
        for flags, (low, high) in states.items():
            eligible = [ending for ending in endings if _allowed(ending, flags)]
            assert len(eligible) == 1, (flags, eligible)
            assert len(eligible[0]["Nodes"]) == 1
            node = eligible[0]["Nodes"][0]
            assert len(node["Choices"]) == 1 and node["Choices"][0]["Next"] is None
            amount = word(node["Text"]) + word(node["Choices"][0]["Text"])
            completed.append((low + amount, high + amount))
        totals["saved" if saved else "lost"] = {"minimum": min(x[0] for x in completed), "maximum": max(x[1] for x in completed)}
    return totals


def validate_minimum_continuation():
    """Follow the final three visits with the outcomes their predecessors produce."""
    from itertools import product

    def outcomes(current, initial):
        nodes = {node["Id"]: node for node in current["Nodes"]}
        def walk(key, flags, visited):
            assert key not in visited
            node = nodes[key]
            choices = [choice for choice in node["Choices"] if _allowed(choice, flags)]
            assert choices, (current["Id"], key)
            for choice in choices:
                assert not choice.get("Check"), "These settlement visits contain no new checks."
                if choice["Abort"]:
                    continue
                updated = flags | set(choice["Set"])
                route = visited + (key,)
                if choice["Next"]:
                    yield from walk(choice["Next"], updated, route)
                else:
                    yield updated, route
        assert _allowed(current, initial)
        return walk(current["Nodes"][0]["Id"], initial, ())

    completed = 0
    for saved, map_kept, parts_kept, partnership, claim_bought in product((True, False), repeat=5):
        history = {SAVED, SAVED_CUE} if saved else {LOST, LOST_CUE}
        state = set(EAST_AGENT_SCENE["Requires"]) | history | {PARTNERSHIP_DONE, EAST_STORE_DONE}
        state |= {VAULT_MAP_KEPT, VAULT_SHARED_POWER} if map_kept else {VAULT_MAP_BURNED}
        state.add(EAST_DOOR_KEPT if parts_kept else EAST_DOOR_BROKEN)
        state.add("devarra.trickster.chosen_partnership" if partnership else "devarra.trickster.chosen_separate_lives")
        state.add(EAST_CLAIM_BOUGHT if claim_bought else EAST_CLAIM_PUBLIC)
        for agent_flags, agent_path in outcomes(EAST_AGENT_SCENE, state):
            assert ("agent_held" in agent_path) == map_kept
            assert ("agent_warned" in agent_path) != map_kept
            assert ("agent_bought" in agent_path) == claim_bought
            assert ("agent_public" in agent_path) != claim_bought
            for settled_flags, settled_path in outcomes(EAST_SETTLEMENT_SCENE, agent_flags):
                assert ("price_kept" in settled_path) == parts_kept
                assert ("price_broken" in settled_path) != parts_kept
                assert len({EAST_RESTITUTION, EAST_REVENUE} & settled_flags) == 1
                for final_flags, final_path in outcomes(LAST_INVITATION_SCENE, settled_flags):
                    assert ("height_partners" in final_path) == partnership
                    assert ("height_visitors" in final_path) != partnership
                    assert ("height_saved" in final_path) == saved
                    assert ("height_lost" in final_path) != saved
                    assert len({"height_company", "height_ambition"} & set(final_path)) == 1
                    assert LAST_INVITATION_DONE in final_flags
                    endings = [history_variant(item, saved) for item in PARTNERSHIP_ENDINGS]
                    assert sum(_allowed(item, final_flags) for item in endings) == 1
                    assert not any(_allowed(item, final_flags - {LAST_INVITATION_DONE}) for item in endings)
                    completed += 1
    assert completed == 128
    store = {node["Id"]: node for node in EAST_STORE_SCENE["Nodes"]}
    assert "dispensed with the counterweight" in store["store"]["Text"]
    assert "counterweight" not in store["store_destroy"]["Text"]
    assert "housing to its stone socket" in store["store_destroy"]["Text"]
    assert "an overturned stool" in store["store"]["Text"]
    return completed


def validate_eastern_consequences():
    """Walk real choice states through the eastern check and later damage menu."""
    store = {node["Id"]: node for node in EAST_STORE_SCENE["Nodes"]}
    account = {node["Id"]: node for node in EAST_ACCOUNT_SCENE["Nodes"]}
    for saved in (True, False):
        history = {SAVED, SAVED_CUE} if saved else {LOST, LOST_CUE}
        for method in ("store_turned", "store_failed", "store_manual"):
            for outcome in ("store_destroy", "store_keep"):
                state = set(EAST_STORE_SCENE["Requires"]) | history
                key = EAST_STORE_SCENE["Nodes"][0]["Id"]
                selected = []
                while key:
                    selected.append(key)
                    node = store[key]
                    options = [choice for choice in node["Choices"] if _allowed(choice, state)]
                    if key == "store_plan":
                        choice = options[1] if method == "store_manual" else options[0]
                    elif key == "store_parts":
                        choice = next(choice for choice in options if choice["Next"] == outcome)
                    else:
                        assert len(options) == 1, (key, state)
                        choice = options[0]
                    state.update(choice["Set"])
                    key = method if choice.get("Check") else choice["Next"]
                assert EAST_STORE_DONE in state
                assert (EAST_CHECK_FAILED in state) == (method == "store_failed")
                if method != "store_manual":
                    assert not _allowed(store["store_plan"]["Choices"][0], state)
                assert len(set(selected) & {"store_turned", "store_failed", "store_manual"}) == 1
                assert [c["Next"] for c in account["account_damage"]["Choices"] if _allowed(c, state)] == ["account_failed" if method == "store_failed" else "account_held"]
                assert len({EAST_DOOR_BROKEN, EAST_DOOR_KEPT} & state) == 1
        for home in ("home_fixed_terms", "home_taken", "home_declined"):
            for relation in ("chosen_partnership", "chosen_separate_lives"):
                state = history | {PARTNERSHIP_DONE, EAST_ACCOUNT_DONE, LAST_INVITATION_DONE, "devarra.trickster." + home, "devarra.trickster." + relation}
                endings = [history_variant(item, saved) for item in PARTNERSHIP_ENDINGS]
                eligible = [item for item in endings if _allowed(item, state)]
                assert len(eligible) == 1
                assert "cup" not in eligible[0]["Nodes"][0]["Text"].lower()
                assert not any(_allowed(item, state - {EAST_ACCOUNT_DONE}) for item in endings)
    date = {node["Id"]: node for node in APPOINTMENT_SCENE["Nodes"]}
    assert all("blue-painted brick" in date[key]["Text"] for key in ("story", "ambition"))


def validate_partnership():
    """Check the new decision carryover, ending exclusivity and nonphysical exits."""
    nodes = {node["Id"]: node for node in PARTNERSHIP_SCENE["Nodes"]}
    for flag, target in (("home_fixed_terms", "return_owned"), ("home_taken", "return_claimed"), ("home_declined", "return_roaming")):
        state = {"devarra.trickster." + flag}
        assert [c["Next"] for c in nodes["return_choice"]["Choices"] if _allowed(c, state)] == [target]
    for key in ("return_quiet", "return_depart"):
        assert all(c["Next"] is None for c in nodes[key]["Choices"])
    assert REFUSED in nodes["return_end"]["Choices"][0]["Set"]
    assert PARTNERSHIP_DONE not in nodes["return_end"]["Choices"][0]["Set"]
    for saved in (True, False):
        history = {SAVED, SAVED_CUE} if saved else {LOST, LOST_CUE}
        endings = [history_variant(item, saved) for item in PARTNERSHIP_ENDINGS]
        for choice in ("chosen_partnership", "chosen_separate_lives"):
            state = history | {PARTNERSHIP_DONE, EAST_ACCOUNT_DONE, LAST_INVITATION_DONE, "devarra.trickster." + choice}
            assert sum(_allowed(item, state) for item in endings) == 1
            assert not any(_allowed(item, state | {REFUSED}) for item in endings)
        assert all(item["Remote"] and item.get("ContactUnit") is None for item in endings)
    # Waiting longer cannot restore the lost cart opportunity: every delayed
    # delivery starts after departure and has no capture/ledger acquisition edge.
    for saved in (True, False):
        delayed = history_variant(KILN_RETRY_SCENE, saved)
        flags = set(delayed["Requires"])
        for elapsed in (1, 24, 168):
            assert _allowed(delayed, flags) and elapsed >= delayed["DelayHours"]
            assert "The cart left when the hour ended" in delayed["Nodes"][0]["Text"]
        assert not any({KILN_SEREVIN_HELD, KILN_LEDGER_TAKEN} & set(c["Set"])
                       for node in delayed["Nodes"] for c in node["Choices"])


if __name__ == "__main__":
    import hashlib
    import json
    import re
    from pathlib import Path

    nodes, reached = validate()
    validate_history_delivery()
    validate_branch_staging()
    validate_vault_and_retry()
    validate_partnership()
    validate_eastern_consequences()
    final_visit_outcomes = validate_minimum_continuation()
    continuation_lengths = validate_continuation_paths()
    source = Path(__file__).read_bytes()
    text = re.sub(r"\{/?n\}", " ", " ".join(node["Text"] for node in nodes.values()) + " " + " ".join(choice["Text"] for node in nodes.values() for choice in node["Choices"]))
    words = re.findall(r"\b[\w'-]+\b", text)
    print(json.dumps({
        "scene": SCENE["Id"],
        "nodes": len(nodes),
        "reachable_nodes": len(reached),
        "choices": sum(len(node["Choices"]) for node in nodes.values()),
        "skill_checks": sum(bool(choice.get("Check")) for node in nodes.values() for choice in node["Choices"]),
        "distinct_words": len({word.casefold() for word in words}),
        "total_words": len(words),
        "sha256": hashlib.sha256(source).hexdigest().upper(),
        "continuation_max_words": continuation_lengths,
        "selected_completed_route_words": selected_completed_word_bounds(),
        "final_visits_verified_outcomes": final_visit_outcomes,
        "retry_scene_templates": 1,
        "unique_narrative_scenes": len(_SCENE_TEMPLATES),
        "history_guarded_delivery_scenes": len(SCENES),
    }, indent=2))
