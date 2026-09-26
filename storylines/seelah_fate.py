"""The first physical fate action: revive the retained fallen companion.

Departure, missing-entity recovery, and all-path alternatives remain separate work.
"""
from story_format import c, n, scene

SCENES = [
    scene("seelah.fate_life", "A tomorrow that was omitted", "Seelah", 3, "", [
        n("start", "Narrator", '''{n}There is something intolerably final about the way people have begun speaking of Seelah. Every sentence knows where it ends. Even the stories she would have interrupted have acquired a respectful silence.{/n}
{n}Your power finds a flaw in that certainty. Death has taken a woman who still has things to say. Somewhere in the world's account of her, tomorrow has been omitted.{/n}
{n}You could attempt to put it back. Her life would be her own to spend; the trick would buy you no promise about how she spends it.{/n}''',
          c('[Use your Trickster power to attempt Seelah\'s resurrection.]', revive="seelah", flags=("seelah.revived",)),
          c('[Leave the possibility open. You are not ready to attempt it.]', abort=True),
          portrait="Seelah"),
    ], Relationship="seelah", Recovery="seelah", Remote=True, Chapters=[3, 5],
          Areas=["2570015799edf594daf2f076f2f975d8"], requires=("trickster", "seelah_dead")),
    scene("seelah.fate_return", "Something she still means to say", "Seelah", 3,
          '"Seelah. How are you feeling?"', [
        n("start", "Seelah", '''{n}Seelah takes a breath before answering, and seems briefly distracted by the simple fact that she can.{/n}
"Alive. I keep noticing."
{n}She tries to smile. It holds for a moment, then becomes something more uncertain.{/n}
"People are going to ask what it was like. I don't have a story ready for them. I may not want one."''',
          c('"You do not owe anyone an account of it."', "own"),
          c('"I wanted you to have more time. What you do with it is yours."', "own"),
          portrait="Seelah"),
        n("own", "Seelah", '''"Good. Because the first thing I want is a little time to stop being brave about how strange this feels."
{n}She rests her hands on her knees and looks at them.{/n}
"Thank you. I mean that. I also mean that I still get to argue with you. I would hate to discover I had come back owing you several years of being agreeable."''',
          c('"I would have suspected the trick had brought back the wrong paladin."', "end"),
          c('"Take the time you need. I will be here."', "quiet"),
          portrait="Seelah"),
        n("end", "Seelah", '''{n}This time her laugh sounds like herself.{/n}
"That is reassuring. Annoying, but reassuring."
{n}She asks you to stay for a while. There is no great revelation waiting to be told, only a conversation she would otherwise have missed.{/n}''',
          c('[Stay with her.]', flags=("seelah.return_acknowledged",)), portrait="Seelah"),
        n("quiet", "Seelah", '''{n}She moves her hand to make room beside her.{/n}
"Here would be good. For a while."
{n}She sits with you without trying to fill the silence. When she does speak again, she asks about something ordinary that happened while she was gone.{/n}''',
          c('[Stay with her.]', flags=("seelah.return_acknowledged",)), portrait="Seelah"),
    ], Relationship="seelah", AnswerLists=["417fa384f3250634bb71859fbc913453"],
          Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[3, 5], requires=("seelah.revived",)),
]
