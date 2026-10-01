"""The first physical fate action: revive the retained fallen companion.

Departure, missing-entity recovery, and all-path alternatives remain separate work.
"""
from story_format import c, n, scene

SCENES = [
    scene("seelah.fate_life", "A tomorrow that was omitted", "Seelah", 3, "", [
        n("start", "Narrator", '''{n}People lower their voices when they speak of Seelah. They tell her stories solemnly, without the laughter or the interruptions. Even the worst ones get a respectful silence.{/n}
{n}Your power finds a flaw in that certainty. Death has taken a woman who still has things to say. Somewhere in the world's account of her, tomorrow has been omitted.{/n}
{n}You could attempt to put it back. You want to hear her laugh again, even if the first joke is at your expense.{/n}''',
          c('[Use your Trickster power to attempt Seelah\'s resurrection.]', revive="seelah", flags=("seelah.revived",)),
          c('[Wait before making the attempt.]', abort=True),
          portrait="Seelah"),
    ], Relationship="seelah", Recovery="seelah", Remote=True, Chapters=[3, 5],
          Areas=["2570015799edf594daf2f076f2f975d8"], requires=("trickster", "seelah_dead")),
    scene("seelah.fate_return", "Something she still means to say", "Seelah", 3,
          '"Seelah. How are you feeling?"', [
        n("start", "Seelah", '''{n}Seelah takes a breath before answering, and seems briefly distracted by the simple fact that she can.{/n}
"Alive. I keep noticing."
{n}She tries to smile. It holds for a moment, then becomes something more uncertain.{/n}
"They'll all want to hear what it was like. I can barely get a sentence out. And I'm damned if I'm making a tavern tale of it."''',
          c('"Then they can go thirsty for a tale."', "own"),
          c('"I wanted you alive. I came to hear your voice, not give you orders."', "own"),
          portrait="Seelah"),
        n("own", "Seelah", '''"Good. Because I'm shaking like a recruit with a practice sword. Don't ask me to make a brave face just yet."
{n}She rests her hands on her knees and looks at them.{/n}
"Thank you. And don't look so pleased! I'll still argue with you. If you wanted a paladin who agreed with everything you said, you picked the wrong corpse."''',
          c('"I would have suspected the trick had brought back the wrong paladin."', "end"),
          c('"I will stay. The brave face can wait."', "quiet"),
          portrait="Seelah"),
        n("end", "Seelah", '''{n}This time her laugh sounds like herself.{/n}
"Oh, good. Back from the dead, and you're already a nuisance."
{n}She asks you to stay. Her laugh catches in her throat, and she swallows before launching into a question about the camp.{/n}''',
          c('[Stay with her.]', flags=("seelah.return_acknowledged",)), portrait="Seelah"),
        n("quiet", "Seelah", '''{n}She moves her hand to make room beside her.{/n}
"Here. Sit down before somebody finds you a job."
{n}She sits with you, rubbing her hands together. After a while she asks who has been making trouble while she was gone.{/n}''',
          c('[Stay with her.]', flags=("seelah.return_acknowledged",)), portrait="Seelah"),
    ], Relationship="seelah", AnswerLists=["417fa384f3250634bb71859fbc913453"],
          Areas=["2570015799edf594daf2f076f2f975d8"], Chapters=[3, 5], requires=("seelah.revived",)),
]
