"""Native political context without treating a shown dialogue as completed business."""
from story_format import c, n, scene

STARTED_DIALOGS = {
    "konomi.rank_six_started": "30333438aac8d3647bef882fa87e978e",
    "konomi.rank_eight_started": "6178470b05c75484085753b821a6a614",
}
ETUDES = {"konomi.foreign_help_playing": "c6e9a69f602a48e18424f4b6d71062b4"}
SEEN_CUES = {
    "konomi.council_conclusion_seen": ["7f64a30ceb4bfb046990bccbded7ac75"],
    "konomi.political_respect_seen": ["8311ef29223c4fe469c95cd8eb80e539"],
}
DREZEN = "2570015799edf594daf2f076f2f975d8"


def pages(private):
    opening = '''{n}Konomi has kept an evening free in the room she is using during her return to Drezen. A folded letter lies beside the lamp.{/n}
"An acquaintance thought leaving my appointment might have cured my interest in Mendev. She sent me an account of a supper instead of the news I asked for. I have replied with more precise questions."
{n}She puts the letter down.{/n}
"I no longer advise you by virtue of that office. You may still ask what I think. I will probably tell you."''' if private else '''{n}Konomi has put two letters beside the chair opposite hers. When you sit down, she leaves them folded.{/n}
"You asked how I have been. Part of the answer concerns what I want to do next. I would prefer you to hear it before we make private plans around a woman who has conveniently ceased to have political opinions."
{n}Her expression softens, though only a little.{/n}
"I have not. I doubt you expected otherwise."'''
    role = '''"Leaving the appointment has not made me indifferent to what becomes of my country. It has changed which letters I can expect people to answer."
{n}She turns the folded letter over.{/n}
"I can ask an acquaintance for information. I cannot call it a council instruction and expect a clerk to hurry because I have signed it. Occasionally I have to be pleasant. You may appreciate the sacrifice."''' if private else '''"The council's work and my appointment are not the same thing. I can put down one piece of work without pretending I have been dismissed from the other."
{n}She moves one of the letters beneath the other.{/n}
"There will still be people whose decisions I want to influence. I would like to choose where to spend that effort, rather than have everyone assume I have become content to watch."'''
    return [
        n("start", "Konomi", opening,
          c('"Tell me what is occupying you."', "situation"),
          c('[Ask to return when you can listen properly.]', abort=True)),
        n("situation", "Konomi", '''"The answer depends upon what we are trying to protect now. An argument which was useful during the crisis may become a very convenient excuse afterward."
{n}She waits until she has your attention before continuing.{/n}''',
          c('[Listen to her assessment of foreign intervention.]', "foreign", requires=("konomi.rank_eight_started", "konomi.foreign_help_playing")),
          c('[Listen to her assessment of the domestic recovery.]', "domestic", requires=("konomi.rank_eight_started",), forbids=("konomi.foreign_help_playing",)),
          c('[Listen to her concerns about the continuing crisis.]', "crisis", requires=("konomi.rank_six_started",), forbids=("konomi.rank_eight_started",)),
          c('[Ask what she can say without assuming a later settlement.]', "uncertain", forbids=("konomi.rank_six_started", "konomi.rank_eight_started",))),
        n("foreign", "Konomi", '''"The foreign garrisons have restored a measure of order. They have also taken tax collection and administration into their hands. Both facts matter."
{n}She presses the edge of the folded letter flat.{/n}
"I will not tell a person who can safely cross a street again that nothing has improved. I will also not tell an army administering that street that gratitude gives it permission to remain indefinitely."
"What would you ask for?"
"An account of what must happen before authority returns to Mendev's own officials. Specific responsibilities. Specific obstacles. I want the question asked while our allies still find it courteous."
{n}Her eyes meet yours.{/n}
"That is work I want to have a part in. You may dislike some of the people I would need to persuade. I shall dislike some of them myself."''', c('[Ask what that means for her own work.]', "council")),
        n("domestic", "Konomi", '''"Mendev has brought the crisis under control without handing its administration to foreign forces. The cities and the capital are acting together again. That is worth defending."
{n}She does not smile at the neatness of the summary.{/n}
"It will tempt people to declare every measure they favored indispensable. Success produces very accomplished storytellers. I would like to know which arrangements are actually working before their authors make them impossible to question."
"You expect to argue with the people who helped restore order?"
"Certainly. I expect them to argue with me. We shall manage better if neither side begins by calling disagreement ingratitude."
{n}She looks toward the closed writing case.{/n}
"I want a part in those decisions. Peace should leave us better occupations than defending our wartime reputations."''', c('[Ask what that means for her own work.]', "council")),
        n("crisis", "Konomi", '''"The divisions in Nerosyan are doing damage far beyond the rooms where the arguments begin. Public services are failing. Roads are unsafe. The danger of famine grows while people debate who deserves to issue the next instruction."
{n}She stops herself from unfolding the letter.{/n}
"I have a great many opinions about that. You know several of them already. Tonight I wanted to tell you why I will not promise to become less interested when our conversations become more personal."
"I have not asked you to."
"No. I would like to avoid discovering that either of us assumed it. I want a future in a country capable of governing itself. There are evenings when wanting that makes me very poor company."
{n}Her glance toward you is dry.{/n}
"You are permitted to say so. Preferably with a better argument than that I would look prettier if I smiled."''', c('[Ask how she sees her work continuing.]', "council")),
        n("uncertain", "Konomi", '''"I will not give you a convenient ending to a dispute merely because it would make this conversation easier. There are accounts I would need to check before attaching my name to one."
{n}She taps the folded letter without opening it.{/n}
"What I can tell you is what I intend to keep asking. Who can still do the work they claim to control? Who answers when a promise fails? Which ally has begun to confuse being needed with being entitled?"
"You can make those questions sound like accusations."
"Sometimes they are. I try to discover which before sending them."
{n}A slight smile escapes her.{/n}
"You need not agree with my eventual answer in order to hear why the question matters to me."''', c('[Ask what she wants to do with those answers.]', "council")),
        n("council", "Narrator", '''{n}Konomi draws her writing case closer, then leaves it shut. She seems to be deciding which part of the answer belongs in this room.{/n}''',
          c('"You said the Diplomatic Council had served its purpose. What comes after that?"', "concluded", requires=("konomi.council_conclusion_seen",)),
          c('"What part of that work do you want for yourself?"', "unconcluded", forbids=("konomi.council_conclusion_seen",))),
        n("concluded", "Konomi", '''"I meant what I said about the council. I did not mean that I had lost the desire to be useful, or to have my advice taken seriously."
{n}She gives you an appraising look.{/n}
"I am aware that those are not always identical ambitions. It would be tedious to pretend otherwise with somebody I want to know me."
''' + role, c('[Hear what she wants you to understand.]', "respect")),
        n("unconcluded", "Konomi", '''"Influence over a decision before everyone has spent a week defending it. The chance to ask an unwelcome question while the answer can still change something."
{n}She rests her hands on the writing case.{/n}
"We need not settle the future of every institution tonight. I am telling you which part of my work I would miss, and which part I have no intention of giving up merely to become an agreeable guest."''', c('[Hear what she wants you to understand.]', "respect")),
        n("respect", "Narrator", '''{n}She watches your reaction with more interest than she gives the letters.{/n}''',
          c('"When you acknowledged my political judgment, did you expect us to stop disagreeing?"', "earned", requires=("konomi.political_respect_seen",)),
          c('"And where would you put my judgment among those decisions?"', "unearned", forbids=("konomi.political_respect_seen",))),
        n("earned", "Konomi", '''"No. I expected you to remember that I was capable of revising an opinion. That includes a favorable one."
{n}Her smile takes the sting out of only part of the answer.{/n}
"You earned that acknowledgment. I did not give it because I wanted an invitation from you. I would object rather strongly to having it explained that way."
"Even by me?"
"Especially by you. You were there."
{n}She lets the silence last long enough for you to recognize the pleasure beneath her severity.{/n}''', c('[Ask what she would like to share next.]', "offer")),
        n("unearned", "Konomi", '''"Beside the evidence, where I hope you would put mine."
{n}She studies your face.{/n}
"You may be hoping for a more flattering answer. I can offer one about your company. I enjoy it sufficiently to risk telling you things which do not flatter either of us."
"A formidable recommendation."
"I thought so. I have been unusually generous."
{n}Her smile makes it easier to answer the invitation without mistaking it for agreement on every political question.{/n}''', c('[Ask what she would like to share next.]', "offer")),
        n("offer", "Konomi", '''"Another conversation when I have something worth showing you. I would like you to see how I decide which question to send, or what I do with an answer I dislike."
{n}She pushes neither letter toward you yet.{/n}
"The people who wrote to me have not consented to having their private business used to entertain my guest. I can ask what they are willing to share. That may leave us with a less impressive example."
"You would still want me here?"
"Yes. I am trying to invite you, not recruit an audience."''',
          c('"Show me how you frame the questions, when you have permission."', "questions"),
          c('"I would rather hear what you do with a difficult reply."', "replies")),
        n("questions", "Konomi", '''"Then you may object before I send anything. I reserve the right to disagree with the objection."
{n}She puts the letters away and gives you her attention again.{/n}
"For tonight, you know what has been occupying me. Tell me something that has been occupying you. I am willing to hear an answer which has no bearing on Mendev's future."
{n}Her hand rests beside yours on the table. She stays to hear what you choose to tell her.{/n}''', c('[Stay and tell her.]')),
        n("replies", "Konomi", '''"You may find me less charming when the reply has arrived. I tend to compose my first answer aloud."
"I should like to hear it."
"I suspected you might."
{n}She closes the writing case, then turns her chair a little toward yours.{/n}
"There. That can wait. You cannot accuse me of bringing you here solely to discuss correspondence. I would like the rest of the evening with you."''', c('[Stay for the rest of the evening.]')),
    ]


SCENES = []
for private in (False, True):
    nodes = pages(private)
    for node in nodes:
        node["Portrait"] = "Konomi"
    options = dict(Remote=True, ManualOnly=True) if private else dict(AnswerLists=["0dc8b8604bb33c846a63f3eb62443674"])
    SCENES.append(scene("konomi.private_political_account" if private else "konomi.political_account",
                        "Opinions she intends to keep", "Konomi", 5,
                        "" if private else '"What part of your work do you want to keep for yourself?"', nodes,
                        requires=("konomi.dismissed", "konomi.office_completed", "konomi.private_returned") if private
                        else ("konomi.present", "konomi.return"),
                        forbids=("konomi.present", "inhuman", "konomi.farewell", "konomi.private_future") if private
                        else ("konomi.dismissed", "konomi.farewell"),
                        delay=24, optional=private, Relationship="konomi", Chapters=[5], Areas=[DREZEN], **options))


def integrate(payload):
    """Add verified native predicates and require the ordinary context before new future plans."""
    for key, bindings in (("StartedDialogs", STARTED_DIALOGS), ("Etudes", ETUDES), ("SeenCues", SEEN_CUES)):
        target = payload.setdefault(key, {})
        for flag, value in bindings.items():
            if flag in target and target[flag] != value:
                raise ValueError("Conflicting Konomi political binding: " + flag)
            target[flag] = value
    by_id = {item["Id"]: item for item in payload["Scenes"]}
    for required in ("konomi.political_account", "konomi.private_political_account", "konomi.power"):
        if required not in by_id:
            raise ValueError("Konomi political integration missing scene: " + required)
    required = by_id["konomi.power"]["Requires"]
    if "konomi.political_account" not in required:
        required.append("konomi.political_account")
