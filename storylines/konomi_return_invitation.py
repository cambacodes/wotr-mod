"""Remote consent to a first personal visit after a verified retained return.

Authored alternate correspondence, not physical arrival or office reinstatement.
"""
from story_format import c, n, scene
from storylines.konomi_retained_return import DREZEN, DEAD

SCENES = [scene("konomi.return_letter", "A reply in her own hand", "Konomi", 3, "", [
    n("start", "Narrator", '''{n}You have written Lady Konomi's name on a fresh sheet. The map lies folded beneath a paperweight. It has contributed nothing to the letter, though one corner has tried to lift itself twice.{/n}
{n}There is a great deal you could ask her. You begin with a question she can answer without explaining what happened to her.{/n}''',
      c('[Ask whether she would welcome a short personal visit.]', "request"),
      c('[Send your good wishes without asking her to receive you.]', "good_wishes"),
      c('[Put the unfinished letter aside for now.]', abort=True)),
    n("request", "Narrator", '''{n}You keep the request brief. You would like to see her when she feels able, and there is no need to send an immediate answer. You add that you can bring the map if she wishes to inspect the instrument of your argument.{/n}
{n}Her reply arrives folded around your own letter. Your final sentence has acquired a small mark in the margin.{/n}
{n}"I am pleased to discover that the map has not been appointed to manage my correspondence. Please keep it occupied elsewhere for the present. I have questions for you before I have questions for a piece of paper."{/n}
{n}Beneath that, in slightly less even handwriting, she has written another paragraph.{/n}''',
      c('[Read the rest of her reply.]', "reply")),
    n("reply", "Narrator", '''{n}"I would welcome a short visit in Drezen. I shall sit down, and you may tell me what you attempted without turning it into a report for the council. If I become tired, I shall say so. Please believe me before I have to become diplomatic about it."{/n}
{n}There is a pause in the ink before the last line.{/n}
{n}"I find that I would rather hear your voice than read another account of myself."{/n}
{n}She has signed the letter herself. You recognize the care with which she has made the final stroke, even though the pen has pressed harder than the flourish requires.{/n}''',
      c('[Accept the short visit she has offered.]', "accept"),
      c('[Reply that you will leave her these quiet hours.]', "decline"),
      c('[Keep her reply while you consider whether to visit.]', abort=True)),
    n("accept", "Narrator", '''{n}You send a short acceptance. The map begins to unfold as you reach for the seal. You put the paperweight back.{/n}
{n}Konomi's reply has settled one question. She would like to see you. The visit itself must wait until she is able to receive you and Drezen's other demands leave the hour free.{/n}
{n}You keep her letter where you will find it again. There is no title beneath her signature, and no request for you to supply one.{/n}''',
      c('[Keep the appointment as a personal visit.]', flags=("konomi.return_meeting_accepted",))),
    n("decline", "Narrator", '''{n}You thank her for the invitation and write that you will leave her the quiet time. Her answer is a single line.{/n}
{n}"Very well. I intend to make disgracefully little use of it."{/n}
{n}You set the note beside the map. For once, neither has anything further to add.{/n}''',
      c('[Leave the visit unarranged.]', flags=("konomi.return_visit_declined",))),
    n("good_wishes", "Narrator", '''{n}You write that you are glad she is alive and that she need not account for her recovery to you. You stop before adding an invitation disguised as a question about her health.{/n}
{n}Her reply thanks you for the letter. She has underlined one word in her own sentence.{/n}
{n}"I am discovering that rest requires a certain determination. Fortunately, I possess some."{/n}
{n}The paper carries no appointment. You leave it that way.{/n}''',
      c('[Let the good wishes stand on their own.]', flags=("konomi.return_visit_declined",))),
], Relationship="konomi", Remote=True, AfterRecovery="konomi", Chapters=[3, 5], Areas=[DREZEN],
    requires=("konomi.retained_return_confirmed", "konomi.return_correspondence_available"),
    forbids=(DEAD, "inhuman", "konomi.return_first_words"), delay=12, optional=True)]


def integrate(payload):
    """Physical aftercare waits for the reply; existing completed visits stay completed."""
    first = next(item for item in payload["Scenes"] if item["Id"] == "konomi.return_first_words")
    first["Requires"].append("konomi.return_meeting_accepted")
