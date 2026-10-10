"""ER-A1-RETURN: a played, voluntary debate after the completed sitting."""
from story_format import c, n, p, scene


OPENING = "eritrice.trickster.reconciled_debate"


OPEN_TEXT = """{n}The borrowed table in Drezen has been dressed like the hall: a scroll, an uncapped inkwell, two cups, one chair drawn out. Eritrice does not sit. She stands behind her own, claws resting on its back, and the claws have left five thin pale grooves in the wood.{/n}
"The sitting is closed. The minutes are entered, and nobody has bled on them." {n}Her tail moves once behind her.{/n} "I did not come to Drezen to be thanked. I came because I am hungry for an argument I cannot win by showing claws, and you are the only creature I know who has made the chair lose a vote and walked out of the room afterwards. A private debate. My case against yours, point by point, before no Council. Say yes or say no. I shall write down which.\""""
OPEN_GRUDGE = """"First, the standing item." {n}She unrolls the older scroll and does not look at it; she has it by heart.{/n} "The Commander struck this Council unconscious and let its essences be taken. I woke on my own floor with the taste of it still in my mouth." {n}The claws sink into the chair back, all five, until the wood splits along the grain.{/n} "I have not forgiven it. I have not tabled it. I have not struck it, and if you ask me to strike it I will put your quill hand on this table beside the scroll and see what is left to hold a pen." {n}She breathes out, and the claws come free one at a time.{/n} "Entered. It stands. The offer stands beside it, and I do not lower either.\""""
EXCHANGE_TEXT = """{n}She does not wait for you to arrange your argument. She takes the quill and writes, and reads aloud what she writes, as she always has, so that the one who spoke can never say later that they were misquoted.{/n}
"First objection, entered as an honest one: that a chair who says 'contribute your essence or I will take it by force' has no standing to call a vote on it afterwards." {n}The quill stops. Her eye does not.{/n} "A fair objection. Now the chair's answer. I said it because the Worldwound was eating the Mendev border a village a week and the Council had talked for a year. I would say it again. Force and the vote are not opposed, Commander. The vote is what force looks like once it has been taught manners, and I am the one who taught it." {n}Her tail lays itself along the floor behind her, slow.{/n} "You dislike that. You are meant to dislike it. You are meant to answer it, and not with a sword."
{n}She sands the page.{/n} "Until you do, it stands unanswered in the minutes, and so does my claim. I can bear being wrong later. I cannot bear being silent now.\""""
RECORD_TEXT = """"Entered." {n}She writes the date, the hour, and beneath them, in a smaller hand, the words private debate, first sitting, unresolved. She blots it and does not show you.{/n} "Understand what this is. It is not a vote. It is not a promise. It is a record that two parties sat at one table and neither left bleeding." {n}Her lip lifts and shows a canine, not unkindly.{/n} "Yet. The next point is yours. Bring it when you are ready to lose it well.\""""


def integrate(payload):
    from storylines import eritrice_trickster as route
    if any(s["Id"] == OPENING for s in payload["Scenes"]):
        return
    payload["Scenes"].append(scene(OPENING, "", "Eritrice", 5, "Continue", [
        n("open", "Eritrice", '[PROSE PENDING: eritrice.trickster.reconciled_debate/open - offer voluntary private debate after the earned sitting; assume neither chair usurpation nor a lost native vote; retain sharp temper and return costs]',
          c('"Enter it, Madam Chair. We debate."', "exchange"),
          c('"Not at this table, and not today."', abort=True),
          paragraphs=(p(OPEN_GRUDGE,
                        requires=(route.ON_AGENDA,)),)),
        n("exchange", "Eritrice", "",
          c("Continue", "record", flags=(route.STARTED, route.MINUTES_READ, route.STRAIGHT)),
          paragraphs=(p(EXCHANGE_TEXT, requires=(route.THREAT,)),
                      p('[PROSE PENDING: eritrice.trickster.reconciled_debate/exchange - betrayal-specific exchange for a Council fight that bypassed Cue_0035; no remembered force threat; retain sharp temper, voluntary debate and return costs]', forbids=(route.THREAT,)))),
        n("record", "Eritrice", RECORD_TEXT),
    ], requires=("trickster.now", route.RETURNED, route.VISIT),
       forbids=(route.CLOSED, route.MINUTES_READ, route.DECLINED, OPENING),
       last=5, Relationship="eritrice", Areas=[route.DREZEN],
       ContactUnit=route.UNIT, InteractionHub="eritrice.presence", optional=True))
    # Book presentation may auto-start a relationship on entry. The performed
    # exchange, rather than that presentation side effect, unlocks this reading.
    point = next(s for s in payload["Scenes"] if s["Id"] == "eritrice.minutes.point_one.drezen")
    point["Requires"].append(route.MINUTES_READ)
