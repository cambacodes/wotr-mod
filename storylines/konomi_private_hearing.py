"""Reuse the pending complaint and its payoffs after verified private return.

Shared decisions and prose remain one authored event, not new content credit.
"""
from copy import deepcopy

from storylines import konomi


SCENES = []
for original_id in ("hearing", "hearing_after", "new_letter"):
    original = next(s for s in konomi.SCENES if s["Id"] == "konomi." + original_id)
    private = deepcopy(original)
    private["Id"] = "konomi.private_" + original_id
    private["Entry"] = ""
    private["Remote"] = True
    private.pop("AnswerLists")
    private["Requires"] = ["konomi.dismissed", "konomi.office_completed", "konomi.private_returned"] + [
        flag for flag in original["Requires"] if flag != "konomi.present"
    ]
    private["Forbids"] = list(dict.fromkeys([
        *original["Forbids"], "konomi.present", "inhuman", "konomi.private_future"
    ]))
    SCENES.append(private)

SCENES[0]["Nodes"][0]["Text"] = '''{n}Konomi asks you to visit the room she is using during her return to Drezen. On its little table, your letter lies in a plain wrapper beside the stolen copy and the receipt for the copyist's payment.{/n}
"The association has offered us a morning. At last. I was beginning to think I should send the complaint a change-of-address notice of its own."
{n}She moves a folded shawl off the second chair.{/n}
"Tomorrow, if you can attend. Three members will adjudicate. I have confirmed that leaving my appointment changes neither my complaint nor their authority to hear it. Their members can refuse the buyer further work. They cannot put him in prison."
"What does he say?"
"He admits buying a copy and calls it a memorandum he believed he could circulate. The receipt says what he paid, not what he read."
{n}Konomi rests one hand beside the wrapped original without opening it.{/n}
"I want them to compare the pages. It is your hand on the page, and they will want you to swear to it. Coming back to Drezen has not taught me to forge your signature."'''

SCENES[1]["Nodes"][0]["Text"] = '''{n}Konomi opens the door of her borrowed room. The association's written finding lies on the table beside your letter. She has moved her work to the windowsill to make space for supper.{/n}
"They sent it here, as I asked. Nobody has attempted to deliver it to my former office. A modest success, but I intend to enjoy it."
{n}She sets a second cup beside yours.{/n}
"The wording is as agreed. Our names in the finding, our private sentences out of it. I checked twice."
{n}She leaves the finding on the table and turns toward you in the doorway.{/n}'''

SCENES[2]["Nodes"][0]["Text"] = '''{n}You find Konomi at the table in her borrowed room. When she sees the folded page in your hand, she closes her appointment book and sets it on the windowsill.{/n}
"You remembered."
{n}She reaches for the letter, then looks up at you.{/n}
"I cleared the afternoon. Do not look so pleased with yourself until I have read what you propose to do with it."'''
