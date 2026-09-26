# Native capital contacts for the Tirabade campaigns

The reproducible probe `tools/probe-tirabade-capital-contact.py` reads the installed Drezen capital default mechanics scene with UnityPy and records matching game objects and components.
It then resolves six referenced native unit, dialogue and answer-list blueprints from the installed archive, retaining their exact records and hashes.
The evidence is `tirabade-capital-contact-records.json` in this directory.
No installed files are modified.

| Character | Capital unit | Spawner | Native dialogue | Answer list |
| --- | --- | --- | --- | --- |
| Anevia | `b5e867e13503c6f41bb1316705efb4a2` | `86b332a9-5910-4d46-9951-8e06f7dcf0cf` | `de4cc2dd71694b842be37b75d1705b83` | `33960c7f7af40cd43b7f801a76c87a0b` |
| Irabeth | `280d4712dceb37f4a88e98f1f4c6e64f` | `3dc302d8-58ce-44f3-9766-2a437a080108` | `20e94a828d4016d45a6b723765306522` | `871af36f2ab2b1f40b5de77976c54276` |

The unit GUIDs come from the actual spawner components, not guesses from dialogue names.
The dialogue GUIDs come from their interaction components.
The answer lists match the existing engine's native entry targets and resolve to the named native conversation folders.
This establishes identities for new individual contact metadata; it does not establish that either actor is currently alive, unhidden, loaded or available in any particular save.
The existing NativeContact guard must still observe the actual unit and view.

The current single `ContactUnit` field can guard one woman's physical presence.
A scene narrating both women present needs both actors observed, or explicit remote presentation that does not claim their world actors are present.
Do not weaken the existing uniqueness, loaded-view or native-state checks to make a paired scene appear available.
New independent relationship records must use each woman's own native unavailability rather than the shared derived `loss` flag.
Parent dialogue answers and finish actions must remain intact when adding new entry choices.

The writer independently confirmed the same actors and inspected the parent's Anevia invitation dispatcher.
That dispatch service is not evidence of an existing parent Anevia romance and must be preserved alongside the new campaign.
Further actual native condition, paired-contact, save and runtime validation remains required before release.
