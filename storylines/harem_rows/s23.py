"""S23's authorized historical acknowledgment; settlement remains blocked.

Authored addition, not a native encounter. The reviewed A.md sheet reserves
settlement/retry IDs but explicitly withholds their concessions and recovery.
No successful negotiation, live Herrax reply, attitude or intimacy is emitted.
The coordinator must call register after the household/attendance adapters.
"""
from story_format import c, n, scene

PREFIX = "household.pair.herrax_chivarro."


def register(payload, scenes, refs):
    """Append the no-reply history root without touching either solo route."""
    sid = PREFIX + "turf"
    if any(body["Id"] == sid for body in scenes):
        raise ValueError("S23 already registered: " + sid)
    scenes.append(scene(
        sid, "The turf named twice", "Chivarro", 5,
        '"Herrax asked me to kill you."', [
            n("start", "Chivarro", '''{n}Chivarro digs a claw into the Table's cloth. Through the tavern window, a wounded crusader limps after the quartermaster's cart.{/n}
"And here I am. How disappointing for her."
{n}She leans across the table, baring her teeth.{/n}
"Herrax can call the Delights her turf. She has my floor, my customers — and now she wants my corpse. Do you think she'll stop wanting it because you brought me a chair?"''',
              c('"Your quarrel remains unsettled."', "historical"),
              c('[Later.]', abort=True), portrait="Chivarro"),
            n("historical", "Chivarro", '''"Then don't carry her generosity into my house. Let her keep her customers. I remember which of them watched me leave."
{n}Chivarro releases the cloth. A strip of it hangs from her claw; she drops it into the empty chair beside her.{/n}
"That's all she gets of me today."''',
              c("Continue", flags=(PREFIX + "turf.seen", PREFIX + "historical")),
              portrait="Chivarro"),
        ],
        requires=("trickster", "foresight.page_taken", "household.stance_eligible",
                  "household.table.kept", "herrax.asked_kill_chivarro",
                  "participant.chivarro.available", "chivarro.present_now",
                  "minagho_chivarro.trickster.chivarro_in"),
        forbids=("trickster.failed", "fool_king.gone", PREFIX + "turf.seen",
                 "minagho_chivarro.trickster.chivarro_declined", "sacrifice"),
        last=5, Relationship="household", Chapters=[5],
        Areas=["2570015799edf594daf2f076f2f975d8"],
        InteractionHub="household.table", Participants=["minagho_chivarro"],
        ParticipantWomen=["chivarro"], RestAllowance="household.protected",
        HouseholdCategory="protected", HouseholdWitness=PREFIX + "turf.seen",
        ForbidOverrides={"sacrifice": "trickster.commander_back"},
    ))
    payload.setdefault("ForesightConsumers", {})[sid] = "foresight.page_taken"
