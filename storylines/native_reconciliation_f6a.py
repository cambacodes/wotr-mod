"""eng7-f6a: authored DLC-tier corrections for the existing route outcomes.

Areelu 001-005/008: the paid graft extraction removes her Abyssal magic, not
her calculations; the Commander executes the same native workings. Her account
to Pharasma names her former nature across every fate, without changing judgment.
Anevia 001: Beth's earned return makes the bread conversation's mourning false.
Mielarah 002: the prepared interventions retain their injuries and Oskel's death;
the unprepared account establishes only apparent death, never a free return.
The existing paid search still determines whether anyone finds her alive.

Only text is authored. Original conditions, actions, answers and continuations
remain on NativeEpilogueEdit's reviewed runtime path. No progression is granted.
Native observations use the existing read-only bindings (native_facts discipline);
no romance flag is substituted for a native raid, voyage or final outcome.
"""
from story_format import n, scene
from storylines.native_overrides import declare

DRAWN = "areelu.trickster.graft_drawn"
SELF = "mielarah.trickster.primed.self"
MINDER = "mielarah.trickster.primed.minder"
VOYAGE = "mielarah.voyage_begun"
INTRO = "areelu.trickster.afterlogue.former_half_demon"
TE = "e3fcab126b91a414b821f7390d23b40d"

# eng7-f6a begin: verified blueprints.zip parents and enGB localization keys.
AREELU = (
    ("5b567bdd747e497cb9f6984b1ca1dfc8", INTRO,
     "57e18f5158904030a84a772fb361ceb4", "57e18f5158904030a84a772fb361ceb4",
     "7e3fd30b-9eed-4980-8fd9-1af519d90b99",
     '"And what of me, the writer of these words, once a half-demon, still the Architect of the Worldwound?"'),
    ("a9510daab8a04163933d9ecaeffac563", "areelu.trickster.native.crystal_drawn",
     "71d8a418ce148c647af24e7344cf6497", TE, "ea881b36-bb48-4232-9787-0491c91cb01e",
     '"There. Follow the blood. Do not let the essence disperse." {n}Areelu traces the spell in the air with powerless fingers. '
     'You supply the magic; the frozen crystal leaps into your hands.{/n}'),
    ("f8d2b851faecddf448fe18db41e17120", "areelu.trickster.native.ascension_shared",
     "5127f768a916c4a449992d5240e2f35a", TE, "59491c63-89e0-4924-ba8b-b89d7bd8e9b1",
     '"Then follow my instructions. You took my power; you can do the work." {n}Areelu places the Nahyndrian crystals '
     'before you, naming each turn of the spell. Under your magic, several crystals dissolve. Their essences merge '
     'into a single vortex and pour into you, infusing you with power.{/n}'),
    ("1c8a6796436a7164fa9d63ec79e0395a", "areelu.trickster.native.ascension_without",
     "71ebf92472f64ff478674e5beb142a07", TE, "2dd1fdaf-2faf-4af3-b5d5-565064e2b599",
     '{n}A fierce resolve burns in Areelu\'s eyes. She sets a Nahyndrian crystal before you.{/n} '
     '"Draw out the essence. Slowly. I will tell you when." {n}Your magic raises the crystal; at her word, '
     'it dissolves into pure essence. The power flows into you.{/n}'),
    ("0fa64f1d24f706d41b09dee83acf621d", "areelu.trickster.native.cauldron_test",
     "91c5eca80c8779c4a8bd5754f5533cad", "f125dc501dc6e984385332e67f324f01",
     "06df2f80-e5b5-44fb-8e3b-46355ecef58a",
     '{n}Areelu watches the crystalline cauldron, her hand pressed over the wound in her chest.{/n} '
     '"The Council\'s toy. It took the graft. Now we find out whether the rift will accept what you put in its place."'),
)


def integrate(payload):
    def line(id, relationship, text, requires, chapter, last=99, forbids=()):
        payload["Scenes"].append(scene(id, "", relationship.title() + "Epilogue", chapter, "", [
            n("line", "Narrator" if relationship == "mielarah" else relationship.title(), text)],
            requires=requires, forbids=forbids, last=last, Relationship=relationship))

    for target, id, parent, dialog, key, text in AREELU:
        line(id, "areelu", text, ("trickster.now", DRAWN), 6)
        declare(payload, source=__name__, target=target, target_type="cue", action="REPLACE",
                spec=dict(Parent=parent, Dialog=dialog, Key=key, Replacement=id,
                          When=[["trickster.now", DRAWN]], KeepNativeImage=False, Variants=[]))

    bread = "anevia.trickster.native.bread_returned"
    line(bread, "anevia", '"I\'ll break her off a steaming piece '
         'and watch her try to eat it without burning her fingers. She\'ll pretend it doesn\'t hurt. Stubborn bloody woman."',
         ("trickster.ever",), 5)
    # Authored survival persists after loss of power; reconciliation is separate.
    next(book for book in payload["Scenes"] if book["Id"] == bread)["RequiresAnyGroups"] = [[
        "irabeth.trickster.returned", "irabeth.trickster.cost.dug_out", "irabeth.trickster.raised_on_record"]]
    declare(payload, source=__name__, target="ec1219cf3a664baab8987200e0fe1aa7", target_type="cue", action="REPLACE",
            spec=dict(Parent="97efeec1d2aa45a4cab6111d14767825", Dialog="de4cc2dd71694b842be37b75d1705b83",
                      Key="f0c8aaa0-bdc0-468a-9301-9815c5ac52c0", Replacement=bread,
                      When=[["trickster.ever", flag] for flag in (
                          "irabeth.trickster.returned", "irabeth.trickster.cost.dug_out", "irabeth.trickster.raised_on_record")],
                      KeepNativeImage=False, Variants=[]))

    lead = ("Captain Mielarah protests the raid, calling the Commander a pirate. Her sailors surround her, grinning. "
            "A slip noose falls over her head before she can cast a spell. ")
    self_id, minder_id, late_id = ("mielarah.trickster.native.hanging_" + suffix for suffix in ("self", "minder", "uncertain"))
    line(self_id, "mielarah", "{n}" + lead + "You cut the rope before it draws taut. The yardarm block breaks loose "
         "and smashes your collarbone. You cling to her as she calls the southern wind with a strangled breath. "
         "For ten heartbeats she lies still in your arms. Then she gasps. The crew retreat, leaving you together "
         "on the deck as the ship pulls away from Vazglar.{/n}", ("trickster.now", SELF), 4, 4, (MINDER,))
    line(minder_id, "mielarah", "{n}" + lead + "Oskel hauls her up. With her last breath she calls the southern wind. "
         "The yardarm block splits; the swinging yard catches the line around Oskel's arm and drags him over the rail. "
         "His wings foul in the rigging. The rope goes slack at Mielarah's throat, but Oskel does not rise again. "
         "She lies motionless in the scuppers. No sailor dares touch her. The wind carries the ship away from Vazglar.{/n}",
         ("trickster.now", MINDER), 4, 4)
    line(late_id, "mielarah", "{n}" + lead + "The line tightens. With a desperate wheezing breath, she calls the "
         "southern wind into the sails. The ship jerks away from Vazglar. In seconds the captain hangs motionless. "
         "The crew call her dead, but nobody goes near enough to feel for a pulse. All night the wind blows, "
         "carrying them away from the rock they have plundered.{/n}",
         ("trickster.now", VOYAGE), 4, 4, (SELF, MINDER))
    declare(payload, source=__name__, target="dbec675b71e9d5f4d96055f4bb31762e", target_type="slide", action="SLIDE-SWAP",
            spec=dict(Page="b8d5d14d96bedab44873aa0520304e73", Sequence="", Key="b5c3d293-f547-4848-895b-03b2bdba5a95",
                      Replacement=self_id, When=[["trickster.now", SELF, "!" + MINDER]], KeepNativeImage=False,
                      Variants=[dict(Replacement=minder_id, When=[["trickster.now", MINDER]], KeepNativeImage=False),
                                dict(Replacement=late_id, When=[["trickster.now", VOYAGE, "!" + SELF, "!" + MINDER]],
                                     KeepNativeImage=False)]))
# eng7-f6a end
