"""Expansion-only final-watch gates and explicit continuation of older saves."""
from story_format import c, n, scene

SCENES = []
DREZEN = "2570015799edf594daf2f076f2f975d8"


def s(id, title, entry, nodes, requires=(), forbids=(), delay=0, catchup=False):
    SCENES.append(scene(id, title, "Together", 5, entry, nodes,
                        requires=("future", "committed", "kept_terms", *requires),
                        forbids=("closed", "loss", "inhuman", "irabeth_away", "anevia_away", *forbids),
                        delay=delay, Relationship="tirabade", Areas=[DREZEN], Chapters=[5],
                        ForbidOverrides={"last_watch": "three_progression.catchup_requested"} if catchup else {}))


s("three_choose_days", "Before we call it the last evening",
  '"Are we ready to speak about the final battles?"', [
    n("start", "Irabeth", '''"We can. But I do not want to mistake making a promise for having lived it."
{n}Anevia looks at her wife, then toward you.{/n}
"We've still got things we meant to do together. Some are small. They're the ones that get put off because nobody's likely to die if we miss them. Then somehow we never do them."
"I want those days," Irabeth says. "I also know we may not have all the time we want. I would rather hear you say that than sit here waiting for an evening you cannot give us."
{n}She reaches for Anevia's hand. Her wife takes it without turning the question into a joke.{/n}''',
      c('"Let us make time for the days we planned before our final goodbyes."', "days"),
      c('"I cannot promise all those days before the fighting. I want to speak about leaving now."', "short"),
      c('[Leave this decision for another conversation.]', abort=True)),
    n("days", "Anevia", '''"Then come and find us. We can pick up where we left off."
{n}Irabeth nods.{/n}
"The final watch can wait while there is still time to live here. We need not spend every evening pretending it is the last."
"And we don't have to turn every evening into a great seduction," Anevia adds. "Though I reserve the right to try occasionally."
{n}Her wife smiles at that, then looks back at you.{/n}
"When we have kept those appointments, I would like to talk again. About what we have actually found together."''',
      c('[Continue the shared Drezen conversations; return when you are ready.]', abort=True)),
    n("short", "Irabeth", '''"Then we will speak about leaving. I won't pretend the things we have not done are memories."
{n}Anevia rubs a thumb across her wife's fingers.{/n}
"I still want you here. That doesn't become untrue because we have less to look back on. We'll have to find out what we can make of the promise when there's time."
{n}The remaining shared Drezen conversations will stay unfinished when you complete the final watch. This choice keeps the earlier promise, without treating those unplayed days as part of your history.{/n}''',
      c('[Choose the shorter course and make the final watch available.]', flags=("three_progression.short_chosen",)),
      c('[Do not settle this yet.]', abort=True)),
], forbids=("last_watch", "three_rooms_unlocked.kept", "three_progression.developed"), delay=24)


s("three_more_days", "After the words already said",
  '"We have spoken our goodbyes, but we are still here. May we make more time together?"', [
    n("start", "Anevia", '''"I haven't forgotten what we said."
{n}Anevia looks toward Irabeth, who closes the paper she was reading.{/n}
"Neither have I," Irabeth says. "I also haven't left. If we have time for another evening, I would like to use it."
"There are things we never got round to," Anevia tells you. "We can pick up the next one. Nobody needs to tear up a farewell speech first."
{n}The wives wait for your answer. Continuing will reopen the unfinished shared Drezen conversations while preserving the choices and goodbyes already recorded.{/n}''',
      c('"I would like those evenings with you both."', "yes"),
      c('[Keep the earlier goodbye for now. You can ask again later.]', abort=True)),
    n("yes", "Irabeth", '''"Then come when you can stay. We will begin with the next thing we meant to do."
{n}Anevia puts her arm around her wife's waist.{/n}
"I might complain that you kept us waiting. Don't let that put you off."
"You may also be pleased," Irabeth says.
"Very. I thought that was obvious."
{n}She looks at you, and the smile she gives you leaves little doubt.{/n}''',
      c('[Make time for the unfinished conversations.]', flags=("three_progression.catchup_requested",))),
], requires=("last_watch",), forbids=("three_progression.developed",))


s("three_kept_days", "The days behind the promise",
  '"We have made time for each other. What do you want to keep building?"', [
    n("start", "Irabeth", '''"More of it. That is my first answer."
{n}Irabeth has left her blue coat open. Anevia straightens the collar as she passes, then settles beside her wife.{/n}
"I liked choosing an evening for us. I liked seeing you arrive because you wanted to be there. I don't want that to become something I only did once."
"She has begun collecting ideas," Anevia says. "Some alarming ones."
"You suggested half of them."
"I did. I have excellent taste."
{n}Her grin softens when Irabeth takes her hand.{/n}''',
      c('[Sit with them and talk about what you have made together.]', "unfinished"),
      c('[Ask to return when you can give them your attention.]', abort=True)),
    n("unfinished", "Anevia", '''"I still look for Vald when I'm out. Sometimes I catch myself doing it on the way to meet you."
{n}She shrugs, irritated by the habit.{/n}
"We didn't finish everything. Ista and Wenna have their own work to do. Malven didn't turn honest because we made him answer a few questions."
"And we cannot make our time together wait for him to become honest," Irabeth says.
"We'd die of old age."
{n}Anevia looks toward her wife, then at you.{/n}
"I liked having you with me while we tried. I liked coming home afterward. That's what I want more of. You in the middle of a day, instead of only at the beginning of a grand promise."''', c('[Ask what Irabeth wants from those days.]', "beth")),
    n("beth", "Irabeth", '''"I want to be able to ask for something before I have earned it by exhausting myself."
{n}She smiles at Anevia's expression.{/n}
"Yes. You have said so before. I am trying to say it for myself."
"I'll be quiet for a moment, then."
"A rare gift."
{n}Irabeth turns toward you.{/n}
"I want work I believe in. I want my wife. I want you. We will have to keep deciding how those wants fit into a day, and sometimes we will be bad at it. I have seen enough of us together to want the next attempt."
{n}Anevia kisses her wife's hand before turning her own palm toward you.{/n}
"Your answer?"''',
      c('"I want to keep building a life with you both, with room for the people and work we each love."', "keep"),
      c('"I mean the promise I made. We will keep finding the days for it."', "keep")),
    n("keep", "Narrator", '''{n}You take Anevia's hand. Irabeth moves closer, leaving room for you beside them. For a while the conversation concerns the next actual evening, rather than the rest of your lives.{/n}
{n}There are other people to see and work which will not disappear. You name what you can promise; the wives do the same. Anevia changes one suggestion when Irabeth reminds her of a commitment she has already made.{/n}
{n}"Next day, then," she says. "You see? Very reasonable woman."{/n}
{n}Irabeth kisses her cheek, then looks at you.{/n}
{n}"We have things worth coming back to."{/n}
{n}You stay with them until the conversation has found a day all three can keep.{/n}''',
      c('[Keep the promise with the days you have already shared behind it.]', flags=("three_progression.developed",))),
], requires=("three_rooms_unlocked.kept",), forbids=("last_watch", "three_progression.developed"), delay=24, catchup=True)


SCENES.append(scene("ending_promised", "A promise with days still to find", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}The Commander, Anevia and Irabeth had made a promise before the war ended. They had not yet found all the days in which to discover what keeping it would ask of them.{/n}
{n}The wives remained married, with work and habits that did not vanish to make room for a third person. The Commander returned to a possibility they had chosen together, rather than a settled household waiting to be claimed.{/n}
{n}There was affection to begin from. There were conversations they had put off and things they still wanted to do. What followed would depend on the time they gave one another after the promises, when the war could no longer answer every difficult question for them.{/n}'''),
], requires=("committed",), forbids=("three_progression.developed", "closed", "irabeth_dead", "anevia_dead",
    "irabeth_gone", "anevia_gone", "swarm", "true_lich", "sacrifice", "ascended", "ascend_all",
    "ascend_alone", "ascend_areelu", "ascend_companions"), last=99, Relationship="tirabade"))

SCENES.append(scene("ending_ascend_promised", "The promise before the ascent", "Epilogue", 0, "", [
    n("end", "Narrator", '''{n}The Commander's ascent changed what an ordinary future would ask of the three. Their earlier promise did not explain how they might keep it across the distance that now divided their lives.{/n}
{n}Anevia and Irabeth kept their marriage, their work, and the right to decide what place the transformed Commander might have among them. The affection behind the earlier promise was real. Its future remained something they would have to choose together, if such a future could still be made.{/n}
{n}The wives would not allow worshipers to turn those unfinished plans into a legend of perfect devotion. They had known a person they wanted to see again. That was the account they were willing to give.{/n}'''),
], requires=("committed", "ascended"), forbids=("three_progression.developed", "closed", "irabeth_dead",
    "anevia_dead", "irabeth_gone", "anevia_gone"), last=99, Relationship="tirabade"))


def integrate(payload):
    """Apply only after all expansion scenes are appended; leave the standalone route intact."""
    by_id = {item["Id"]: item for item in payload["Scenes"]}
    for required in ("three_choose_days", "three_more_days", "three_kept_days", "three_rooms_unlocked",
                     "ending_promised", "ending_ascend_promised"):
        if required not in by_id:
            raise ValueError("Tirabade progression missing scene: " + required)
    by_id["last_watch"]["RequiresAny"] = ["three_progression.developed", "three_progression.short_chosen"]
    for ending in ("ending_together", "ending_ascend"):
        if "three_progression.developed" not in by_id[ending]["Requires"]:
            by_id[ending]["Requires"].append("three_progression.developed")
    if "ascended" not in by_id["ending_together"]["Forbids"]:
        by_id["ending_together"]["Forbids"].append("ascended")
