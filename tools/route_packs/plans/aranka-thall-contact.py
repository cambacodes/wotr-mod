# Native Thall's shy reply is heard only from his real, living island actor.
# No spawned helper, new lover, affection receipt or retroactive meeting.
THALL_CONTACT_PROPOSAL = scene("aranka.thall.answer", "The low part", "Aranka", 5,
    '"Aranka still wants you to sing. Will you?"', [
        n("start", "Thall", '''"Oh. No, I... I would rather listen."
{n}Thall lowers the scroll a little.{/n} "She is taking the songs on the road? Good. I hope they hear her. Tell her that, if you like. Not the part about singing. She will ask again."''',
          c("Continue"), speaker_unit="8fb65bd79574771429526eaef26762a9"),
    ], requires=("aranka.ran_romance", "aranka.ran_quest_complete", "aranka.extension_kept"),
    forbids=(*BLOCKED, "aranka.thall.dead"), last=5, optional=True,
    Relationship="aranka", Chapters=[5], Areas=[AREA],
    AnswerLists=[ANSWERS], ContactUnit="8fb65bd79574771429526eaef26762a9")
