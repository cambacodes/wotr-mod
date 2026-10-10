"""Nocticula: cloud voice-owner pass (villain-route-nocticula, design-first).

Applied last, at the end of expansion._make_expansion, after every appender and
every earlier cloud layer, so appended paragraphs move no registered index.
Text and flag-gated paragraphs only: no scene, node or choice id, choice
position, Next, Set, gate, check, cost or GuidFor changes. Every replacement
asserts the exact text it replaces and the exact number of places it lives.
Review and truth table: tools/route_packs/redesign/nocticula/cloud-review.md.

Structure fixed here (see the review, section 1):
  * S1 the partner-stance block: 24 report-register paragraphs ("Shamira's
    name remained in the court's accounts", "No answer came from the Ardent
    Dream herself") printed on 30+ epilogue and Last Call pages, re-voiced in
    place (Shamira acts from her own appetite; Nocticula from hers);
  * S2 the partner discovery copied from the letter route into the Threshold
    chain: a clerk, a dispatch, a private invitation and a broker's demand that
    the defeated chain never staged. Threshold now has its own discovery: the
    four crescents, a Harem spy in the camp, and what the shadow does to her;
  * S3 the favour named twice on one page (refused_page/inn p24 and p25 both
    read cost.shade_paid and named the chair twice, differently);
  * S4 Last Call as paperwork ("the account in your pocket", "You mark it
    beside the other claims") and a line wrong for every said-yes run ("a
    refused invitation");
  * S5 W5 pair readers on her Last Call page as first-person ledger lines
    ("cost 200 Finances: 150 and 50 respectively") and a wrong prisoner name
    (Venn for Veldran);
  * S6 promises and harem results without a reader: the crimson mark (shown /
    covered), the Commander's lodge confessions, Arueshalae's renunciation
    (respected / left disputed), Shamira's precedence, Areelu (Areelu review
    6.3);
  * canon-fix1 renames (claude-work-queue): Neris -> Nerethi, Vessa ->
    Vezhara, Mera -> Merzila, Harem of Ardent Dream -> Harem of Ardent Dreams.

Canon used (enGB): 13c0979e, b41c2c6c, f9799f60, 16243ce7, afa1bd23,
c6c5e760, e34b006d, f079f66d, 6c27d43e. Authored, no canon claim: the runner,
the burned crescents, the factor's hand, the merchant's hands, the leash.
"""
from authoring.generation_errors import OverlayMismatch, overlay_item, overlay_node, record
import re

from story_format import p

OWN = ("noct.", "nocticula.", "trickster.lastcall.account.nocticula")
RENAMES = [(r"\bNeris\b", "Nerethi"), (r"\bVessa\b", "Vezhara"), (r"\bMera\b", "Merzila"),
           (r"Harem of Ardent Dream(?!s)", "Harem of Ardent Dreams")]

RENAME_EXPECT = {
    'noct.acq.borrowed_signature': {'Nerethi': 4},
    'noct.acq.the_missing_line': {'Nerethi': 4},
    'noct.acq.the_paid_address': {'Nerethi': 18},
    'noct.acq.the_retained_copy': {'Nerethi': 1},
    'noct.after_the_lamps': {'Vezhara': 2},
    'noct.after_the_lamps.acquired.new': {'Vezhara': 2},
    'noct.after_the_lamps.acquired.prior': {'Vezhara': 2},
    'noct.after_the_lamps.acquired.refused': {'Vezhara': 2},
    'noct.bell_without_master': {'Merzila': 1},
    'noct.bell_without_master.acquired.new': {'Merzila': 1},
    'noct.bell_without_master.acquired.prior': {'Merzila': 1},
    'noct.bell_without_master.acquired.refused': {'Merzila': 1},
    'noct.demonstration.acquired.new': {'Vezhara': 4},
    'noct.demonstration.acquired.prior': {'Vezhara': 4},
    'noct.demonstration.acquired.refused': {'Vezhara': 4},
    'noct.ending_aeon.acquired.new': {'Harem of Ardent Dreams': 1},
    'noct.ending_aeon.acquired.prior': {'Harem of Ardent Dreams': 1},
    'noct.ending_aeon.acquired.refused': {'Harem of Ardent Dreams': 1},
    'noct.ending_alliance': {'Vezhara': 1},
    'noct.ending_alliance.acquired.new': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_alliance.acquired.prior': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_alliance.acquired.refused': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_ascent': {'Vezhara': 1},
    'noct.ending_ascent.acquired.new': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_ascent.acquired.prior': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_ascent.acquired.refused': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_changed.acquired.new': {'Harem of Ardent Dreams': 2},
    'noct.ending_changed.acquired.prior': {'Harem of Ardent Dreams': 2},
    'noct.ending_changed.acquired.refused': {'Harem of Ardent Dreams': 2},
    'noct.ending_company': {'Vezhara': 1},
    'noct.ending_company.acquired.new': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_company.acquired.prior': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_company.acquired.refused': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_death.acquired.new': {'Harem of Ardent Dreams': 2},
    'noct.ending_death.acquired.prior': {'Harem of Ardent Dreams': 2},
    'noct.ending_death.acquired.refused': {'Harem of Ardent Dreams': 2},
    'noct.ending_limit': {'Vezhara': 1},
    'noct.ending_limit.acquired.new': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_limit.acquired.prior': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_limit.acquired.refused': {'Harem of Ardent Dreams': 2, 'Vezhara': 1},
    'noct.ending_sacrifice.acquired.new': {'Harem of Ardent Dreams': 2},
    'noct.ending_sacrifice.acquired.prior': {'Harem of Ardent Dreams': 2},
    'noct.ending_sacrifice.acquired.refused': {'Harem of Ardent Dreams': 2},
    'noct.last_buyer.acquired.new': {'Vezhara': 3},
    'noct.last_buyer.acquired.prior': {'Vezhara': 3},
    'noct.last_buyer.acquired.refused': {'Vezhara': 3},
    'noct.no_applause': {'Merzila': 10},
    'noct.no_applause.acquired.new': {'Merzila': 5},
    'noct.no_applause.acquired.prior': {'Merzila': 5},
    'noct.no_applause.acquired.refused': {'Merzila': 5},
    'noct.return_count': {'Vezhara': 10},
    'noct.return_count.acquired.new': {'Vezhara': 11},
    'noct.return_count.acquired.prior': {'Vezhara': 11},
    'noct.return_count.acquired.refused': {'Vezhara': 11},
    'noct.uninvited_guest': {'Merzila': 3},
    'noct.uninvited_guest.acquired.new': {'Merzila': 5},
    'noct.uninvited_guest.acquired.prior': {'Merzila': 5},
    'noct.uninvited_guest.acquired.refused': {'Merzila': 5},
    'noct.voices_in_glass': {'Vezhara': 1},
    'noct.voices_in_glass.acquired.new': {'Vezhara': 1},
    'noct.voices_in_glass.acquired.prior': {'Vezhara': 1},
    'noct.voices_in_glass.acquired.refused': {'Vezhara': 1},
    'noct.what_she_keeps': {'Vezhara': 1},
    'noct.what_she_keeps.acquired.new': {'Vezhara': 2},
    'noct.what_she_keeps.acquired.prior': {'Vezhara': 2},
    'noct.what_she_keeps.acquired.refused': {'Vezhara': 2},
}

PARAS = [
    ("{n}Shamira's court remained in the Harem of Ardent Dreams. Its mistress was still Nocticula's chosen lover and would-be rival. Her place in the Midnight Isles had not passed to the Commander.{/n}",
     "{n}Shamira kept the Harem of Ardent Dreams and her place in her lady's bed. She still wanted the throne, and Nocticula still let her want it, the way one leaves a knife on the table to see who reaches for it first. The Commander changed neither appetite.{/n}", 46),
    ("{n}Shamira remained in her Harem. Nocticula had ended her claim to the royal bed. The dismissal had cost Nocticula her favorite; Shamira had kept the Harem and answered the Lady in Shadow's orders with threats of her own.{/n}",
     "{n}Shamira kept her Harem and lost her lady's bed, and never forgave the mortal who had taken it. Every year she sent the Commander a glass of the Harem's best wine, poured by her own hand and carried by a courier who stood and watched it drunk. It was never poisoned. Shamira wanted the Commander to wonder; Nocticula, who knew exactly what was in the glass, never said.{/n}", 50),
    ("{n}Shamira's court remained in the Harem of Ardent Dreams. Its mistress had closed her doors to Nocticula over the exposed affair. She was alive, separated from her former lover, and still buying intelligence about the Lady in Shadow's throne.{/n}",
     "{n}Shamira had found the affair out and barred the Harem's doors to her own lady. Nobody in Alushinyrra had ever done that and kept a head. Nocticula let her keep hers: a lover sulking behind locked doors was a lover still buying spies against the throne, and Nocticula liked knowing which spies, and liked having them flayed one at a time on the Harem's own steps, where Shamira could hear.{/n}", 46),
    ("{n}Shamira's court had its mistress back in the body the Commander earned for her. Survival had not restored her old place in Nocticula's bed or settled her claim on the throne.{/n}",
     '{n}Shamira ruled her Harem again from the body the Commander had found for her. Nocticula visited it once, walked around it as if around a statue she had not commissioned, and remarked that the hips were an improvement. She did not take it back to bed. Shamira took that as a declaration of war, and waged it beautifully.{/n}', 50),
    ("{n}Shamira's name was spoken inside the Commander's head. She remained bodiless there. Nocticula's former lover could listen there; she could neither occupy the royal bed nor sit beside its owner.{/n}",
     "{n}Shamira lived on behind the Commander's eyes, bodiless, and listened to every evening the Commander spent with her lady. She said nothing during. Afterwards she said a great deal. Nocticula, told of it, laughed until the lamps shook, and asked for the commentary to be repeated, word for word, at her table.{/n}", 50),
    ("{n}Shamira's name remained in the court's accounts. What survived of her remained captive inside the Commander. She had once shared Nocticula's bed and coveted her throne. No answer had come from the cage to the new invitation.{/n}",
     '{n}What was left of Shamira stayed caged inside the Commander, where it could neither answer nor leave. Nocticula never once asked to see her. At a window over the burning city she said, only once, that the cage suited Shamira better than the throne would have, and that she had always preferred her lovers quiet afterwards.{/n}', 50),
    ("{n}Shamira was dead. Nocticula's court still remembered the lover who had coveted the Lady in Shadow's throne. No guest could claim the Ardent Dream's agreement.{/n}",
     "{n}Shamira was dead. Her girls fought for the Harem of Ardent Dreams on its own throne steps, and Nocticula watched the fight from a balcony and bet on it, and won. She never spoke of the old mistress in the Commander's hearing, except once, to say that Shamira had died still wanting the throne, which was the only proper way for Shamira to die.{/n}", 50),
    ("{n}Shamira was dead; what had clung to the Commander had been cast back into the Abyss. The name of Nocticula's former lover remained in the court's accounts; no guest could speak for her.{/n}",
     '{n}Shamira was dead, and what had clung on inside the Commander had been thrown back into the Abyss to be eaten. Nocticula, told how, said she hoped it had been something with a very large mouth. Her court took that for mourning. It was the most mourning anybody ever got from her.{/n}', 50),
    ('{n}Shamira was dead; her last remnant had gone under. Her Harem outlasted her. Its courtiers could not claim their mistress had willingly surrendered her place beside Nocticula.{/n}',
     "{n}Shamira was dead; the last of her had gone under somewhere behind the Commander's eyes, and nobody had pulled her up. Her Harem outlived her and squabbled over her jewels. Nocticula let the squabble run as far as knives before she ended it, and kept the best of the jewels for herself.{/n}", 50),
    ("{n}The Commander did not return from the sacrifice. Shamira died again without that mind's warmth. The Harem's courtiers found the cold shell in an Alushinyrra doorway. The Ardent Dream's old place beside Nocticula remained empty.{/n}",
     '{n}The Commander did not come back from the sacrifice, and the body Shamira had been living in did not outlast its anchor by a day. Her courtiers found it in a doorway in Alushinyrra, cold, beautiful and empty. Nocticula had it carried to the palace, looked at it for a long while, and then had it thrown from the cliffs into the sea.{/n}', 50),
    ("{n}The Commander did not return from the sacrifice. The death of Shamira followed: she had still been bodiless, sheltered inside that mind. Nothing came back to her Harem. The Ardent Dream's old place beside Nocticula remained empty.{/n}",
     "{n}The Commander did not come back from the sacrifice, and Shamira, still bodiless inside that mind, went down with it. Nothing came back to her Harem: no body to burn, no ghost to bargain with. Nocticula let the Harem's girls fight over the name for a season, and did not stop the fighting.{/n}", 50),
    ("{n}The Commander had chosen to share Nocticula's company. Shamira's name remained part of that bargain, with her answer where she could still give one; no claim on the Midnight Isles came with it.{/n}",
     '{n}The Commander had agreed to share her. Nocticula took the Commander when she pleased, and whoever else she pleased, and never once pretended otherwise. A lover who did not ask her to pretend was, she said, the rarest thing in the Abyss, and she said it in bed often enough to be believed.{/n}', 50),
    ("{n}Nocticula had chosen the Commander alone as her lover. She had bound that promise to the work the Commander already owed her, and dismissed Shamira from her bed. She had asked for the Commander's time and service, and given no claim on her throne.{/n}",
     "{n}Nocticula kept her promise: no other lover in her bed for as long as she chose to keep it. She kept it the way she kept everything, jealously and expensively, and made the Commander pay for it in work: a broker silenced here, a rival's secret fetched there, a sentence pronounced at her trials and watched to the end. Every one of them, she said, came cheaper than Shamira had.{/n}", 50),
    ('{n}The Commander had demanded exclusivity. Nocticula refused the claim. Her bed and her throne remained hers to dispose of.{/n}',
     "{n}The Commander had asked to be the only one. Nocticula had said no and meant it, and the Commander had stayed anyway. She never let the Commander forget either fact. There were other lovers; she made sure the Commander met some of them, and watched the Commander's face while they were introduced.{/n}", 46),
    ('{n}The Commander had asked for a secret affair. Its private invitations were evidence in a court that sold pillow talk.{/n}',
     "{n}The affair was kept secret, which in Alushinyrra only ever meant that nobody had yet been paid enough to tell. Nocticula enjoyed that enormously. She took the Commander to bed in rooms Shamira's spies had been allowed to search and find empty, and left her marks where only the Commander would see them.{/n}", 50),
    ("{n}The secret affair had been exposed through Nocticula's invitations. Nocticula withdrew the private letters. Future visits came at her summons, with the slight still remembered.{/n}",
     "{n}The secret had come out, as she had warned it would, and she had not hidden behind the Commander's lie. Afterwards the Commander came only when summoned, at hours of her choosing, and waited in her antechamber among the petitioners while the court watched. She called it the price of discretion, and never once let the Commander pay it in private.{/n}", 46),
    ("{n}No new arrangement concerning Shamira's name had been concluded. Nocticula's interest in the Commander did not erase her lover or settle their struggle for the throne.{/n}",
     "{n}Nothing was ever agreed about Shamira, alive or otherwise. Nocticula did not consider her lovers the Commander's business, and the Commander was never told which nights belonged to whom.{/n}", 50),
    ('{n}Shamira\'s old letter of refusal was nailed to the Harem\'s doors: "Let her keep the mortal. Nocticula comes here at my invitation now." The royal bed had lost its old favorite; the royal throne still had her attention.{/n}',
     '{n}Shamira nailed her answer to the doors of the Harem in her own hand, where the whole city could read it: "Let her keep the mortal. My lady comes here now at my invitation, or not at all." Nocticula read it on her way past, laughed, and had the servant who had sold Shamira the affair nailed up beside it, alive, for the rest of the season.{/n}', 50),
    ('{n}Shamira\'s old letter of refusal was nailed to the Harem\'s doors: "Let her keep the mortal. Nocticula comes here at my invitation now." Survival had not reconciled the two queens. The court no longer accepted Nocticula\'s private messages.{/n}',
     '{n}Shamira, in her new body, nailed her answer to the doors of the Harem where the whole city could read it: "Let her keep the mortal. My lady comes here now at my invitation, or not at all." It was the first thing she wrote with the new hand. Nocticula had the servant who had sold her the affair nailed up beside it, and sent Shamira his tongue by way of reply.{/n}', 50),
    ('{n}Shamira\'s name preceded a threat heard inside the Commander\'s head: "I shall remember every word she whispers here." She kept her threat. Nocticula had lost a lover and acquired a listener she could not dismiss.{/n}',
     "{n}Shamira, behind the Commander's eyes, made good on her threat: she remembered every word Nocticula whispered there and repeated them, at the worst moments, in the Commander's own head. Nocticula had lost a lover and gained an audience she could not throw out. She decided, after some thought, that she liked performing for it.{/n}", 46),
    ("{n}The courtiers in Shamira's court sold copies of the exposed invitation. No answer came from the Ardent Dream herself.{/n}",
     "{n}Shamira's courtiers sold the story of the affair to anyone with coin, since their mistress could no longer stop them. Nocticula bought it back from each seller, once, in person. None of the sellers was seen again.{/n}", 200),
    ("{n}Her next sealed note named the favour bought at Threshold: a chair at the Commander's right hand when matters of state were heard. The chair was provided. The Lady in Shadow had bought that place with protection; she had not bought a lover. The refusal stood.{/n}",
     "{n}She named the favour bought at Threshold in the second spring after it, in person: she walked into the Commander's council unannounced, in the middle of a general's sentence, and took the chair at the Commander's right hand. That was the favour. Nobody at the table dared ask who she was, and she did not offer.{/n}", 2),
    ('{n}The next spring a sealed note found the Commander: "My favour. A chair at your right hand, wherever you eat. I did not ask for your bed." The Commander set it there. Nocticula came to dinner, looked once at the empty place beside her debtor, and sat down. She returned the following month without asking whether the refusal had changed.{/n}',
     '{n}After that she came to dinner as well, uninvited, and sat in the same place. Once she looked through two open doors at the bed the Commander had refused her, smiled, and went back to her plate. She came again the next month without asking whether the refusal had changed. She was owed a chair, not a bed, and she made the Commander feel the difference at every meal.{/n}', 2),
    ('{n}The war ended at Threshold; the Commander later stepped away from her chair. Nocticula remembered the refusal. Her accounts survived it; the place beside her stayed empty.{/n}',
     '{n}The Commander had answered her before Threshold, and then walked away from her chair anyway. Nocticula remembered both. She kept the place beside her empty, and was seen to keep it empty, so that every courtier in Alushinyrra knew exactly who had refused her.{/n}', 1),
    ('{n}The next invitation came back bearing another seal. Shamira\'s old letter of refusal was enclosed: "I know how she marks a lover. She may keep you. My Harem is closed to her." Nocticula withdrew the private letters. The Commander would come at her summons, with an insult waiting on either side of the royal bed.{/n}',
     '{n}The secret lasted exactly as long as it took Shamira to stand close to the Commander at a crowded table, breathe in, and smile. "I know how she marks a lover," she said, loud enough for the table. "I have worn it. Keep her, mortal; my Harem is closed to her." Nocticula, told of it, laughed, and made the Commander come to her bed through the front of the palace ever after, at her summons, past every courtier who had heard.{/n}', 6),
    ('{n}Shamira\'s name preceded a voice heard inside the Commander\'s head at dawn: "You hid her from me? Here? I shall remember every word she whispers." Nocticula withdrew the private letters when the Commander repeated it. Their next meeting came at her summons; the listener never left.{/n}',
     '{n}Shamira, living behind the Commander\'s eyes, woke one dawn into the memory of the night and said, very quietly, "You hid her from me? In here?" She never let it go. Every word Nocticula whispered afterwards, Shamira whispered back a breath later in the same voice. When the Commander finally confessed it, Nocticula stopped sending for the Commander in private and summoned instead, at hours of her choosing, to watch the Commander\'s face while two queens talked in one skull.{/n}', 3),
    ("{n}Shamira's court sent back the next invitation with an offer to sell its copies. No answer came from the Ardent Dream herself. Nocticula withdrew the private letters. The Commander would come at her summons; the court kept the evidence.{/n}",
     "{n}Shamira's courtiers found the affair out in the end, as courtiers do, and offered to sell their silence to both lovers at once. Nocticula paid them in person, at the Harem, and nobody there offered to sell her anything again. After that she trusted no private hours: the Commander came at her summons, through the front doors, where everyone could see.{/n}", 12),
    ('{n}The last call of the war had left an answer between them. Nocticula received it in her own chair, after the Commander crossed the room. She kept that place beside her occupied on the evenings she chose; the Commander had finally taken it.{/n}',
     '{n}The Commander had answered her before Threshold, and she had not forgotten the sound of her own name said that way. She never mentioned it. She simply kept the Commander, on the evenings she chose, in the chair beside hers, and let the court work out the rest.{/n}', 2),
    ("{n}The Queen's unsigned breakfast note followed the Commander back to the inn. Threshold had left them business; leaving her room had promised her no nights.{/n}",
     '{n}The Commander had answered her before Threshold; walking out of her room afterwards bought nothing back. The next night every other guest at the inn woke screaming from the same dream, and in the morning the innkeeper asked the Commander, very politely, to find other lodgings.{/n}', 1),
    ("{n}Shamira's court remained in the Harem of Ardent Dreams. Its mistress had been Nocticula's chosen lover and would-be rival. After Nocticula's death, the Harem shut its doors to mourners. Its courtiers began buying reports from the other islands.{/n}",
     '{n}Shamira kept the Harem of Ardent Dreams. When word came that her lady was dead she shut its doors to mourners, sat down on the steps of the throne she had always wanted, and did not get up again until the other islands had stopped sending knives.{/n}', 4),
    ("{n}Shamira's court remained in the Harem of Ardent Dreams. Before Nocticula's death, its mistress had closed her doors to her former lover over the exposed affair. The courtiers kept their copies of the invitations and began buying reports from the other islands.{/n}",
     '{n}Shamira had found the affair out before the end and barred the Harem to her own lady. When Nocticula died, the doors were still barred. Shamira kept the copies of the invitations her spies had stolen, and read them aloud to her court on the anniversary, every year, in a voice nobody dared laugh at.{/n}', 4),
    ('{n}The Commander had demanded exclusivity. Nocticula refused the claim. Until her death, she had kept her own choice of lovers.{/n}',
     '{n}The Commander had asked to be the only one, and Nocticula had said no. She kept her other lovers until the day she died, and made sure the Commander met some of them.{/n}', 4),
    ("{n}The secret affair had been exposed through Nocticula's invitations. She had withdrawn the private letters and summoned the Commander on her own terms. Her death ended those invitations too; copies of the old ones remained in the courtiers' hands.{/n}",
     "{n}The secret had come out before the end, and she had never hidden behind the Commander's lie. After it, the Commander came only at her summons, and waited among her petitioners. Her death ended the summonses. It did not end the stories the court told about them.{/n}", 4),
    ('{n}Shamira\'s name preceded a threat heard inside the Commander\'s head: "I shall remember every word she whispers here." She had kept her threat while Nocticula lived. After the Lady\'s death, she still asked the Commander to recall the last invitation.{/n}',
     "{n}Shamira, behind the Commander's eyes, kept her threat: she remembered every word Nocticula had whispered there. After the Lady in Shadow died she went on repeating them, in the dark, in that voice, whenever the Commander was nearly asleep.{/n}", 4),
    ("{n}In the lost history, Shamira had been Nocticula's chosen lover in the Harem of Ardent Dreams. The Commander's demands, bargains and secret invitations belonged to that erased court; none settled her place in the remade world.{/n}",
     "{n}In the lost history Shamira had been Nocticula's chosen lover in the Harem of Ardent Dreams, and had wanted her throne. In the remade one she still did. Whatever the Commander had demanded, bargained or hidden there belonged to a court that had never happened.{/n}", 4),
    ("{n}The agreement to share Nocticula's company had been erased with those evenings.{/n}",
     '{n}The evenings the Commander had agreed to share had never happened, and nobody in the remade Alushinyrra remembered being shared.{/n}', 4),
    ('{n}The demand that Nocticula abandon Shamira had never been spoken in this history.{/n}',
     '{n}In the remade history nobody had ever asked Nocticula to put Shamira out of her bed, and Shamira slept in it undisturbed.{/n}', 4),
    ("{n}The secret invitations were gone. Shamira's court had no copies to sell.{/n}",
     "{n}The secret affair had never happened, so there was nothing for Shamira's spies to find. They went on looking anyway. It was what they were for.{/n}", 4),
]
# These ending histories are appended by the household registrar.
HAREM_PARAS = [
    ('{n}The levy was countermanded. I burned the survey and recalled my sortie.{/n}',
     "{n}Her factor, who had sold her protection twice, was not seen in the Fleshmarket again. The pilot's survey burned in Drezen and the scouts went home. The wounded crossed for nothing, which Galfrey called justice and Nocticula called a very good joke on her factor.{/n}", 2),
    ("{n}My trimmed demand left the queen's levy over the passage.{/n}",
     "{n}The levy stood, because the Commander had trimmed the factor's demand until it read as hers. The wounded paid it or stayed in the Midnight Isles. Nocticula did not mind in the least: the money reached her either way.{/n}", 2),
    ('{n}I carried the full demand separately; both women then kept their undertaking.{/n}',
     "{n}The Commander had carried the factor's whole demand, every word, to both queens, and both had kept their word. Neither ever thanked the other, and each was heard to say the other had been made to look a fool.{/n}", 2),
    ('{n}I sent her an insult instead of an undertaking.{/n}',
     '{n}The Commander had once sent her an undertaking with her title stripped off it. She never forgot. Years later she still addressed the Commander, in company, by no title at all.{/n}', 2),
    ('{n}I hid reconnaissance inside the passage undertaking.{/n}',
     '{n}The Commander had tried to slip a scout in among the wounded. Nocticula closed that passage and never reopened it, and when it came up afterwards she would only say that she had expected a better lie, and look at the Commander until the subject went away.{/n}', 2),
    ('{n}I let her factor keep the levy.{/n}',
     '{n}The Commander had let the factor keep his levy. He grew fat on it for a season. Then Nocticula heard whose protection he had been selling, and he grew thin very quickly.{/n}', 2),
    ("{n}Two courier fares and the pilot's survey cost 200 Finances: 150 and 50 respectively.{/n}",
     "{n}The crusade paid two hundred crowns for the couriers and the pilot's survey, which Galfrey counted out without comment. Nobody in Drezen ever got used to paying a demon's ferryman.{/n}", 2),
    ('{n}I put my own name on the undertaking.{/n}',
     "{n}The Commander's own name had stood guarantor for that passage, and Nocticula remembered it, the way she remembered every name ever pledged to her.{/n}", 2),
    ("{n}The orderly's claimed sponsorship of the reconnaissance was publicly withdrawn.{/n}",
     "{n}Galfrey's orderly never lived down the morning his queen revoked his sortie in front of her officers.{/n}", 2),
    ('{n}Nocticula stripped her protected factor of collection on this passage and forfeited his levy.{/n}',
     "{n}Nocticula took the factor's levy from him in front of his own clerks, and then took the hand he had collected it with.{/n}", 2),
    ("{n}I answered the factor's public accusation in my own name.{/n}",
     '{n}The factor had named the Commander a meddler in public, and the Commander had answered him in public, by name. He did not get the chance to answer back.{/n}', 2),
    ('{n}The only acquired survey was burned; the mustered sortie was recalled without a replacement scout.{/n}',
     "{n}The only survey of her harbour the crusade ever had went into a fire in Drezen. The Commander's scouts never got another look.{/n}", 2),
    ('{n}My omitted clause prolonged the levy. Both women held me answerable.{/n}',
     "{n}The clause the Commander had cut from the factor's demand kept the wounded waiting a season longer. Galfrey and Nocticula agreed on exactly one thing in their lives: whose fault that was.{/n}", 2),
    ("{n}The exposed scout lost this passage's innocent cover.{/n}",
     '{n}After the hidden scout, nobody in the Midnight Isles ever again believed that a crusader ship carried only the wounded.{/n}', 2),
    ('{n}The independent interpreter cost another 300 Finances.{/n}',
     "{n}The interpreter cost another three hundred crowns and was worth every one: he read the factor's demand aloud to its last clause, and the factor never forgave him either.{/n}", 2),
    ('{n}A fresh courier and independent attestation cost another 400 Finances.{/n}',
     "{n}Carrying the factor's whole demand cost another four hundred crowns in couriers and witnesses. Nocticula said it was the most expensive honesty anyone had ever sent her, and laughed at the price.{/n}", 2),
    ('{n}Nocticula\'s reply dwells on the burnt survey.{/n} "She withdrew her sponsorship before her own people. You surrendered something useful. My factor merely surrendered something that was never his to demand. I trust he remembers the difference."',
     '{n}Nocticula gave her verdict on the business at her own table, to the Commander, with her factor standing behind her chair to pour. He poured left-handed now.{/n} "She withdrew her sponsorship in front of her own people. You burned something useful. My factor surrendered something that was never his to sell. He remembers the difference every time he reaches for a cup."', 2),
    ('{n}Nocticula sends a recollection of her broker\'s loss. "The goddess named me. He paid for the privilege of hearing it. I found both quite satisfactory."{/n}',
     '{n}Nocticula told the story of the six names at her table for years, always the same way.{/n} "The goddess named me, in her own sanctuary, as the one who set them free. My broker paid for the privilege of hearing it, first in men and then in skin. I found both quite satisfactory."', 2),
    ('{n}Two names still lacked their men after my failed inspection.{/n}',
     "{n}Veldran and Rul stayed in the broker's cages because the Commander had not looked closely enough at a wagon. Iomedae kept their places at the sanctuary empty, and let the Commander see them empty.{/n}", 2),
    ('{n}I retrieved Veldran and Rul after the failed reception.{/n}',
     "{n}The Commander went through the crossing for Veldran and Rul in person, and carried Rul out of the broker's cage with his splint cut into the bone.{/n}", 2),
    ('{n}I asked for a gesture instead of the men.{/n}',
     "{n}The Commander had wanted a gesture instead of six men, and Iomedae had refused to send the request. The six stayed in the broker's cages. Nocticula never learned how close she had come to being asked for something cheap; she would have been insulted.{/n}", 2),
    ('{n}She refused my false count.{/n}',
     "{n}Iomedae had refused the Commander's false count at the wagon. Nocticula, told of it, laughed for a long time: a mortal who would lie to a goddess about her own prisoners was, she said, very nearly worth keeping.{/n}", 2),
    ("{n}Two remained in the slaver's claim when I abandoned their retrieval.{/n}",
     "{n}Veldran and Rul stayed in the broker's cages; four was enough, the Commander had said. The broker sold the other two at the Fleshmarket that winter, and Nocticula took her cut.{/n}", 2),
    ('{n}I paid two hundred for the courier and receiving transport.{/n}',
     "{n}The crossing and the receiving wagon cost the crusade two hundred crowns, paid in the Commander's name to a demon's broker. Iomedae did not look at the purse while it changed hands.{/n}", 2),
    ('{n}I undertook to meet the last prisoner myself.{/n}',
     '{n}The Commander had promised a goddess to meet the last prisoner in person, and Iomedae held the Commander to it.{/n}', 2),
    ("{n}Iomedae named Nocticula's release order without excusing her market.{/n}",
     "{n}Iomedae said Nocticula's name aloud in her own sanctuary as the one who had ordered six men freed, and in the same breath called her markets an abomination. Nocticula had both sentences repeated to her twice.{/n}", 2),
    ("{n}Iomedae assigned the sanctuary's watch to the six rescued crusaders.{/n}",
     "{n}The six men Nocticula's broker had sold stood watch at Iomedae's sanctuary for the rest of their lives, Rul on his bad leg.{/n}", 2),
    ("{n}Nocticula surrendered the broker's protection payment and stripped him of six men's resale value.{/n}",
     "{n}Nocticula gave the broker back his protection money and took the six men's price out of him instead. Her court bet on how long he would last without her protection. He lasted nine days.{/n}", 2),
    ("{n}I carried Rul into care and missed the evening's court entertainment.{/n}",
     "{n}The Commander carried Rul into the sanctuary with his bandage soaking through, and left Nocticula's invitation to the court's entertainment unopened on the wagon. She noticed. She mentioned it, at intervals, for years.{/n}", 2),
    ('{n}My failed inspection delayed the reception; Veldran and Rul remained captive.{/n}',
     "{n}Because the Commander had not checked the wagon, Veldran and Rul spent another month in the broker's cages, and Rul's leg set crooked in one.{/n}", 2),
    ('{n}The inspected ransom cost five hundred.{/n}',
     '{n}Five hundred crowns went to the broker for six living men, counted at the wagon. Nocticula took the five hundred back from him later, with interest she did not count in coin.{/n}', 2),
    ('{n}The correction cost seven hundred for the inspected crossing.{/n}',
     "{n}The broker's price for the last two men had risen to seven hundred, and the crusade paid it. He did not live to spend it.{/n}", 2),
]
CORRESPONDENCE_PARAS = [
    ('{n}Her renewed Gift remained a separate bargain. The half-seal still carried requests; it did not open the palace doors. She kept the signed undertaking beside the next unanswered letter.{/n}',
     "{n}Her renewed Gift sat in the Commander's head the whole time, and she used it: whole nights when the Commander sat at a desk in Golarion and felt her reading over the shoulder from the inside. The half-seal was for the things she wanted said aloud.{/n}", 4),
    ('{n}The earlier Gift remained what it had been. Their correspondence had paid none of its debts. She retained the undertaking and answered the next request through the narrow mark.{/n}',
     "{n}The old Gift still held. She read the Commander's thoughts when the mood took her and laughed out loud at the parts the Commander had meant to keep, sometimes in a letter and sometimes in company. The letters never paid down anything the Gift was owed.{/n}", 4),
    ('{n}No Gift came through the correspondence. The half-seal cooled without joining its missing half. The Commander still had to ask, and Nocticula still kept the signed undertaking.{/n}',
     '{n}There was no Gift between them, only the half-seal, and it never joined its other half. Everything the Commander wanted from her had to be asked for in ink, and she made sure the Commander knew how much the asking amused her.{/n}', 4),
    ('{n}She had kept the surrendered sketch out of the correspondence. None of the subsequent invitations carried another copy of the exposed aperture.{/n}',
     '{n}She kept the sketch of the failed opening the Commander had surrendered, pinned above her bed in Alushinyrra, and showed it to guests who thought themselves clever.{/n}', 4),
]

NODES = [
    (('nocticula.trickster.defeated.',),
     '{n}The clerk has put the morning dispatch on top of your private packet. Beneath it, Nocticula\'s seal carries a second impression, burned deep into the wax. Her answering mark stops when your fingers uncover it.{/n} "Your private invitation has acquired an answer. Read it before you send another."',
     '{n}A runner you do not recognise is waiting by your tent when you come out: too pretty for this camp, and too clean, with eyes that go straight to the edge of your collar where the four crescents show. She smiles as if she has been paid to, and she has.{/n} "A message for the Commander, from the Harem of Ardent Dreams. Shall I say it here, where your soldiers can hear?"', 5),
    (('noct.',),
     '{n}The clerk has put the morning dispatch on top of your private packet. Beneath it, Nocticula\'s seal carries a second impression, burned deep into the wax. Her answering mark stops when your fingers uncover it.{/n} "Your private invitation has acquired an answer. Read it before you send another."',
     "{n}The clerk has laid the morning dispatch on top of your private packet. Beneath it, the wax carries a second seal pressed over Nocticula's, scorched black at the edges and smelling of cinnamon. Somebody has opened your invitation, read it, and sent it home.{/n}", 5),
    (('nocticula.trickster.defeated.',),
     '{n}A scrap of Nocticula\'s invitation has come back with another seal burned across it.{/n} "I know that hand, mortal. I know what she writes when she wants someone in her bed. Let her keep you. My Harem is closed to her tonight. She may send an assassin if she wants an audience."',
     '{n}The runner recites it in a voice that is not her own, a voice you last heard in Alushinyrra, sweet as poisoned wine.{/n} "I know that mark, mortal. I have worn it. Let her keep you, then; my Harem is closed to her. If she wants an audience she may send an assassin, and I shall send her back whatever is left of it."', 10),
    (('noct.',),
     '{n}A scrap of Nocticula\'s invitation has come back with another seal burned across it.{/n} "I know that hand, mortal. I know what she writes when she wants someone in her bed. Let her keep you. My Harem is closed to her tonight. She may send an assassin if she wants an audience."',
     '{n}Across the back of the invitation, in a sharp hand driven through the paper:{/n} "I know that hand, mortal. I have had it on my skin. Let her keep you, then; my Harem is closed to her. If she wants an audience she may send an assassin, and I shall send her back whatever is left of it."', 10),
    (('nocticula.trickster.defeated.',),
     '{n}Inside your mind, the voice catches the memory of Nocticula\'s invitation as you wake. Her voice burns behind your eyes.{/n} "You hid her from me? In my own lodging? Keep your little affair. I shall remember every word she whispers here. Tell her that."',
     '{n}Before the runner can open her mouth, the voice behind your eyes does it for her. It woke with you and found the night still there, warm, where you left it.{/n} "You hid her from me? In here, in the head I live in? Keep your little affair. I shall remember every word she whispers here. Tell her that."', 5),
    (('noct.',),
     '{n}Inside your mind, the voice catches the memory of Nocticula\'s invitation as you wake. Her voice burns behind your eyes.{/n} "You hid her from me? In my own lodging? Keep your little affair. I shall remember every word she whispers here. Tell her that."',
     '{n}Before you can break the second seal, the voice behind your eyes has already read it. It woke with you and found the night still there, warm, where you left it.{/n} "You hid her from me? In here, in the head I live in? Keep your little affair. I shall remember every word she whispers here. Tell her that."', 5),
    (('nocticula.trickster.defeated.',),
     '{n}The answering message comes from Shamira\'s court, where her courtiers still trade in her name. The captive behind your eyes cannot answer it.{/n} "The Lady\'s invitations have found another bed. The court thanks you for the intelligence."',
     '{n}The runner does not pretend the message comes from her mistress; her mistress is caged behind your eyes and cannot send anything. Her courtiers can.{/n} "The Harem\'s compliments, Commander. The Lady\'s marks have been seen on a crusader\'s shoulder. The court thanks you for the news, and has already sold it twice."', 5),
    (('noct.',),
     '{n}The answering message comes from Shamira\'s court, where her courtiers still trade in her name. The captive behind your eyes cannot answer it.{/n} "The Lady\'s invitations have found another bed. The court thanks you for the intelligence."',
     '{n}The second seal is the Harem\'s, not Shamira\'s; Shamira is caged behind your eyes and cannot answer anything. Her courtiers can.{/n} "The Harem\'s compliments. The Lady\'s invitations have found another bed. The court thanks you for the news, and has already sold it twice."', 5),
    (('nocticula.trickster.defeated.',),
     '{n}The answering message comes from Shamira\'s court. Her surviving courtiers have copied the private invitation; their mistress is dead.{/n} "The Lady\'s invitations have found another bed. The court thanks you for the intelligence."',
     '{n}The runner does not pretend the message comes from her mistress; her mistress is past sending messages. Her courtiers are not.{/n} "The Harem\'s compliments, Commander. The Lady\'s marks have been seen on a crusader\'s shoulder. The court thanks you for the news, and has already sold it twice."', 15),
    (('noct.',),
     '{n}The answering message comes from Shamira\'s court. Her surviving courtiers have copied the private invitation; their mistress is dead.{/n} "The Lady\'s invitations have found another bed. The court thanks you for the intelligence."',
     '{n}The second seal is the Harem\'s. Its mistress is past answering anything; her courtiers are not, and they copied your invitation before they sent it back.{/n} "The Harem\'s compliments. The Lady\'s invitations have found another bed. The court thanks you for the news, and has already sold it twice."', 15),
    (('nocticula.trickster.defeated.',),
     '''"So much for discretion. No more letters beyond the business already agreed. When I want your company, I shall summon you. You may arrive, or let me wonder whose door you used instead."
{n}Her mark strikes out the invitation, then moves onto the war dispatch beside it. She corrects the broker's demand in three strokes.{/n}
"That business proceeds. The next private letter does not."''',
     '{n}Your shadow lengthens across the trodden ground toward the runner, further than the fire allows, and the runner stops smiling.{/n} "So much for discretion," {n}says the shadow, in Nocticula\'s voice.{/n} "I told you I would not hide behind your lie, and I shan\'t. From now on you come when I summon you and not before, and you wait in my antechamber among the petitioners while my court watches you wait." {n}The runner is backing away. The shadow lets her reach the edge of the camp before it closes over her. There is a scream, then nothing, then a smell like burnt cinnamon.{/n} "She sold you to Shamira\'s court. I do not like my things sold."', 5),
    (('noct.',),
     '''"So much for discretion. No more letters beyond the business already agreed. When I want your company, I shall summon you. You may arrive, or let me wonder whose door you used instead."
{n}Her mark strikes out the invitation, then moves onto the war dispatch beside it. She corrects the broker's demand in three strokes.{/n}
"That business proceeds. The next private letter does not."''',
     '"So much for discretion." {n}Her mark scores through the invitation hard enough to tear the paper.{/n} "I told you I would not hide behind your lie, and I shan\'t. From now on you come when I summon you and not before, and you wait in my antechamber among the petitioners while my court watches you wait. The servant who carried your letter to the Harem is being skinned while you read this. I thought you should know the hour." {n}The mark moves to the war dispatch beside it and lies still.{/n} "Our business goes on. The private letters do not."', 5),
    (('nocticula.trickster.defeated.',),
     '''{n}A hand knocks at the door. The clerk asks for the next dispatch; its corner lies beneath the private invitation. You draw the dispatch free and hold the invitation to the lamp. It curls in the flame before the clerk enters. No seal leaves the room; no marked gift goes to the Harem.{/n}
"You would have enjoyed keeping that," {n}Nocticula writes on the answering scrap.{/n} "Burn this too. You may come when I summon you. You may not keep a pretty collection for her servants to buy."
{n}You feed the last scrap to the flame. There is nothing for the courier to carry.{/n}''',
     '''{n}The four crescents on your shoulder are the only thing she has given you, and they are a marked gift. On the way to the horse lines you heat a knife in a smith's brazier and lay the flat of it over them until they are a burn and nothing else. A runner who is too pretty for this camp watches you do it, finds nothing left worth selling, and goes.{/n}
"You would have enjoyed keeping those," {n}says your shadow, in a voice only you can hear.{/n} "Burned clean. Good. Come when I summon you, and do not keep a pretty collection for her servants to buy."''', 5),
    (('noct.', 'nocticula.'),
     '''{n}Nocticula lays out Shamira's old letter: terms for another lover, answered before she invited you. The hand is sharp, the seal scorched.{/n}
"Another amusement? Keep the mortal away from my throne. When you tire of crusade reports, you know where I am."''',
     '''{n}Nocticula lays out a letter from Shamira, answered before you were ever invited: the hand sharp, the seal scorched, the paper smelling of cinnamon.{/n}
"Another pet, my lady? Keep it, then. Feed it, walk it, let it sleep at the foot of your bed. Only keep it away from your throne, because one day that chair is mine, and I do not share my furniture."''', 67),
    (('noct.', 'nocticula.'),
     '''{n}Nocticula lays out Shamira's old letter, written after her return to the Harem. It bears the Ardent Dream's seal, not an invitation back to Nocticula's bed.{/n}
"Your bed is yours. My Harem is mine. Send your mortal if you want an answer; I would enjoy finding out what else you have told them."''',
     '''{n}Nocticula lays out the letter Shamira wrote after her return to the Harem in her new body. It bears the Ardent Dream's own seal, and no request to come back to Nocticula's bed.{/n}
"Keep your mortal, my lady. My Harem is mine, and so, one day, is your chair. Send the creature to me if you want my answer in person; I should like to see what it looks like with its armour off."''', 67),
    (('nocticula.lastcall.call',),
     "{n}The Lady in Shadow's claim survives a refused invitation. Her mark lies on the account in your pocket; no promise of a night together appears beside it. You read the debt aloud.{/n}",
     '''{n}The night before Threshold you stand with your back to the fire, so that your shadow falls long across the trodden ground, and you say her name into it.{/n}
{n}For a moment it is only a shadow. Then it lies a little longer than the fire allows.{/n} "Calling in your debts before the Wound, clown? How tidy of you. I am not a debt. I am the one who is owed." {n}A cold mouth touches the back of your neck, though nobody stands behind you.{/n} "The favour stands. I will name it when it hurts most to pay, and you will be alive to pay it, because I have decided so. Now go down there and close that hole. I want my favour paid by someone with a pulse."''', 1),
    (('trickster.lastcall.account.nocticula',),
     "{n}The Lady in Shadow's ledger still lists the price you pledged for protection: one favour, hers to name. A refused invitation did not cancel it. You mark it beside the other claims that will survive Threshold. No answer from her is needed to keep that entry.{/n}",
     '{n}You do not call her. Behind you your shadow lies a little longer than the firelight allows, and you leave it lying there. The favour you owe the Lady in Shadow is not yours to settle by remembering it: it is hers to name, at the worst possible hour, and she has never yet chosen a convenient one.{/n}', 1),
    (('noct.acq.epilogue.correspondence',),
     '''"You have spent enough nights imagining my room. Come and inspect the error. One visit. Leave the undertaking where I can find it."
{n}The half-seal carried a date and the name of an Alushinyrra landing court. The Commander obtained a conjurer's price for passage and return, and set the offer beside Nocticula's invitation.{/n}''',
     '''"You have spent enough nights imagining my room. Come and see how wrong you were. One visit. Bring the undertaking; I want to watch you not ask for it back."
{n}The half-seal burned a name into the desk: a landing court in Alushinyrra, and a night. A conjurer in Drezen named his price for the crossing and the way back, and did not ask whose door it was.{/n}''', 1),
    (('noct.acq.epilogue.correspondence',),
     '''{n}The Commander paid the conjurer for passage and return before leaving Golarion. The spell delivered them to the named court. A doorkeeper took the invitation inside. The Commander waited while the return papers grew damp in the night air. At last the doors opened. Nocticula stood beyond them, with the retained signature in her hand.{/n}
"I considered leaving you outside. Come in. I want to hear how you would have described the wait."''',
     '''{n}The conjurer's spell put the Commander down in the landing court at dusk, among succubi who looked the Commander over like a cut of meat and then, seeing the mark of the wax, decided not to. The doors stayed shut for an hour. Then they opened, and Nocticula stood beyond them with the Commander's signed undertaking in her hand, turning it over like a card she had won.{/n}
"I considered leaving you outside. Come in. I want to hear how you would have described the wait."''', 1),
    (('noct.acq.epilogue.correspondence',),
     '''{n}At dawn she was still there, reading a broker's appeal over the Commander's shoulder. She crossed out his proposed fee, kissed the bare shoulder beneath her hand, and returned the travel papers.{/n}
"Go. Ask for the next visit through the mark. I may make you wait longer."''',
     '''{n}At dawn she was still there, one leg thrown across the Commander's, reading a petition aloud: a broker in the Middle City begging her pardon for something. She laughed at the third line, told the Commander in detail what she would do to him, and did not let the Commander go until the conjurer's spell was nearly spent.{/n}
"Go. Ask for the next visit through the mark. I may make you wait longer."''', 1),
    (('nocticula.acquisition.lastcall.page',),
     '{n}After the war, the half-seal moved while the Commander was putting away the travel accounts. "Alive, then. Send me something worth my evening." The Commander wrote back. By midnight Nocticula had corrected one figure and left a second page for a private answer. The dispatch waited until morning.{/n}',
     '{n}The half-seal moved on the first night after the war, while the Commander was still washing the Wound off. "Alive, then. Send me something worth my evening." The Commander wrote back. By midnight her answer had become a second page, and the second page had become the kind of letter the Commander burned at dawn, after reading it twice.{/n}', 1),
    (('noct.acq.',),
     '''{n}The next paper to arrive at your desk bears your title twice. Once in the address, once beneath a promise you did not make.
An itinerant broker named Salven offers safe passage for letters to the Lady in Shadow. He has sent a sample of his guarantee to Drezen's clerks, hoping to sell the privilege to people with more money than sense. The sample promises that the Commander will intercede if a message displeases its recipient. Beneath that promise he claims the protection of the Council whose business brought you to her.
Your clerk Nerethi has held it back from the incoming petitioners. She asks whether the seal is yours.
It resembles the outward face of the divided wax. The central line is wrong. Somebody has seen enough of a request to sell an imitation, and too little to make one answer.
You lay the false guarantee beside your own half. When Nocticula's answering stroke appears, you copy Salven's wording onto the permitted sheet. You do not place the unfamiliar seal against hers.{/n}
"If you are selling introductions," {n}she writes,{/n} "I expect a better description. This makes me sound like an office with inconvenient hours."
"Would you prefer expensive ones?"
"I would prefer the money. Why have you sent me an advertisement instead?"
"Because he is selling your brother's promise of access with my name underneath it. I want to discover who buys it before somebody takes a false invitation seriously."
"My brother's actual invitations have been quite troublesome enough. Show me this improvement."''',
     '''{n}The next paper to reach your desk bears your title twice: once in the address, once beneath a promise you never made.
An itinerant broker named Salven is selling safe passage for letters to the Lady in Shadow. He has sent a sample of his guarantee to Drezen's clerks, fishing for buyers with more money than sense. It promises that the Knight Commander will intercede if a message displeases its recipient, and it claims the protection of the Council whose business brought you to her.
Your clerk Nerethi held it back from the petitioners' table. She asks whether the seal is yours.
It is a copy of the outer face of the divided wax, and the central line is wrong. Somebody has seen enough of your packet to sell an imitation, and too little to make one answer.
You lay the forgery beside your own half. When Nocticula's mark wakes, you copy Salven's wording onto the sheet for her, word for word.{/n}
"Someone is selling me," {n}she writes, and the mark presses so hard that the paper smokes.{/n} "Badly. He makes me sound like a bathhouse with inconvenient hours."
"He is selling my name with yours."
"Yes, I can read. Why have you sent me his advertisement, and not his hands?"
"Because I want to know who buys before somebody takes a false invitation seriously."
"My brother's real invitations were troublesome enough. Show me the forgery. Then I shall decide whether Salven is worth a long evening or a short one."''', 2),
    (('noct.acq.',),
     '''{n}You propose sending a reply that appears to accept one purchased introduction. Salven will have to name where he expects a petition to be delivered. Nerethi can attend his advertised collection point in Drezen with a closed packet, soldiers close enough to hear her call.{/n}
{n}Nocticula wants to know what is in the packet.{/n}
"A request from someone who thinks you will enjoy hearing how easily they purchased your attention."
"You have a model close at hand."
"I was going to sign it."
{n}The next line forms more slowly.{/n}
"Then he will learn that you are investigating him."
"After he has supplied the delivery instructions. Before that, I offer a seller the possibility of a better customer."
"Better in which sense?"
"More expensive to disappoint."
{n}You offer a further concession. If she supplies an outer mark which her actual servants recognize as false, you will let her keep a signed undertaking naming your part in the investigation. It will prove your involvement if the affair later becomes inconvenient. Anyone selling Council protection will have to account for your recorded cooperation with the woman his guarantee claims to reach.{/n}
{n}She will gain a record you cannot dismiss as an anonymous forgery. You will gain a way to distinguish a bought promise from a reply she actually chose to send.{/n}''',
     '''{n}You propose an answer that seems to buy one introduction. Salven will have to name where a petition should be delivered. Nerethi can take a closed packet to his collection point in Drezen, with soldiers close enough to hear her call.{/n}
{n}Nocticula wants to know what is in the packet.{/n}
"A request from someone who thinks you will enjoy hearing how cheaply they bought your attention."
"You have a model close at hand."
"I was going to sign it."
{n}The next line forms slowly.{/n}
"Then he will learn that you are hunting him."
"After he names the address. Before that, I am only a better customer."
"Better in which sense?"
"More expensive to disappoint."
{n}Then you offer her more than bait. If she gives you an outer flourish her own servants will know for a forgery, you will sign your part in the hunt and let her keep it: the Knight Commander of the crusade, in writing, hand in glove with the Lady in Shadow. It is the kind of paper crusaders are burned over.{/n}
{n}On the other side of the wax she goes very still, the way a cat goes still when the mouse offers it the knife.{/n} "Your neck, in my drawer," {n}she writes.{/n} "Now that is a gift."''', 2),
    (('noct.acq.',),
     '''{n}Nerethi returns from the broker's collection point with your packet unopened and a narrow strip of paper. Salven would not take the packet without an advance; she would not pay without knowing where a failed delivery could be disputed. He gave her an address and called the question provincial.
Two soldiers saw him hand it over. Neither touched him. Nerethi reports that he was packing his display case before she reached the door.
Salven tore the strip from an acceptance counterfoil while she watched. Nerethi asked for the discarded half too, saying a receipt needed its number. It records three pending deliveries to the merchant whose room is named in the address. She has not seen the letters.
The address is above a bathhouse in Drezen. On the counterfoil, the receiving merchant's initials stand beneath a date earlier than the gate book's record of his arrival. Another date has been crowded into the margin and scratched through. Nerethi has brought the gate clerk's copy of his entry; both papers are on your desk.
You can send your officers there immediately. You can also compare the dates with the gate clerk's arrival book before Salven learns what Nerethi noticed.
Nocticula's mark waits in a sheet beside the papers. You have copied the address to her; no answer has arrived.{/n}''',
     '''{n}Nerethi comes back from the broker's collection point with your packet unopened and a strip of paper. Salven would not take the packet without money in advance, and she would not pay without knowing where to find him if it went astray. He gave her an address, called her provincial, and was packing his display case before she reached the door. Two of your soldiers watched him go; you had told them not to touch him.
The strip is torn from a delivery slip. Nerethi asked for the other half as well, and got it: three letters waiting with a merchant who has a room above a bathhouse in Drezen. The date under the merchant's mark is older than the gate's record of his arrival in the city. A second date has been crowded into the margin and scratched out.
You can send soldiers now, or check the gate book first, before Salven learns what Nerethi noticed.
Nocticula's mark lies quiet on the sheet beside the papers. You copied her the address an hour ago. She has not answered; you have the impression that she is listening.{/n}''', 1),
    (('noct.acq.',),
     '''{n}The merchant supplies two forwarding contacts. One address is empty when your officers reach it; the other belongs to a woman who copies advertisements and has kept his unpaid bill. She gives Nerethi the original wording for her claim against his seized funds.{/n}
{n}Your new arrangement begins with a creditor, a room and a man who will lie when it becomes profitable. You write those limitations into the first report to Nocticula.{/n}
"You omitted the most troublesome proprietor," {n}she answers.{/n}
{n}You add your own name.{/n}
"Better."
{n}Nerethi prepares a different notice: an office that receives requests, and a keeper who copies every one before she refuses it. Nocticula reads the copies. Nobody who writes to that office is told so.{/n}
{n}Nocticula receives the first ledger page before you close the room for the night. It contains the merchant's account and your correction of it. She now knows which contacts you obtained and which escaped.{/n}
{n}The false flourish stays in a sealed drawer. Using it outside this one forwarding arrangement would contradict the signed undertaking she holds.{/n}''',
     '''{n}The merchant gives up two forwarding contacts. One address is empty when your soldiers kick the door in; the other belongs to a woman who copies advertisements for a living and is owed money by him. She hands Nerethi the guarantee's original wording in exchange for a claim on his seized purse.{/n}
{n}You tell Nocticula what you have: a creditor, a room, and a man who will lie the moment it pays.{/n}
"You left out the most dangerous proprietor," {n}she answers.{/n}
{n}You add your own name.{/n}
"Better."
{n}From then on there is an office in Drezen that receives requests for the Lady in Shadow, and a keeper who copies every one before refusing it. Nocticula reads the copies. Nobody who writes there is ever told, and some of them, later, are visited.{/n}
{n}The merchant keeps his hands; she says she prefers him writing. The false flourish goes into a locked drawer. Using it outside this one arrangement would break the signature she holds.{/n}''', 1),
    (('noct.acq.',),
     '''{n}Nerethi places the seized payments in the clerk's strongbox and writes the sum on the posted denial. Claimants must describe what they bought; the notice does not promise that every claim can be paid.
You hold the unused bait letter over the lamp. The false flourish curls inward first. Nocticula's answering mark remains on the other sheet, beside the copy of your undertaking which she has returned for you to sign as fulfilled.
She has not returned her original.
"An expensive performance of honesty," she writes. "You have lost a useful imitation."
"I kept the address that answers."
"For the moment."
You leave her qualification where it is and sign. The copy darkens beneath your hand. Somewhere beyond the paper, she receives the proof that you surrendered the instrument instead of using it a second time.{/n}''',
     '''{n}Nerethi locks the seized money in the clerk's strongbox and writes the sum on the posted denial. Anyone who bought Salven's guarantee may come and describe what they paid for; the notice does not promise that everyone will be paid.
You hold the unused bait letter over the lamp. The false flourish curls first. On the other sheet Nocticula's mark waits beside a copy of your undertaking, sent back for you to sign as kept. She has not returned the original.{/n}
"An expensive performance of honesty," {n}she writes.{/n} "You have burned a perfectly good lie."
"I kept the address that answers."
"For the moment."
{n}You sign. The copy darkens under your hand as she takes it.
That night the merchant's cell is found empty, its door still locked from the outside. In the morning a pair of hands lies on Nerethi's desk, wrapped neatly in his own advertisement. Nobody in Drezen sells the Lady in Shadow's name again that year.{/n}''', 1),
]

SUBS = [
    (('noct.', 'nocticula.'), "{n}Her answering mark cuts across Shamira's name.{/n}",
     "{n}A black line cuts through Shamira's name, deep enough to score the paper.{/n}", 469),
    (('noct.', 'nocticula.'), '{n}Shamira\'s answer burns across the letter.{/n} "You dismiss me from your bed? Keep your mortal. You will still hear from my Harem when your city displeases me."',
     '{n}Shamira\'s answer burns up through the letter before the line is dry.{/n} "Dismissed? For that? Keep it, then, my lady, and keep it close. Mortals break so easily, and my Harem has such clumsy servants."', 134),
    (('noct.', 'nocticula.'), "{n}The message to Shamira's court brings no answer from its mistress. Nocticula does not call the silence agreement.{/n}",
     '{n}Nobody answers for Shamira. Nocticula does not call the silence agreement. She calls it a relief, and does not sound relieved.{/n}', 268),
    (('noct.acq.epilogue.correspondence',), 'a question, a sum corrected in another hand,',
     'a question, an insult, a description of what she was wearing,', 1),
    (('noct.acq.epilogue.correspondence',), 'The next letter arrived three nights later, with a correction to the last argument.',
     'The next letter came three nights later and began with the one point of the argument she had lost, restated as though she had won it.', 1),
    (('noct.acq.epilogue.correspondence',), 'The next business report received her corrections.',
     'For a month afterwards every letter she sent began with a description of the room the Commander had refused to see.', 1),
    (('noct.acq.',), '"An address which leads to a person. You should send my brother the method. He has always preferred the reverse."',
     '"An address which leads to a person. You should send my brother the method. He has always preferred the reverse." {n}Under it, smaller:{/n} "Keep the merchant breathing until I say otherwise. I have plans for his evening."', 1),
    (('noct.acq.',), '"You may keep the ingenious explanation. I shall keep the fact that he had time to burn the names. What will you offer the people you can no longer warn privately?"',
     '"You may keep the ingenious explanation. I shall keep the fact that he had time to burn the names. Somebody will pay for that hour, Commander, and I have not yet decided that it will not be you."', 1),
]

CHOICES = [
    (('nocticula.trickster.defeated.',), '[Keep the signed invitation. Let the clerk carry the next one.]', '[Keep her marks. Let them show.]', 5),
    (('noct.', 'nocticula.'), '[Keep her name in the agreement.]', "[Share her, then. Ask no dead woman's blessing.]", 201),
    (('noct.acq.',), 'Account for the held letters and identified buyers.', 'Give her the names.', 1),
    (('noct.acq.',), 'Post a notice for the missing buyers and record the lost names.', 'Post the warning in the square. Let the buyers come to you.', 1),
    (('noct.acq.',), 'Post the notice and record that the assistant escaped with warning.', 'Post the warning. The assistant is already running.', 1),
    (('noct.acq.',), 'Keep the restitution account and relinquish the reusable pattern.', 'Burn the pattern. Hold the money for the cheated.', 2),
    (('noct.acq.',), 'Retain the limited pattern and give her the first required report.', "Keep the pattern. Give her the merchant's contacts, and your own name with them.", 2),
    (('noct.acq.',), 'Accept the copied-report obligation and prepare the bait.', 'Agree: every petition copied to her first. Prepare the bait.', 2),
    (('noct.acq.',), 'Let her retain the undertaking and prepare the single bait letter.', 'Let her keep your signature. Prepare the one bait letter.', 2),
    (('noct.acq.',), 'Make the merchant supply his forwarding contacts. Establish the copied-report arrangement you promised.', 'Squeeze the merchant for his contacts. Set up the arrangement you promised her.', 1),
]


# ---------------------------------------------------------------------------
# Appended read-only consumers (S6). (scene, node, [(requires, forbids, text)]).
# ---------------------------------------------------------------------------
AREELU = ((("areelu.committed", "crossroute.areelu.available"), (),
           "{n}She knew whose bed Areelu Vorlesh slept in after the war, and never once sent an assassin to it, which "
           "in Alushinyrra was understood to be the most expensive courtesy she had ever paid anyone. She did tell the "
           "Commander, more than once and in some detail, exactly where she would have started the knife.{/n}"),)
HARBOR = (
    (("noct.crimson_mark",), ("noct.mark_hidden",),
     "{n}The Commander wore her crimson mark where it showed, at the throat, through every audience and every war "
     "council afterwards. Paladins looked away from it. Succubi looked at nothing else. Nocticula said it saved her "
     "the trouble of telling anyone whose the Commander was.{/n}"),
    (("noct.mark_hidden",), (),
     "{n}The Commander kept her crimson mark under a high collar for the rest of the war and after. It made no "
     "difference. Every succubus who ever stood close enough could smell it, and every one of them stepped back.{/n}"),
    (("noct.lodge_appetite_admitted",), (),
     "{n}She never let the Commander forget the night at the lodge window. Whenever the Commander called something "
     "duty in her hearing, she repeated, word for word, what the Commander had admitted wanting that night, and waited, "
     "smiling, for a denial that never came.{/n}"),
    (("noct.lodge_vigilance_admitted",), ("noct.lodge_appetite_admitted",),
     "{n}She remembered what the Commander had confessed at the lodge window, about bringing danger into rooms where it "
     "was not invited, and took it as permission. Afterwards there was always something dangerous waiting in the "
     "Commander's rooms in Alushinyrra: an assassin she had not dismissed, a guest she had not disarmed, once a vrock "
     "chained in the bath. She called them presents.{/n}"),
    (("noct.lodge_danger_desired",), (),
     "{n}\"I liked watching you take the house from her,\" the Commander had told her once. Nocticula made sure there "
     "was always another house to take.{/n}"),
    (("noct.lodge_desire_contested",), ("noct.lodge_danger_desired",),
     "{n}The Commander had told her once, after Istrava's lodge, that they disliked what she could make sound "
     "reasonable and wanted her anyway. She had the sentence cut into the headboard of her bed, on the Commander's "
     "side.{/n}"),
) + AREELU
CORRESPONDENCE = (
    (("nocticula.harem.attitude.arueshalae.respect", "crossroute.arueshalae.available"), (),
     "{n}Arueshalae never went back to Alushinyrra, and Nocticula never once sent for her, exactly as she had "
     "written. She made sure every succubus in her city knew the name of the one who had walked out of her service in "
     "front of soldiers and lived. She called it a lesson. Three of her succubi took it for a dare and tried the same. "
     "None of them lived.{/n}"),
    (("household.pair.arueshalae_nocticula.unsettled", "crossroute.arueshalae.available"),
     ("household.pair.arueshalae_nocticula.resolved",),
     "{n}Arueshalae's claim to her own name was never settled. Once a year, on the same night, a succubus from the "
     "Harem came to the Commander's door with a leash of black silk, laid it on the step, and left without a word. "
     "Arueshalae burned every one, and the year she did not bother to burn it, Nocticula sent two.{/n}"),
    (("household.pair.nocticula_shamira.resolved", "crossroute.shamira.available"), (),
     "{n}Shamira's claim to sit beside the throne, not behind it, stood for exactly as long as Nocticula found it "
     "amusing, which turned out to be years. They fought over it in public, at table, with the whole court betting, "
     "and went to bed together afterwards, and the Commander was never told which of them had won.{/n}"),
)
APPENDS = [
    ("noct.ending_company", "end", HARBOR),
    ("noct.ending_alliance", "end", HARBOR),
    ("noct.ending_limit", "end", HARBOR),
    ("nocticula.trickster.defeated.epilogue", "end", AREELU),
    ("noct.acq.epilogue.correspondence", "page", CORRESPONDENCE),
]


PARAS += HAREM_PARAS + CORRESPONDENCE_PARAS


def _own(payload):
    return [s for s in payload["Scenes"] if s["Id"].startswith(OWN)]


def _surfaces(scene):
    for node in scene["Nodes"]:
        yield node
        yield from node.get("Paragraphs") or []
        yield from node.get("Choices") or []


def _check(label, got, want, *, scene=None):
    if got != want:
        record('overlay.text_mismatch', scene=scene, detail=f"nocticula_cloud: {label}: expected {want} replacements, got {got}")


def apply(payload, *, include_harem=True):
    own = _own(payload)
    if not own:
        record('overlay.text_mismatch', detail="nocticula_cloud: no Nocticula scenes in the payload")
    # canon-fix1 renames (every owned surface; each queue scene must have been hit as counted).
    hits = {}
    for scene in own:
        for item in _surfaces(scene):
            text = item.get("Text") or ""
            for pattern, new in RENAMES:
                text, k = re.subn(pattern, new, text)
                if k:
                    hits.setdefault(scene["Id"], {}).setdefault(new, 0)
                    hits[scene["Id"]][new] += k
            if "Text" in item:
                item["Text"] = text
    for sid, names in RENAME_EXPECT.items():
        for name, count in names.items():
            _check(f"rename {name} in {sid}", hits.get(sid, {}).get(name, 0), count, scene=sid)
    # Whole paragraphs (identical bodies on many pages).
    for old, new, count in PARAS:
        if not include_harem and (old, new, count) in HAREM_PARAS:
            continue
        got = 0
        for scene in own:
            for node in scene["Nodes"]:
                for para in node.get("Paragraphs") or []:
                    if para["Text"] == old:
                        para["Text"] = new
                        got += 1
        _check("paragraph " + old[:50], got, count)
    # Whole node texts, by scene group.
    for group, old, new, count in NODES:
        got = 0
        for scene in own:
            if scene["Id"].startswith(group):
                for node in scene["Nodes"]:
                    if node["Text"] == old:
                        node["Text"] = new
                        got += 1
        _check("node " + old[:50], got, count)
    for group, old, new, count in SUBS:
        got = 0
        for scene in own:
            if scene["Id"].startswith(group):
                for node in scene["Nodes"]:
                    k = node["Text"].count(old)
                    if k:
                        node["Text"] = node["Text"].replace(old, new)
                        got += k
        _check("substring " + old[:50], got, count)
    for group, old, new, count in CHOICES:
        got = 0
        for scene in own:
            if scene["Id"].startswith(group):
                for node in scene["Nodes"]:
                    for choice in node.get("Choices") or []:
                        if choice["Text"] == old:
                            choice["Text"] = new
                            got += 1
        _check("choice " + old[:50], got, count)
    by = {s["Id"]: s for s in own}
    for sid, nid, bodies in APPENDS:
        with overlay_item():
            node = overlay_node(by, sid, nid)
            node.setdefault("Paragraphs", [])
            for requires, forbids, text in bodies:
                with overlay_item():
                    if any(para["Text"] == text for para in node["Paragraphs"]):
                        raise OverlayMismatch('overlay.text_mismatch', scene=sid, node=nid, detail=f"nocticula_cloud: {sid}:{nid} already carries {text[:40]!r}")
                    node["Paragraphs"].append(p(text, requires=requires, forbids=forbids))
    return payload


def integrate(payload, *, include_harem=True):
    apply(payload, include_harem=include_harem)
