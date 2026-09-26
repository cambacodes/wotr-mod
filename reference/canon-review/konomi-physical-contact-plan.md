# Konomi physical contact evidence

Root inspected the installed capital scene on 26 September 2026 using UnityPy.
The reproducible probe is `tools/probe-konomi-contact.py`; exact scene objects and native records are in `konomi-contact-records.json`.
The probe passed its exact spawner/unit/dialogue checks and recovered four native blueprint records.

`drezencapital_default_mechanics.scenes` contains GameObject 535, `RankUpOfficer_Diplomacy`.
Its spawner component 2855 has unique ID `c658c4cf-116e-4b61-9ff9-8905bcf4fd6b` and unit blueprint `ca2d58c5c65723945857e04fb85d30ce`.
It spawns on scene initialization, has no spawn condition, and does not respawn if dead.
Component 2856 on the same object supplies dialogue `a81655ed97277974e947c1aaf9e33525`.
Component 2857 sets `m_SpawnHidden` true, so the existence of the spawner does not prove visible contact.

GameObject 521 supplies position locator `e6a7de2a-ce6f-4413-b24d-06daf1990e4c`.
These are the exact spawner and locator targeted by the ordinary presence etude's unhide/translocate actions in `konomi-availability-review.md`.
The dialogue supplies the already integrated reusable answer list `0dc8b8604bb33c846a63f3eb62443674`.
This establishes the scene-to-unit-to-dialogue link without inferring a unit from its display name.

## Implementation contract

Ordinary meetings should retain `konomi.present`, Drezen and chapter requirements and additionally use the exact unit as `ContactUnit`.
The shared contact observer can then check unique living, conscious, friendly, loaded physical availability without waking or restoring the actor.
It also rechecks the ordinary presence requirement during continuation, covering temporary rank-up displacement and dismissal after a book begins.
Temporary loss of contact must suspend delivery without closing the relationship or clearing native history.

Do not apply the ordinary actor requirement to the solitary Abyss letter, epilogues or dismissed private correspondence.
Those scenes have different delivery contracts; the hidden former officer does not prove a private meeting is physically delivered.
The private route still needs its own presentation verification.
Do not restart the office etude, unhide the officer manually or replace it with a new actor to bypass a native dismissal.

The next technical step is a reproduced entry/continuation fixture followed by staged metadata changes and independent review.
No contact metadata has been changed by this evidence collection.
No actual Unity interaction, save transition, death recovery or ToyBox verification is claimed.
