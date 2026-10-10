"""Residual Elyanka replacements blocked by external prose-based presence classification.

INQUIRY and COLLECTORS must run after crossroute_presence until the owning
engine inventory can migrate those reviewed references to stable IDs/flags.
"""

from authoring.generation_errors import record

E = "elyanka.trickster."

def _scenes(payload):
    return {s["Id"]: s for s in payload["Scenes"]}

def _paragraphs(payload, scene_ids, table):
    """Replace whole paragraph texts (same gates) wherever they occur in the named scenes; every entry must be used."""
    used = set()
    scenes = _scenes(payload)
    for sid in scene_ids:
        if sid not in scenes:
            record("overlay.scene_resolution", scene=sid)
            continue
        for node in scenes[sid]["Nodes"]:
            for para in node.get("Paragraphs") or []:
                if para["Text"] in table:
                    used.add(para["Text"])
                    para["Text"] = table[para["Text"]]
    missing = set(table) - used
    for text in sorted(missing):
        record("overlay.paragraph_snippet", detail=text[:70])

COLLECTORS = {
    "{n}The Whispering Way demanded the body named in the death notice. Its collector was shown a living Commander and refused possession. He returned to Caliphas with the bequest still disputed.{/n}":
    "{n}The Whispering Way came for the body named in the death notice: Elyanka Camilary, with the hearse and her six. She was shown a living Commander, and put two cold fingers to the throat in front of everyone to be sure of it. She left without her corpse and without giving up one whispered word of the claim.{/n}",
    "{n}The Whispering Way demanded the body named in the death notice. The coffin was empty. Its collector left without the concealed stranger's name, and without withdrawing the bequest.{/n}":
    "{n}The Whispering Way came for the body named in the death notice, and Elyanka Camilary tore open an empty coffin. She left without the concealed stranger's name, and without withdrawing one whispered word of the bequest.{/n}",
    "{n}No death had made the whispered bequest payable. The Way's collector examined the sealed flask and left the living Commander to wait. The bequest remained on file in Caliphas.{/n}":
    "{n}No death had made the whispered bequest payable. Elyanka weighed the sealed flask in her palm, sniffed at the wax, and gave it back to the living Commander to carry. The bequest stayed where the Way keeps such things: unwritten, in the ears of the people who had heard it.{/n}",
}

INQUIRY = {
    "{n}The Commander remembered Seelah hearing the truth about the sixty-one from the mouth that had ordered their removal. The count went to the chaplains; a witness stood at the dead-house door. Elyanka had stayed out of the paladin's road.{/n}":
    "{n}Seelah heard the truth about the sixty-one from the Commander's own mouth, on the chapel steps, and never again asked the Commander to help her find anything. After that a young crusader with a lamp stood at the dead-house door whenever the carts came in. Elyanka stayed out of the paladin's road. She whispered the lamp-bearer's name to her Lady every seventh night instead, as a grace before meat, so that her Lady would know him when he came.{/n}",
    "{n}A resurrection man hanged at the south gate of Drezen for sixty-one bodies he never touched. The Commander remembered Seelah blocking the gallows steps with the carters' testimony, and the watch forcing her down under the Commander's seal. The Commander's order had kept her from stopping the carts, not from recording who sent them. The chaplains received the testimony; a witness stood at the dead-house door.{/n}":
    "{n}A resurrection man hanged at the south gate of Drezen for sixty-one bodies the man had never touched, with a placard on the dead man's chest and the Commander's seal on the sentence. Seelah had stood on the gallows steps with the carters' word in her fist until the watch shoved her down them, and after that she put a crusader with a lamp at the dead-house door and never believed the Commander again. When they cut the hanged man down nobody claimed him but Elyanka. He went south in the hearse, past the lamp, and Seelah watched him go.{/n}",
    "{n}Elyanka told the paladin the truth about the sixty-one herself, in the dead-house yard, without one lie. The Commander remembered Seelah refusing the excuse that the dead could not suffer. She had taken the names and count to the chaplains and put a witness at the dead-house door. Neither culprit had received her forgiveness.{/n}":
    "{n}Elyanka told the paladin the truth about the sixty-one herself, in the dead-house yard, without one lie, and enjoyed every word of it. Seelah did not draw. She would not hear that the dead could not suffer, and she forgave neither of them, and from that day a crusader with a lamp stood at the dead-house door when the carts came in. Elyanka gave him a stool, and wine he never drank, and called him her little mourner.{/n}",
    "{n}Her Lady's table was still laid every seventh night. The witness at the dead-house door counted the guests and took their names to the chaplains. Elyanka made him stand outside while her worshippers ate, and sent the bones out under his lamp. The Commander's protection kept her in Drezen; it did not silence the testimony.{/n}":
    "{n}Her Lady's table was still laid every seventh night, and the paladin's lamp-bearer stood at the dead-house door and counted the masks going in. Elyanka made him stand in the lane while her worshippers ate, and sent the bones out past him on a platter, still warm, so that he could count those too. He carried every name he could get to the chaplains. The Commander's protection kept the table laid; it never kept the lamp from the door.{/n}",
    "{n}The Commander remembered the sixty-one chalk marks on the dead-house floor after the inquiry. Elyanka had swept around them; a witness had stood at the door.{/n}":
    "{n}Seelah's sixty-one chalk crosses stayed on the dead-house floor for as long as Elyanka kept the house. She swept around them, and set her Lady's table over them, and on her Lady's nights she made her guests eat with their boots on the paladin's count.{/n}",
}

def integrate(payload):
    # S3 / S4: whole-paragraph rewrites, gates unchanged.
    epilogues = [E + "epilogue." + k for k in ("claim", "debt", "lock", "left_free")]
    _paragraphs(payload, epilogues, INQUIRY)
    _paragraphs(payload, ["trickster.lastcall.page.collectors"], COLLECTORS)
