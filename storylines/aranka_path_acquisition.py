"""Design-only contracts for path-specific Aranka contact.

Nothing in this file is registered by the story loader.
The authored invitations become usable only after a runtime contact producer is implemented.
"""

PATH_FLAGS = {
    "angel": "angel",
    "aeon": "aeon",
    "azata": "azata",
    "demon": "demon",
    "devil": "devil",
    "gold_dragon": "dragon",
    "legend": "legend",
    "lich": "lich",
    "swarm": "swarm",
    "trickster": "trickster",
}

PATH_ETUDES = {
    "angel": "3a82aba4de71b89458ac82949ed957c4",
    "aeon": "3a040afde22f4b742a2f607354ab17e7",
    "azata": "d3b47e973d65c6c46af1cce815d1f6ce",
    "demon": "9a3739370f84b0b4196d0e4d326ea3a8",
    "devil": "a1db9daf676b36f4d99c6a788a0fe1af",
    "gold_dragon": "9b193d30c89a20b409fd3dda9bd109bf",
    "legend": "c6165efcd5571c442ae38d7c0601f2df",
    "lich": "11fc5662e0ce8074ea145a022282b879",
    "swarm": "439e63fed37f52048887d98f99255e40",
    "trickster": "9f486a9c0c9abfc4a952bb22e88a7e96",
}

CONTACT_PROOF = "aranka.path_contact_verified"
REQUIRED_CHAPTER = 5
PARENT_ROMANCE = "aranka.ran_romance"
PARENT_QUEST = "aranka.ran_quest_complete"
PARENT_FAILURE = "aranka.ran_failure"
PARENT_CLOSED = "aranka.extension_closed"

# Every invitation is an optional contact scene, never an affection or romance-state award.
# `source_hook` is the proposed producer. The unresolved producer means no scene is live.
PATH_INVITATIONS = {
    "angel": {
        "entry_requires": ("angel", CONTACT_PROOF),
        "source_hook": "A surviving Desnan pilgrim carries Aranka's sealed reply from the island; verify the pilgrim and the message in the active save before delivery.",
        "invitation": "The letter asks whether you can meet as the person who chose mercy when anger would have been easier. It promises no absolution and asks for no confession.",
        "availability": "Design only. The game script evidence does not establish an Angel-to-Aranka correspondent or a universal post-Island route.",
    },
    "aeon": {
        "entry_requires": ("aeon", CONTACT_PROOF),
        "source_hook": "A dated, ordinary courier route carries Aranka's request; an Aeon intervention may preserve the route's appointment, but cannot summon Aranka from an unverified location.",
        "invitation": "She asks for one conversation without a verdict about what either of you must become. If your answer is no, she will not ask the question again through another timeline.",
        "availability": "Design only. No inspected native clue identifies an Aeon courier, appointment or safe contact event.",
    },
    "azata": {
        "entry_requires": ("azata", "native.aranka_island_actor_live"),
        "source_hook": "Reuse the installed Azata Island Aranka and the existing romance/island route without adding another invitation or actor.",
        "invitation": "The existing island conversation remains the entry. This module must not duplicate it or relax its live-unit and area checks.",
        "availability": "The native route is evidenced for Azata. Runtime actor timing and scene attachment still need an in-game save check.",
    },
    "demon": {
        "entry_requires": ("demon", CONTACT_PROOF),
        "source_hook": "Only a verified living Aranka or her explicit letter can initiate contact after the Demon route's confrontation history; no dream, captive or enemy actor may stand in for her.",
        "invitation": "She asks whether you can listen without turning the meeting into a contest of appetite. You may answer plainly, refuse, or leave the letter unanswered.",
        "availability": "Design only. The parent romance has Demon exclusions and the native Aranka evidence does not prove her survival or willingness after those outcomes.",
    },
    "devil": {
        "entry_requires": ("devil", CONTACT_PROOF),
        "source_hook": "A verified post-contract sender must deliver the invitation without a contract clause, obligation, or leverage over Aranka.",
        "invitation": "She names the bargain plainly and asks you to meet her outside its terms. The reply can be no without penalty, favor owed or later pursuit.",
        "availability": "Design only. Existing Devil deception and contract histories block the island continuation; neither proves Aranka remains available for a new contact route.",
    },
    "gold_dragon": {
        "entry_requires": ("dragon", CONTACT_PROOF),
        "source_hook": "A verified witness to the Chapter 5 island events carries her message; do not infer Aranka is in Drezen because the Dragon path is active.",
        "invitation": "She asks to meet without making your change of form or purpose the subject of the whole evening. Curiosity is welcome; inspection is not.",
        "availability": "Design only. The inspected sources do not establish a Dragon-path Aranka placement or messenger.",
    },
    "legend": {
        "entry_requires": ("legend", CONTACT_PROOF),
        "source_hook": "A confirmed living correspondent uses a mundane route that does not depend on mythic power or the Azata island; delivery is verified before showing the scene.",
        "invitation": "She asks for an evening where neither of you has to become a symbol. She offers a real meeting and an easy refusal, not a promise to repair everything the path changed.",
        "availability": "Design only. The native island mechanics are nested under PlayerIsAzata, so Legend cannot inherit that location by alias.",
    },
    "lich": {
        "entry_requires": ("lich", CONTACT_PROOF),
        "source_hook": "Require a verified living Aranka and an explicit response to a risk disclosure; a body, memory or reanimation proxy cannot provide consent.",
        "invitation": "She says she knows what your path costs and will not pretend the cost disappears because she misses you. She asks if you can meet without demanding she bless what you have become.",
        "availability": "Design only. The parent continuation blocks high-level Lich; contact and consent after Lich outcomes are not established by inspected native records.",
    },
    "swarm": {
        "entry_requires": ("swarm", CONTACT_PROOF),
        "source_hook": "No route is eligible unless a runtime audit confirms Aranka is alive, herself, free to answer, and independently willing; never fabricate a swarm copy or use a dead character's recorded lines as consent.",
        "invitation": "If those proofs exist, Aranka may send one refusal or invitation in her own voice. Silence is the default when identity or agency cannot be established.",
        "availability": "Unresolved and presumptively unavailable. The inspected sources provide no credible survival/contact proof under Swarm, so this must remain closed unless new game-script evidence supports it.",
    },
    "trickster": {
        "entry_requires": ("trickster", CONTACT_PROOF),
        "source_hook": "The Trickster prepares a one-use, in-world chain of evidence and couriers that reaches the actual Aranka, then waits for her uncoerced reply; it must not set PlayerIsAzata, teleport a clone, or set romance state.",
        "invitation": "The note admits that a route was made where the world had left none, then asks Aranka whether she wants to use it. She controls whether to answer, meet, or close the route.",
        "availability": "Design only. The existing Chapter 2 and 3 parent intro branches require Azata acceptance, and the island is native Azata content. This does not solve Trickster romance acquisition.",
    },
}

ENTRY_FORBIDS = ()


def invitation_entry_ready(path, chapter, flags):
    """Return whether a runtime adapter may show this path's invitation."""
    route = PATH_INVITATIONS.get(path)
    if chapter != REQUIRED_CHAPTER or route is None or route["availability"].startswith("Unresolved"):
        return False
    if any(flags.get(alias, False) for other, alias in PATH_FLAGS.items() if other != path):
        return False
    if any(flags.get(flag, False) for flag in ENTRY_FORBIDS):
        return False
    return all(flags.get(flag, False) for flag in route["entry_requires"])


def _self_check():
    """Exercise predicate contracts with synthetic flags; this is not an integration test."""
    for path in PATH_FLAGS:
        route = PATH_INVITATIONS[path]
        state = {key: True for key in route["entry_requires"]}
        assert invitation_entry_ready(path, REQUIRED_CHAPTER, state) is (path != "swarm")
        for required in route["entry_requires"]:
            assert not invitation_entry_ready(path, REQUIRED_CHAPTER, {key: True for key in route["entry_requires"] if key != required})
    assert not invitation_entry_ready("trickster", REQUIRED_CHAPTER - 1, {"trickster": True, CONTACT_PROOF: True})
    assert not invitation_entry_ready("trickster", REQUIRED_CHAPTER, {"trickster": True})
    assert not invitation_entry_ready("trickster", REQUIRED_CHAPTER, {"trickster": True, "angel": True, CONTACT_PROOF: True})


if __name__ == "__main__":
    _self_check()
