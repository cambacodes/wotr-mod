"""S07: authored Ch2 acknowledgment of the native Tirabade marriage.

Fixed couple: no ladder, stance, reconciliation, return or intimacy producer.
Contract and reopened native evidence: tools/route_packs/harem/S07.md.
Direct contact guards are deliberate: household Participants require committed
eligibility, which cannot be required before the Ch3 page offer.
"""
from story_format import c, n, scene

ID = "household.pair.anevia_irabeth.ack"
ANEVIA = "ea562adea1736874c9c5616d140fe773"
IRABETH = "d1e567736abf23943b9f041ba7a0bc23"
HUB = "871af36f2ab2b1f40b5de77976c54276"
CAMP = "7a25c101fe6f7aa46b192db13373d03b"

SCENES = [scene(
    ID, "The dispatch that waits until morning", "Irabeth", 2,
    '"Have I interrupted something, Irabeth?"', [
        n("start", "Irabeth", '''{n}Irabeth folds a dispatch as Anevia comes up beside her. Her wife catches the corner before she can seal it.{/n}
"Not the names, Beth. If this falls into a cultist's hands, they'll have my people strung up before we reach Drezen," {n}Anevia says.{/n}
"The patrol needs to know whom to meet," {n}Irabeth says.{/n}
"They'll know the sign. Put that in," {n}Anevia answers.{/n}
{n}Irabeth reads the dispatch again, then strikes out a line.{/n}
"You are right. I will tell the patrol leader myself."
{n}Anevia releases the paper, but stays close. Irabeth looks up at you.{/n}
"Was there something you needed, Commander?"''',
          c('"Only a moment. I can leave you and your wife to it."', "wives"),
          c('"Does the Eagle Watch always argue over its dispatches?"', "dispatch"),
          c('[Later.]', abort=True), portrait="Irabeth"),
        n("dispatch", "Anevia", '''"Only the ones that'll get somebody killed. The others we argue over at supper."
"You make it sound as though I bring work home every evening," {n}Irabeth objects.{/n}
"You brought a patrol map to bed," {n}Anevia says.{/n}
{n}Irabeth's ears redden.{/n}
"Once," {n}Irabeth mutters.{/n}
"And I folded it up and put it under your boots. Very delicate operation. Didn't lose a single soldier," {n}Anevia says.{/n}
{n}Irabeth gives her wife a reproachful look. Anevia grins back, entirely unrepentant.{/n}''',
          c('"Then I had better leave before you bring out another map."', "wives"),
          portrait="Anevia"),
        n("wives", "Irabeth", '''"Thank you. The dispatch can wait until morning. The patrol is not leaving before then."
"Hear that?" {n}Anevia slips her hand into her wife's.{/n} "I've got witnesses."
{n}Irabeth turns toward her.{/n}
"And you will eat with me before you disappear after your scouts."
"A proper meal? Or that heel of bread you've been guarding?" {n}Anevia peers at the dispatch pile.{/n}
"A proper meal. I was guarding it from you," {n}Irabeth replies.{/n}
{n}Anevia laughs and pulls her down for a quick kiss. Irabeth returns it, then tucks the unfinished dispatch beneath the map.{/n}
"Good evening, Commander."
{n}She leaves with her wife, still holding her hand.{/n}''',
          c('[Leave them to their evening.]', flags=(ID + ".marriage_acknowledged",)),
          portrait="Irabeth"),
    ], forbids=("anevia.closed", "irabeth.closed", "closed",
                 "anevia_dead", "anevia_gone",
                 "irabeth_dead", "irabeth_gone", "inhuman"),
    last=2, optional=True, Relationship="household", Chapters=[2],
    Areas=[CAMP], AnswerLists=[HUB], ContactUnit=IRABETH,
    AdditionalContactUnits=[ANEVIA], RestAllowance="household.protected",
    HouseholdCategory="protected", HouseholdWitness=ID)]
