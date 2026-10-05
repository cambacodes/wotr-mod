"""Narrated living-pair continuation after actual RanRomance Book 3 terminals.

The visits author travel and meetings in book format; they do not spawn native units.
Parent romance, service, departure, death and reunion histories remain read only.
All newly introduced performers, assistants and business contacts are adults.
"""
from copy import deepcopy
from story_format import c, n, scene

DREZEN = "2570015799edf594daf2f076f2f975d8"
ETUDES = {
    "minagho.ran_banner": "4a29c758798d47a1a32f506d1ca6081b",
    "minagho.ran_conscience": "813cc79c053d4b3e869a0d0ca2f3d85d",
    "minagho.ran_freed": "f18391398cb5470c94f8932e9d8d2fd7",
    "minagho.ran_demon": "58557969a797441983022c8ba0400400",
    "minagho.ran_legend": "a87da83417ff4be28c9ccfaf9b154e96",
    "minagho.ran_dragon": "e303c58d307849cd892fa5810124da92",
    "minagho.ran_sanctuary": "1e6ca1514807446ea2fddd65e4f5bcc8",
    "minagho.ran_romance": "b5c19cd01e364df99f6c946c7da14751",
    "minagho.ran_cult": "3d21fa8120d040338ec1d4b8461fa536",
    "minagho.ran_redemption": "592dcdccbef043f58031fa234faf137a",
    "minagho.dead": "3b8c0801d5e9a694b848ee13564d2ad7",
    "chivarro.dead": "fd2ab9b67ce3e284184b1894c82c6c5d",
    "chivarro.searching": "71f85264d9064074f9cf74999ecbffa9",
}
COMPLETED_QUESTS = {"minagho.ran_complete": "5cd5f22437a1465180b45c080899577a"}
SEEN_CUES = {
    "minagho.book_three_finished": ["19099aba216e46e98d446709c3f2e0f3", "5584da70433e4f079d521d40ce77f230", "c01f7f83a2584555b2f551918f169cdb", "4dbb41f1fb134b90ab3900dc05488e8f", "c51a76731dc24865b6c472ffe6bf3e18", "341b62dd58d14906959d3262b12f1a43", "98baa5299ae444bfa1ac8ba8e84f2c7c"],
    "minagho.accepted_final": ["5584da70433e4f079d521d40ce77f230", "c01f7f83a2584555b2f551918f169cdb", "4dbb41f1fb134b90ab3900dc05488e8f"],
    "minagho.rejected_final": ["c51a76731dc24865b6c472ffe6bf3e18", "341b62dd58d14906959d3262b12f1a43", "98baa5299ae444bfa1ac8ba8e84f2c7c"],
    "minagho.chivarro_scrolls_reported": ["e15de525c99d40c6a6faf0afa61be756"],
    "minagho.brand_trick_seen": ["a8f7a881cc6d427b91cbbee14f43e0ee"],
}
# Proposed parent cue edit contract for independent review and root integration.
# Preserve each original page selector, cue condition and nonlisted cue verbatim.
# Apply each edit only in its earned Requires scope; None suppresses that cue alone.
# Actual death/erased-history arbitration must run before these living-history edits.
# Text below replaces mixed relationship/consequence cues while retaining their
# political, divine, draconic and service outcomes. It earns no new word credit.
PARENT_EPILOGUE_EDITS = {
    "c47829fba057400c8e0279990be3d25e": dict(ParentKey="056942f6-32d0-4480-8ff7-29356b43db19", Text="Far from Golarion, Minagho and Chivarro were seen together on another plane. Their search for each other had ended before the final battles of the Fifth Crusade; the worlds beyond it gave their old rivalry and attachment a wider field."),
    '819314e916514a498a8e336371b4788e': dict(ParentKey='RanRomMinaSlide0001Cue0003.Text', Text=None),
    '9bfbb3f217ca476cadbeffc4d389717d': dict(ParentKey='RanRomMinaSlide0001Cue0004.Text', Text=None),
    'd6b960c14e37492682de6284af1c5417': dict(ParentKey='RanRomMinaSlide0001Cue0007.Text', Text=None),
    '19fd9027465f4cbebe949b26d04a2826': dict(ParentKey='RanRomMinaSlide0001Cue0008.Text', Text=None),
    '59cf28c3824944fd88547bc61bc5cf62': dict(ParentKey='RanRomMinaSlide0001Cue0011.Text', Text=None),
    '92162854b221413984468d2663ffcffb': dict(ParentKey='RanRomMinaSlide0001Cue0012.Text', Text=None),
    'cce5f180fbe7455989544c1c81428463': dict(ParentKey='RanRomMinaSlide0002Cue0007.Text', Text=None),
    '829c837c76f6429fa01d3d2583069b35': dict(ParentKey='RanRomMinaSlide0002Cue0008.Text', Text=None),
    '51104e1c8755436e8aa290a6cedfcb3a': dict(ParentKey='RanRomMinaSlide0002Cue0011.Text', Text=None),
    'fb32a8f9c464496abe90307c68ec271e': dict(ParentKey='RanRomMinaSlide0002Cue0012.Text', Text=None),
    '5ab5c6a3c62b4f2ba88053cbbbc47737': dict(ParentKey='RanRomMinaSlide0003Cue0003.Text', Text=None),
    'dc14cdafb9fa43e8bc3b0816626b3dbe': dict(ParentKey='RanRomMinaSlide0003Cue0004.Text', Text=None),
    'f37b7a5fcff84551b86ecbba823e2fa5': dict(ParentKey='RanRomMinaSlide0003Cue0007.Text', Text=None),
    '982627a0bbd34fe4b16b5b078e56355a': dict(ParentKey='RanRomMinaSlide0003Cue0008.Text', Text=None),
    '784575a522e64ad58f2171abcb073d0c': dict(ParentKey='RanRomMinaSlide0004Cue0003.Text', Text=None),
    '5db846019acd46ef83f12be220727f50': dict(ParentKey='RanRomMinaSlide0004Cue0004.Text', Text=None),
    '9e3bd8247f0c40eba62368fe2912bb84': dict(ParentKey='RanRomMinaSlide0004Cue0007.Text', Text=None),
    '18d22b6258a24fe29dd9d0ea4235432e': dict(ParentKey='RanRomMinaSlide0004Cue0008.Text', Text=None),
    '8009e775a3a343c79ef4e40d72bc5e6a': dict(ParentKey='RanRomMinaSlide0005Cue0007.Text', Text=None),
    '5b0a132d97404072b3d664899871d7b7': dict(ParentKey='RanRomMinaSlide0005Cue0008.Text', Text=None),
    'd6714bd8d48e425d862f854018cb123c': dict(ParentKey='RanRomMinaSlide0007Cue0003.Text', Text=None),
    'ff2042ad95e14b73a5f75f2cfd84b5e4': dict(ParentKey='RanRomMinaSlide0007Cue0004.Text', Text=None),
    'a875684118e64d7ab29f70ca3460c365': dict(ParentKey='RanRomMinaSlide0002Cue0003.Text', Text="To Minagho's surprise, her efforts and her connection with the Commander led to her selection as the church's first leader. She retained a sharp interest in which factions invoked the Commander's name and what they expected to gain by doing so."),
    '9a5eb7aff04943c28da2260aac68874e': dict(ParentKey='RanRomMinaSlide0002Cue0004.Text', Text="To Minagho's surprise, her efforts and her connection with the Commander led to her selection as the church's first leader. Chivarro became her right hand in the church."),
    'a1774d0a9fb34fd2ac58abc1c6db55bd': dict(ParentKey='RanRomMinaSlide0005Cue0002.Text', Text="Chivarro joined Minagho in the new realm without accepting that Minagho's service placed the same bond upon her. Her own dealings there remained hers to negotiate."),
    'd47984953fc74c488ef0a02588bde92b': dict(ParentKey='RanRomMinaSlide0005Cue0003.Text', Text="Minagho continued masterminding schemes in the mortal realm to expand the Commander's influence beyond the Sarkoris Scar. The service under which she worked remained distinct from any affection she expressed."),
    'b474eb4460cb42729be2717d05e7d42b': dict(ParentKey='RanRomMinaSlide0005Cue0004.Text', Text="Minagho continued masterminding schemes in the mortal realm to expand the Commander's influence beyond the Sarkoris Scar. Chivarro kept her own dealings and could assist Minagho without acquiring her service bond or an unchosen role in the Commander's bed."),
    '2cd9538f67f7414d808d9032386f6be9': dict(ParentKey='RanRomMinaSlide0005Cue0006.Text', Text="Chivarro remained close to Minagho and assisted schemes she chose to support. Minagho's service did not make Chivarro another servant, and Chivarro did not allow her own affection to be cited as proof that the bond had disappeared."),
    '64afcd565e044e53977e1878444f4ee1': dict(ParentKey='RanRomMinaSlide0006Cue0003.Text', Text="Minagho joined the Commander in the divine realm. Remnants of her former master's presence still troubled her, but with the Commander's help she mastered the draconic soul awakened through the dragons' teaching. A female dragon was later seen accompanying the Commander through the realm."),
    'b9e2550bc7244f6c8480106b41667d96': dict(ParentKey='RanRomMinaSlide0006Cue0004.Text', Text="Minagho and Chivarro joined the Commander in the divine realm. With the Commander's help they learned to master their draconic souls, though the remnants of Minagho's former master's presence still troubled her. Two female dragons were later seen accompanying the Commander through the realm."),
    'bb49f54dc0a547c287238b5d7d8489b3': dict(ParentKey='RanRomMinaSlide0006Cue0005.Text', Text='Minagho continued studying her draconic soul after the Fifth Crusade. Years later, stories described the Commander teaching a delighted female dragon to fly.'),
    '5831af75932d43ed902a2d8def2adf3d': dict(ParentKey='RanRomMinaSlide0006Cue0006.Text', Text='Minagho and Chivarro continued studying their draconic souls after the Fifth Crusade. Years later, stories described the Commander teaching two delighted female dragons to fly.'),
    '8399dbc5987b462594b2b4168764e269': dict(ParentKey='RanRomMinaSlide0007Cue0002.Text', Text="Chivarro remained beside Minagho after their earlier reunion. Minagho's decision to stay among mortals gave the two women new things to argue about and a life neither had fully imagined when their search for each other began."),
}

# Every alternate gets a private addon key; ParentKey is evidence, never a key to mutate.
PARENT_EPILOGUE_EDITS["5787f92575364c1459df8f075676c2db"] = deepcopy(PARENT_EPILOGUE_EDITS["c47829fba057400c8e0279990be3d25e"])
for cue_guid, edit in PARENT_EPILOGUE_EDITS.items():
    edit["Requires"] = ["minachiv.arrival_kept" if cue_guid in {
        "c47829fba057400c8e0279990be3d25e", "8399dbc5987b462594b2b4168764e269",
        "5787f92575364c1459df8f075676c2db",
    } else "minachiv.invitation_kept"]
    edit["LocalizedKey"] = "Tirabade.Minachiv.ParentEnding." + cue_guid
    edit["Owner"] = "Epilogue"
    edit["Forbids"] = ["minagho.dead", "chivarro.dead"]

# Apply only in the ordinary epilogue sequence after a matching addon loss page
# is available or already played. Evaluation failure leaves the original intact.
# Never use sacrifice as either woman's death or apply these rules to Aeon.
# Loss rules supersede ordinary edits. SuppressCues hides originals, while each
# SurvivorAlternate retains that original cue's conditions and list position.
# Original page order, selectors and OnShow actions remain unchanged.
PARENT_EPILOGUE_LOSS_RULES = [{'Id': 'both_lost',
  'Owner': 'Epilogue',
  'Requires': ['minachiv.invitation_kept', 'minagho.dead', 'chivarro.dead'],
  'Forbids': [],
  'ReplacementScenes': ['minachiv.ending_both_lost', 'minachiv.ending_both_lost_completed'],
  'SuppressPages': ['951e4432cf844a36a8a222b27589fb43',
                    '6db8635856e74b6cac46330bd82b4ff5',
                    '8df5edb6f69040c69d7da78d2bf20cb6',
                    '5a5865ceca0e42049288351a76b18ba9',
                    '126762ac92364ac5bdec69c6e3fdfd1a',
                    '01677da8df6e42c6b4803ceef524b1fe',
                    '9c5c5825bf3245d0ae763c6e69ecdc38',
                    '3792457f35734d75a4d4b53055f7f5d0',
                    '5c95d8e3fa4f3b44896914987cb04b0b'],
  'SuppressCues': [],
  'Survivor': None,
  'SurvivorAlternates': {}},
 {'Id': 'minagho_lost',
  'Owner': 'Epilogue',
  'Requires': ['minachiv.invitation_kept', 'minagho.dead'],
  'Forbids': ['chivarro.dead'],
  'ReplacementScenes': ['minachiv.ending_minagho_lost', 'minachiv.ending_minagho_lost_completed'],
  'SuppressPages': ['951e4432cf844a36a8a222b27589fb43',
                    '6db8635856e74b6cac46330bd82b4ff5',
                    '8df5edb6f69040c69d7da78d2bf20cb6',
                    '5a5865ceca0e42049288351a76b18ba9',
                    '126762ac92364ac5bdec69c6e3fdfd1a',
                    '01677da8df6e42c6b4803ceef524b1fe',
                    '9c5c5825bf3245d0ae763c6e69ecdc38',
                    '3792457f35734d75a4d4b53055f7f5d0',
                    '5c95d8e3fa4f3b44896914987cb04b0b'],
  'SuppressCues': [],
  'Survivor': 'Chivarro',
  'SurvivorAlternates': {}},
 {'Id': 'chivarro_lost',
  'Owner': 'Epilogue',
  'Requires': ['minachiv.invitation_kept', 'chivarro.dead'],
  'Forbids': ['minagho.dead'],
  'ReplacementScenes': ['minachiv.ending_chivarro_lost', 'minachiv.ending_chivarro_lost_completed'],
  'SuppressPages': ['5c95d8e3fa4f3b44896914987cb04b0b'],
  'SuppressCues': ['e87b43c31c1c4253a7137c7d6c05b246',
                   '9bfbb3f217ca476cadbeffc4d389717d',
                   '7edf5529523a4a9da520138783fdeb93',
                   '19fd9027465f4cbebe949b26d04a2826',
                   'f5e580bedafc43f3acb6843fd71d8120',
                   '92162854b221413984468d2663ffcffb',
                   '6eba6f627ac34cf4955c89e5ad59e106',
                   '9a5eb7aff04943c28da2260aac68874e',
                   '9806218e467f41acb502b52160ab38dd',
                   '829c837c76f6429fa01d3d2583069b35',
                   '3b8d47b3c9694002aff26510ac4dedf0',
                   'fb32a8f9c464496abe90307c68ec271e',
                   'a77e415c6eb44d719839e07a3f164d87',
                   '0a8411c2cb0a44f1ab317ed425f6ec94',
                   'dc14cdafb9fa43e8bc3b0816626b3dbe',
                   'acb0d15ef71c410484b7c37b270e30fe',
                   '982627a0bbd34fe4b16b5b078e56355a',
                   '67e3bb3b649d42a4a84115f3c7ac6bf1',
                   '286434b491b74174a97dfd2d7344f57a',
                   '5db846019acd46ef83f12be220727f50',
                   '3d4137f1cf98459f996ef1da83737cdb',
                   '18d22b6258a24fe29dd9d0ea4235432e',
                   'a1774d0a9fb34fd2ac58abc1c6db55bd',
                   'b474eb4460cb42729be2717d05e7d42b',
                   '2cd9538f67f7414d808d9032386f6be9',
                   '5b0a132d97404072b3d664899871d7b7',
                   '0b1b31d7125547219daa747eba45a063',
                   '85b479a3da8a4fa6b602fedf89201695',
                   'b9e2550bc7244f6c8480106b41667d96',
                   '5831af75932d43ed902a2d8def2adf3d',
                   '8399dbc5987b462594b2b4168764e269',
                   'ff2042ad95e14b73a5f75f2cfd84b5e4',
                   '1980e50e5e204431bf643fbad487909f',
                   'c47829fba057400c8e0279990be3d25e',
                   '5787f92575364c1459df8f075676c2db'],
  'Survivor': 'Minagho',
  'SurvivorAlternates': {'9a5eb7aff04943c28da2260aac68874e': {'Text': "To Minagho's surprise, her efforts "
                                                                      'and her connection with the Commander '
                                                                      "led to her selection as the church's "
                                                                      'first leader. She retained a sharp '
                                                                      'interest in which factions invoked '
                                                                      "the Commander's name and what they "
                                                                      'expected to gain by doing so.',
                                                              'LocalizedKey': 'Tirabade.Minachiv.Survivor.9a5eb7aff04943c28da2260aac68874e'},
                         'b474eb4460cb42729be2717d05e7d42b': {'Text': 'Minagho continued masterminding '
                                                                      'schemes in the mortal realm to expand '
                                                                      "the Commander's influence beyond the "
                                                                      'Sarkoris Scar. Her service remained '
                                                                      'unresolved.',
                                                              'LocalizedKey': 'Tirabade.Minachiv.Survivor.b474eb4460cb42729be2717d05e7d42b'},
                         'b9e2550bc7244f6c8480106b41667d96': {'Text': 'Minagho joined the Commander in the '
                                                                      'divine realm. Remnants of her former '
                                                                      "master's presence still troubled her, "
                                                                      "but with the Commander's help she "
                                                                      'mastered her draconic soul. A female '
                                                                      'dragon was later seen accompanying '
                                                                      'the Commander through the realm.',
                                                              'LocalizedKey': 'Tirabade.Minachiv.Survivor.b9e2550bc7244f6c8480106b41667d96'},
                         '5831af75932d43ed902a2d8def2adf3d': {'Text': 'Minagho continued studying her '
                                                                      'draconic soul after the Fifth '
                                                                      'Crusade. Years later, stories '
                                                                      'described the Commander teaching a '
                                                                      'delighted female dragon to fly.',
                                                              'LocalizedKey': 'Tirabade.Minachiv.Survivor.5831af75932d43ed902a2d8def2adf3d'}}}]

RELATIONSHIP = dict(Title="The company they choose", Description="Minagho and Chivarro have unfinished business with an old acquaintance. Each has her own reason for asking me to stay.", Objective="Answer their invitation", Guidance="After completing Minagho's RanRomance Book 3, return to Drezen in Chapter 5. Both women must be alive, and Chivarro must have begun her search for Minagho. These optional book visits arrive between rests and can also be read from the mod's available events.", StartedFlag="minachiv.started", ClosedFlag="minachiv.closed", CommittedFlag="minachiv.complete", UnavailableFlags=["minagho.dead", "chivarro.dead", "inhuman"], FailureFlags=[])
SCENES = []
BLOCKERS = ("minachiv.closed", "minagho.dead", "chivarro.dead", "inhuman")


def done(*flags):
    return tuple("minachiv." + flag for flag in flags)


def s(id, title, nodes, previous=None, delay=24):
    for page in nodes:
        page["Portrait"] = page["Speaker"] if page["Speaker"] in ("Minagho", "Chivarro") else ""
        if id == "the_entrance_she_wants" and page["Id"] == "warm":
            page["Portrait"] = "ChivarroWarm"
    SCENES.append(scene("minachiv." + id, title, "Memory", 5, title, nodes,
        requires=("minagho.ran_complete", "minagho.book_three_finished", "minachiv.reunion_history") + (("minachiv." + previous,) if previous else ()),
        forbids=BLOCKERS, delay=delay, optional=True, Relationship="minagho_chivarro", Remote=True,
        Areas=[DREZEN], Chapters=[5]))


s("two_answers", "A message with two answers", [
    n("start", "Narrator", '''{n}A folded note reaches you in Drezen. The outside bears a name you know rather better without its human disguise. Mina. Inside, Minagho has drawn a little skull beside a time and an address in the damaged quarter. Below that, in another hand, someone has written, "If this is her idea of a reassuring invitation, bring your own judgment."
The address is a room above a shuttered gaming house. You find Minagho there after dusk, wearing the blonde woman's shape she used for your earlier meetings. She turns the note over when you put it down.{/n}
"She insisted on seeing what I wrote. Then she insisted on making it worse. I was almost nostalgic."
"Chivarro?"
"She has answered. We have arranged how she will reach me. Separately, and with rather more caution than my little drawing suggests."
{n}Minagho drops the disguise. The room has no street-facing window. She chose it for that reason.{/n}
"I rented this for a few meetings. Do not infer that I have settled down and begun collecting respectable neighbors. One of them tried to sell me a history of the siege. He was wonderfully inaccurate about me."''',
      c('"What does Chivarro want from this meeting?"', "reply"),
      c('[Put the invitation aside for another evening.]', abort=True)),
    n("reply", "Minagho", '''"To see me. To find out whether your victory has made you insufferable. To discuss someone who owes her something. In that order, though she will pretend the last is first."
{n}She unfolds a second sheet. The writing is small and exceptionally controlled.{/n}
"Listen to this. 'I shall not arrive as the grateful dependent in whatever account you have given of me.' A whole line wasted saying something I knew."
"Is she your dependent?"
"Try asking her that. I want to watch."
{n}For a moment Minagho's amusement warms into an expression she does not offer the street outside.{/n}
"She has lost a great deal. She will not thank you for speaking softly around the empty places. Neither shall I. We can have a perfectly tolerable evening without pretending any of us has become harmless."''',
      c('"You told me you had already spoken through scrolls."', "scrolls", requires=("minagho.chivarro_scrolls_reported",)),
      c('"Have you agreed what you are asking of me?"', "asking")),
    n("scrolls", "Minagho", '''"Yes. Those conversations were ours. This reply is about a meeting that includes you."
{n}She folds the smaller sheet along its existing crease.{/n}
"She knows I have spoken about her. I spared her a recitation. If she wants your version, she will ask you herself. I recommend the truth. It will save you having to remember which of us you lied to first."
"You give that advice often?"
"Only when lying would make my evening more tedious."''', c('"Then tell me what is settled."', "asking")),
    n("asking", "Minagho", '''"Very little. She has agreed to meet. You may agree to meet. It is a remarkable quantity of agreement for people with our histories."
{n}She draws the empty chair away from the table with one foot, leaving you room to sit beside her or opposite.{/n}
"There is someone called Veyr who used to arrange introductions for her. Not a friend. Friends cost less and complain more honestly. He has heard that she is looking for a new foothold and offered one. He also knows that she has found me."
"A threat?"
"He has the manners to call it an opportunity. Chivarro thinks it may be both. I think he has discovered an excellent way to get himself killed. She wants to speak before I demonstrate."
{n}Minagho waits while you choose your chair.{/n}''',
      c('"And what about us?"', "past", requires=("minagho.ran_romance", "minagho.accepted_final")),
      c('"Our last conversation ended with a refusal. This invitation does not change that by itself."', "refusal", requires=("minagho.rejected_final",), forbids=("minagho.ran_romance",)),
      c('"I will meet her and hear this offer."', "agreement")),
    n("past", "Minagho", '''"I remember. You needn't introduce yourself again."
{n}She leans toward you, then stops before the small distance between your chairs closes.{/n}
"But I am not sending Chivarro a place setting and telling her she has acquired a lover. She has opinions about that sort of surprise. Some are fatal."
"Do you want me there?"
"Yes. For reasons I have already been foolish enough to let you hear. Also because the two of you are likely to disagree about something, and I have missed enjoying myself without an assassin interrupting."
{n}Her hand rests on the table near yours. She leaves the remaining distance to you.{/n}''', c('"Then I will come."', "agreement")),
    n("refusal", "Minagho", '''"I heard you the first time."
{n}Her answer comes quickly. A little too quickly for indifference.{/n}
"There are other uses for your company. You know what happened to me. Chivarro knows what happened before you. Veyr will find it harder to sell each of us a different version if we are in the same room."
"And afterward?"
"We can discover whether conversation alone is as exhausting as I remember. If you surprise me, I shall pretend I expected it."''', c('"A meeting, then."', "agreement")),
    n("agreement", "Minagho", '''{n}Minagho writes the agreed hour on the back of Chivarro's reply. She folds it into a narrow packet and pockets it.{/n}
"She will come by a route she chose. No procession, no announcement, and no one escorting her through the city as proof that I have been rewarded for good behavior."
"You were worried I would arrange a procession?"
"I was worried you would arrange something useful. People forgive themselves so much when they are being useful."
{n}At the door she touches your sleeve briefly.{/n}
"Thank you for answering. That is the last time I shall say something so agreeable tonight. Leave while you can still believe it."''', c('[Keep the agreed meeting.]', flags=done("invitation_kept"))),
], delay=24)

s("her_own_arrival", "The woman who answered", [
    n("start", "Narrator", '''{n}On the appointed evening, Minagho opens the gaming-house door before you knock. Chivarro is already inside. A traveling cloak hangs from a peg, rain darkening its hem. She has reached Drezen under a mortal guise and discarded it here, after checking the room herself.
She is standing close to Minagho. One hand rests at the back of her neck. Neither moves away when you enter. Chivarro finishes the sentence you interrupted.{/n}
"And if you ever send me another message that begins 'You may have heard I was dead,' I shall make the next one accurate."
"You came."
"An extraordinary deduction."
{n}Minagho laughs into the kiss Chivarro gives her. The sound stops being laughter for a moment. Then Chivarro releases her and turns to you.{/n}
"Commander. I chose the road here. She chose the room. That should tell you which of us was more cautious."
"The room has two exits," {n}Minagho says.{/n}
"One of which you blocked with a chest because the draught annoyed you."''', c('"It is good to meet you without an intermediary."', "account")),
    n("account", "Chivarro", '''"Yes. Intermediaries become ambitious when they discover that you need them. I used to encourage it. Then I would make them compete."
{n}She sits without waiting to be offered a chair.{/n}
"You may ask what I intend. You may not decide that the answer must be gratitude. I have paid for this journey myself, and I can leave it the same way."
"Minagho said you have received an offer."
"Several. Veyr's was the first worth reading twice. He places guests in private houses that want wealthy visitors without admitting them through the front door. Introductions, entertainments, information. He sells discretion and sometimes remembers to supply it. I knew his customers before he did."
{n}She glances toward Minagho, who has finally moved the chest away from the second exit.{/n}
"I want a business whose keys I hold. I have no desire to stand at somebody else's table while they decide whether I have been forgiven enough to be useful."''',
      c('"What would you refuse to buy back?"', "price"),
      c('"Then tell me where I fit in your plans."', "place")),
    n("price", "Chivarro", '''"The old establishment at any price? No. Sentiment is a splendid way to be overcharged."
"That is not what I asked."
{n}Chivarro's smile thins, then returns with more interest in it.{/n}
"No. It wasn't. I will not purchase a chair by agreeing that I may be dismissed from it whenever its present owner grows frightened. I have tried arrangements in which a powerful patron mistakes toleration for ownership. They are inconvenient to end."
"And other people's freedom?"
"You want a list of virtues before you hear a proposal. I dealt in desire, influence and fear. I know which customers preferred each. I am not going to rename my former business because we are drinking in your city."
{n}She rests a finger on the folded offer.{/n}
"This proposal concerns introductions and old debts. Hear the terms, then argue with something I am actually considering."''', c('"Fair. Where do I fit?"', "place")),
    n("place", "Chivarro", '''"That is partly what I came to discover. Minagho talks about you as though you are an aggravating piece of good fortune. I find the combination promising."
"She talks about you rather differently."
"She had better. I have had longer to improve my methods."
{n}Minagho reaches across and turns Chivarro's cup so its chipped edge faces away from her mouth. Chivarro lets her, though she must already have noticed the flaw.{/n}
"You are welcome at this table," {n}Chivarro says.{/n} "If we find something else we want, we can say so. I will not have an evening negotiated for me in a room where I was absent."
"You could have written a shorter reply," {n}Minagho says.{/n}
"You could have made fewer predictions."
{n}The rebuke is familiar enough to make Minagho grin. Chivarro keeps her attention on you.{/n}''',
      c('"I would like to discover whether there is an attraction between us."', "interest"),
      c('"For now, I want to know you without a courtship waiting behind every question."', "company")),
    n("interest", "Chivarro", '''"There may be."
{n}She lets the answer remain small. Then she moves her chair a little closer, so you can speak without addressing the whole table.{/n}
"I enjoy people who listen to the answer they have asked for. You have managed that twice. Try not to become complacent."
"What would you like to ask me?"
"What do you miss when everyone has stopped needing you for an hour?"
{n}She hears your answer without turning it into a test. When you ask the same question, she touches the folded cloak.{/n}
"A room I have chosen because I like it. I have spent too long choosing them for what cannot get through the door."
{n}Minagho's hand closes briefly over hers. Chivarro squeezes it, then leaves her free hand resting near you.{/n}''', c('[Stay and hear the offer.]', flags=done("arrival_kept", "chivarro_interest"))),
    n("company", "Chivarro", '''"Then I shall have to survive being interesting. A severe demand."
{n}She unfolds the offer and smooths it beneath her palm.{/n}
"Minagho says you are more patient than she expected. I would like to know whether that is a compliment or an accusation."
"Both," {n}Minagho says.{/n}
"I thought so."
{n}Chivarro asks what you enjoy in Drezen when no one is presenting you with a crisis. Minagho interrupts your answer with a complaint about the tavern's beer. Chivarro listens to that, too, then asks you to finish.
By the time she returns to the letter, the three of you have found a way to speak without every silence becoming a negotiation.{/n}''', c('[Read Veyr\'s offer together.]', flags=done("arrival_kept", "chivarro_company"))),
], "invitation_kept", 24)

s("the_remaining_customers", "The remaining customers", [
    n("start", "Chivarro", '''"Veyr wants the names of six customers who used to ask me to find unusual company. He has their public names. He wants the names they used with me."
{n}She has copied the offer onto a clean sheet. A second sheet lies underneath it, blank.{/n}
"With those, he can prove he knows their private tastes. He says the proof will persuade them to attend a small gathering he is arranging. I suspect it would persuade them to pay him whether they attend or not."
"And you get?"
"A share in the gatherings. Introductions in my own name. A room whose guests know they are there because I invited them."
{n}Minagho makes an impatient sound.{/n}
"And he gets a list he can sell to someone less entertaining. One of those customers supplied agents of Baphomet. I recognize the account description. The last pursuit failed. This would give another employer an excellent address book."
"Or give us a way to know who is buying it," {n}Chivarro says.{/n}
"I would rather give him a reason to stop breathing."
"Yes. You have been wonderfully consistent about that."''', c('"What do you each want to send him?"', "plans")),
    n("plans", "Minagho", '''"A convincing mistake. Let him think the contact he wants has changed hands. He passes it to whoever is buying, and I discover which servant of Baphomet is still spending money on me."
"You promised me a meeting," {n}Chivarro says.{/n} "I will not buy my way back into business by becoming the bait in your next private war."
"He has already made you bait. I propose choosing the hook."
{n}Chivarro pulls the blank sheet out from beneath the letter.{/n}
"I can offer him two introductions without giving him anyone's private name. People who owe me a conversation and can decline the second one. He will want more of the profit in exchange. I will have less authority at the beginning, but the business will be mine to develop."
"Until he sells the fact that you found me."
"He knows that already. Killing him will not remove it from everyone he has told."
{n}For a moment neither looks at you. This is an argument they have begun before, and both have learned where the other is hardest to move.{/n}''',
      c('"Before choosing, show me exactly what he knows."', "document"),
      c('"Minagho, what would you put at risk yourself?"', "stake")),
    n("stake", "Minagho", '''"My face. My time. A little of the reputation everyone keeps telling me I have lost."
"Something you would mind losing," {n}Chivarro says.{/n}
{n}Minagho goes still. Then she speaks without smiling.{/n}
"The distance between us. I stayed away because following me would have led them to you. I have no wish to begin that again."
{n}Chivarro presses her lips together. Her anger does not vanish, but it has to make room for something else.{/n}
"Then do not decide for me that a clever trap is worth it."
"I am explaining it before setting it."
"An improvement I intend to enjoy."
{n}Minagho's laugh is reluctant and brief. She pushes the original letter toward you.{/n}
"Read. If he has been careless, I would like to know before she talks me into behaving."''', c('[Examine the document.]', "document")),
    n("document", "Narrator", '''{n}Veyr's letter offers a meeting with a factor named Orven. The factor will bring a sample invitation from the house Veyr proposes to use. The original gives the house a different name from the copy Chivarro received a day later. Both letters bear the same courteous assurance that nothing material has changed.
Chivarro has marked the discrepancy with her nail. Minagho has marked the word "courteous" with a small drawing of teeth.{/n}
"We can ask the factor," {n}Chivarro says.{/n} "But I would prefer to know whether he is lying before we ask."
"I know a simpler way," {n}Minagho says.{/n}
"You know one way."
"Several. You disapprove of the enjoyable ones."
{n}Chivarro turns the letter over. Its reverse carries an impression from another sheet, too faint to read in this light.{/n}
"Tomorrow, then. We examine what he has sent. After that I will hear whether you want to risk my introductions, her bait, or neither."''', c('[Agree to examine the evidence before committing anyone.]', flags=done("offer_heard"))),
], "arrival_kept", 24)

s("the_second_address", "The second address", [
    n("start", "Narrator", '''{n}Chivarro has borrowed a lamp with a broad glass chimney. She holds the paper beside it while Minagho moves the flame's shadow with a folded screen. At one angle, the impressions on the back rise clearly enough to show separate words.
The two women work comfortably together. Chivarro says "lower" and Minagho lowers the screen before finishing her complaint about mortal furniture. Then Chivarro raises a finger. Both fall silent while you read.{/n}
"There," {n}she says.{/n} "A second address. Or part of one."
"It could be an earlier letter," {n}Minagho says.{/n} "Or a list of where to send the bodies. I prefer the latter. It suggests someone has planned ahead."
"If you would hold the screen still, we might find out."
{n}Beside the original lie both copied invitations. Their ornamental headings agree; the spaces left for the guest's private name do not. One is narrow enough for initials. The other would take several lines.{/n}''',
      c('[Read the impressions and compare the invitation forms. Knowledge: World, DC 32.]', check=dict(Skill="SkillKnowledgeWorld", DC=32, Success="read", Failure="blurred", CommanderOnly=True)),
      c('"Let us ask Orven to explain both versions before we offer anything."', "ask"),
      c('"I have seen a condition defeat its own purpose before. Give me the two invitations."', "trick", requires=("trickster", "minagho.brand_trick_seen"))),
    n("read", "Narrator", '''{n}The visible words are not an address for a house. They form part of a forwarding instruction. You compare the spaces on the two invitations and find the reason for the longer blank. It is meant to receive both the invited name and the person who supplied it.
You show Chivarro where a clerk has pressed hard enough to leave the word "source" on the sheet underneath.{/n}
"He would be buying a customer and the person who introduced him," {n}she says.{/n}
"A list of witnesses," {n}Minagho says.{/n} "Someone wants to know who can connect the names."
{n}Chivarro sets the letter down with care.{/n}
"Then Orven can tell us what he expected me to sign. He may still be useful."
"You are very generous."
"No. I intend to charge him more."
{n}Minagho bends over the impression once more. You point out the forwarding instruction. Her finger follows the edge of the paper without touching its faint marks.{/n}
"We know which question he does not want asked," {n}she says.{/n} "That should improve our manners considerably."''',
      c('"Take the evidence to the meeting. Make him account for it."', "read_end")),
    n("read_end", "Chivarro", '''"I shall begin with the business he thought I was foolish enough to accept. Then we can enjoy the surprise."
{n}She makes a copy of the impression while you hold the lamp. Minagho watches you work together with an expression that is pleased without being entirely restful.{/n}
"What?" {n}Chivarro asks her.{/n}
"You used to dictate while someone else copied."
"I still would, if either of you could be trusted with my handwriting."
"The Commander's is probably more threatening."
{n}Chivarro looks at the line you have written to identify the sheet.{/n}
"It is certainly less susceptible to forgery. I cannot imagine anyone choosing to learn it."
{n}She touches your wrist as she takes the lamp. The gesture lasts just long enough to make the insult affectionate. Then she caps the ink and prepares the packet for Orven.{/n}''', c('[Keep the forwarding evidence intact.]', flags=done("evidence_kept", "source_found"))),
    n("blurred", "Narrator", '''{n}You turn the paper to catch a deeper impression. The flame flares as the screen moves; the light washes out the shallow marks. By the time you find the angle again, the words you thought you recognized no longer join into a sentence.
Minagho holds the screen still. Chivarro waits until you admit you cannot read enough to trust it.{/n}
"Then we do not send an accusation based on a guess," {n}she says.{/n}
"We could send a very unpleasant question," {n}Minagho offers.{/n}
"We can ask one in person."
{n}Chivarro puts the unreadable sheet aside. She takes a narrow strip of blue silk from her traveling case and lays it on the table.{/n}
"Veyr knows this. I used it to mark requests that came from me. If Orven is merely a hired mouth, he can carry it back and require his employer to explain the two forms. We lose the pleasure of surprising him, and Veyr learns that I still have an old signet."
"That sounds like more information than you wanted to give him."
"It is. Failing to learn something does not make the ignorance cheap."''', c('"Use the ribbon to demand the explanation. Do not pretend we read what we could not."', "ribbon")),
    n("ask", "Chivarro", '''"A question with the papers laid out in front of him. Sensible. It warns him that we have compared them, of course."
"Would the other approach avoid that?"
"Only if we learned enough to make him betray the missing part himself. I would enjoy it. I do not need it."
{n}She takes a narrow strip of blue silk from her traveling case.{/n}
"This will persuade Veyr to answer through his factor. He knows the old mark. I had hoped to keep him wondering how much I still possess."
"A ribbon seems a small thing to tell him."
"It tells him I kept the means to claim old favors. People behave differently when they think you have burned your address book."
{n}Minagho lifts one end of the silk.{/n}
"I remember this. You wore it when you wanted someone to think he had pleased you."
"Sometimes he had."
"You never wore it for me."
"You could tell without it."''', c('"Ask directly, with the ribbon as your introduction."', "ribbon")),
    n("ribbon", "Narrator", '''{n}Chivarro writes a precise request for the difference between the invitation forms. She wraps it with the blue silk. Minagho adds nothing to the letter, though she has several suggestions that grow less printable as Chivarro continues to ignore them.
When the packet is sealed, Chivarro looks at you.{/n}
"That was one of the few things I brought because I liked having it. Now he will see a piece of my past and price it. I should like the meeting to be worth that."
"I will remember."
"Good. I am not asking you to apologize for choosing a question. I am telling you what the question cost me."
{n}Minagho turns the lamp down. Her hand remains on Chivarro's shoulder while the flame settles.{/n}''', c('[Send the question and keep the meeting.]', flags=done("evidence_kept", "ribbon_spent"))),
    n("trick", "Minagho", '''"If you require more of my blood, ask before you reach for a knife."
"No blood. He has sent two invitations that claim to be the same invitation. Let us make them agree about where their answer belongs."
{n}You put the sheets together. For a moment the wet-looking ink of one address lies above the other, though both pages are dry. You turn them apart again. Each now carries the same forwarding line, written in the same careful hand. The address is a rented counting room, with a smaller instruction beneath it naming the desk that receives lists of introductions.
Chivarro reads both copies, then presses a finger to the unbroken surface of the paper.{/n}
"You made the lie provide its own correction."
"This invitation, wherever its writer has copied it. We have given all his versions the same inconvenient destination."
"A pity," {n}Minagho says.{/n} "I could have made you a list."
{n}She is laughing. Chivarro is already considering the price.{/n}
"Veyr will notice that his forms have changed. We shall have the address, but not a quiet inquiry. He will know someone here can interfere with his messages."
"Would you rather return to the original papers?"
"No. I want to see what he does when he cannot trust his own stationery."''',
      c('[Keep the corrected forwarding address and the risk that comes with it.]', flags=done("evidence_kept", "fate_address"))),
], "offer_heard", 24)

s("a_factor_at_the_table", "A factor at the table", [
    n("start", "Narrator", '''{n}Orven arrives carrying a flat case. He is a mortal man in a well-cut coat, with the careful courtesy of someone who knows he has been sent to a dangerous room. He waits while Chivarro examines the case for anything she has not agreed to receive.
Minagho stands by the unblocked second door. Her disguise is back in place. Orven recognizes her anyway; a brief tightening around his mouth gives him away. She enjoys that very much.
Chivarro directs him to the chair opposite hers.{/n}
"You have brought the terms?"
"And a sample guest list. Master Veyr hopes the Commander will understand that discretion is essential."
"The Commander has understood the subject without your assistance," {n}Chivarro says.{/n} "Show me what you want me to sign."
{n}Orven opens the case. The top document contains the longer blank you noticed in the invitation. Beneath it is a narrow receipt with a space for the introducer's name.{/n}''',
      c('[Lay out the forwarding evidence before he explains the receipt.]', "proof", requires=done("source_found")),
      c('"We asked for an explanation. Did Veyr send one?"', "ribbon_reply", requires=done("ribbon_spent")),
      c('"Does your copy have the new address too?"', "changed_reply", requires=done("fate_address"))),
    n("proof", "Chivarro", '''"You are recording the people who supply the names as well as the names themselves. Your first letter omitted that."
{n}Orven looks at the copy of the impression. He takes too long before denying that there was any intent to conceal it.{/n}
"Then you will have no difficulty removing it," {n}Chivarro says.{/n}
"My employer must know who guarantees an introduction."
"He can know that I made one. He cannot sell a signed account of everyone who helped me arrange it."
{n}Minagho leaves the door and comes to the table.{/n}
"Who wanted the second copy?"
"I cannot disclose another client's arrangements."
"A principle you should try applying to this client."
{n}Orven looks at you, seeking a less hostile face. The receipt remains between you, unsigned.{/n}''', c('"Answer her question."', "buyer")),
    n("ribbon_reply", "Chivarro", '''{n}Orven produces the blue ribbon. It has been cut through the middle. One half is pinned to a short reply; the other is gone.{/n}
"Master Veyr accepts the authenticity of your request. He has retained a sample for future correspondence."
{n}Chivarro's expression hardly changes.{/n}
"He would. Read the explanation."
{n}The factor explains that a third party has offered to underwrite the gathering if every introduction carries the name of its source. Veyr proposes to charge that party for the assurance, then give Chivarro a smaller share of the evening's proceeds because her list is incomplete.{/n}
"He asks me to supply the guests and the people who could identify them," {n}she says.{/n} "Then reduces my fee because I noticed."
"Because the arrangement has become more complex."
"For you, perhaps. I have understood it very well."
{n}She unpins her half of the ribbon and folds it into her palm.{/n}''', c('"Who is underwriting it?"', "buyer")),
    n("changed_reply", "Minagho", '''"He does have the new address. Look at his face."
{n}Orven removes a sheet from the case. The forwarding line has changed on his copy as well. He places it beside yours without pretending that the match is accidental.{/n}
"Master Veyr says that interference with his papers makes trust difficult."
"I should think discovering what they say would make it easier," {n}Minagho says.{/n}
"He will require payment in advance for any further arrangements."
"And the person who wanted the list?" {n}Chivarro asks.{/n}
{n}Orven hesitates. Minagho taps the common address with one finger.{/n}
"If the paper has more to tell us, I shall ask the Commander to listen. You can save us time by speaking first."
{n}Orven shuts the empty side of his case. The small movement looks like an attempt to keep the rest of its contents obedient.{/n}''', c('[Let him answer.]', "buyer")),
    n("buyer", "Chivarro", '''{n}The buyer calls herself Sareth. Orven cannot give a better name. She trades in information about people who have changed patrons, and one of her agents asked specifically whether Chivarro had renewed contact with Minagho. She wants introductions she can trace backward.
Minagho says the agent's description belongs to a messenger who once carried offers for servants of Baphomet. She does not claim to know where he is now.{/n}
"So," {n}Chivarro says.{/n} "There is still an evening to arrange. There is also someone hoping to buy the path to our door. I shall answer those separately."
{n}She turns to Orven.{/n}
"You may carry an unsigned offer for two introductions, each confirmed by the person attending. Veyr takes the larger fee. He receives no former private names and no list of my sources. If that displeases his underwriter, he can find another."
"He may refuse."
"Then he refuses."
{n}Minagho rests her palms on the table.{/n}
"Or you carry a false appointment for Sareth's agent. Somewhere empty, with no one else's name on it. Chivarro loses the respectable half of your offer, and we discover whether the buyer is real."
"You mean to ambush him?"
"I mean to let him arrive before deciding how much he has to say. You may quote that exactly."
{n}Chivarro studies Minagho for a long moment, then nods once.{/n}
"I will consider that. I will also consider sending you away with nothing. Commander, you have heard the terms. Which undertaking are you willing to help with?"''',
      c('"The limited introductions. You keep the business; the private names stay out of it."', "business"),
      c('"The false appointment. I want the buyer cut off before this becomes another pursuit."', "bait"),
      c('"Neither offer is worth reopening this channel. Send a refusal."', "refuse")),
    n("business", "Chivarro", '''"Then I shall have less money and a door I can still use. That is an acceptable beginning."
{n}She writes the limitations herself. Orven objects to a clause forbidding resale of the introductions. She crosses out the entire offer and waits. He withdraws the objection before the ink dries.{/n}
"You may take a copy," {n}she tells him.{/n} "You may not take my first draft and sell the corrections."
{n}Minagho watches the factor leave with the sealed copy. She does not follow him.{/n}
"You dislike it," {n}Chivarro says.{/n}
"I dislike leaving someone a reason to keep asking about us."
"So do I. I also dislike discovering that every road except hiding must be burned before you can bear to walk it."
{n}Minagho looks toward you, then back to her.{/n}
"Keep the first gathering small. No unfamiliar assistants. If the buyer sends someone, I want to be there."
"As a guest."
"As an extremely observant guest."
"I would expect nothing less."
{n}Chivarro keeps the unsigned receipt. Its blank spaces seem to please her.{/n}''', c('[Help her prepare the limited gathering.]', flags=done("terms_sent", "business_chosen"))),
    n("bait", "Minagho", '''"Good. An empty counting room. A time late enough that the other tenants have gone. No fictitious servant who will be punished when he fails to appear."
{n}Chivarro draws the proposed address from Orven. She checks that the room belongs to the same intermediary whose desk appeared in the forwarding instruction, then dictates the appointment. Minagho makes no attempt to write it in Chivarro's hand.{/n}
"Veyr will know I have let this happen," {n}Chivarro says after the factor leaves.{/n} "The business will close to me. Even if he forgives it, he will need his customers to believe that he has not."
"I know," {n}Minagho says.{/n}
"Tell me you will remember when it is your turn to accept something you dislike."
{n}Minagho's answer is quieter than her earlier triumph.{/n}
"I shall remember."
{n}Chivarro turns to you.{/n}
"You will come as a witness. I want someone present who can tell her when the useful part is over. And I want you to hear what the buyer actually knows, rather than a story improved for my benefit afterward."''', c('[Keep the appointment with both women.]', flags=done("terms_sent", "bait_chosen"))),
    n("refuse", "Chivarro", '''"Then he receives my answer and nothing to sell with it."
{n}She tears the unsigned offer into strips. Orven gathers the sample invitation and leaves. Minagho lets him reach the stairs before closing the door.{/n}
"I could have made him more frightened," {n}she says.{/n}
"He will tell Veyr enough," {n}Chivarro answers.{/n}
{n}She remains beside the table after the papers are gone. You ask whether she regrets sending him away.{/n}
"Of course. I wanted part of that offer. I would have enjoyed making those people wait outside a door I controlled again. I can think a bargain is too costly and still resent losing what it would have bought."
"What now?"
"I shall use the two introductions myself. A smaller gathering, without Veyr's house or purse. It will cost me more to arrange. I know how to begin small. I simply have no intention of remaining there."
{n}Minagho picks up the discarded sample invitation.{/n}
"Then I had better find somewhere worthy of your displeasure."''', c('[Help arrange the smaller gathering on their own terms.]', flags=done("terms_sent", "refusal_chosen"))),
], "evidence_kept", 24)

s("what_the_offer_bought", "What the offer bought", [
    n("start", "Narrator", '''{n}Minagho meets you at the gaming house with her traveling cloak already fastened. Chivarro is checking a small purse. She counts its contents once, closes it, then makes herself put it away.
No one mistakes the evening for a casual visit. The papers you agreed to send have received their answers.{/n}
"Before we go," {n}Minagho says,{/n} "I should like to hear your plan without the parts that make it sound pleasant."
"An unusual request from you," {n}Chivarro says.{/n}
"I contain surprises."
{n}Chivarro turns toward you. Her expression is almost amused, but she has not taken her hand off the purse.{/n}''',
      c('"We see whether Veyr honors the limited invitations."', "business", requires=done("business_chosen")),
      c('"We hear the buyer\'s agent at the false appointment."', "bait", requires=done("bait_chosen")),
      c('"We hold the gathering without Veyr."', "independent", requires=done("refusal_chosen"))),
    n("business", "Narrator", '''{n}The gathering occupies a rented private room beyond the district's busy streets. Veyr has accepted Chivarro's reduced terms through Orven. Two guests arrive separately, under names they have chosen to use tonight. Chivarro introduces them by those names and no others.
One is a collector seeking performers for a private house. The other arranges journeys for people who dislike explaining their destinations. Each has come to hear what the other will offer. Neither has been brought as a gift.
Chivarro conducts the introductions with a pleasure she has not shown while discussing them. She notices a hesitation, leaves a question unanswered until its value rises, then supplies exactly the detail that makes both guests lean forward.
Minagho watches from beside you.{/n}
"There. That is what she wanted."
"The fee?"
"Listen to them stop talking when she begins."
{n}Orven brings the settlement halfway through the evening. Veyr has taken the larger share as agreed. There is also a charge for safeguarding the guests' identities. Chivarro taps it once.{/n}
"That was the condition of the gathering. You do not charge me twice for meeting it."
"My employer's expenses were greater than expected."
"Then he has learned something about his prices."
{n}Orven looks to the guests, hoping she will avoid a dispute in front of them. Chivarro closes the account book and asks the traveler to finish describing his route. She makes the factor wait until both guests have left, satisfied with their meeting and owing her their next answer.{/n}''', c('[Stay while she settles the disputed charge.]', "business_end")),
    n("business_end", "Chivarro", '''"You may take the agreed fee. Or you may tell Veyr that the introductions happened, his guests were satisfied, and you decided not to collect his money."
{n}Orven removes the extra charge. Chivarro pays without smiling. Only after he leaves does she allow herself to sit.{/n}
"I used to have people who could do that part."
"Would you have trusted them?" {n}Minagho asks.{/n}
"No. I would have checked it afterward and punished the mistake. This arrangement is exhausting in a different direction."
{n}She draws your chair toward hers by its back.{/n}
"Stay a moment. I want to enjoy the part where it worked before I begin calculating the next expense."
{n}Minagho remains beside the door until the last servant has gone. Then she joins you, placing a second cup near Chivarro's elbow.{/n}
"No buyer's messenger," {n}she says.{/n} "At least none who showed himself."
"No list sold to one either," {n}Chivarro answers.{/n} "I have a business connection. You have lost tonight's chance to bait him. I know what you gave up."
{n}Minagho accepts the acknowledgment with a small tilt of her head. For once she does not improve it with a joke.{/n}''', c('[Remain until Chivarro is ready to leave.]', flags=done("offer_resolved", "broker_open"))),
    n("bait", "Narrator", '''{n}The counting room is empty except for a desk, a cold brazier and three chairs. Minagho checks behind its inner door while Chivarro arranges the invitation on the desk where an arriving guest will see it.
The agent comes alone. He is a thin, horned stranger wearing gloves too fine for the dust on his coat. He stops when he recognizes Minagho. She closes the inner door behind him.{/n}
"The appointment is real," {n}she says.{/n} "The person you expected is not. Sit."
{n}He looks at you, then at the outer door, where Chivarro is waiting. He sits.
His employer bought rumors after the last pursuit failed. She has no new command from Baphomet to show him. She wants names and routes that might become valuable if someone powerful begins asking again. He carries a coded list of prospective buyers, but no order to attack tonight.
Minagho reads the first marks he identifies and asks three questions whose answers make him visibly less comfortable. Chivarro stops her before the fourth.{/n}
"Enough to know what he was buying. What does it cost him to stop?"
"His employer will be disappointed," {n}Minagho says.{/n}
"She is not in this room."
{n}The agent offers to take back a report that the list was false and the named sources unreliable. Minagho offers to send his gloves without him. Chivarro turns toward you.{/n}
"You heard him. He is a broker's scout. A useful message could make us expensive to investigate. What do you want to leave this room?"''',
      c('"A scout who can report that there is no list to buy. Let him carry the warning."', "warning"),
      c('"His buyer list stays here. Then he leaves with the same warning."', "list")),
    n("warning", "Minagho", '''"You are letting him keep a great deal."
"He came to buy a list. He can go back having failed."
{n}Chivarro steps away from the outer door.{/n}
"And he can describe the people who explained the failure. Accurately."
{n}The agent leaves at a pace that becomes a run on the stairs. Minagho listens until the footsteps have faded.{/n}
"I could have learned more."
"Yes," {n}Chivarro says.{/n} "And I could have had a share in Veyr's gatherings. We agreed which problem we were solving tonight."
{n}Minagho looks at the invitation left on the desk. She tears it through the middle and lets the pieces fall into the cold brazier.{/n}
"Then I shall take the satisfaction of his face. It was an unusually good face to disappoint."
{n}Chivarro takes her arm. Their shoulders touch as they leave. Outside, Chivarro waits for you before choosing the street home.{/n}''', c('[Leave the false appointment behind.]', flags=done("offer_resolved", "pursuit_warned"))),
    n("list", "Narrator", '''{n}The agent places his coded list on the desk. Chivarro makes him explain the marks that identify a buyer from a rumor. Minagho listens without correcting the details she already knows. When he has finished, you let him leave with the warning.
Minagho keeps the list. Chivarro watches her fold it.{/n}
"You have what you asked for," {n}she says.{/n} "Do not use it to begin something else while calling it the end of this."
"There are people here who deserve an unpleasant surprise."
"I am aware. I have met several."
{n}Minagho glances toward you.{/n}
"I will not pursue this list tonight. Is that an answer you can bear?"
"It is an answer I believe," {n}Chivarro says.{/n}
{n}She leaves the desk, and Minagho follows. Outside, the city smells of damp stone and wood smoke. Chivarro takes a deep breath, then tells you which part of Veyr's offer she will replace first. She has already begun making another plan.{/n}''', c('[Walk back with them.]', flags=done("offer_resolved", "buyer_list_kept"))),
    n("independent", "Narrator", '''{n}Chivarro's own gathering is held in a smaller room hired with her money. There is no factor to wait upon it. Minagho has found a table without a wobble and seems almost offended by the amount of effort that required.
The two invited guests arrive under the names they have chosen for tonight. One seeks performers for a private house. The other can arrange discreet journeys. Chivarro introduces them, then leaves enough silence for each to discover why the other might be useful.
She is good at it. She makes neither guest feel hurried, though she stops both from wasting her time. When the traveler begins speaking as though the performers can be purchased with the passage, she corrects him without raising her voice.{/n}
"You are offering transport to people who may accept it. I am introducing you to someone who can ask them. The price you have quoted does not buy an answer in advance."
{n}The collector laughs and asks for a better offer. The traveler supplies one.
Afterward, Chivarro counts her remaining coin and discovers that the evening has cost more than it earned. Both guests have agreed to another conversation. Neither has paid for the pleasure of being made useful to the other.{/n}
"An investment," {n}she says, with distaste.{/n}
"You sound as though it tastes bad," {n}Minagho says.{/n}
"It tastes of paying for my own wine."''', c('"Was it worth what you gave up?"', "independent_end")),
    n("independent_end", "Chivarro", '''"Ask me after they answer. Tonight I bought the chance to hear them without Veyr sitting between us."
{n}She puts away the purse before you can offer anything.{/n}
"Do not rescue my arithmetic. I chose the smaller room. I knew what it would cost."
"I can still help clear the table."
"A rare service. Everyone offers money when it is time to lift something."
{n}Minagho picks up two empty cups. Chivarro looks at her, surprised enough to be unguarded.{/n}
"I have carried heavier things," {n}Minagho says.{/n} "Some of them objected."
{n}Chivarro laughs. It is the first laugh of the evening that has not been measured for a guest.
The three of you put the hired room back in order. Chivarro keeps a small card on which the collector has written a new address. When she finally allows herself to examine it, she does so with pleasure.{/n}''', c('[Leave the room with her new contact safely kept.]', flags=done("offer_resolved", "independent_open"))),
], "terms_sent", 24)

s("the_unhired_evening", "The unhired evening", [
    n("start", "Narrator", '''{n}Chivarro has put the correspondence out of reach. On the table is a shallow tray of carved stones, each painted with part of a mask. Minagho claims it is a game of deception. Chivarro calls it a game of recognizing when someone is about to become unbearably pleased with herself.
You learn by losing a round. Minagho has been showing you the correct stone with such elaborate deceit that you choose another. Chivarro takes the prize from between you, a sugared plum she apparently brought for precisely this purpose.{/n}
"You were supposed to warn me," {n}Minagho says.{/n}
"Against a plan you admired that much? You would have taken it as encouragement."
{n}Chivarro breaks the plum in half and offers one piece to her. Minagho accepts it from her fingers, then catches her hand before she can withdraw it. For a moment the game is forgotten by both of them.
Chivarro frees her hand gently and turns the tray toward you.{/n}
"Again? Or have you endured enough instruction?"''',
      c('"One more. This time explain what I should have noticed."', "game"),
      c('"I would rather know what you enjoy when no one has to win."', "want")),
    n("game", "Chivarro", '''"The stone was right. The performance was excessive. She wanted you to believe she could not possibly make so obvious a mistake."
"You are revealing my methods," {n}Minagho says.{/n}
"You will invent worse ones."
{n}Chivarro lets you arrange the next mask. She does not soften her play for you. Twice she asks whether you are certain, with such perfect neutrality that the second question is much more unsettling than the first.
When the round ends, Minagho has lost the remaining plum. She accuses Chivarro of enjoying that outcome more than the game.{/n}
"Yes," {n}Chivarro says.{/n}
{n}She divides the prize with you. Her fingers brush yours when you take it. Then she puts the stones away, leaving the tray empty.{/n}
"There. No one owes an introduction, an explanation or a fee for the next hour. I thought we might see what happens to conversation under such unusual conditions."''', c('"What would you like to happen?"', "want")),
    n("want", "Chivarro", '''"I would like to be wanted for something I am not supplying."
{n}She says it lightly, then decides not to turn it into a joke.{/n}
"I enjoy arranging a room. I enjoy seeing exactly what would make someone cross it. But I have spent evenings making everyone else's appetite appear effortless. Sometimes I want to sit down and let someone come to me."
{n}Minagho settles beside her.{/n}
"You could have said that."
"I have. Usually while you were explaining why I should come to you."
{n}Minagho smiles, unabashed, and kisses the inside of her wrist. Chivarro's answer is a hand beneath Minagho's chin, holding her there for another moment.
When they turn toward you, both are plainly waiting to see what you will bid.{/n}''',
      c('"Minagho. A word. Alone."', "minagho", forbids=("minagho.ran_demon",)),
      c('"Chivarro. Move over."', "chivarro", requires=done("chivarro_interest")),
      c('"I want you both. Tell me I\'m not the only one at this table who does."', "together", requires=done("chivarro_interest"), forbids=("minagho.ran_demon",)),
      c('"Not tonight. Deal the stones again."', "slow", forbids=("minagho.ran_demon",)),
      c('"Just the game tonight. I intend to win something."', "company"),
      c('"Minagho. You are still in my service. That sits between us."', "service", requires=("minagho.ran_demon",))),
    n("minagho", "Minagho", '''{n}Minagho does not answer for a moment. Chivarro studies her, then reaches for the tray of stones.{/n}
"I have been meaning to return this," {n}she says.{/n} "I can be gone for an hour. If I come back to find you have resumed discussing the factor, I shall be offended on behalf of the evening."
{n}After Chivarro leaves, Minagho moves to the seat beside you.{/n}
"She makes leaving sound like a threat. It is one of her better accomplishments."
"And what do you want?"
"You. Here. Paying attention to something that is not about to kill either of us."
{n}She rests a hand against your cheek, and her thumb traces a short, deliberate line down to the corner of your mouth and presses there, the way a buyer presses fruit.{/n}
"One hour. She will time it to the grain of sand. I have waited for this through two cities and a demon lord's patience, and I am not going to spend it watching you think. Kiss me, or go and help her carry the tray."''',
      c('"Kiss me."', "minagho_kiss"),
      c('"Stay close. Just the hour, tonight."', "minagho_close")),
    n("minagho_kiss", "Narrator", '''{n}Minagho leans close enough that her hair brushes your cheek, then stops.{/n}
"You say that very confidently. Has someone been encouraging you?"
"You have been trying for most of the evening."
"Trying?"
{n}That earns you the kiss. Her hand tightens at your collar; the little triumphant sound she makes when you draw her closer is almost a laugh. She has forgotten the elegant position she meant to maintain. One knee strikes the table. A stone from the abandoned game falls, and she catches it without looking away from you.{/n}
"A witness. We should dispose of it."
{n}You take the stone from her fingers and put it beside the others. When you turn back, the levity has thinned. She is waiting, mouth slightly parted, as if your returning were the uncertain part.
You kiss her again. This time she lets the waiting show before answering it, and then answers it all at once. She shoves the tray off the couch with her heel, stones and all, drags her dress off one shoulder and then the other without breaking the kiss, and climbs into your lap with a knee either side of your hips, pulling your hands up the bare length of her back. "One hour," she says into your mouth, already working at your belt. "Do not waste it being gentle."
Afterwards she steals your place on the cushion while you reach for the wine, then complains when you insist on sharing it. Her head settles against you halfway through the complaint.{/n}
"Next time, two hours. Chivarro negotiated very poorly on my behalf."''', c('"Two hours, next time. I\'ll bring the plums."', flags=done("evening_kept", "minagho_chosen"))),
    n("minagho_close", "Minagho", '''"Then I shall have to be interesting while dressed. A terrible hardship."
{n}She settles against your side. You ask what she enjoyed before she learned to make pleasure useful. At first she offers an answer so extravagant that it is plainly a deflection. When you wait, she tries again.{/n}
"Being the first person to know something. Not because I could sell it. Because everyone else's certainty looked ridiculous for a moment."
"You still enjoy that."
"Yes. I have retained a few accomplishments."
{n}Her hand finds yours. When Chivarro returns, Minagho is still telling you a story whose ending she has promised not to improve. Chivarro hears the last sentence and immediately accuses her of doing so.{/n}''', c('[Keep the closeness and the slower pace.]', flags=done("evening_kept", "minagho_chosen", "gentle_evening"))),
    n("chivarro", "Chivarro", '''"I do."
{n}She moves the empty tray away so you can sit close without balancing it between you. Minagho watches the two of you for a moment, then rises.{/n}
"I am going to discover whether the lower room still has anything worth drinking. If it does, I shall bring some back. If it doesn't, you will hear my opinion from here."
{n}Chivarro waits until the door has closed.{/n}
"She can be considerate with an extraordinary amount of noise."
"Does this trouble you?"
"Her leaving us an hour? No. The possibility that you will spend it asking me to explain her? Very much."
{n}Her smile takes the sting out of the answer without withdrawing it.{/n}
"I have sold a thousand evenings like this one to other people, and I know exactly how every one of them begins. Surprise me. I have left you very little room to do it in."''',
      c('"I would like to kiss you."', "chivarro_kiss"),
      c('"Take my hand. Tell me something you have never needed a guest to like."', "chivarro_close")),
    n("chivarro_kiss", "Chivarro", '''"Yes. Come here."
{n}She meets you halfway. Her hand rests at the back of your neck, firm enough that you feel the decision in it. When you separate, she remains close, studying your answer before asking for another kiss.
You give it. She lets you lead for exactly as long as it amuses her, and then it stops amusing her: she pushes you down along the couch with one palm flat on your chest, unlaces her bodice with the other hand without looking at it, a madam's quick, practised fingers, and lowers herself over you until her loosened hair closes around both your faces like a curtain. "I have arranged this for other people all my life," she murmurs, settling her weight across your hips. "This one I am arranging for me."
Much later, when Minagho returns and announces through the door that the wine is appalling, Chivarro laughs against your shoulder before sitting up.{/n}
"Then leave it outside. I would like to preserve my opinion of the evening."''', c('[Ask Chivarro for another evening together.]', flags=done("evening_kept", "chivarro_chosen"))),
    n("chivarro_close", "Chivarro", '''{n}She takes your hand and considers the question.{/n}
"I dislike being congratulated on remembering people. They think it is kindness. Sometimes it is simply an excellent memory and a wish not to be deceived twice."
"That sounds useful."
"It is. You asked what I had never needed a guest to like."
{n}She turns your hand between hers.{/n}
"But I also remember absurd things. A woman who always removed one earring when she was about to tell an extravagant lie. A musician who believed the fourth performance of a song was unlucky and stopped counting after the third. The way Minagho used to wait until everyone had gone before admitting she had enjoyed herself."
"Will you make me wait?"
{n}Chivarro brings your hand to her lips.{/n}
"No. I have enjoyed myself. There, you have something to remember too."''', c('[Keep the slower, affectionate evening.]', flags=done("evening_kept", "chivarro_chosen", "gentle_evening"))),
    n("together", "Chivarro", '''"I would want to be here because you want me, and because I want you. She already knows why I want her."
{n}Minagho lifts an amused brow.{/n}
"I would tolerate hearing it again."
"Later. You have an answer of your own to give."
{n}Minagho reaches for your hand.{/n}
"I want the evening. I want to see what makes you laugh when she has finished pretending to be severe. And I want her to stop looking at your mouth long enough to admit she has been doing it."
"I thought I had been admirably clear," {n}Chivarro says.{/n}
{n}She offers you her hand as well. Neither pulls you toward the other.{/n}
"There is room," {n}she says.{/n} "There has always been room. She simply never learned to share a cushion without drawing blood over it."''',
      c('"I want to kiss each of you, and stay together tonight."', "together_kiss"),
      c('"Let us stay close without taking the evening further."', "together_close")),
    n("together_kiss", "Narrator", '''{n}Chivarro leans toward you and asks for the first kiss. Minagho watches with an attention that makes Chivarro smile against your mouth. When you turn to Minagho, she catches your chin with two fingers.{/n}
"I refuse to be compared on an inadequate sample."
{n}She makes her case thoroughly. Chivarro's laugh is close to your ear. Then Chivarro draws Minagho toward her, and for a moment you see how little of their language requires you to translate it: a lifted hand, a familiar impatient look, the kiss that spoils the look.
Minagho reaches back for you before they part.{/n}
"Do not become a spectator. She charges for those."
"You still owe me for the game," {n}Chivarro says.{/n}
{n}She gathers the stones and puts them safely on the floor. Minagho accuses her of planning this rearrangement from the beginning. Chivarro does not deny it. Instead she holds out both hands, one to each of you, and when you take them she pulls.
Minagho is already behind you, unhooking your collar with her teeth. Chivarro's dress comes off over her head in one practised motion; Minagho's does not so much come off as tear, and she does not care. Between them they bear you down onto the cushions, Chivarro astride your hips with her hands braced on your chest, Minagho's mouth at your throat and her hand sliding lower, and the last lamp but one goes over when somebody's foot finds it.
Much later, by the one lamp left, Chivarro discovers that Minagho has kept the last sugared plum hidden in her hand all evening. The three-way argument over its division ends with none of you remembering who won.{/n}''', c('[Stay through the quiet end of the evening.]', flags=done("evening_kept", "minagho_chosen", "chivarro_chosen", "together_chosen"))),
    n("together_close", "Narrator", '''{n}Chivarro arranges the cushions with more authority than the task requires. Minagho objects until she discovers that the result gives her a place against both of you. Then she becomes suspiciously cooperative.
You sit together and talk. Chivarro asks a question she has been saving about something you said at your first meeting. Minagho answers a different one, realizes what she has done, and laughs when Chivarro tells her to wait her turn.
The closeness becomes easier as the hour passes. Chivarro's fingers rest loosely through yours. Minagho leans against your shoulder and grows quiet without leaving. When you eventually move, both women let you go, then make room for you to return.{/n}''', c('[Keep this pace for the three of you.]', flags=done("evening_kept", "minagho_chosen", "chivarro_chosen", "together_chosen", "gentle_evening"))),
    n("slow", "Minagho", '''"We can be slow. Chivarro has spent centuries accusing me of hurrying toward the wrong things. I am interested to discover whether she enjoys being right."
"Immensely," {n}Chivarro says.{/n}
{n}She leaves room for you beside them without drawing you into an embrace. You choose where to sit. Minagho asks for another round of the mask game; Chivarro refuses to play for the right to ask personal questions, so you play for the last of the fruit instead.
Afterward, Chivarro declares the evening a success before anyone can dispute it and bills Minagho for the fruit. Minagho regards the empty tray with satisfaction.{/n}
"Then next time I shall bring enough prizes to lose gracefully."
"You have never lost gracefully," {n}Chivarro says.{/n}
"I enjoy having something left to attempt."''', c('[Leave with nothing promised and the fruit unpaid for.]', flags=done("evening_kept", "slow_chosen"))),
    n("company", "Chivarro", '''"Then I shall stop calculating what the empty space on the seat is worth. Sit wherever you like. I shall charge you for the view either way."
{n}She brings the mask stones back. Minagho proposes new rules that would have made her the winner of the earlier round. Chivarro rejects them on those grounds and asks you to arrange the first mask.
The evening grows pleasantly argumentative. Neither woman becomes easier to defeat. Minagho does become worse at concealing her delight when you catch one of Chivarro's tricks. Chivarro notices, accuses her of divided loyalties, and kisses her before she can reply.
At the door, Chivarro asks whether you will come again without a letter to answer. Minagho adds that you should bring a better prize.{/n}''', c('[Agree to another evening as friends.]', flags=done("evening_kept", "company_chosen"))),
    n("service", "Minagho", '''"You have noticed."
{n}The answer is quiet. Chivarro puts the empty tray down.{/n}
"I know what I am to you," {n}Minagho says.{/n} "A gentler voice tonight does not loosen the leash. I can want things and still know exactly what it costs me if wanting them displeases you."
"I am not asking you to pretend otherwise."
"Good. Pretending bores me, and nobody is paying me for it."
{n}Chivarro moves beside her, close enough that their hands meet.{/n}
"I came here for her," {n}she tells you.{/n} "I sat through your plans for my own reasons. Do not buy anything with either."
{n}Minagho does not look away from you. She is not asking Chivarro to rescue her, and she is not offering you anything to soothe your conscience.{/n}
"We can still talk. I have talked through worse, with knives in the room."''',
      c('"Then we talk. Nothing else tonight."', "company"),
      c('"Chivarro. Your offer was your own. Does it stand?"', "chivarro", requires=done("chivarro_interest"))),
], "offer_resolved", 24)

s("the_answer_after_business", "The answer after business", [
    n("start", "Chivarro", '''{n}Chivarro has received her answers. She meets you alone at the rented room, with a small stack of letters sorted by a method that becomes apparent only when she throws the most elaborately sealed one into the empty fireplace.{/n}
"That one offered advice. He wrote six pages before discovering that he had nothing to invest."
"Did he ask for a share?"
"A large one. His confidence in his own conversation was magnificent."
{n}She invites you to sit, then takes the chair beside you. There are fewer possessions in the room now. She and Minagho are preparing to give it back.{/n}
"I wanted you to hear what came of the introductions before I asked you about anything else. Otherwise you might suspect I was presenting another expense as the reward for helping with the first."''',
      c('"Has Veyr kept his part of the bargain?"', "broker", requires=done("broker_open")),
      c('"What happened after the false appointment?"', "scout", forbids=done("broker_open", "independent_open")),
      c('"Did your own guests answer?"', "independent", requires=done("independent_open"))),
    n("broker", "Chivarro", '''"The fee was settled. The two guests have agreed their next conversation. Veyr will take his share, and I shall keep the introductions. I have the agreement here."
{n}She shows you a short confirmation rather than making you admire the whole correspondence.{/n}
"His underwriter withdrew. He tells me this made the business less profitable than he expected. I have congratulated him on surviving a disappointment."
"And the people asking after Minagho?"
"No new request through this channel. I cannot tell you that no one elsewhere remains interested. I can tell you he has failed to sell the source list he wanted from me."
{n}She folds the confirmation.{/n}
"I used to despise a small success. It reminded me of how much larger it ought to have been. I still find that an excellent way to remain dissatisfied. But I am learning to collect the fee before complaining about its size."''', c('"What will you do with the connection?"', "next")),
    n("scout", "Chivarro", '''"Veyr sent a refusal so formal that I could hear him trying to keep his hands steady. He will arrange nothing further for me. The scout's employer has withdrawn the offer for the list. She appears to have decided that the information costs too much."
"Appears?"
"It is what Orven was told. I would not purchase a guarantee from it. But the immediate channel is closed, and I have asked the two people I intended to introduce to speak directly with me instead."
{n}She places the refusal beneath the other letters.{/n}
"They accepted. A smaller arrangement, with more work for me. Minagho offered to help find a place. She did not pretend that made it the same bargain. I appreciated that."
"She remembered the cost."
"Yes. I shall try not to make her regret remembering it. At least not until she has enjoyed being right about something else."''', c('"What do you want to build from it?"', "next")),
    n("independent", "Chivarro", '''"Both. The traveler has agreed to carry inquiries. The collector wants to see something before discussing payment. Naturally, everyone finds their own caution respectable and other people's caution expensive."
{n}She gives you the two replies.{/n}
"There. No debt to Veyr, no house ready for me, no one to blame for the arithmetic. I have an audience for a proposal. I paid for that with an evening and a room I would never have chosen for pleasure."
"You enjoyed part of it."
"I did. Do not tell anyone. They might try to pay me in satisfaction."
{n}She takes back the replies and smooths their folds with the edge of her nail.{/n}
"It was good to speak without watching a factor count the value of every name. I want more than that. But I am glad we kept it."''', c('"What comes next?"', "next")),
    n("next", "Chivarro", '''"Someone called Sivane. She used to perform in rooms I arranged. A succubus with an excellent sense of an audience and a much less excellent sense of when to stop insulting the person paying her."
"You liked her."
"I paid her. The distinction mattered to both of us."
{n}Chivarro draws a final letter from the stack. This one has no elaborate seal.{/n}
"She heard I was making introductions again. She has a performance and no patron willing to purchase it on terms she can tolerate. I have a prospective audience and no performance to show them. It is almost suspiciously convenient. I have told her so."
"And her answer?"
"That she expected me to recognize a good offer without requiring it to flatter me. I missed her less after reading that."
{n}The amusement fades into something more intent.{/n}
"I want a place where the guest comes because I have chosen what is worth seeing. I used to own the room, the introductions, the rules. Losing them taught me which parts I wanted back. It did not make me grateful to have lost them."''',
      c('"And where do I come into it?"', "request"),
      c('"Can you stand letting her own something you cannot overrule?"', "control")),
    n("control", "Chivarro", '''"Able? Certainly. Willing? That depends on what she asks me to pay for it."
"That sounds like the beginning of an argument."
"It is the beginning of every useful agreement. I know what makes people wait for a door to open. Sivane knows what she can do once they are inside. If she wants me to supply an audience and sit silently while she insults it, she should expect an argument worth hearing."
{n}Chivarro studies you.{/n}
"You are wondering whether I will put a collar on the disagreement. I have used worse things than a sharp answer to keep a house orderly. I am not pretending you invented that suspicion."
"And this time?"
"This time she owns the thing I want to sell. I can refuse it. I cannot make it better by tightening something around her throat. I shall have to be persuasive. It is irritating to be reminded of a skill one has not lost."
{n}There is no apology in the answer. There is a plan you can question.{/n}''', c('"Then what part are you asking me to take?"', "request")),
    n("request", "Chivarro", '''"Come to the first rehearsal. Tell me what you actually see. Sivane knows which audiences please me. Minagho knows which answers will amuse or aggravate me. I want a third opinion that is neither trying to keep a contract nor sharing my bed out of habit."
{n}She pauses.{/n}
"That last phrase was less graceful than I intended."
"Habit can be pleasant."
"It can. I want to know what you pick when nobody is steering you. It is the only market research I trust."
{n}She places Sivane's letter between you.{/n}
"You need not finance the venture. Nor lend it your title. I have already told the prospective guests that they are paying for a performance. If it fails to interest them, I would rather know before I have rented somewhere large enough to echo."''',
      c('"I will attend as your guest and give you an honest opinion."', "guest"),
      c('"I will help with the rehearsal, if Sivane wants someone unfamiliar to try it with."', "participant")),
    n("guest", "Chivarro", '''"Good. I shall try not to argue with every disagreeable word. Only the ones you cannot defend."
{n}She sets your chair a little closer before putting the letters away.{/n}
"Stay a moment before you go. I have spent the day making arrangements. I would like to hear something that does not require an answer by tomorrow."
{n}You tell her about a small pleasure from your day. She asks one exact question, then another. By the third, you realize she is enjoying the detail rather than looking for a use for it.
When she tells you about hers, it is the look on a messenger's face when she paid him promptly and refused to receive the speech he had prepared about trust. She demonstrates his expression so precisely that you laugh before you can help it.{/n}''', c('[Keep the invitation as a guest.]', flags=done("business_finished", "rehearsal_guest"))),
    n("participant", "Chivarro", '''"I will ask her. She enjoys discovering how a stranger moves before he learns what she expects. You may find her difficult to impress."
"Does she find you difficult to impress?"
"She claims otherwise. Her most irritating habit is noticing when I am pleased."
{n}Chivarro writes your offer beneath her reply. Then she leaves it open for you to read. She has promised Sivane an available participant, not an obedient one.{/n}
"There. Accurate enough to be almost dull."
{n}You stay while she folds the letter. The conversation wanders away from plans. She asks what you would do with an evening that nobody could interrupt, then supplies an answer of her own that begins with a locked door and ends, after some revision, with a room whose door she would not need to lock.{/n}''', c('[Offer to take part in the rehearsal.]', flags=done("business_finished", "rehearsal_participant"))),
], "evening_kept", 24)

s("minaghos_unfinished_sentence", "Minagho's unfinished sentence", [
    n("start", "Minagho", '''{n}You find Minagho on the narrow stair outside the rented room. She is holding a chipped cup and listening to rain tick against a broken gutter.{/n}
"Chivarro is writing to the performer. She has crossed out the same line four times. I thought I would leave before she asked whether it sounded reasonable."
"Would you have told her?"
"I would have told her it sounded like an order pretending to ask a question. She knows that already. She is trying to make it sound like a better question."
{n}Minagho makes room for you on the stair. The cup contains water, which she regards with the disappointment she usually reserves for the tavern's beer.{/n}
"I wanted a moment without anyone else improving the conversation. There are things I can say in front of her. There are things I would rather not have her finish for me."''', c('"Then I am listening."', "history")),
    n("history", "Minagho", '''"I am trying to decide what to do with a morning in which I am not waiting for news of the next person sent to kill me."
"You do not expect the danger to end."
"No. But the immediate list is shorter, and I am tired of giving the remaining names every hour I possess."
{n}She turns the cup between her palms.{/n}
"You know something of what I have chosen since coming here. You have had opinions about it. I should like to hear what you think I am making for myself, rather than another account of what I could become if I were sufficiently impressed by you."''',
      c('"You have put work into helping people you once would have used."', "redemption", requires=("minagho.ran_redemption",)),
      c('"You have built influence through the cult. You enjoy the authority."', "cult", requires=("minagho.ran_cult",)),
      c('"The training has given you something that takes time to earn."', "training", requires=("minagho.ran_dragon",)),
      c('"You have been testing strength that does not depend on a patron\'s favor."', "legend", requires=("minagho.ran_legend",)),
      c('"You have a roof. That is not the same as wanting to stay under it."', "sanctuary", requires=("minagho.ran_sanctuary",)),
      c('"You are still bound to my service. I cannot ignore that in the answer."', "service", requires=("minagho.ran_demon",)),
      c('"You could go anywhere now. Where?"', "freedom", forbids=("minagho.ran_demon",))),
    n("redemption", "Minagho", '''"Do not make me sound patient. I supplied information. I did useful things. I have also spent afternoons wanting to tear an imbecile apart because he made a simple task difficult."
"Wanting and doing are different."
"Yes. I have discovered that the space between them can be extremely tiresome."
{n}She drinks the water, makes a face at its lack of interest, and sets the cup beside her.{/n}
"Chivarro knows why I am trying. She does not always like the result. Sometimes I do not like it either. But I have done enough to know that stopping would be a choice, not proof that the effort was impossible."
{n}Her voice hardens slightly.{/n}
"I do not want to be admired for the first inch forever. It is an excellent way to remain very small."''', c('"What would you rather I notice?"', "morning")),
    n("cult", "Minagho", '''"Yes. They listen. They want something I can give them, and they have discovered that pleasing me is easier than disappointing me. I shall not pretend the arrangement disgusts me."
"Do you want that from everyone?"
"Sometimes. Then Chivarro tells me precisely why I am being an idiot, and I remember that an audience which never contradicts me is less useful than I expected."
{n}She leans back against the stair's wall.{/n}
"I could fill a room with people who tell me what I want to hear. I have done it. The room becomes unbearable when I have a question whose answer matters. I am trying to keep a few people outside that arrangement. It is more difficult than acquiring the worshippers in the first place."''', c('"Then ask me something whose answer matters."', "morning")),
    n("training", "Minagho", '''"Time. Repetition. Being told that trying to win every lesson defeats the purpose of the lesson. I have developed an impressive collection of objections."
"Have any of them helped?"
"Some. Not the ones I enjoyed making."
{n}She holds one hand open, then closes it slowly, as if testing a movement she has practiced.{/n}
"I do not know what the last day of that work will feel like. I know I have begun wanting to reach it for something other than the pleasure of proving that I could. Chivarro finds that interesting. She also finds the hours inconvenient. Both observations are fair."
"And you?"
"I intend to find it inconvenient, loudly, without anyone deciding I have abandoned it."''', c('"You can complain to me."', "morning")),
    n("legend", "Minagho", '''"I liked the idea better before discovering how much effort it involves. There ought to be a more entertaining way to become strong."
"You know several."
"Yes. Most came with someone else's hand around the result."
{n}She rubs one palm with her thumb.{/n}
"This is mine to practice badly. Mine to improve. I have begun to understand why you thought that distinction was worth the inconvenience. Do not look too pleased. I have not agreed that every difficult thing is secretly good for me. Some are merely badly arranged."
"You will tell me which?"
"At length. I hope you have considered what sort of company you have acquired."''', c('"I have had some warning."', "morning")),
    n("sanctuary", "Minagho", '''"No. A safe roof is useful while deciding. It becomes less useful if everyone beneath it expects gratitude to occupy the rest of one's life."
"Is that what you expect from me?"
"I expect you to tell me when you want something. I have become suspicious of generosity that waits quietly until it can name its price as a disappointment."
{n}She looks at the rain beyond the stair.{/n}
"I want to choose some company. Some work. Somewhere to go that I have not selected because I have run out of other places. I am capable of wanting those things while remaining a thoroughly inconvenient guest. Chivarro considers that one of my more reliable qualities."''', c('"Then begin with the company."', "morning")),
    n("service", "Minagho", '''"At least you have not begun calling it a gift."
{n}She leaves the cup where it is.{/n}
"There are things I want while bound to you. There are things I have said to you before this evening. I am not going to erase them to make the account simpler. But I will not tell Chivarro that your permission is the same as my freedom."
"And what do you want out of this?"
"To finish it without a sermon."
{n}Her voice is steady, and her hand has found the edge of the stair the way it used to find a hilt.{/n}
"And to hear whether you can sit beside me while I am displeased. You have received more agreeable company from people who had less reason to be afraid of displeasing you."''', c('"Finish it, then."', "morning")),
    n("freedom", "Minagho", '''"An excellent beginning. Also a large amount of empty space when one has spent too long thinking only of the next escape."
"You could leave."
"I could. I may. I told you what I intended then, and I have not taken a short visit as a vow to inhabit your city forever. But Chivarro is here now. She wants to try something. I want to see it."
{n}She smiles at the sound of a chair moving in the room above.{/n}
"She believes she has invented wanting a venture on her own terms. I remember her wanting it before either of us was willing to admit we enjoyed seeing the other succeed. It would be a shame to miss the performance."''', c('"And what do you want for yourself while you stay?"', "morning")),
    n("morning", "Minagho", '''"An hour in which I do not have to make my past useful."
{n}The answer comes so quickly that she seems annoyed with herself for having it ready.{/n}
"Everyone who knows me has something to say about what I did. Usually they are right about the events and less interesting about the conclusions. I took this city. People suffered for it. I can remember that without wanting every conversation to become a ceremony in which I either boast or beg."
"What would you talk about instead?"
"The roof opposite. Someone has repaired one tile and left the rest. It is an extraordinarily hopeful thing to do. I would like to know whether they ran out of tiles or confidence."
{n}You look where she indicates. The new patch gleams darker than the old roof beneath the rain.{/n}
"Perhaps they began with what they had."
"That sounds like something Chivarro would say before sending for more expensive materials."
{n}Minagho draws her knees slightly closer, making room for you to settle on the stair. Neither of you has a good view, but the broken gutter provides a small, irregular rhythm. She listens to it for a while before speaking again.{/n}
"I used to know this district by how easily people could be made to disappear in it. Now I have a favorite bad stair. You may enjoy the absurdity. I do."''',
      c('[Take her hand.]', "hand", requires=done("minagho_chosen"), forbids=("minagho.ran_demon",)),
      c('"I can give you an hour and an opinion about the roof."', "roof")),
    n("hand", "Minagho", '''{n}She lets you take her hand. Then she turns it so your fingers fit more comfortably together.{/n}
"Chivarro asked what you are like when you do not want an answer immediately. I said she would have to discover that herself."
"You could have told her."
"I could. I wanted her to have a reason to sit with you. It is an excellent thing to know about someone, and people rarely think to ask until they need it."
{n}Minagho leans against you. Her hair brushes your cheek. When you turn your head she is already there, and the kiss she gives you is not quiet at all.
Afterward she keeps her forehead near yours.{/n}
"Do not make every hour sensible. I am beginning to like them too much."''', c('[Stay until the rain eases.]', flags=done("minagho_answered", "minagho_quiet_hour"))),
    n("roof", "Minagho", '''"Then I shall be extravagant and ask for both."
{n}You discuss the roof. Minagho proposes motives for the repairer that grow progressively less credible. By the fourth, you accuse her of inventing a better story because she dislikes the likely one. She admits it without shame.
The rain slackens. Someone in the street below carries a ladder past the doorway. Both of you fall silent until the footsteps have gone, then Minagho begins laughing.{/n}
"Now I shall have to find out. We have invested too much thought in it to tolerate uncertainty."
"You wanted an hour without a task."
"And look how long I managed. I should be congratulated."
{n}When Chivarro opens the upper door, Minagho tells her about the roof as though it is an urgent matter. Chivarro hears enough to understand what sort of conversation she has interrupted, and stays on the landing to listen.{/n}''', c('[Leave them the rest of the quiet evening.]', flags=done("minagho_answered", "minagho_quiet_hour"))),
], "business_finished", 24)

s("the_performer_and_the_key", "The performer and the key", [
    n("start", "Narrator", '''{n}Chivarro's new rehearsal room was once a bathhouse. The water has been shut off, and a platform now spans the empty shallow basin. A narrow gallery runs above it. The place smells of old plaster, lamp oil and rain that has found a patient way through the roof.
Chivarro stands in the middle of the platform, looking up. A woman in a dark traveling coat watches from the gallery rail. She is a mature succubus, wearing her own form in the shuttered building. Her wings are folded close enough to suggest she has already measured every inconvenient passage.{/n}
"Sivane," {n}Chivarro says.{/n} "You have my answer about the upper rail. It will not bear your weight and the scenery."
"It will bear mine."
"Until it doesn't."
"I could fly."
"The scenery cannot. Nor can the audience."
{n}Sivane looks down at you.{/n}
"Our third opinion?"
"Our guest," {n}Chivarro says.{/n} "Who has agreed to be honest. Try not to resent it when the agreement becomes inconvenient."''', c('[Introduce yourself and ask to hear the performance proposal.]', "proposal")),
    n("proposal", "Sivane", '''"A host invites Winter into his house because he thinks a guest must obey the rules beneath another's roof. Winter accepts. The host discovers that his table, his servants and finally his own reflection have begun answering the guest instead of him."
"A comedy?"
"Until the audience realizes which of the two they have been applauding."
{n}Sivane descends the stairs and joins you beside the platform.{/n}
"I can perform the host and Winter. My two assistants handle the masks and the lamps. I hand a guest a key. They may refuse it, give it back, or use it when I tell them what it opens. A refusal changes the scene; it does not stop it. Audiences adore a guest who refuses. It lets them feel brave at someone else's expense."
"She wants to finish with Winter keeping the house," {n}Chivarro says.{/n}
"I want the audience to wonder why they assumed the host deserved it."
"He does not have to deserve it for losing it to become repetitive."
{n}Sivane spreads her hands.{/n}
"That is why I asked her to watch a rehearsal before improving something she has not seen."''', c('"Then show us the room as you mean to use it."', "room")),
    n("room", "Narrator", '''{n}The proposed audience will sit on benches around the shallow basin. The platform is low enough that a guest can step onto it. A painted door stands at one end, held upright by braces that remain visible when you walk behind it. On its reverse, the wood is bare.
Chivarro points out a narrow passage between the last bench and the wall.{/n}
"That stays clear. If you make people step over each other to leave, the suspense becomes irritation."
"Or fear," {n}Sivane says.{/n}
"Fear they have paid to enjoy is useful. Fear that their coat is trapped beneath a stranger is untidy."
{n}She moves the bench herself, then asks you to walk the passage. There is room now, though barely.
Sivane joins you behind the painted door. From here the room looks smaller, and the guests would appear in fragments between its braces.{/n}
"This is where I change the mask. I want the host to hear the audience before Winter appears. It gives me their impatience. I can work with that."
{n}Chivarro listens. She has stopped touching the furniture.{/n}''',
      c('"Let her try the delay. We can judge what it does after seeing it."', "delay"),
      c('"Show us the transformation without the delay first. We can compare the effect."', "comparison")),
    n("delay", "Chivarro", '''"A full attempt before objections. I can manage that."
{n}Sivane looks at her with sufficient disbelief to make Chivarro smile.{/n}
"I said I could manage it. I did not say you should grow used to it."
{n}The first trial begins. Sivane, as the host, welcomes you to a feast at which nothing has been served. She offers the invisible abundance with such confidence that the empty table becomes funny. Then she steps behind the door.
You wait. Chivarro shifts once beside you. From behind the bare wood comes the sound of one chair being drawn back. Sivane appears in Winter's pale mask and asks whom you have been waiting for.
The question lands before either of you has prepared an answer.
Chivarro exhales slowly.{/n}
"Keep the silence. Shorten the speech before it. You asked us to wait twice, and only the second time was worth it."
{n}Sivane thinks, then nods.{/n}''', c('[Help reset the room for the full rehearsal.]', "fee")),
    n("comparison", "Narrator", '''{n}Sivane performs the transformation twice. The first time she changes quickly, keeping the host's last word alive in Winter's mouth. The second time she leaves you waiting while a chair moves behind the door.
Chivarro dislikes being asked to choose before discussing what each version sells. Sivane dislikes the word "sells." They argue for several minutes before discovering that both prefer the silence.{/n}
"You could have trusted my first answer," {n}Sivane says.{/n}
"I did not have your first performance," {n}Chivarro replies.{/n} "Now I do."
{n}She turns to you.{/n}
"You wanted the comparison. What changed?"
"I began supplying my own reason for the delay."
"Exactly. We should leave them something to do with the time."
{n}Sivane rests the mask against her hip. She is trying not to look pleased with the answer. Chivarro notices and has the kindness, or the discipline, not to mention it.{/n}''', c('[Help reset the room for the full rehearsal.]', "fee")),
    n("fee", "Chivarro", '''"Now the unattractive part. The room, lamps and assistants cost this much."
{n}She gives Sivane a short account. The performer reads it, then points to the advance beside her own name.{/n}
"Less than we discussed."
"The gallery repairs cost more."
"You chose the room."
"You wanted the height."
{n}Neither looks away. Chivarro turns the account around and crosses out the reduced advance.{/n}
"Very well. I carry the room's excess. You receive the amount we agreed. If we make another booking, we choose the room together before either of us promises a fee."
{n}Sivane accepts. Chivarro's mouth tightens as she recalculates her own share.{/n}
"You needn't congratulate me," {n}she tells you after the performer goes to unpack.{/n} "I dislike being praised for noticing an agreement I wrote myself."
"I was going to ask whether you still want the room."
{n}She looks up at the empty gallery.{/n}
"Very much. Which is how I know the expense is mine."''',
      c('"You looked pleased during the transformation."', "pleasure"),
      c('"What should they feel when they walk in?"', "audience")),
    n("pleasure", "Chivarro", '''"I was. I could hear the moment when people would stop pretending they knew what came next. It is a small sound. Usually the absence of another one."
"You miss it."
"I want it. Missing implies that the best part belongs to somewhere I cannot return. I have a performer, a room and an audience I have not yet persuaded. That is a present difficulty. I find it considerably more attractive."
{n}She takes a piece of chalk from the platform and marks where she wants the first lamp.{/n}
"Stand there. Yes. Now turn toward the door."
{n}You do. She studies the angle, then moves the mark a few inches.{/n}
"Better. Thank you. I wanted the first thing you saw to be her hand on the latch. The mask can wait. Wanting to know who is about to enter is more interesting than being shown at once."''', c('[Keep the lamp position for the rehearsal.]', flags=done("venture_begun"))),
    n("audience", "Chivarro", '''"That someone has expected them carefully. That they have entered a room where pleasure may require attention. And that the person beside them might notice if they fail to understand the first joke."
"You want them a little uneasy."
"I want them awake. They can be comfortable in their own rooms."
{n}She walks to the entrance and asks you to wait beside the painted door. When she turns back, her voice changes. You hear the welcome she would give a guest she wants to impress.{/n}
"Come in. We have saved the first question for you."
{n}The line is simple. The promise in it is not. For a moment the damaged room seems ready to justify the trouble of reaching it.
Then she relaxes and smiles at your expression.{/n}
"There. That is what I want to sell. You may keep this attempt without paying."''', c('[Return for the full rehearsal.]', flags=done("venture_begun"))),
], "minagho_answered", 24)

s("the_key_in_your_hand", "The key in your hand", [
    n("start", "Narrator", '''{n}The lamps are in place when you return. Sivane's two assistants are testing their cues. One moves a shutter across a lamp; the other turns a wooden wheel whose faint scraping sounds remarkably like snow against a door.
Chivarro welcomes you from the first bench. She is wearing a dark dress with a narrow line of pale stitching at the throat. There is nothing accidental about the way its plainness directs attention to her face.{/n}
"I have been told not to give advice until the end. You may observe what this costs me."
{n}Sivane brings the small brass key used in the performance. It opens the latch in the painted door. Behind that door there is only the back of the platform, not a hidden passage.{/n}
"If you hold it, I will ask you when Winter may enter. Refuse, give it back, do something I have not thought of: I need to know what a stranger actually does, not what Chivarro thinks everyone ought to do."''',
      c('[Take the key and try the scene.]', "take"),
      c('"Chivarro first. I want to see how a professional ruins it."', "watch")),
    n("take", "Narrator", '''{n}Sivane begins as the host. She offers you a seat at an imaginary feast and gives you the key with an air of immense generosity. It is apparently an honor to guard her door while she enjoys her own hospitality.
When Winter knocks, the host explains why you must not answer. The explanation grows more elaborate with every knock. Finally she admits that she invited Winter herself and has become frightened of being held to the invitation.
Chivarro watches you over the host's shoulder. She is enjoying the performance and your predicament with equal concentration.{/n}
"The latch," {n}Sivane says, still as the host.{/n} "Only a little. Tell me what you see."
{n}There is room to move around the host's sweeping cloak and reach the door. The movement is awkward by design. You can also ask her to step aside.{/n}''',
      c('[Slip past the turning cloak without breaking the scene. Mobility, DC 28.]', check=dict(Skill="SkillMobility", DC=28, Success="grace", Failure="caught", CommanderOnly=True)),
      c('"Move your splendid cloak, or open your own door."', "ask_move")),
    n("grace", "Narrator", '''{n}You pass behind the turning cloak at the moment it opens. Sivane adjusts without losing a word. When you reach the door, Chivarro gives one quiet, approving laugh.
You open the latch. Winter's mask appears from the other side, hanging where Sivane has placed it during the turn. The host is still beside you. For a moment it seems that the invited guest has arrived without needing her performer.
Sivane stops the scene and retrieves the mask.{/n}
"Good. That is what it does when the participant moves easily. Now I know where to stand when they don't."
"The Commander looked very pleased," {n}Chivarro says.{/n}
"You may tell the Commander that after I have finished using the door."''', c('[Let Sivane reset the scene.]', "grace_end")),
    n("grace_end", "Chivarro", '''{n}During the pause, Chivarro joins you by the bench.{/n}
"You moved well. I was beginning to wonder whether you would spend the whole evening trying to solve the host's problem instead of making her admit it."
"You would have made her ask more politely."
"I would have let her finish the speech. People reveal so much when they think they have not yet persuaded you."
{n}She brushes a speck of dust from your shoulder, then leaves her hand there long enough for you to notice.{/n}
"I enjoyed watching you. Not because you followed the cue perfectly. You looked curious. It is an attractive expression on someone who spends so much time being expected to know."''', c('[Stay for the rest of the rehearsal.]', flags=done("rehearsal_kept", "rehearsal_grace"))),
    n("caught", "Narrator", '''{n}Your foot catches the trailing edge of the cloak. Sivane stops before the fabric pulls her off balance. The key knocks against the painted door, producing a loud, thoroughly unseasonal clatter.
For a moment everyone is silent. Then Chivarro begins to laugh. Sivane looks at the cloak beneath your foot and considers it.{/n}
"No," {n}she says.{/n} "Do that again. More slowly."
{n}You free the cloth, apologize, and repeat the movement. This time the host's grand command ends with her own cloak preventing you from obeying it. Chivarro laughs again, before Sivane can ask whether it works.{/n}
"The host has built the difficulty herself," {n}Chivarro says.{/n} "Keep it as an option. Not every participant will arrive with the Commander's particular gift for disaster."
"I can hear you."
"I had hoped so. I was very clear."''', c('[Help turn the stumble into a deliberate alternative.]', "caught_end")),
    n("caught_end", "Chivarro", '''{n}Sivane adjusts the cloak's fastening so it will release under a sharp pull. The assistants try the movement. No one falls; the cloth drops with an indignity that suits the host perfectly.
Chivarro beckons you to the bench, still smiling.{/n}
"Do you realize what I could charge for a second performance of that?"
"I would expect a share."
"Naturally. A generous share of the blame."
{n}She picks a thread from your sleeve and holds it up between two fingers.{/n}
"I have seen a much smaller embarrassment end with blood on the scenery. You have deprived me of an expensive repair and provided a better joke. I am almost persuaded to keep you."
"Almost?"
"Your demands for payment concern me."
{n}She drops the thread. Her fingers remain on your sleeve while Sivane demonstrates the revised fall. When you look down at them, Chivarro looks directly at you and leaves them where they are.
The assistant pulls the fastening. The cloak collapses. Chivarro laughs again, but she is watching your face when she does.{/n}''', c('[Stay for the rest of the rehearsal.]', flags=done("rehearsal_kept", "rehearsal_stumble"))),
    n("ask_move", "Narrator", '''{n}Sivane, as the host, looks appalled that her guest has noticed the obstruction. She gathers her cloak with great dignity and moves it just far enough to help. You wait. Chivarro laughs before the host is forced to move it the rest of the way.
When you open the door, the waiting mask is exactly as unsettling as it would have been after a more graceful approach. Sivane stops and asks to try the exchange once more.
The second time, the host insists that the cloak is part of the honor she has bestowed on you. You return the key. That produces a silence so effective that Chivarro lifts a hand to prevent anyone from speaking over it.{/n}
"Keep that," {n}she says.{/n} "Let the host discover what happens when her favor is refused."
{n}Sivane nods. She writes the alternative into the margin of her working pages.{/n}''', c('[Let them keep the refusal as a real part of the performance.]', "ask_end")),
    n("ask_end", "Chivarro", '''"You made her do her own work. I enjoyed that."
{n}Chivarro joins you on the bench while the assistants move a lamp.{/n}
"I have spent centuries arranging invitations that make refusal seem impolite. It is galling to watch someone hand a key back as though it were a spoon."
"Will you arrange a different invitation?"
"A better one. Something no guest would be fool enough to hand back."
{n}She leans closer, lowering her voice.{/n}
"If my cloak obstructs you, move it. Patient guests are terribly easy to overcharge, and I should hate to find you cheap."
{n}Sivane calls for quiet, and Chivarro settles beside you to watch the next scene.{/n}''', c('[Stay for the rest of the rehearsal.]', flags=done("rehearsal_kept", "rehearsal_refusal"))),
    n("watch", "Narrator", '''{n}Chivarro accepts the key. Sivane offers her the host's elaborate welcome, and for the first few lines Chivarro allows herself to be guided through it. Then the host asks her to guard the door while the feast begins.
Chivarro sits down.{/n}
"I have come as a guest. You may employ someone if you want the door guarded."
{n}Sivane remains in character with visible effort.{/n}
"It is an honor."
"Then you will have no difficulty finding someone who wants it."
{n}The assistants laugh. Sivane pauses the scene and considers how to continue from an immediate refusal. Chivarro offers to play more cooperatively. The performer refuses that offer, which seems to please her.
The new version makes the host guard her own door. She cannot reach the feast she has promised while keeping Winter outside. When Chivarro offers to let the guest in, the host finally has to explain why she is afraid.
You watch the answer become part of the performance.{/n}''', c('"You gave her a difficult guest."', "watch_end")),
    n("watch_end", "Chivarro", '''"She asked for an unfamiliar answer. I supplied one."
{n}Chivarro returns the key and joins you on the bench.{/n}
"Would you have obeyed the first request?"
{n}You tell her what you might have done. She does not turn it into an argument about the best way to attend a play. Instead she asks what you thought of the host when the door became her own responsibility.
The question leads somewhere more interesting than praise. You speak about the moment when the joke became uncomfortable. Chivarro listens, then asks Sivane to repeat just that exchange. The second attempt is quieter. It holds the room.
When it ends, Chivarro rests her hand on the bench close to yours.{/n}
"That is why I wanted you here. Stay curious. I have enough people who tell me the room was splendid."''', c('[Stay for the rest of the rehearsal.]', flags=done("rehearsal_kept", "rehearsal_watched"))),
], "venture_begun", 24)

s("a_room_she_likes", "A room she likes", [
    n("start", "Narrator", '''{n}Chivarro invites you to see the rooms she has hired for the remainder of the rehearsals. The address is close enough to the bathhouse that she can walk between them without arranging a journey. It is also farther from the main street than the more convenient lodgings she rejected.
She opens the door herself. Inside are a low couch, a table with one sound drawer, and a broad window facing a blank wall. A strip of late light has found its way down between the buildings.{/n}
"You may dislike it honestly," {n}she says.{/n} "I have already paid."
"The wall?"
"No one opposite can look in. I am very fond of it."
{n}She has hung a length of dark cloth above the couch to cover a stain in the plaster. It changes the room more than the hired furniture does. On the table lies a small box of ornaments and an unfinished cup of tea.{/n}
"I wanted you here before I filled the place with work. After that, every chair becomes a place where someone has asked me for a decision."''', c('"What made you choose it?"', "choose")),
    n("choose", "Chivarro", '''"The door closes without being lifted. The window opens. The owner asked how long I wanted it rather than who would be visiting. I found the combination irresistible."
{n}She touches the edge of the hanging cloth.{/n}
"And this corner. I could imagine sitting here before I imagined receiving anyone in it. That has become an expensive preference."
"Where is Minagho?"
"Out. She has her own errands and a place here when she wants it. We have a rule about bringing company home. We break it with great ceremony, and then bill each other."
{n}She takes two cups from a shelf.{/n}
"She asked why I wanted this room instead of sharing whichever hiding place suited us both. I told her that I wanted to leave a book open and find it where I had put it. She offered not to move my books. It took us some time to reach the part where I meant more than the books."
"Did she understand?"
"She complained about the view and left. I am still waiting to learn which part of the conversation she intends to have next."''',
      c('"Show me the part you chose for yourself."', "notice"),
      c('"You wanted a door she has to knock on."', "separate")),
    n("notice", "Chivarro", '''"That I chose it. You would be surprised how many people assume a woman who can arrange a splendid evening has no preferences when she is alone."
{n}She puts the cups on the table and opens the ornament box. Inside are several pieces wrapped separately in scraps of cloth. She chooses a dark pin, then a pale one, and holds them against the hanging fabric.{/n}
"I have spent too long deciding what an audience will see first. I am trying to decide what I would like to see when I wake. An embarrassing problem to find difficult."
"Must it be one of those?"
{n}Chivarro lowers both pins.{/n}
"No. That is irritatingly obvious now that you have said it."
{n}She puts them away and leaves the cloth unadorned. For a while she simply looks at it.{/n}
"There. A decision with no witness to impress. Except you, who have already ruined the opportunity."''', c('"I will try to be a less useful guest."', "tea")),
    n("separate", "Chivarro", '''"Sometimes. Sometimes I simply want to sleep without hearing her invent a better version of an argument she had six hours earlier."
{n}She reaches for the teapot. The lid rattles against the rim.{/n}
"She offered to move everything here. I said that would rather defeat the purpose. Then she asked which of her possessions offended me."
"What did you tell her?"
"That her questions were taking up more room than her possessions. An excellent answer. I have enjoyed it considerably less since she left."
{n}Chivarro pours too much into one cup and pushes the other beneath the stream.{/n}
"You could send for her."
"And have her arrive convinced I was lonely enough to surrender? No."
{n}She sets the pot down. The dark tea has reached the lip of your cup.{/n}
"There. You have heard the entire sensible conversation I intended us to have. Now tell me whether you prefer this wall with a curtain or without."
"Chivarro."
"I know. I heard myself. I am still entitled to dislike it."
{n}She waits beside the couch instead of beginning another explanation. When you join her, she sets the overfilled cup on the table with an expression that dares you to complain.{/n}''', c('"And tonight?"', "tea")),
    n("tea", "Chivarro", '''"Company while the light lasts. After that, we shall see what you can afford."
{n}She gives you a cup. The tea is too strong. She notices your first sip and removes the leaves, which have been steeping throughout your conversation.{/n}
"I could pretend I prefer it this way."
"Do you?"
"No. Fortunately I invited someone who has already seen me make a more expensive mistake."
{n}She dilutes both cups. The small failure seems to make the room easier to inhabit.
For a while you speak about the rehearsal. Chivarro is pleased that Sivane kept the participant's refusal in the scene. She is less pleased that the performer has begun treating every correction as a test of independence. You ask whether she has told her that.{/n}
"Tomorrow. Tonight I should like an hour without another woman discovering how much I need her to be brilliant."
{n}Chivarro sits beside you, leaving a little space.{/n}''',
      c('[Put your arm around her.]', "close", requires=done("chivarro_chosen")),
      c('"Forget the view. Come here."', "new_interest", forbids=done("chivarro_chosen")),
      c('"Then let us spend it as friends. Tell me something you have done badly on purpose."', "friends")),
    n("close", "Chivarro", '''"Finally. I was beginning to think I had priced that space too high."
{n}She settles against you. The position is comfortable until one of the couch's cushions gives way beneath her elbow. She pauses, considers the insult, and moves the cushion to the floor.{/n}
"That will be the first thing I replace if the performance earns anything."
"Before the view?"
"I like the view. Do listen."
{n}You kiss her when she turns toward you. She draws you closer, then breaks the kiss long enough to inform the couch that it is on notice. When the other cushion attempts the same betrayal, she laughs and gets up to fetch a folded blanket.
The remedy works. You have no audience to appreciate the result and no need to make the interruption elegant.{/n}''',
      c('"I would like to stay close like this for the evening."', "warmth"),
      c('"I\'m staying later."', "later")),
    n("new_interest", "Chivarro", '''{n}She does not move closer to make it easier for you. She looks you over the way she once looked at a new face at the top of her stair: pricing it, and enjoying the pricing.{/n}
"I have been wondering how long you would sit there being tasteful."
{n}She holds out her hand, palm up, the gesture of a madam naming a sum.{/n} "Come and find out what I cost when I am not charging."
{n}You take the hand and she pulls, not hard, only enough. The kiss begins as a negotiation and stops being one when she catches your lower lip between her teeth. Chivarro keeps your hand in hers afterward. She looks pleased in a way she has not arranged for anyone else to notice.{/n}''', c('[Keep the date gentle and make time for another.]', flags=done("room_kept", "chivarro_date_earned"))),
    n("warmth", "Narrator", '''{n}Chivarro stays against you while the strip of daylight climbs the wall outside. She tells you about a room she once disliked so intensely that she rearranged its furniture every time its owner left. Eventually he began crediting her with a theory of design. She let him.
You ask what was wrong with the room. She describes a chair that forced every guest to look up at its owner, a lamp that shone into their eyes, and a door placed where no one could see who was listening outside.
Then she stops.{/n}
"I have made it sound like strategy. Mostly the chair was ugly. I wanted it gone."
{n}You laugh together. She kisses you again, less cautiously this time, then returns to the comfortable place she has found against your shoulder.
When you leave, she walks you to the door and asks for another evening without work spread across the table.{/n}''', c('[Promise to ask her for another unhurried evening.]', flags=done("room_kept", "room_warmth"))),
    n("later", "Narrator", '''{n}Chivarro looks at your mouth, then sets your cup deliberately out of reach.{/n}
"First, I would enjoy your undivided attention. You have been watching the curtain as though you expect an ambush."
"Minagho?"
"Would knock. Once. For the pleasure of making me hear it."
{n}The thought amuses her until your hand reaches her waist. For a heartbeat her clever answer disappears. You have seen her recover from threats more quickly.
She catches your wrist and draws you closer.{/n}
"There. You have discovered an effective interruption. Use it again."
{n}You kiss her. The couch complains beneath the change in weight, and she closes her eyes with an expression of profound disgust.{/n}
"If you laugh, I shall remember it."
"For how long?"
"Stay and find out."
{n}You do. She lights one lamp, leaving the other cold, and hangs her outer robe on the chair she warned you not to trust. Its legs hold. When she returns, her composure is still there in the lifted chin, the measured approach. Then she bends to kiss you and forgets the line she had clearly prepared, pushes you down onto the complaining couch, and straddles you there with her knees sunk into the blanket, working your shirt open from the collar down, one button to a breath.
Much later, she points at the surviving chair.{/n}
"That one has earned another week."
{n}You suggest the couch was equally obliging. Chivarro presses her lips to your wrist before answering.{/n}
"You have a weakness for damaged things that make an unreasonable amount of noise. I shall have to watch that."''', c('[Stay until you are both ready to part.]', flags=done("room_kept", "room_intimacy"))),
    n("friends", "Chivarro", '''"Badly on purpose? I once gave a man exactly the introduction he requested after he explained my own guests to me for half an evening. The two of them despised each other immediately. Both blamed me. It was worth the inconvenience."
"Did you know they would?"
"I hoped. There are pleasures in the world one cannot guarantee."
{n}You trade stories of mistakes whose consequences became funnier with distance. Chivarro is less interested in whether you were right than in how long it took you to notice the part you had misunderstood.
The light fades. She lets the room become dim before lighting a lamp, enjoying the brief interval in which nothing needs to be shown clearly.
When you rise to leave, she touches your arm.{/n}
"Thank you for coming. I wanted someone to know that I like this place before I begin complaining about it."''', c('[Leave her the quiet room she chose.]', flags=done("room_kept", "room_friendship"))),
], "rehearsal_kept", 24)

s("the_price_of_her_name", "The price of her name", [
    n("start", "Narrator", '''{n}Minagho is waiting at the bottom of Chivarro's stair. She wears Mina's face, an expensive expression of boredom, and gloves too fine for the loose railing beneath her hand.
She looks up when you descend.{/n}
"How was the view?"
"A wall."
"She described its virtues at length. I had no idea masonry could be such excellent company."
{n}She pushes away from the railing and offers you a folded handbill.{/n}
"Someone has found a more profitable use for me. Look. I have become an instructive example."
{n}The advertisement offers private readings from the correspondence of Baphomet's fallen general. Its author promises details of the treachery at Drezen, names of secret worshippers, and a list of those who bought the demon's favor. A woodcut beneath the title gives Minagho an improbable crown.
She taps the crown.{/n}
"I would never have worn that."
"Is any of it yours?"
"Some. Enough to interest me. I should like to discover which thief has developed literary ambitions."
{n}The advertised reading takes place in a disused storeroom two streets away. Minagho has already found its entrance. She has waited here for you instead of going inside.{/n}''', c('"What do you want me to do?"', "want")),
    n("want", "Minagho", '''"Listen before you decide you have understood. It will distinguish you from the rest of the audience."
{n}She turns the handbill over. On the back, three lines have been copied in a cramped hand. They concern stores taken from a quartermaster who later disappeared.{/n}
"This order was mine. The date has been changed. So has the recipient. Someone has given a dead man a buyer who is still alive."
"To sell the name?"
"Or to sell the omission. People become remarkably generous when a document is about to be read aloud."
{n}Her smile returns, thin and appreciative.{/n}
"I would have charged more. He has put the wrong sum beside the fee."
"You sound almost offended on professional grounds."
"Almost? I taught better liars than this."
{n}She tucks the sheet away. For a moment you can see the old general in the casual way she measures the street, the doors, the people who could be persuaded to remember her passage differently.{/n}''',
      c('"Is this a threat to the cult?"', "cult", requires=("minagho.ran_cult",)),
      c('"You have been trying to build something different. This will follow you into it."', "changed", requires=("minagho.ran_redemption",)),
      c('"What would the dragons tell you to do?"', "dragon", requires=("minagho.ran_dragon",)),
      c('"Would your new mortal acquaintances recognize you in these papers?"', "mortals", requires=("minagho.ran_legend",)),
      c('"If your service is the reason you waited for me, say so."', "service", requires=("minagho.ran_demon",)),
      c('"Let us hear what he thinks he owns."', "reading")),
    n("cult", "Minagho", '''"Some of the names would be useful. Some would be inconvenient. I can work with either, provided I learn them before everyone else."
"You want his list."
"I want his sources. Any fool can steal a list. A useful fool knows where another can be found."
{n}She studies the little crown again.{/n}
"He has made one excellent decision. He promises to describe me in detail but never promises that I am safely dead. Fear keeps the price up. Perhaps he can be taught."
"And the living man he has falsely named?"
"May be innocent of this particular purchase. I have no idea what else he has bought."
{n}You wait. She sighs.{/n}
"Very well. We can distinguish his actual sins from the ones printed here. Do not expect me to stop noticing which are useful. I have followers to feed and people who would cheerfully see them dead. You know what I built."
{n}She folds the paper small enough to disappear into her glove.{/n}''', c('"Then begin by learning what is true."', "reading")),
    n("changed", "Minagho", '''"Yes. I had noticed the inconvenience of having done things."
{n}The words are sharp. She looks toward the stair, then back at you.{/n}
"The original order is real. I cannot produce a corrected version in which I was somewhere else being admirable. If we take the paper away, the man who wrote it is still dead. If we leave it, someone alive will pay for a purchase he never made."
"So correct that part."
"And stand there while they ask about the rest?"
{n}A cart passes. She watches its wheels until it has gone.{/n}
"I would rather frighten him into handing it over. There. You may stop looking for the improved answer. That is the one I thought of first."
"You came to ask me to listen."
"An impulse I am beginning to regret. Come along before I recover my judgment."
{n}She goes ahead of you, anger lending the disguise a briskness that would look almost ordinary to a stranger.{/n}''', c('[Follow her to the reading.]', "reading")),
    n("dragon", "Minagho", '''"Something patient. They have a terrible supply of patience. I suspect they hoard it."
{n}She smooths the handbill against her palm.{/n}
"They would ask whether I wanted to keep living as though every witness were an enemy. I would ask whether they had met my witnesses. Then one of them would say something generous enough to make me want to bite him."
"And after that?"
"I might listen. Do not report it. They become insufferably encouraged by very little."
{n}She glances at the crown once more.{/n}
"The picture is wrong in another way. He has drawn someone certain she will always be what she is. I remember that certainty. I miss how little thought it required."
"Would you take it back?"
{n}She starts to answer quickly, stops, and pushes the paper into your hand.{/n}
"Ask me after this. If I am magnificent, I shall answer with appropriate modesty. If I am not, we can discuss his dreadful drawing."''', c('[Go with her.]', "reading")),
    n("mortals", "Minagho", '''"The soldiers? Some would recognize an order written by someone who never intended to carry the stores herself. They have opinions about officers. Most are refreshingly unpleasant."
{n}She flexes one gloved hand. A seam near the thumb has split.{/n}
"One of them repaired this after a practice bout. Badly. He told me to repair it myself next time. Imagine speaking to me like that while holding a needle."
"Did you?"
"I bought another pair. Then discovered I preferred these. I have spent an unreasonable amount of time being angry with the seam."
{n}She looks back at the bill.{/n}
"I could tell the man inside exactly who I am and watch him stop breathing for a moment. Or I could make him prove what he says while he still thinks I am someone he can cheat. The second will take longer."
"You have already chosen the second."
"I have chosen an escort. Do not hurry to congratulate the rest of me."''', c('[Enter with her.]', "reading")),
    n("service", "Minagho", '''"Your enemies would enjoy seeing your servant accused in a crowded room. They would enjoy seeing her kill the accuser considerably more. I thought you might have an opinion about which amusement to supply."
"What is yours?"
"Take his sources. Leave him frightened enough to remember whose papers he sells."
{n}She studies your expression with an attention quite unlike the insolence in her voice.{/n}
"You asked. I have given you the answer before trying to improve it for you."
"I am coming to hear the reading, not to order a killing."
"Then we shall both listen. I hope he has rehearsed."
{n}She steps aside to let you choose the direction. Her smile returns when you take the street she already indicated, but the little calculation that preceded it remains plain.
At the door, she removes one glove, checks the split seam, and pulls it on again. Nothing in that familiar gesture settles the bond between you.{/n}''', c('[Attend the reading.]', "reading")),
    n("reading", "Narrator", '''{n}Six people sit on borrowed stools. A narrow table supports a locked box, three copied pages and a candle whose light flatters none of them. The reader introduces himself as a salvager of important records. Minagho pays for two places and requests a receipt.
The man blinks at that. He supplies one.
His first reading is a genuine order. His second mixes a genuine opening with a sentence written by someone who has never commanded a garrison. He gives the living buyer's name slowly, allowing the audience to appreciate its value.
Minagho leans close to your ear.{/n}
"He has confused a ration mark with a purchase price. I was right. He has charged too little."
{n}One listener begins copying the name. Another watches Minagho, uneasy without knowing why. The reader unlocks the box to display the original at a safe distance from anyone who might recognize the ink.
Beside the first sheet lies a packet tied with a faded cord. Minagho's fingers stop moving on your sleeve.{/n}
"That one was sealed when I sent it. He has more than a handbill."
{n}The reader asks whether anyone would like to pay for a closer inspection.{/n}''',
      c('[Compare the order with the copied page before the reader can hide it. Knowledge: World, DC 31.]', check=dict(Skill="SkillKnowledgeWorld", DC=31, Success="proof", Failure="price", CommanderOnly=True)),
      c('"I will pay for an inspection. Keep the original on the table."', "price"),
      c('"Minagho knows this hand better than any of us. Let her question him."', "question")),
    n("proof", "Narrator", '''{n}The altered sum is not the only mistake. The date belongs to a week before the recipient held the office named beneath it. You ask the reader which of his records supplied that title.
He begins explaining the difficulty of wartime copies. Minagho interrupts with the correct abbreviation, its meaning, and the name of the clerk whose handwriting he has attempted to imitate.
The listener with the notebook stops writing.
The salvager reaches for the sheet. You lay his own receipt beside it.{/n}
"An account supported by genuine papers," {n}Minagho says, reading the promise above his signature.{/n} "Show us what we paid to hear about."
{n}He looks at the receipt. Inspection was meant to cost extra; she has made refusing it sound like an admission that the advertisement was false.{/n}
{n}She has not raised her voice. The reader takes his hand away. She draws the true order toward herself and points to the line she dictated years ago.
For the first time that evening, she does not offer a joke.{/n}
"This part happened. That part is your invention. Do not make me defend you by mixing them."
{n}The room has grown very still. The reader looks from her to the woodcut and back. Recognition begins badly and gets worse.{/n}''', c('[Require the public correction and take a witnessed copy of the real order.]', flags=done("name_read", "name_corrected"))),
    n("price", "Narrator", '''{n}The reader asks a price high enough to make the other listeners look up. You cannot establish the discrepancy quickly enough to keep the original on the table without paying for the time.
Minagho opens her purse. She counts the coins one by one, making him watch what each additional moment costs.{/n}
"I intended to buy better gloves. You have become a personal disappointment."
{n}He accepts the payment. She holds the true order beside his copy and begins asking questions only its author could ask. His replies become shorter. The audience supplies an attentive silence in which every shortened reply can be heard.
At last he admits that the buyer's name came from an unsigned note. He will print a correction.
Minagho keeps his receipt and the note. She does not recover the coins.{/n}
"You bought the truth from a liar," {n}you say outside.{/n}
"I bought his time until the other customers could hear him. There is a difference of several very annoying coins."
{n}She flexes the torn glove once, sharply.{/n}''', c('[Keep the correction and the price it cost her.]', flags=done("name_read", "name_corrected", "name_paid"))),
    n("question", "Minagho", '''"How kind of you to provide an introduction."
{n}She puts the handbill beside the box, with its absurd crown uppermost.{/n}
"Who supplied the note about the buyer?"
"My sources are confidential."
"Then invent a less nervous one."
{n}He looks toward the door. She remains seated. The space between them suddenly seems much shorter than the table.{/n}
"You know whose order this is. You have recognized the hand. You are wondering whether the Commander brought a witness or a punishment. I suggest you keep wondering until you have answered."
{n}He produces the unsigned note. The people on the stools watch him do it, but when Minagho asks for the packet too, no one insists on seeing her pay.
Outside, she puts it into her sleeve.{/n}
"Efficient."
"They were afraid."
"Yes. Several had paid for the privilege of hearing about me. They received excellent value."
{n}She does not apologize. Nor does she pretend the correction would have been harder to obtain by another means. You have seen which answer still comes easily.{/n}''', c('[Leave with the packet and the public correction.]', flags=done("name_read", "name_corrected", "name_seized"))),
], "room_kept", 24)

s("the_paper_she_kept", "The paper she kept", [
    n("start", "Narrator", '''{n}Minagho has returned the hired room's chairs to their original places. On the table lies the salvager's corrected handbill. Beside it are a witnessed copy of the order, a list of names and a torn glove.
She is holding a needle as though considering where it would cause the most inconvenience.{/n}
"The buyer sent a thank-you note. He addressed it to Mina. I find that irritating in several ways."
"Will he keep the correction?"
"He has already paid to have it posted beside the first bill. Sensible man. No one tears down an accusation more eagerly than someone who has discovered what replaces it."
{n}She threads the needle on her second attempt. The thread catches in the split seam.{/n}
"I copied the names before sending the order where it could be examined. There were people in those stores when they were taken. The paper says nothing about them. It was not written to."
"Do you remember them?"
"Some. Not enough to give you a comforting answer."
{n}She sets the glove down and looks directly at you.{/n}''',
      c('"You lost the money for those gloves getting the correction."', "cost", requires=done("name_paid")),
      c('"The room went quiet when you threatened him."', "fear", requires=done("name_seized")),
      c('"You left them with proof they could examine without believing you."', "record", forbids=done("name_seized", "name_paid"))),
    n("cost", "Minagho", '''"Do not make a monument of the purse. I have lost larger sums on less useful evenings."
{n}She draws the needle through. The stitch is too tight and puckers the leather.{/n}
"I wanted him to suffer for making me pay. Afterward, outside. I had the note, the correction, everything we went for. I still considered going back."
"What stopped you?"
"You were there. So were the witnesses. I was tired of giving him interesting material. Choose whichever answer you find least disappointing."
{n}She cuts the bad stitch and starts again.{/n}
"Next time I shall find the error faster. That is the improvement I am prepared to promise."
"Your stitch is crooked."
"And your timing is appalling. Come here and hold the light."
{n}She waits until you have moved the lamp before threading another length. The next stitch sits flatter. Neither of you congratulates it.{/n}''', c('[Hold the lamp while she works.]', "door")),
    n("fear", "Minagho", '''"It usually does. You have seen me use a room before."
"Those people will remember the threat as clearly as the correction."
"Perhaps more clearly. Fear has an excellent memory."
{n}She tests the seam between her fingers.{/n}
"The packet came with us. The false buyer's name will be withdrawn. I am not going to pretend I failed merely because the efficient answer was ugly."
"And if the next accusation is true?"
{n}The needle stops. She studies the small hole it has made in the leather.{/n}
"Then you may have to decide whether to stop me. I would prefer knowing that before I rely on you to stand in a doorway."
"I will not help you frighten a true account out of existence."
{n}She looks at you for a long moment. Then she takes up the needle again.{/n}
"You remain difficult company. Bring the lamp closer."
{n}The argument has not made her ashamed. It has made the next invitation less simple. She works beside you with that knowledge and does not ask you to soften it.{/n}''', c('[Stay without withdrawing what you said.]', "door")),
    n("record", "Minagho", '''"For which at least two of them will consider me a liar anyway. They arrived expecting a monster. They were offered a dispute about dates. I suspect they want their evening back."
"You were precise."
"I was angry. The two have been mistaken for each other before."
{n}She touches the copied list. One name is underlined.{/n}
"This clerk survived longer than I thought. I remembered the wrong man when he described the hand. I nearly supplied a second false accusation while correcting the first."
"But you checked."
"Yes. Before you say anything intolerable, I enjoy being right."
{n}She folds the list and puts it beside the corrected bill. The papers will leave together. She has not removed the mistaken recollection from the margin of her copy.
The glove is less accommodating. She pulls the thread too hard, curses, and gives you the lamp to hold while she frees it.{/n}
"You may remember me doing this badly. I would prefer that to having the room crowded with admirers of my newly discovered skill."''', c('[Make room beside her and hold the light.]', "door")),
    n("door", "Narrator", '''{n}A knock interrupts the next stitch. Chivarro comes in carrying a small book bound in cracked red leather. She puts it on the table, well away from the ink.
Minagho looks at it and says nothing.{/n}
"You left it at my room," {n}Chivarro says.{/n}
"I thought you wanted to find your books where you put them."
"My books. This is yours."
"You used to complain when I took it away."
"You used to read the best passages aloud instead of leaving it open across the only chair."
{n}Minagho's mouth tightens. Chivarro stands with one hand on the book, waiting. You set the lamp down carefully.
At last Minagho opens to a folded page.{/n}
"This one?"
{n}She reads two sentences. The second is a vicious description of a general who won a battle because his enemies could not believe anyone would attempt something so stupid. Chivarro begins laughing before Minagho finishes it.{/n}
"You changed the name."
"It improved the passage."
"You changed it to mine."
"You noticed."
{n}Chivarro sits. The book remains between them. She asks what happened at the reading, and Minagho supplies an account in which she complains more about the crown than the cost. When Chivarro looks at you, you supply the missing part.
Minagho objects to one adjective. She leaves the rest intact.{/n}''', c('[Stay while they finish arguing over the book.]', "kept")),
    n("kept", "Minagho", '''{n}When Chivarro rises to leave, Minagho closes the book and offers it to her. Chivarro shakes her head.{/n}
"Bring it when you visit. I should like to hear the rest without finding it on my chair tomorrow."
{n}Minagho keeps hold of it. She is very still for a moment, then slides it into the pocket beside the glove.{/n}
"Tomorrow evening?"
"Tomorrow evening. Knock more than once if I am slow. I may be changing."
"An excellent argument against knocking."
{n}Chivarro bends and kisses her, slowly enough to spoil the retort Minagho had begun preparing. At the door she glances toward the copied names, but she does not ask for an account of them a second time.
After she leaves, Minagho takes the glove out. The last stitch holds when she pulls it on. She admires it with a satisfaction quite out of proportion to the repair.{/n}
"Well. I seem to have acquired an appointment and saved myself the price of another pair. This is an absurdly successful evening."
{n}She offers you the corrected bill to read. The crown remains ridiculous. Everything beneath it is less convenient now, including the parts that are true.{/n}''', c('[Keep the corrected account and the evening you actually shared.]', flags=done("name_kept"))),
], "name_read", 24)

s("the_man_who_remembers", "The man who remembers", [
    n("start", "Narrator", '''{n}The musician waiting in the bathhouse keeps his instrument case on his knees. Grey has reached the tiefling's temples; the lacquer on his instrument case has survived less gracefully. His hands are steady. He does not rise when Chivarro enters.
Sivane introduces him as Rasen. She wants him for the final performance. He wants to know who is hiring him.{/n}
"You know me," {n}Chivarro says.{/n}
"That is why I asked."
{n}She pauses beside the platform. Rasen opens his case just far enough to check a fastening, then closes it again.{/n}
"I played in rooms you controlled," {n}he says.{/n} "I was paid. I also watched people discover that the rules they had agreed to were not the rules that mattered when someone important grew angry. I want the fee and the authority settled before I take out the instrument."
{n}Sivane folds her arms. She is allowing him to speak for himself, though the effort seems to cost her something.
Chivarro sits opposite him.{/n}
"Then let us settle them."''', c('[Listen to Rasen\'s terms.]', "terms")),
    n("terms", "Rasen", '''"Half now. Half before the audience enters. I leave when the agreed performance ends. If you want another, ask me and pay for it. No guest comes behind the platform without Sivane's permission and mine. If either of us stops because someone has threatened us, the fee remains ours."
"You have imagined a busy evening," {n}Chivarro says.{/n}
"I have attended one."
{n}She accepts the payment schedule and the limit on a second performance. At the last term, she asks what he considers a threat.{/n}
"Someone may dislike the music," {n}she says.{/n} "You may dislike the way he says so. I will not pay for an empty platform because you discover that a guest has an unpleasant voice."
"Someone may tell me what happens if I do not play a song he wants. I am not waiting to find out whether he means it."
{n}Neither answer is unreasonable. Neither is sufficient for the other.
Sivane asks to rehearse the final scene before deciding. Rasen agrees, provided it is understood that the rehearsal is part of the advance, not a free demonstration from someone who has yet to be hired.{/n}''', c('"Hear the scene. Then decide what the evening needs."', "music")),
    n("music", "Narrator", '''{n}Rasen's instrument is a flat stringed box played with two small hammers. Its first notes are dry and delicate. Then he strikes a lower course and the room seems to acquire a second, much colder ceiling.
Sivane takes Winter's mask. She does not need to raise her voice over the music. Rasen leaves space for the words and answers only after she has spoken. The effect is less a tune than another intelligence waiting at the table.
Chivarro remains perfectly still. When the scene ends, she asks to hear the last passage once more.
Rasen plays it differently. The lower notes now arrive before the host's final refusal, making the refusal sound anticipated. Sivane stops him.{/n}
"The first way. I want him to believe the answer is still his."
{n}Rasen nods. Chivarro looks from one performer to the other, measuring how much of what she wants depends on an agreement she cannot impose.{/n}''',
      c('"The first version changes the scene. I think the room is worth paying to keep safe for it."', "hire"),
      c('"The scene can stand with the lamps and your assistants. Do not buy an arrangement you cannot both trust."', "decline")),
    n("hire", "Chivarro", '''"Yes. I want the music."
{n}She says it to Rasen, without making the admission sound like a concession he should be grateful to receive.{/n}
"If a guest threatens you, stop and tell me. I remove the guest. If I refuse to remove him, you may leave with the fee. Ordinary criticism is not a threat. We can write examples until the lamps burn out, but those are the terms I will actually enforce."
{n}Rasen considers her answer.{/n}
"And if the guest is useful to you?"
"Then I shall be particularly annoyed with him."
"You used to be annoyed with the person who made it a problem."
{n}Chivarro's expression sharpens. She lets the silence last until she can answer without using it to frighten him.{/n}
"I want this performance. You have heard the price I am willing to pay. You may judge whether the answer is enough."
{n}He does. At last he places the instrument case on the floor and reaches for the written terms.{/n}''', c('[Witness the agreed payment and the guest-removal term.]', "hire_end")),
    n("hire_end", "Chivarro", '''{n}After Rasen and Sivane leave to rehearse, Chivarro remains beside the empty case.{/n}
"You think I wanted to threaten him."
"Did you?"
"For a moment. He spoke as though the only thing I could do well was make him afraid. I wanted to show him how carelessly he had decided to stop."
{n}She folds her hands.{/n}
"Then he played. I wanted that more. You may find the order unattractive. I am telling you because it was the order."
"What do you think will happen when a useful guest tests the rule?"
"I shall discover whether I priced the evening honestly. I expect to dislike the discovery."
{n}She rises and takes the advance to the performers herself. You hear her ask for the first ending once more. This time she is listening from the back of the room, where a paying guest will sit.{/n}''', c('[Keep the terms she chose to enforce.]', flags=done("musician_settled", "musician_hired"))),
    n("decline", "Chivarro", '''{n}Chivarro looks at the instrument. For a moment you think she will argue merely to keep hearing it.{/n}
"Then I shall not offer you work whose terms I mean to resent," {n}she tells Rasen.{/n} "The rehearsal fee is yours. Sivane may ask for the passage again while we have the time we paid for. After that, we part."
{n}Rasen accepts the payment without thanking her for the absence of a worse offer. Sivane asks for the last passage twice, learning where she will need to make the silence work instead.
When the musician leaves, Chivarro closes the door and leans against it.{/n}
"I wanted him."
"You could have accepted his terms."
"Yes. I could also have spent the evening waiting for someone to prove that accepting them was a mistake. He would have felt it. The music would have suffered. I am too vain to purchase that result."
{n}She returns to the platform.{/n}
"Show me the ending without him. I want to dislike the actual version, not the one I am inventing."''', c('[Watch the quieter ending with her.]', "decline_end")),
    n("decline_end", "Narrator", '''{n}Without the instrument, the assistants' small sounds become more important. A shutter against a lamp. One step on the platform. The host's breath between two lines he has not wanted to say.
Chivarro asks Sivane to shorten a movement that now waits for music which will not come. Sivane tries it. The scene becomes less grand and more exposed. You hear the host's fear clearly enough that his last act seems almost courageous.
Afterward, Chivarro stands close to you in the empty room.{/n}
"It has lost something. It has also become something else. I would like to resent the first fact without being accused of failing to notice the second."
"You can."
"Good. I intend to."
{n}She takes your arm for a moment, then releases it to help an assistant move the lamp. The evening's work continues with one less person and a different sound.{/n}''', c('[Keep the performance without the musician.]', flags=done("musician_settled", "musician_declined"))),
], "name_kept", 24)

s("the_first_small_audience", "The first small audience", [
    n("start", "Narrator", '''{n}The preview has four invited viewers, none of them attending under the Commander's authority. Chivarro seats them herself. She has asked you to stand beside her at the back and tell her afterward which moments changed the room.
The collector from her earlier introductions arrives last. He uses the name Nerath tonight and wears a mortal shape that fits his careful manners. Chivarro has met him before and does not mistake the shape for a history.
He compliments the choice of building, then asks whether the performer can be instructed to repeat particular effects privately after the showing.{/n}
"She can be asked," {n}Chivarro says.{/n} "The performance tonight is what you were invited to see."
"Naturally. I am interested in what else it might become."
{n}He takes his seat before she answers. Chivarro watches him settle, then turns to you.{/n}
"Hear the difference between a question and a purchase he has not yet paid for. He enjoys blurring it."''', c('[Watch the performance and the audience.]', "show")),
    n("show", "Narrator", '''{n}Sivane's host begins by making the viewers feel that they have arrived at a table where something desirable is about to happen. The empty feast amuses them. The first knock holds them still.
When the key is offered, one guest refuses it immediately. Sivane uses the refusal you rehearsed. The host must guard his own door, and his elaborate dignity becomes a practical inconvenience. The guest laughs, relieved to discover that refusing has not made him the evening's fool.
Nerath leans forward when Winter speaks. He is less interested in the threatened host than in the moment when the house begins to obey someone new.
Chivarro touches your sleeve, asking you to notice without interrupting the scene.
At the end, Winter keeps the house. The host stands outside his own painted door, still insisting that an invitation should have placed the guest under his authority. The lamps go dark before he can finish explaining why he deserved a different outcome.
There is a short silence. Then the viewers applaud.{/n}''',
      c('[Notice which reaction belongs to the performance and which to a private plan. Perception, DC 31.]', check=dict(Skill="SkillPerception", DC=31, Success="noticed", Failure="unclear", CommanderOnly=True)),
      c('"Ask them what they would actually buy, before we guess at their reasons."', "direct")),
    n("noticed", "Narrator", '''{n}Three viewers keep looking toward the painted door as they applaud. Nerath looks toward the person who refused the key. He has enjoyed the refusal less than the moment when the host lost control of his own room.
You tell Chivarro what you saw. She asks Nerath about the participant rather than the ending.{/n}
"Would you preserve the guest's ability to refuse in a private showing?"
{n}He smiles.{/n}
"I would prefer to know who will take the part. It could be arranged before the evening. Someone who would find the ending instructive."
"For whom?"
"For everyone present."
{n}Chivarro does not smile back. He has answered more than he intended.{/n}
"Then we should discuss the proposed guest before we discuss the price."''', c('[Let her require the actual proposal.]', "proposal")),
    n("unclear", "Narrator", '''{n}Applause and conversation overlap before you can separate Nerath's reaction from the others. You have impressions, but none you would trust as the basis for an accusation.
Chivarro listens when you tell her so.{/n}
"Then we ask. He would enjoy being condemned for an intention he could deny. I prefer to make him choose the words."
{n}She approaches Nerath while the other guests are examining the platform. He asks her price for a private showing with one appointed participant.{/n}
"Someone who would benefit from the lesson," {n}he says.{/n}
"Has this person asked for instruction?"
"That would spoil the surprise."
{n}Chivarro glances toward you, then draws a chair for him. Her expression is hospitable enough to make him underestimate how much explaining remains.{/n}''', c('[Hear the proposal before answering it.]', "proposal")),
    n("direct", "Chivarro", '''"Yes. They have had the pleasure of watching. They can now perform something useful for us."
{n}She asks each guest what they would pay to see again. Two want another public showing. One wants to know whether Sivane has other work. Nerath asks for a private version with a participant chosen in advance.{/n}
"A person I know would benefit from the lesson," {n}he says.{/n} "He has begun to misunderstand the source of his good fortune."
"And you would like Winter to remind him."
"Precisely."
{n}Chivarro looks at the painted door. Then she asks Nerath to sit and explain whom he wants on the other side of it.{/n}''', c('[Listen while he names the intended participant.]', "proposal")),
    n("proposal", "Nerath", '''"An associate. Well paid, and becoming ungrateful. I would invite him as my guest. He would receive the key. The performer would make the consequences of refusal rather clearer than they were tonight. Nothing crude. He should leave convinced that his position depends on remembering who opened the door for him."
{n}Sivane joins you before Chivarro answers. She has removed the mask, but the pale fastening still marks her hair.{/n}
"You want him frightened of losing his work."
"I want him to understand it."
"Then speak to him. I am selling a performance."
{n}Nerath directs his next words to Chivarro.{/n}
"I had understood you could arrange a more flexible evening."
{n}She looks at Sivane, then back at the buyer.{/n}
"You have seen the performance she brought. If you want a commissioned piece, offer her a fee and let her laugh at it. You cannot buy her with my invitation."
"An unusually scrupulous distinction."
"An unusually simple one. Do try to follow it."''',
      c('"Would you buy a private performance in which every guest knows what participation means?"', "counter"),
      c('"He has heard the answer. End this negotiation and use the interest the other guests showed."', "end")),
    n("counter", "Chivarro", '''{n}Chivarro names a price almost twice the sum written on the proposal beside Sivane's elbow. Then she lifts the proposal, folds it before Nerath can look down, and gives him a smile you have not seen directed at anyone she likes.{/n}
"For an exclusive evening. Your acquaintances will know whose generosity brought them here. Of course, if that is more display than you intended, the other offers can be considered."
{n}There are no other offers for an exclusive evening. Sivane opens her mouth. Chivarro places the folded paper in her hand.{/n}
"The performance remains as you saw it," {n}she tells Nerath.{/n} "My performer is tiresomely proud of her work. I find it sells better that way."
"And the choice of participant?"
"Will be hers. You will choose the wine. It will give your guests something agreeable to thank you for."
{n}He studies her, trying to decide whether he has been insulted. Chivarro waits with the serenity of someone whose answer to that question could only make the price rise.
He accepts. She requires the fee in advance, names the date, and escorts him out while he is still explaining how little expense matters to a man in his position.
Sivane unfolds the proposal when she returns.{/n}
"You doubled it."
"Nearly. I left him something to congratulate himself on."
"My fee remains the same?"
"We agreed it before rehearsals began."
{n}Sivane's expression changes. Chivarro notices and puts the coin purse beside her rather than between them.{/n}
"Finish the lamps. We can discuss the next performance when this one has paid for its room."
{n}The performer takes her mask and leaves. Chivarro watches the door, then counts the money without offering an explanation for either victory.{/n}''', c('[Keep the limited private booking.]', flags=done("preview_kept", "private_booking"))),
    n("end", "Chivarro", '''"There is nothing here for you," {n}Chivarro tells Nerath.{/n} "Sivane performs tragedy. You appear to require someone to frighten a clerk."
{n}He looks toward the other guests. They have heard. Chivarro raises her voice just enough to spare them the effort of pretending otherwise.{/n}
"Do write if you acquire a taste for the theater. I shall send a seat price your associate can afford."
{n}Nerath's compliment arrives polished into an insult. She receives it with a gracious inclination of the head and opens the door herself. The other guests suddenly discover questions that require them to remain.
Afterward, she walks the empty benches while Sivane collects her masks.{/n}
"You wanted them to hear," {n}you say.{/n}
"I wanted them to repeat it. He enjoys being thought dangerous. Now he will have to spend several very tedious dinners being thought ridiculous."
"He will resent that."
"Then we have both taken something from the evening."
{n}She lifts the folded proposal, looks at the generous price, and tears it cleanly down the middle.{/n}
"I did want the money. Do not ruin this by telling me otherwise."
{n}She puts the pieces beneath a crooked table leg. The table steadies. Chivarro tests it once, then leaves it there.{/n}''', c('[Help her send replies to the interested guests.]', flags=done("preview_kept", "open_booking"))),
], "musician_settled", 24)

s("the_entrance_she_wants", "The entrance she wants", [
    n("start", "Narrator", '''{n}Chivarro asks you to meet her before the final rehearsal. She has brought two dresses to her room and laid them across the couch. One is dark, severe and expensive enough that its restraint must have been difficult to purchase. The other is a warmer color, with a loose sleeve that moves whenever the wearer turns.
She is standing between them in a plain dressing robe, considering neither with much affection.{/n}
"Do not tell me they are both becoming. That would be true and useless."
"What do you want to know?"
"Which woman you would expect to greet you at the door."
{n}She holds up the dark dress.{/n}
"This one has already heard every excuse you intend to give her. The other might allow you to enjoy inventing them first. I know how to use either. I am trying to decide which evening I want to have."
"Have you asked Minagho?"
"Yes. She offered an opinion that would have left both dresses on the couch. I enjoyed it, but it did not solve the problem."''',
      c('"Try the severe one. I want to see what changes when you move."', "dark"),
      c('"Try the loose sleeve. You have spent enough rehearsals standing still."', "warm")),
    n("dark", "Narrator", '''{n}Chivarro changes behind the hanging cloth while you wait beside the window. When she steps out, the dark dress gives every movement a clear edge. She can make simply turning toward you feel like the end of another person's opportunity to speak.
Then she relaxes, and you see how much of the effect was her own choice.{/n}
"I would enjoy making Nerath wait in this," {n}she says.{/n} "I would also spend the whole evening looking as though I had expected him to disappoint me."
"Would that be inaccurate?"
"No. It might become tiresome. There are other guests."
{n}She tries the first greeting aloud. It is welcoming, exact and almost impossible to interrupt. You tell her which word made you want to answer. She repeats the line without that word. The welcome becomes an announcement.
She notices the difference at once.{/n}
"Yes. I need to leave them somewhere to enter the conversation as well as the room."''', c('"What would you choose if there were no guests?"', "alone")),
    n("warm", "Narrator", '''{n}Chivarro changes behind the hanging cloth while you wait beside the window. When she returns, the loose sleeve follows her hand half a moment after each gesture. It makes a small movement look unhurried.
She turns, testing the fabric, then catches the trailing cuff before it brushes a cup.{/n}
"There. The price of appearing effortless. One must remember where all the cloth has gone."
"You look less as though you are waiting to correct someone."
"Then I shall have to do it verbally."
{n}She offers the opening welcome. This version makes you feel she has noticed something interesting before deciding whether to tell you what it is. You tell her so. She tries it again without the pause, and the line becomes merely polite.
Chivarro restores the pause with a satisfied nod.{/n}
"I thought so. The dress suggested the wrong sort of haste. I can correct that."''', c('"What would you choose if there were no guests?"', "alone")),
    n("alone", "Chivarro", '''"Something soft enough to sleep in if the evening improves unexpectedly."
{n}She laughs at your expression, then sits carefully on the unoccupied end of the couch.{/n}
"You asked. I have spent a considerable part of my life making desire seem more complicated than it is. Some of it is simple. A fabric I like. A person whose hand I want on it. A bed I do not have to leave before dawn."
"And the complicated part?"
"Telling the ones who want me from the ones who want what I can arrange. In the Delights I kept ledgers for that. Here I have only you, and you keep coming back without an invoice."
{n}She smooths the dress over one knee.{/n}
"You argue with me, and then you return anyway, and you never once present the argument as a bill. I find that suspicious. I also find that I look for you at the door."
"You have disagreed with me too."
"Often with excellent reason. I am trying not to make the compliment entirely about myself."''',
      c('"What have you been meaning to ask me for?"', "asking"),
      c('"Tell me about an evening you enjoyed before you knew what to call it."', "memory")),
    n("asking", "Chivarro", '''"For you to come when I had nothing impressive prepared."
{n}She says it plainly, as though speed will prevent the admission from growing teeth.{/n}
"Not because I had suffered and needed consolation. Not because some difficulty had proved you were kind. Because I might have spent the day being impatient with a lamp, and you might still find me worth sitting beside."
"You could ask."
"I am aware. I have made a great art of knowing what I could do."
{n}Chivarro holds out her hand, palm upward.{/n}
"Come after the performance. Whatever opinion the guests have of it. I shall be tired, vain about some parts, unreasonable about others, and glad to see you. There. A very poor advertisement and an accurate invitation."
{n}She waits for your answer without improving the offer.{/n}''',
      c('"I will come for you, not for a report of the applause."', "promise"),
      c('"I cannot promise which evening. I will come."', "ask_later")),
    n("memory", "Chivarro", '''"Minagho once spent half a night trying to persuade me that she had invented a particular insult. I knew who had said it first. She knew I knew. We kept going because the argument had become more pleasant than anything waiting outside the room."
"Did either of you admit that?"
"No. Eventually I told her the insult was poorly constructed. She spent the rest of the night improving it."
{n}Chivarro smiles to herself.{/n}
"I remembered every version. That should have told me something. At the time, I considered it evidence that she had been annoying."
"What would tell you now?"
"That I want to hear the next version before she tells anyone else. That I notice when you are about to disagree and find myself pleased that the conversation will last longer. That I am choosing a dress and have somehow invited someone to learn what I am like when I cannot decide."
{n}She touches your hand lightly.{/n}
"Come after the performance, if you can. I should like an evening whose value does not depend on the people leaving the room."''',
      c('"I will come."', "promise"),
      c('"After the performance, then. When I can."', "ask_later")),
    n("promise", "Chivarro", '''"Then I shall save no speech for you. If I become eloquent, you may suspect I am avoiding the subject."
{n}She rises to change back into the plain robe. You help gather the unused dress when she asks, taking care with a fastening that has caught the couch's rough seam.
The small task leaves you close enough that she pauses beside you.{/n}
"Thank you. For the invitation's answer, I mean. The dress is less easily damaged than I am pretending."
{n}She chooses the loose-sleeved dress for the performance after all. When you ask why, she turns once, letting the fabric follow.{/n}
"I want to enjoy moving through the room. I have spent enough time arranging where everyone else will stand."''', c('[Keep the invitation for after the performance.]', flags=done("entrance_chosen", "after_show_promised"))),
    n("ask_later", "Chivarro", '''"A sensible answer. I detest sensible answers. I shall charge you for it later."
{n}She rises and folds the unused dress. You help free its fastening from the couch's rough seam, then move aside while she returns to the plain robe.
When she comes back, she has chosen the loose-sleeved dress for the performance.{/n}
"I want to enjoy moving through the room," {n}she says.{/n} "If the audience disappoints me, at least I shall have pleased myself for part of the evening."
{n}At the door she touches your arm.{/n}
"Come when you have the time. The offer stands. I do not withdraw an offer because the buyer is slow; I raise the price."''', c('[Keep the invitation open without promising an exact hour.]', flags=done("entrance_chosen", "after_show_open"))),
], "preview_kept", 24)

s("who_keeps_the_house", "Who keeps the house", [
    n("start", "Narrator", '''{n}Sivane has written another ending. Chivarro is holding its pages so carefully that you suspect the care is preventing her from doing something less useful to them.
In the new version, the host regains his house. He discovers that Winter has accepted the invitation to a feast that has never actually begun. Instead of fighting for the key, he serves the guest a bowl of hot water and ends the meal. Winter must leave when the hospitality is complete.
Sivane has not decided which ending she wants to perform.{/n}
"She asked for a version in which losing a house is not the only interesting thing that can happen to its owner," {n}she tells you.{/n}
"I asked you to consider it," {n}Chivarro says.{/n}
"You asked four times."
"You improved the answer each time."
{n}Sivane rests Winter's mask on the table.{/n}
"I can perform either. I will not pretend they say the same thing. The first leaves the audience inside a house whose owner has changed. The second makes them leave with the guest. I want to know which silence we want afterward."''', c('"Show us both endings without explaining them first."', "versions")),
    n("versions", "Narrator", '''{n}In the first ending, the host remains outside the door. His last appeal to the audience is almost charming. He reminds them that they accepted his invitation, laughed at his jokes, and allowed him to believe they were on his side. Winter says nothing. The door closes while he is still asking them to answer.
In the second, the host begins in the same desperation. Then he notices the empty bowl. He serves the water with the ceremony he used earlier to offer the absent feast. Winter accepts it, trapped for a moment by the pleasure of making him serve.
When the meal ends, the host opens the door himself. He does not ask Winter to leave politely. He recites the guest's own promise and watches the power of it change hands.
Sivane removes the mask.{/n}
"There. I like the first one's cruelty. I like the second one's patience. I do not believe either requires the host to become a better person."
{n}Chivarro has watched without interrupting. She turns to you only when Sivane has finished.{/n}''',
      c('"The first ending leaves me thinking about what the host expected from his guests."', "winter"),
      c('"The second gives the host a real discovery. I want to see him use it."', "host")),
    n("winter", "Chivarro", '''"You prefer the loss."
"I prefer being made to remember that I laughed with him before I knew what he was doing."
{n}She looks back at the painted door. Her first answer is too quick.{/n}
"One can always make an owner look ridiculous by taking away the room in which he knows how to behave."
{n}Sivane waits. You do too. Chivarro notices both acts of patience and does not appear grateful for them.{/n}
"Very well. I heard myself. I have been arguing with more than the ending."
"Would you like us to choose the other because of that?" {n}Sivane asks.{/n}
"No. I would like the first to earn its cruelty. Do not make the host small before he loses. Let us understand why people accepted his invitation. Then let the door close."
{n}Sivane considers the direction, then tries the final appeal again with less desperation and more charm. It becomes harder to answer. Chivarro nods once.{/n}''', c('"That is the version I would keep."', "winter_end")),
    n("winter_end", "Chivarro", '''{n}After Sivane leaves to rehearse, Chivarro sits on the platform's edge.{/n}
"I know a play is allowed to remind me of something unpleasant. I would prefer to be the person who notices it first."
"You did notice."
"After making it everyone's difficulty. A less impressive achievement."
{n}She lifts one foot and turns it slightly, studying the dust on her shoe.{/n}
"I do not want to buy back the Delights merely to prove I could. I want every story about a lost house to stop looking at me as if I deserved mine. I did deserve it, in several respects. I resent being told so by a play."
"We can leave the play as a play."
"Yes. And I can dislike the resemblance without forbidding the door to close. Let us see whether I am capable of enjoying something that has annoyed me this precisely."''', c('[Keep Winter\'s ending and the host\'s dangerous charm.]', flags=done("ending_rehearsed", "winter_ending"))),
    n("host", "Chivarro", '''{n}Chivarro's pleasure is immediate. She makes herself wait until Sivane has considered your answer.{/n}
"I like that he must actually serve the meal," {n}the performer says.{/n} "He cannot simply discover a better command. He has to finish the thing he offered when offering it cost him nothing."
"Keep that part slow," {n}Chivarro says.{/n} "Let Winter enjoy being served. That is why the mistake works."
{n}Sivane tries the movement again. The host's hand shakes as he lifts the bowl; then he steadies it by setting both feet on the floor. Winter accepts the water like a victory.
This time the silence after the meal has a different weight. Chivarro is leaning forward when the door opens.{/n}
"There," {n}she says.{/n} "He has something to lose all the way to the last line. Do not let him sound certain until the guest steps outside."
{n}Sivane agrees. She writes the change in the margin and gives the pages to an assistant.{/n}''', c('"That is the version I would keep."', "host_end")),
    n("host_end", "Chivarro", '''"I am pleased you chose it. I am also relieved that I can say why without beginning with my own lost establishment."
{n}She sits on the platform's edge and gestures for you to join her.{/n}
"I wanted him to discover something he could do. I have heard enough accounts of loss delivered as though the only interesting question is whether the loser has learned to accept it gracefully. Sometimes she would like the door back. Sometimes she would like a different house. The wish does not become simple because someone has written an elegant lesson around it."
"Does this room feel like a different house?"
{n}Chivarro surveys the lamps, the visible braces and the benches she has moved so often.{/n}
"At moments. Then an expense arrives and it feels like a very familiar profession. I am pleased by both, which is an inconvenient answer to give anyone who hoped I had become less ambitious."''', c('[Keep the ending in which the host completes the invitation.]', flags=done("ending_rehearsed", "host_ending"))),
], "entrance_chosen", 24)

s("when_the_door_opens", "When the door opens", [
    n("start", "Narrator", '''{n}On the evening of the finished performance, Chivarro reaches the bathhouse before anyone needs her. She walks the passage behind the benches, checks the platform's braces, and moves one lamp back to the chalk mark you helped her choose.
She is wearing the loose-sleeved dress. When you compliment it, she makes a small turning gesture so you can see why she chose it.{/n}
"I intend to enjoy at least the entrance. After that, I am available to be disappointed on the merits."
{n}Sivane comes out carrying the key. Her assistants have checked the cloak's fastening and the latch. The painted door is ready to refuse or admit its guest.
Chivarro offers the performer her hand. Sivane takes it for a moment.{/n}
"A full house?" {n}she asks.{/n}
"Enough people to know when someone has stopped listening."
"Then I shall try to prevent it."
{n}Chivarro turns toward the entrance as the first knock sounds.{/n}''',
      c('[Join her as she receives Nerath\'s private audience.]', "private", requires=done("private_booking")),
      c('[Join her as she receives the guests from the open booking.]', "open", requires=done("open_booking"))),
    n("private", "Chivarro", '''{n}Nerath brings the guests whose names he submitted. Among them is the associate he once intended to instruct through a trap. Chivarro greets that man separately, describes how participation works, and tells him where he can sit if he prefers only to watch.
He chooses a bench near the side passage. Nerath notices.{/n}
"You have made him timid," {n}he murmurs to Chivarro.{/n}
"I have told him what he bought a seat to see. You may enjoy the performance without improving him."
{n}Her voice carries no farther than it needs to. Nerath smiles as though she has made a private joke he intends to forgive.
Chivarro waits until he has taken his seat before turning to you.{/n}
"He has paid. He knows the terms. If he decides to dislike them now, I intend to believe the dislike. I shall not invent a kinder explanation because I wanted his money."
{n}Then she opens the inner door and invites the room to begin.{/n}''', c('[Watch the opening scene.]', "first_scene")),
    n("open", "Narrator", '''{n}The open booking brings a smaller audience than Nerath would have assembled, but the guests have come because someone described the preview well enough to make them curious. Chivarro enjoys asking which description persuaded them. She learns which phrases have begun circulating and corrects one claim that the door is genuinely haunted.
An elderly guest asks whether the hostess intends to perform too.{/n}
"Only the welcome," {n}Chivarro answers.{/n} "If you find it wanting, you may tell me after the person you paid to see has finished."
{n}The guest laughs and takes a seat. Another arrives determined to explain a different version of the tale. Chivarro hears the first sentence, then introduces him to someone who has already heard it. The two settle into conversation, leaving her free to open the inner door.
When she passes you, her expression is pleased.{/n}
"They have brought their own expectations. It is economical. We need only decide which ones to disappoint."''', c('[Watch the opening scene.]', "first_scene")),
    n("first_scene", "Narrator", '''{n}The host receives the guests with the confidence of someone whose house has never failed to obey him. His feast is empty, but his descriptions are so generous that several viewers glance at the table as though something may have appeared.
Then Winter knocks.
The first refusal comes from the audience. Sivane accepts it into the scene. The host must hold his own key and explain why his invitation has become a danger. The laughter changes. It still belongs to the audience, but the host can no longer be certain it is friendly.
Chivarro stands beside you, watching the benches instead of the platform. She has seen the movements before. Tonight she wants to know which people stop fidgeting when the door begins to matter.
At the next pause, a guest speaks too loudly from the front bench. The interruption is shaped as a joke, but it asks the performer to put another guest on the platform and make him answer for the host's cowardice.{/n}''',
      c('[Watch Chivarro enforce the terms of the private showing.]', "patron", requires=done("private_booking")),
      c('[Let the performer answer the interruption within the scene.]', "heckler", requires=done("open_booking"))),
    n("patron", "Chivarro", '''{n}Nerath has turned toward his associate. The man remains seated beside the passage. Sivane, still wearing the host's mask, says that the key has already been refused.
Nerath insists. His next remark refers to the associate's employment. Chivarro steps forward before he finishes it.{/n}
"You were told how participation works. He has answered."
"This is my evening."
"You purchased the performance. You did not purchase him."
{n}Nerath looks toward you, perhaps hoping Chivarro will hesitate to embarrass him before the Commander. She does not wait for your intervention.{/n}
"Come outside," {n}she tells him.{/n} "We can discuss the rest where the audience has not paid to hear it."
{n}For a moment he seems likely to refuse. Chivarro stands close enough to make the invitation unmistakable, then opens the passage beside his bench. He leaves with her. The door closes quietly.
Sivane waits until the room has settled. Then the host asks whether Winter has brought any other unexpected guests. The audience laughs with an unmistakable release of tension.{/n}''', c('[Remain with the performance while Chivarro settles the interruption.]', "ending")),
    n("heckler", "Narrator", '''{n}The guest has mistaken the invitation to participate for an invitation to nominate someone else. Sivane turns toward him and extends the key.{/n}
"A generous host offers his own chair first," {n}she says.{/n}
{n}He declines. The refusal becomes part of the host's argument with Winter, who appears to have discovered an entire room of people eager to offer someone else's hospitality.
Chivarro watches the man's face. He is embarrassed, but he is also laughing. He has found a way to remain in the audience without pretending he did not speak.
She stays at the back. The performer has handled it.
When the scene moves on, Chivarro leans toward you.{/n}
"That was why we rehearsed the refusal. I should have charged him for demonstrating its value."
{n}Her amusement is quiet enough not to disturb the next line.{/n}''', c('[Watch the final scene.]', "ending")),
    n("ending", "Narrator", '''{n}The host reaches the last part of his bargain. There is no feast left to describe into existence, no servant who will accept responsibility for the invitation, and no flattering account that makes Winter seem less at home.
Sivane gives the host a moment of real charm. He turns toward the audience and reminds them of the welcome they enjoyed. Some are still smiling when they realize he expects their pleasure to oblige them to save him.
Chivarro is beside you when the last scene begins. Her attention goes straight to the door, waiting for the ending she helped choose.{/n}''',
      c('[Watch Winter keep the house.]', "winter", requires=done("winter_ending")),
      c('[Watch the host complete the feast.]', "host", requires=done("host_ending"))),
    n("winter", "Narrator", '''{n}Winter takes the key. The host steps outside to prove that the invitation still means something, certain the audience will demand his return. The door closes.
His last appeal is beautifully measured. It is funny until you hear how little he has left except the belief that being entertaining should have protected him.
Sivane lets the final sentence remain unfinished. The lamps darken. In the silence, one viewer draws breath as though about to answer the host after all.
Then the applause begins. Chivarro remains still through its first wave. At the second, she joins it.
When the lamps return, Sivane stands beside the plainly braced door with the mask in her hands. The audience can see the room again. For a moment that makes the disappearance more impressive rather than less.{/n}''', c('[Meet the performers after the audience leaves.]', "after")),
    n("host", "Narrator", '''{n}The host sets the empty bowl on the table. He offers Winter the feast he promised and fills it with water made warm by his own hands. He serves without another boast.
Winter accepts with visible pleasure. The audience knows the guest has made a mistake before it knows what the mistake is.
When the bowl is empty, the host thanks Winter for attending the feast and opens the door. His hand trembles on the latch. He does not conceal it. The last word of the invitation returns to him, and the guest must step outside.
The door closes. This time the host does not turn toward the audience for praise. He remains with his hand on the wood until the lamps darken.
Chivarro exhales beside you. She begins applauding before the other guests have decided whether to break the silence, and their answer follows hers.{/n}''', c('[Meet the performers after the audience leaves.]', "after")),
    n("after", "Chivarro", '''{n}The guests leave with different accounts of the ending. Chivarro listens to enough of them to hear that the disagreement concerns the performance, not confusion about what happened. She seems satisfied by that distinction.
Sivane comes to the door after the last guest. Her assistants are already putting the lamps out. Chivarro asks them to leave the final one lit until everyone has collected their things.{/n}
"The fee is settled," {n}she tells the performer.{/n} "No deductions for the audience becoming inventive."
"I had noticed the audience becoming familiar," {n}Sivane says.{/n}
"You handled it well."
{n}The compliment is direct enough to stop the expected argument. Sivane accepts it, then asks what comes next.
Chivarro looks around the room.{/n}
"An account in the morning. Tonight, nothing I say while tired will be mistaken for an offer. Go and enjoy having finished."
{n}When the others have gone, she takes your arm.{/n}
"Walk me to the door. I would like to leave before I begin moving the benches for a performance that has not been arranged."''', c('[Leave the finished performance with her.]', flags=done("show_kept"))),
], "ending_rehearsed", 24)

s("after_the_last_lamp", "After the last lamp", [
    n("start", "Narrator", '''{n}Chivarro opens her door with an expression she has made no attempt to arrange. She is tired. Her hair has escaped part of its fastening, and the loose-sleeved dress is folded over a chair behind her.
When she sees you, she steps aside at once.{/n}
"Come in. If I begin telling you what the audience should have understood, interrupt me. I have been rehearsing the speech and it has become intolerable."
{n}There are no accounts on the table. She has put them in the drawer and closed it. A folded blanket now bolsters the couch's unreliable cushions.{/n}''',
      c('"You invited me to come whether the guests pleased you or not. I wanted to keep that promise."', "promised", requires=done("after_show_promised")),
      c('"I found the time. No accounts tonight."', "open", requires=done("after_show_open"))),
    n("promised", "Chivarro", '''"I am glad you did. I spent part of the day thinking that I should have made the invitation more attractive. Then I remembered that doing so would defeat the purpose. A remarkably inconvenient thought."
{n}She takes your coat or cloak if you have brought one and hangs it beside the door.{/n}
"I was pleased by some of them. I resented others. I enjoyed the room much more than I expected. I also spent an entire scene wanting to adjust a lamp that was not actually wrong. There. That is the report. You may prevent me from improving it."
"What would you like instead?"
{n}Chivarro looks at the closed drawer, then back at you.{/n}
"To stop feeling as though the next person who enters will need me to make the evening work."''', c('"You can leave this one to both of us."', "rest")),
    n("open", "Chivarro", '''"Yes. You have arrived before I persuaded myself that wanting company was another task I ought to complete efficiently."
{n}She makes room for you on the couch and sits at its other end.{/n}
"I enjoyed the performance. I have also thought of seventeen things I would change, most of which became urgent only after there was no longer time to change them. If you hear me begin the eighteenth, ask me something unreasonable. It may restore a sense of proportion."
"Would you like to show me the accounts?"
"No. I would like to discover that I can keep a drawer closed when there is someone in the room who might praise its contents."
{n}She looks at you with a tired, candid amusement.{/n}
"Stay. I shall try to make being here less work than producing an audience."''', c('"You do not have to produce anything for me."', "rest")),
    n("rest", "Chivarro", '''"Then tell me something you disliked."
{n}She hears herself and begins laughing.{/n}
"No. Not about the performance. About your day. Something small enough that you have not already been given advice about it."
{n}You tell her. She listens, supplies one thoroughly impractical remedy, and accepts your objection without defending it. When you ask for something from her day, she shows you the faint line where a fastening pressed her wrist during the welcome.{/n}
"I noticed it before the first guest arrived. I could have moved it. Instead I decided that a woman who had arranged the room could tolerate a little discomfort. By the third guest I was imagining the fastening's destruction in considerable detail."
"Did you move it?"
"Eventually. It took less time than resenting it. I remain annoyed by that discovery."
{n}The room grows easier around the shared complaint. Chivarro rests her head against the couch and lets her eyes close in the mortal guise she wore through the streets. After a moment she lets the disguise go, keeping her own face here with you.{/n}''',
      c('[Hold out your hand.]', "affection", requires=done("chivarro_affection")),
      c('"Rest. I\'ll stay, and I won\'t talk."', "quiet"),
      c('"I have a small, unreasonable question. What would you have done with a completely empty house tonight?"', "empty")),
    n("affection", "Chivarro", '''"Closer."
{n}She moves first, settling beside you before you have to decide how much space the invitation means. Her hand finds yours. She is warm from the room and entirely unhurried.{/n}
"I wanted to hear you at the back of the audience," {n}she says.{/n} "Once I knew you were there, I could stop checking."
"I was watching you as well as the performance."
"I suspected. I tried to enjoy that without beginning to perform for you too. I managed at least part of the evening."
{n}You kiss her when she turns toward you. She answers, then rests her forehead close to yours.{/n}
"That. I would like more of that, with fewer people waiting for me to count them afterward."
{n}Her thumb moves over your knuckles while she waits for your answer.{/n}''',
      c('"Then let tonight be quiet and close."', "held"),
      c('"I\'m staying the night."', "night")),
    n("held", "Narrator", '''{n}You remain together on the couch. Chivarro adjusts the blanket so neither of you has to keep rescuing it from the floor. When she becomes quiet, you let the quiet continue.
After a while she tells you that she has begun recognizing the sound of your arrival. She lists the details with a hostess's precision, then becomes annoyed with herself for making affection sound like surveillance.
You tell her what you have begun recognizing about her. That earns a laugh, an objection to one detail, and finally a kiss that ends the argument before either of you has won it.
The drawer remains closed. At the door, later, she tells you to remember the hour when the fighting is done, because she certainly intends to send a bill for it.{/n}''', c('[Keep the quiet evening as something you chose together.]', flags=done("after_lamps_kept", "after_lamps_close"))),
    n("night", "Chivarro", '''"You are. Take that pin out before it makes a hole in either of us."
{n}Chivarro turns her shoulder toward you. The small silver fastening that looked so effortless beneath the lamps resists your first attempt. She reaches back to guide your fingers, then withdraws her hand when you find the catch.
The ornament comes free. She exhales with such pleasure that you laugh.{/n}
"Do not flatter yourself. It has been tormenting me since the overture."
"I shall try to deserve the next one."
{n}She turns, tired amusement sharpening into interest.{/n}
"An ambitious evening after all."
{n}The kiss tastes faintly of the wine she barely had time to drink. She makes you wait through a second one before taking your hand toward the inner room. On the way she stops to put the silver pin into an empty bowl. You ask whether it has been condemned.{/n}
"Sentenced. I may pardon it when I see how it looks with another dress."
{n}That is the last business she attends to. In the inner room she lets the dress fall where she stands and steps out of it, pushes you back onto the bed with both hands, and follows you down, a knee either side of you, her loosened hair falling across your face and her fingers already at your belt. "Now," she says, "the part I have not rehearsed."
Near dawn, a cart rattles beneath the window. She lifts her head, listens as if she might have it arrested, then drops back against you.{/n}
"If you are leaving, lie convincingly. I should like another hour before I begin believing it."''', c('[Stay together through the quiet night.]', flags=done("after_lamps_kept", "after_lamps_close"))),
    n("quiet", "Narrator", '''{n}Chivarro agrees. She settles at one end of the couch while you take the other. Neither of you fills the first silence. The room has its own small sounds: a footstep outside, the settling of the lamp, a draught touching the hanging cloth.
At first she opens her mouth whenever something occurs to her, and shuts it again with visible annoyance. By the third time she has begun to find it funny.
When she finally speaks, it is to complain about the lamp, and then, visibly, to decide not to get up and fix it.
Later, she walks you to the door.{/n}
"I had forgotten that company could make a room quieter. Do not tell anyone. It would ruin my reputation as a hostess."
{n}Her hand rests on your arm for a moment. Then she lets you go.{/n}''', c('[Leave her the rest she wanted.]', flags=done("after_lamps_kept", "after_lamps_rest"))),
    n("empty", "Chivarro", '''"Inspected every room. Decided which one I disliked least. Filled it with the things I could not bear to leave in the others. Then complained that the house was too large."
"You answered quickly."
"I have considered it."
{n}She turns toward you.{/n}
"I used to think a completely empty house would mean that something had gone terribly wrong. No guests, no staff, no one needing the door opened. I could imagine quiet only as the aftermath of a disaster. This room has improved my imagination."
"Would you still want people to come?"
"Yes. I enjoy them. I enjoy wanting them to leave too. I should like to choose both without pretending one cancels the other."
{n}You discuss the impossible house until it has acquired an inconvenient staircase, a splendid view neither of you can describe, and a door Minagho would complain about before discovering she liked the room behind it.
Chivarro sees you out laughing. The real room seems to please her more when she returns to it.{/n}''', c('[Leave the imagined house unfinished and the real evening well spent.]', flags=done("after_lamps_kept", "after_lamps_rest"))),
], "show_kept", 0)

s("the_cost_in_daylight", "The cost in daylight", [
    n("start", "Chivarro", '''{n}Chivarro brings the account to a table by the bathhouse's open shutters. Daylight makes the room less flattering and the ink easier to read. She has already paid the performers and the assistants. What remains to decide is whether she wants another evening badly enough to arrange it.{/n}
"You may look," {n}she says.{/n} "I am not asking you to repair the numbers. I would like you to know what the room cost before you tell me it was worth it."
{n}She lays out the room hire, lamps, repairs and promised fees. There is no imaginary saving beside work someone did without being paid. The late repairs are in her column, where she agreed to put them.{/n}''',
      c('"What did Nerath\'s removal cost?"', "private", requires=done("private_booking")),
      c('"Did the open booking cover the evening?"', "open", requires=done("open_booking"))),
    n("private", "Chivarro", '''"The next booking. He paid for this one in advance, and the terms did not entitle him to a refund for preventing another guest's refusal. He demanded one anyway. I sent back the exact clause he had accepted."
"Will he make trouble?"
"He may speak ill of me. I expect it. He will also have to explain why the rest of his guests saw a finished performance while he waited outside. Several have already asked how to arrange another without him."
{n}She places a short letter beside the account.{/n}
"His associate wrote this. He enjoyed the show. He has not asked me to manage his employment, and I have not offered. He wanted to thank Sivane for letting him remain in his seat. I passed the message to her."
"Were you tempted to keep Nerath in the room?"
"Yes. It would have been convenient for several minutes. Then it would have become the rule everyone else remembered."''', c('"And the balance?"', "balance")),
    n("open", "Chivarro", '''"The agreed expenses, with a little left. Less than I hoped. More than I would have made from several splendid invitations that never became a paid seat."
{n}She shows you two requests for another performance.{/n}
"One wants a larger audience at the same price. I have declined. The other has asked what a fair price would be. I dislike the phrase. It usually means the person hopes I will be embarrassed to name a profitable one. But the question was at least a question."
"What did you answer?"
"The cost of the room, the performers' fees and an amount that makes arranging it worth my time. She asked whether that included receiving the guests myself. I said yes. She accepted."
{n}Chivarro allows herself a small smile.{/n}
"It is pleasant to discover that someone knows which part she wants to buy."''', c('"Then what does the balance mean for you?"', "balance")),
    n("balance", "Chivarro", '''"That I can arrange a second showing without pretending the first paid for a palace. That Sivane has been paid what she expected. That the next room must be chosen before I allow myself to imagine how well it would flatter the performance."
{n}She marks the balance beneath the final line.{/n}
"It also means I spent more hours on this than I would have admitted when we began. I like knowing how the room works. I like knowing which guest came because of something I said. I do not like being the person who has to notice every failing hinge."
"You want someone to share the work."
"Yes. I also want to remain the person who decides which room we are opening. Those desires are about to disagree unless I arrange something better than a servant expected to think like a partner."
{n}She taps Sivane's name.{/n}
"She has an offer of her own."''',
      c('"First, did you keep the musician\'s terms when the audience became difficult?"', "musician", requires=done("musician_hired")),
      c('"Did the quieter performance change what the guests wanted?"', "quiet", requires=done("musician_declined"))),
    n("musician", "Chivarro", '''"Rasen has already asked which room I intend to hire next. He considers this one an insult to the lower register."
"Does that mean he will return?"
"It means he expects me to buy him a better echo. I intend to show him three rooms and hire whichever he criticizes with the greatest affection."
{n}She taps his receipt. Beside his signature he has drawn a small, dreadful likeness of the broken shutter.{/n}
"He also sent me an invoice for an encore he did not play."
"What did you send back?"
"An account for the drinks he did not buy. We have reached an understanding."
{n}She is smiling when she folds the receipt, and she places it with the papers she means to keep rather than those already settled.
A thread of melody reaches you from the street. She pauses until the player turns the corner.{/n}
"He altered that passage on the night. I asked why. He said the room had finally earned it. Infuriating man. I want him at the next performance."''', c('"Tell me Sivane\'s offer."', "offer")),
    n("quiet", "Chivarro", '''"They spoke about the host's voice. Several remembered the breath before his last answer. Rasen's instrument would have made the room larger. Without it, they could hear how small the host had become."
"You preferred the music."
"I did. I can remember wanting it without treating the performance we made as a failed version of the one we did not buy. Sivane has asked to keep the quiet form available even if we hire him later."
{n}She checks the lamps' cost again.{/n}
"I shall have to stop thinking of less as a temporary embarrassment. Sometimes it gives a guest nowhere comfortable to hide from a line. I enjoy that effect too much to dismiss it merely because I could not charge for an instrument."''', c('"Tell me Sivane\'s offer."', "offer")),
    n("offer", "Chivarro", '''"Sivane wants two more performances and a share of whatever I persuade the audience to pay. She has developed a sudden interest in arithmetic."
{n}Chivarro draws a small square around the total. She has pressed hard enough to score the page beneath.{/n}
"I told her her fee was secure. She told me that was an excellent reason to take another commission. Then she named the woman who offered it. I know the woman. Her rooms are hideous, and her purse is not."
"Will Sivane leave?"
"She might. I have been deciding how much of the threat I admire."
{n}She turns the page. Two possible agreements lie beneath the account. One gives Sivane a share of the takings. The other buys two separate dates for a higher fixed fee.{/n}
"I could promise her fame. It works surprisingly often. Unfortunately I made the mistake of teaching this one how much applause costs."
"Which offer do you want to make?"
"The share. If she starts arguing about expenses, she may finally stop demanding a new painted door every time she dislikes the light. And if I fill the room at a higher price, I shall have someone worth boasting to."
{n}She looks again at the scored square.{/n}
"I dislike paying for the same victory twice. I dislike losing useful people more."''',
      c('"Make the offer. Keep the authority you need, and let her decide whether she wants her part."', "partner"),
      c('"Offer the two performances separately first. You can share work without promising a continuing partnership."', "separate")),
    n("partner", "Chivarro", '''"Then I shall try not to look relieved when she accepts."
{n}Sivane arrives carrying a sketch of the next stage. She lays it on the table before sitting. Chivarro glances at it, then pushes the new agreement beside it.
The performer reads the percentage twice. She changes the notice required before a rehearsal is cancelled. Chivarro strikes out an expense she considers imaginary. They disagree about the painted door until Sivane turns it around and shows her the split in the back.
Chivarro studies the damage.{/n}
"That was there before opening night."
"Yes."
"You let me compliment the lighting."
"It was excellent lighting."
{n}Chivarro laughs reluctantly. She adds the repair, and Sivane signs. Neither mentions the rival patron again.
After the performer leaves, Chivarro bends over the two names on the agreement.{/n}
"Mine goes first on the invitation."
"Does that matter?"
"Ask me after I have grown accustomed to seeing another beside it."
{n}She folds the paper and puts it in her own case. The rejected draft goes into the fire.{/n}''', c('[Keep the limited partnership she negotiated.]', flags=done("venture_settled", "venture_partner"))),
    n("separate", "Chivarro", '''"I can offer that. She may prefer it too. We have spent much more time disagreeing over one performance than discovering whether we want to repeat the arrangement."
{n}When Sivane arrives, Chivarro proposes two separate bookings on the terms they have already tested. Either can decline the second without forfeiting payment for the first. The performer considers it, then accepts.
They divide the remaining work: Sivane will confirm the assistants, Chivarro will confirm the room. Neither makes the agreement larger by calling it permanent.
Afterward, Chivarro folds her copy and puts it away.{/n}
"Two evenings I have chosen. After that, another answer. I would once have thought the uncertainty an invitation to be replaced."
"Do you now?"
"Sometimes. I intend to answer by being worth asking again. It is a more interesting use of my vanity."''', c('[Keep the two separate bookings.]', flags=done("venture_settled", "venture_bookings"))),
], "after_lamps_kept", 24)

s("what_she_will_take", "What she will take", [
    n("start", "Narrator", '''{n}Chivarro is packing the things that belong to her rather than to the hired room. The ornament box is closed. The hanging cloth is folded, revealing the stain she covered when she first invited you here.
She has not given up the room yet. The packing is a way to discover what another place would need to hold.{/n}
"Two more performances," {n}she says.{/n} "And then I must decide whether I want to keep asking this city for a room, or take the work somewhere it has not already heard about me."
"Have you chosen?"
"Not a city. I want to see what a place will pay before I decide to conquer it. Every empty seat is still an insult; I have merely learned to invoice it."
{n}She closes a small traveling case and tests its latch.{/n}
"I would like to talk about what I take with me. Some of it cannot be folded."''', c('"Tell me what you want to keep."', "keep")),
    n("keep", "Chivarro", '''"The work. Minagho, if she can resist telling everyone how much better she would have arranged it. And you."
{n}She lifts the ornament box out of the case and discovers that the lid no longer closes. Something beneath it has shifted.{/n}
"That sounded uncomfortably like a list of possessions. Help me before I begin assigning shelf space."
{n}You find a folded handbill under the box. It is the advertisement for Sivane's first performance. Chivarro smooths the crease with her thumb.{/n}
"I want to show you the next one. Preferably from a room where I am still pleased to see you when the lamps have gone out."
{n}She puts the bill into a narrow side pocket, then clears the place beside her on the couch.{/n}
"What shall I keep that place for?"''',
      c('"Keep it for me. Wherever you go, I come back to it."', "lasting", requires=done("chivarro_affection")),
      c('"Keep it for visits. No house, no promises. The nights I can get here."', "visits"),
      c('"Keep it for a friend. I won\'t leave you a promise I don\'t mean."', "friends")),
    n("lasting", "Chivarro", '''{n}Chivarro sits very still.{/n}
"Yes."
{n}She reaches for the case, closes it, and puts it on the floor. It tips against her ankle. She pushes it away without looking.{/n}
"I had prepared something much more impressive. You have inconvenienced me."
"Do you want time to remember it?"
"No. Come here before I do."
{n}Her hand closes over yours. She looks down at your joined fingers, smiling despite an evident effort to make the expression less revealing.{/n}
"You realize I shall write dreadful complaints about the places I stay? I expect replies. Preferably ones in which your accommodations sound worse."
"And if I cannot come?"
"Then tell me where to send the next complaint. I am resourceful."''',
      c('"Then come here."', "lasting_close"),
      c('"And when I have to leave?"', "distance")),
    n("lasting_close", "Narrator", '''{n}You kiss her before the next joke is ready. Chivarro catches your sleeve and keeps you close after the kiss ends.
Afterward she opens the case again. She puts a blank sheet into the narrow pocket with the handbill.{/n}
"For the first address. If I put it elsewhere, I shall decide it is business and write to you like a client."
{n}You ask how she writes to clients she especially likes. She shows you, adopting a courteous expression whose promise becomes quite unmistakable halfway through the demonstration. Then she spoils it by laughing.
You stay while she repacks the case. This time she leaves the lid open and rests her feet beside it on the couch, where you have room to sit close.{/n}''', c('[Keep her, and let her keep her road.]', flags=done("chivarro_future_spoken", "chivarro_lasting"))),
    n("distance", "Chivarro", '''"Your first journey will be worse than mine. I have been trying not to count the ways."
{n}She opens the narrow pocket in the case and slips a blank sheet beside the handbill.{/n}
"An address, when I have one. You will receive it before a description of the room. I know my own habits."
"What would you want sent back?"
"Your own handwriting. Anevia may be wonderfully efficient, but I would prefer she not conduct my courtship for me."
{n}She looks at your hand in hers.{/n}
"And when you do come, arrive early enough to find me awake. I have spent several evenings imagining a grand welcome and then falling asleep over the guest list. I should hate to waste a magnificent entrance on that."
"I could wake you."
"You could try. I am told I am difficult."''', c('[Promise the letters, in your own hand.]', flags=done("chivarro_future_spoken", "chivarro_lasting"))),
    n("visits", "Chivarro", '''"Then I shall have to make the invitations interesting."
{n}She considers you with a hostess's appraising attention.{/n}
"Sivane has promised me a new scene in which a judge must sentence his own reflection. I should like to sit beside you when he discovers who has been summoned as a witness."
"Does the audience get a part?"
"If you are afraid of another key, I can reserve a place beyond throwing distance."
{n}She smiles, then moves the case off the couch.{/n}
"That one is for later. Today I have a little time, a room I enjoy and no performer to distract us. Stay."''',
      c('[Stay close.]', "visits_close", requires=done("chivarro_affection")),
      c('[Stay and talk.]', "visits_talk")),
    n("visits_close", "Narrator", '''{n}Chivarro settles beneath your arm and tells you about a coast where the stones turn green in the shallows. She wants to see it before a merchant improves the description enough to spoil the place.
You ask who told her about it. She admits, reluctantly, that it was a guest she claimed to find boring.{/n}
"He spoke for almost an hour. I cannot remember his name."
"You remember the stones."
"Yes. I am furious with him."
{n}She kisses you, then describes the little boat she would refuse to board and the view she would insist on seeing from it. By the time she finishes, you have both found several reasons to laugh at the imagined journey.{/n}''', c('[Keep the visits.]', flags=done("chivarro_future_spoken", "chivarro_open_visits"))),
    n("visits_talk", "Narrator", '''{n}You remain while Chivarro sorts the ornaments into their separate wrappings. Each has a story she can choose to tell. Some she keeps short. Others acquire an unexpected detail when you ask why she bothered to keep the object.
One plain pin belonged to no powerful admirer. She bought it because the seller insisted it was too severe for her. Chivarro demonstrates the severe expression she wore while paying, and you accuse her of having rehearsed it for years.
She denies the charge badly enough to make you both laugh.
When you leave, the case is packed and the room is still hers for the nights she has agreed to rent it. She stands in the doorway looking pleased with both facts.{/n}''', c('[Keep the visits, and the stories.]', flags=done("chivarro_future_spoken", "chivarro_open_visits"))),
    n("friends", "Chivarro", '''{n}Chivarro hears the entire answer before speaking.{/n}
"Then I shall not leave one there. I enjoy you. I have never yet sold anything to a buyer who did not want it, and I am not beginning with you."
"Are you disappointed?"
"A little. I shall decide exactly how much after you have gone, and I shall not do it in front of you."
{n}Her smile takes the sharpest edge from the words.{/n}
"You will still hear what becomes of the work, whether you like it or not. I want your opinion when it is useful and your company when it is not. If I send an invitation, answer it. I am a demon, not a debt collector. Mostly."
{n}She makes room for you beside the case and shows you the ornament she has finally decided not to take. It is expensive, awkward to pack, and connected with a memory she no longer enjoys retelling. She has found a buyer for it. The transaction seems to please her more than keeping it ever did.{/n}''', c('[Keep her friendship.]', flags=done("chivarro_future_spoken", "chivarro_friendship"))),
], "venture_settled", 24)

s("before_the_last_road", "Before the last road", [
    n("start", "Narrator", '''{n}The last meeting before your departure begins in Chivarro's rented room. She has left the hanging cloth down while she finishes packing. Minagho has brought a small bag of the sugared fruit she lost during your mask game and put it in the middle of the table without explaining the gesture.
For once, no one has brought a proposal from a stranger.
Minagho asks what you know of the road ahead. You tell her what you can. She hears the uncertain parts without supplying a more flattering prediction.
Chivarro sets three cups beside the fruit.{/n}
"We have settled the work," {n}she says.{/n} "The performers have their agreements. The room is paid for. Whatever happens next, I am not leaving a pile of promises for someone else to discover."
"An ambitious standard," {n}Minagho says.{/n}
"I have been told I am an ambitious woman."
{n}Minagho touches her hand, and the answer between them becomes briefly private. Then they turn toward you.{/n}''', c('"There is something I want to settle before I leave."', "answers")),
    n("answers", "Chivarro", '''"Then say it before Minagho eats the last of those."
{n}Minagho has a piece of sugared fruit halfway to her mouth. She offers it to Chivarro instead, who accepts it with no sign that the maneuver has distracted her.
When Minagho turns to you, the amusement fades a little.{/n}
"I dislike farewells. People say things they cannot possibly know, and then expect gratitude for the prophecy. Tell me what you want when you return. I shall try to listen without improving it."
{n}Chivarro moves her cup to make room for yours beside it.{/n}''',
      c('"Minagho. You too. I am not leaving you out of this."', "minagho", requires=done("minagho_chosen"), forbids=("minagho.ran_demon",)),
      c('"The three of us. Together when we are together, our own roads when we are not."', "together", requires=done("minagho_chosen", "chivarro_lasting"), forbids=("minagho.ran_demon",)),
      c('"Minagho, you and I are friends. What Chivarro and I have stays hers and mine."', "friendship", forbids=("minagho.ran_demon",)),
      c('"No promises tonight. Just the visits."', "open", forbids=("minagho.ran_demon", "minachiv.chivarro_lasting")),
      c('"Minagho, you are still in my service. A farewell does not change that, and I will not pretend it does."', "service", requires=("minagho.ran_demon",))),
    n("minagho", "Minagho", '''{n}Minagho looks at you for long enough that Chivarro quietly rescues the fruit from her idle hand.{/n}
"Yes. I should like somewhere beside me that I keep because I expect you."
"Where?"
"An excellent question. I intend to complain about several possibilities before selecting the one Chivarro suggested first."
"I have offered no suggestions," {n}Chivarro says.{/n}
"You will. You are incapable of leaving an inadequately furnished room alone."
{n}Chivarro smiles at you over Minagho's shoulder. Minagho takes your hand, pulls you close and kisses you with a sudden impatience that betrays how carefully she has been sitting still.
Afterward she rests her forehead near yours.{/n}
"Come back with something better to discuss than your enemies. I want to know what makes you useless for an afternoon."''',
      c('[Keep them both, each in her own right.]', flags=done("complete", "future_two"), requires=done("chivarro_lasting")),
      c('[Keep Minagho, and Chivarro\'s visits.]', flags=done("complete", "future_minagho"), forbids=done("chivarro_lasting"))),
    n("together", "Chivarro", '''"Yes," {n}Chivarro says.{/n} "And I am buying a better couch. The one in my room squeaks whenever I look at it. I expect better manners from something I have paid for."
"I hope you intend to look at me instead," {n}Minagho says.{/n}
"You are already excessively pleased with yourself."
"I shall attempt consistency."
{n}Minagho reaches for your hand. Her thumb presses once against your palm before she speaks.{/n}
"Yes. The three of us. I should like another evening in which she forgets which of us she was scolding."
{n}Chivarro takes your other hand and draws both of you toward her. The first kiss becomes an argument over who has moved which chair. The second settles it.
When you sit back, their hands remain with yours on the table. Chivarro begins describing the better couch with such precision that Minagho asks how long she has been considering it. She does not get an answer.{/n}''', c('[Kiss them both.]', flags=done("complete", "future_together"))),
    n("friendship", "Minagho", '''{n}Minagho hears the answer without pretending it has cost her nothing.{/n}
"Then I shall know what invitation I am sending. I would rather have the truth than become very good at misreading your politeness."
"I still want you around."
"I heard. Do not say it twice, or I shall start to suspect pity."
{n}Chivarro remains beside her. She does not speak on her behalf or make you wait for a display of forgiveness.
After a moment, Minagho reaches for the sugared fruit.{/n}
"You still owe me a game in which Chivarro does not win by allowing us to distract each other."
"That is not an arrangement I can offer," {n}Chivarro says.{/n}
{n}Minagho laughs despite herself. The invitation, at least, is now plain.{/n}''',
      c('[Keep Chivarro, and Minagho\'s friendship.]', flags=done("complete", "future_chivarro"), requires=done("chivarro_lasting")),
      c('[Keep the visits, and Minagho\'s friendship.]', flags=done("complete", "future_open"), requires=done("chivarro_open_visits")),
      c('[Keep both friendships.]', flags=done("complete", "future_friends"), requires=done("chivarro_friendship"))),
    n("open", "Chivarro", '''"Then send word when you have an evening," {n}Chivarro says.{/n} "I shall try to have something worth missing sleep over."
"Her letters will sound far more respectable than the event," {n}Minagho warns you.{/n} "Mine will sound worse. You may enjoy comparing them."
{n}They begin disputing who wrote the more misleading invitation. Chivarro produces the little skull Minagho drew on the first note. Minagho claims it was an accurate warning about the conversation.
You leave them arguing over which of you should keep it. Before you reach the stair, Chivarro slips it into your hand.
Minagho has added a second skull beside the first.{/n}''', c('[Keep the skulls, and the invitations.]', flags=done("complete", "future_open"))),
    n("service", "Minagho", '''"Then we have at least named the thing correctly."
{n}She does not offer you a softer answer for the sake of the farewell.{/n}
"I have said what I want. Chivarro has said her piece. Remember both, and do not dress them up as proof that the leash has become a ribbon."
{n}Chivarro's hand rests beside hers.{/n}
"What I have with you is mine," {n}Chivarro tells you.{/n} "It buys you nothing from her. And her service does not make my leaving yours to forbid. Understand that before either of us says anything sweet."
"I understand."
{n}Minagho lifts her cup.{/n}
"Then go and finish the problem that is waiting for you. We have enough of our own to discuss without borrowing its grandeur."
{n}She touches Chivarro's hand after speaking, where you can see it. Neither of them looks to you for leave.{/n}''',
      c('[Keep Chivarro. Leave Minagho\'s service as it stands.]', flags=done("complete", "future_chivarro_service"), requires=done("chivarro_lasting")),
      c('[Leave with Chivarro\'s answer and the service unresolved.]', flags=done("complete", "future_service"), forbids=done("chivarro_lasting"))),
], "chivarro_future_spoken", 24)


def ending(id, title, text, requires=(), forbids=(), owner="Epilogue", complete=True):
    SCENES.append(scene("minachiv.ending_" + id, title, owner, 0, "", [n("end", "Narrator", text)],
        requires=done("complete" if complete else "invitation_kept") + tuple(requires),
        forbids=tuple(forbids) + done("closed") + (() if complete else done("complete")),
        last=99, optional=True, Relationship="minagho_chivarro"))


ORDINARY_BAD = ("minagho.dead", "chivarro.dead", "inhuman", "ascended", "sacrifice")
ending("together", "Three invitations", '''{n}They never made an effortless household. Minagho could turn a delayed arrival into an elaborate complaint; Chivarro could turn a room's arrangement into an argument she had not intended to begin. The Commander learned when to answer and when to ask what either woman had actually wanted.
There were evenings for three and evenings for two. Chivarro kept work that belonged to her, and Minagho kept ambitions that did not become smaller merely because someone loved her. They sent invitations rather than instructions. More of them were answered than any of the three would once have thought sensible.
The mask game traveled. Chivarro continued to win often enough to become insufferable about it. Minagho continued to bring better prizes. The Commander occasionally remembered to stop watching the women long enough to notice which stone had moved.{/n}''', requires=done("future_together"), forbids=ORDINARY_BAD + ("minagho.ran_demon",))
ending("two", "A place with each", '''{n}The Commander kept a place in both women's lives without requiring every visit to become a gathering of three. Chivarro's invitations named an evening, a room, sometimes a performance she wanted someone to criticize honestly. Minagho's tended to begin with a complaint that became an invitation before the last line.
When the three did meet, they had their own news to bring. Chivarro and Minagho remained lovers with a long history neither needed the Commander to narrate for them. The newer relationships acquired histories of their own: a poor couch made comfortable, a rain-soaked stair, a message that arrived later than desired and was answered anyway.
Their separate hours did not make the shared ones less welcome. They gave everyone something worth asking about when the door opened.{/n}''', requires=done("future_two"), forbids=ORDINARY_BAD + ("minagho.ran_demon",))
ending("minagho", "The hour she kept", '''{n}Minagho remembered the stair more often than she expected. In a life that had contained far grander victories, she remained absurdly pleased that someone had once sat beside her to argue about a badly repaired roof.
She and the Commander kept finding other hours. Some were affectionate, some difficult, and a few were lost to journeys neither could rearrange. She learned to ask for the next without pretending she had never wanted the one that failed.
Chivarro remained part of her life in her own right. Her work, her chosen visits and her answers to the Commander were not managed as the price of Minagho's happiness. When she joined them, she brought news and an opinion about whatever Minagho had begun saying before the door opened.{/n}''', requires=done("future_minagho"), forbids=ORDINARY_BAD + ("minagho.ran_demon",))
ending("chivarro", "The room beyond the audience", '''{n}Chivarro's work did not become smaller after the war. She wanted audiences, profitable evenings and rooms people remembered because she had chosen what happened inside them. The Commander learned to find her after the last guest had gone, when she could be delighted, difficult and tired without making any of it a performance.
She kept her promise to send an honest address when she had one and an honest uncertainty when she did not. Some visits were long; others ended too soon. They learned to say which without making the complaint an accusation.
Minagho remained her lover. The friendship Minagho and the Commander had chosen survived its own awkward beginning. Chivarro was glad of that, though she did not pretend it was something either had owed her.{/n}''', requires=done("future_chivarro"), forbids=ORDINARY_BAD + ("minagho.ran_demon",))
ending("open", "Another evening", '''{n}There were later invitations. Chivarro was exact about dates when she could be and candid when she could not. Minagho acquired a habit of disguising the request for company as a question whose answer required an evening.
The Commander answered according to the life actually being lived. Some meetings were warm with affection; others found their pleasure in conversation and the old mask game. No one was promised a home merely because a door had been opened.
Chivarro kept the brass key after the performance's last local showing. It opened only a painted door. She liked remembering how much an audience had made of choosing whether to take it.{/n}''', requires=done("future_open"), forbids=ORDINARY_BAD + ("minagho.ran_demon",))
ending("friends", "Good company, difficult opinions", '''{n}Chivarro and Minagho remained difficult friends to have and rewarding ones to visit. They disagreed with the Commander without making every disagreement a final judgment. Chivarro sent news of her work. Minagho sent observations she insisted were too entertaining to keep to herself.
When they met, the conversation had room for affection without an unfinished courtship waiting behind it. The two women still had their own intimacies, quarrels and reconciliations. The Commander was welcome at the table without being required to turn every welcome into a claim.
They eventually found a better set of mask stones. Minagho said the old ones favored Chivarro. The new set failed to improve her luck.{/n}''', requires=done("future_friends"), forbids=ORDINARY_BAD + ("minagho.ran_demon",))
ending("chivarro_service", "An answer of her own", '''{n}Chivarro kept the lasting relationship she had chosen with the Commander. She also kept saying what she meant when Minagho's service was discussed. An affectionate evening did not make her call the bond by a gentler name.
Her own work gave her places to go and reasons to return that did not depend on being admitted as Minagho's companion. She sent messages in her own hand. When she visited the Commander, she expected to be heard as the woman who had arranged a performance, paid its people and chosen a lover for herself.
Minagho's unresolved service remained a difficulty between them. Chivarro did not offer the Commander her happiness as proof that the difficulty had disappeared.{/n}''', requires=done("future_chivarro_service"), forbids=ORDINARY_BAD)
ending("service", "The thing they had named", '''{n}Chivarro continued the work she had negotiated. She chose her visits and her correspondence without accepting that Minagho's service placed the same claim on her. The Commander received the answer she had actually given, sometimes in person and sometimes in a letter whose courtesy did not soften its meaning.
Minagho remained bound. Their last conversation had not freed her, and Chivarro refused to praise it for doing so. Yet she remembered that Minagho had spoken plainly in the room they shared. When the two women discussed what they wanted next, that plainness remained available to them.{/n}''', requires=done("future_service"), forbids=ORDINARY_BAD)

# Special outcomes also cover earned but interrupted campaigns.
ending("both_lost", "Two absent voices", '''{n}The deaths of Minagho and Chivarro left two absences behind an invitation the Commander had answered. News of one never became consolation for the other.
Among the remembered things was a note with two hands upon it: a skull beside an invitation, and a dry correction beneath the skull. The argument might have continued for years. No new reply could now bring either woman back to the table.{/n}''', requires=("minagho.dead", "chivarro.dead"), forbids=(), complete=False)
ending("minagho_lost", "Chivarro's answer to the news", '''{n}When Minagho died, Chivarro did not accept the first account without questions. She asked who had seen her, what had happened and which parts of the story had been supplied afterward by people who disliked silence.
Once the facts were exhausted, she had no further question that would change them. She kept a small packet of letters. Some evenings she opened it; others she resented the sight of the seal. The Commander could share the news and the grief it allowed, but could not make the absent woman answer.{/n}''', requires=("minagho.dead",), forbids=("chivarro.dead",), complete=False)
ending("chivarro_lost", "The unfinished reply", '''{n}Minagho heard of Chivarro's death and became very precise. She wanted names, places and an account that did not mistake its own elegance for accuracy. Anger gave her something to do with each answer. Eventually the answers stopped.
She kept Chivarro's correction beneath the old invitation. For a long time she could hear exactly how the words would have sounded. The Commander did not offer another voice in place of it. When Minagho finally spoke about the note, she spoke of the woman who had written it, not of a consolation the loss had purchased.{/n}''', requires=("chivarro.dead",), forbids=("minagho.dead",), complete=False)
ending("changed", "A door they did not enter", '''{n}What the Commander became changed the meaning of every invitation. Chivarro would not make her ability to survive dangerous company into a promise to accept whatever stood behind the familiar name. Minagho knew too much about power to mistake that transformation for an ordinary disagreement.
The two women kept their own conversation. The old invitation remained among their papers, a reminder of a meeting they had chosen when choosing it had meant something different.{/n}''', requires=("inhuman",), forbids=("minagho.dead", "chivarro.dead"), complete=False)
ending("ascent", "An address beyond the road", '''{n}After the Commander's ascent, the old invitation belonged to a life in which a room could be reached by following an address. Minagho remembered the audacity of asking someone so powerful to come and listen. Chivarro remembered insisting on an answer of her own.
Their histories followed the powers and loyalties they had chosen, but the memory of that invitation retained its small, stubborn scale. A name, an hour, a correction in another hand. Divinity had become part of the story. It had not been the reason either woman first wanted a reply.{/n}''', requires=("ascended",), forbids=("minagho.dead", "chivarro.dead", "inhuman"), complete=False)
ending("sacrifice", "The invitation kept", '''{n}After the Commander's sacrifice, Chivarro remembered writing beneath Minagho's little drawing of a skull. The correction had been easy to make. Someone had read it and answered the invitation anyway. She had liked that before she knew what else to say about the Commander.
Minagho remembered the note instead. She had expected another dangerous negotiation. Someone had answered it and stayed long enough to become more than the answer to a problem.
They spoke of the Commander differently. Neither required the other to choose a single account of the loss.{/n}''', requires=("sacrifice",), forbids=("minagho.dead", "chivarro.dead", "inhuman", "ascended"), complete=False)
ending("unfinished_lasting", "The address she still meant to send", '''{n}Chivarro had told the Commander what she wanted and received a lasting answer. The final farewell had not taken place, but she did not treat its absence as permission to forget the conversation they had actually had beside her traveling case.
She kept the blank sheet in its narrow pocket until she had an address worth writing on it. Then she sent it. Minagho knew why the message mattered and, for once, supplied no joke while Chivarro sealed it.{/n}''', requires=done("chivarro_lasting"), forbids=ORDINARY_BAD, complete=False)
ending("unfinished", "A conversation still open", '''{n}Minagho's invitation had received an answer. She sent that answer on to Chivarro, who had added her own sharp correction beneath the little skull on the note.
Their later letters were irregular, sometimes affectionate and sometimes occupied entirely by a difficulty neither woman wished to discuss with a stranger. An unfinished visit could still be followed by another question. Whether the Commander would answer it remained part of the life ahead, not something either woman could settle by writing both halves of the exchange.{/n}''', forbids=ORDINARY_BAD + done("chivarro_lasting"), complete=False)
ending("aeon", "The room that was not hired", '''{n}In the remade history, no invitation bearing two different hands brought these evenings into being. Chivarro did not hire the room for this performance, and Minagho did not discover that particular bad stair in the Commander's company.
Their lives had other rooms, other bargains and their own long entanglement. No recollection of the erased visits arrived to turn those lives toward a guest they had not met in that way.{/n}''', owner="AeonEpilogue", complete=False)

# Completed and interrupted histories share the same special-outcome text.
# Duplicate pages are excluded by the exact-segment content inventory.
for item in list(SCENES):
    if item["Id"] in {"minachiv.ending_" + suffix for suffix in ("both_lost", "minagho_lost", "chivarro_lost", "changed", "ascent", "sacrifice", "aeon")}:
        completed = deepcopy(item)
        completed["Id"] += "_completed"
        completed["Requires"] = ["minachiv.complete"] + completed["Requires"][1:]
        completed["Forbids"].remove("minachiv.complete")
        SCENES.append(completed)

for item in SCENES:
    for page in item["Nodes"]:
        for choice in page["Choices"]:
            if set(choice["Set"]) & {"minachiv.chivarro_chosen", "minachiv.chivarro_date_earned"}:
                choice["Set"].append("minachiv.chivarro_affection")


def integrate(payload):
    """Register read-only parent witnesses; root appends copied SCENES separately."""
    for name, bindings in (("Etudes", ETUDES), ("CompletedQuests", COMPLETED_QUESTS), ("SeenCues", SEEN_CUES)):
        target = payload.setdefault(name, {})
        for key, value in bindings.items():
            if key in target and target[key] != value:
                raise ValueError("Conflicting parent binding: " + key)
            target[key] = deepcopy(value)
    payload.setdefault("Relationships", {})["minagho_chivarro"] = deepcopy(RELATIONSHIP)
