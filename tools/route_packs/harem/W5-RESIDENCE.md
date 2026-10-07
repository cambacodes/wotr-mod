# W5-residence: reconciled contract

2026-10-07. Deliverable: WAVE-PLAN's **contract reconciliation**, before the
separate guard, seating and story jobs. P3 is **blocked**, not enabled by this
pack. No scene, presence, story flag, native edit or explicit interval is emitted.
`tools/residence_contract.py` is an offline seating acceptance reference, not
runtime support. Consequently no `harem_rows` registration is needed yet.

## Authority and corrections

Binding: WAVE-PLAN contract 1–10; Writer doc10 §7 (later coordinator acceptance
ruling overrides duplicate earlier proposals); doc10b; CHARACTER-TRUTH;
TRICKSTER-RUBRIC bindings 1–5; harem-lore-check shared corrections. Reviewed
hs-A/B/C/D own-house and current-channel clauses and sheets 36–52 attendance,
first-wins enmity and seating clauses. Their pair contracts do not authorize a
residence gate on pair arcs. The public paid-page spelling is
`foresight.page_taken`, with current `trickster` and no `trickster.failed`;
`trickster.ever` alone is insufficient. No new echo is allocated.

Doc10 contains both “NoCouncil only” and “remove Council1/Fight, ensure
NoCouncil” mechanics proposals. Its §7 selects the latter. This pack uses that
single result, preserving unrelated mechanics. Earlier duplicate guard text
and earlier maximum-distance-only seating requirements are superseded here.
The existing Writer documents are outside this job's edit scope.

## Reopened native evidence

All paths below are in `/wrath/blueprints.zip`, read in this worktree session.
Localization was reopened in
`/wrath/Wrath_Data/StreamingAssets/Localization/enGB.json`.

| Asset path | AssetId / verified fact |
|---|---|
| `World/Dialogs/c3/Mythic_Trickster/Council_1/Cue_0031.jbp` | `c41a346484a44264ba6f918e0dca9fe1`; shared string `07c4cd70-139b-4f27-9766-cf844376cea4` identifies Abadar's collection and Socothbenoth's closet portal. Ownership transfer is an authored inference/story, never a canon gift from Socothbenoth. |
| `World/Encounters/DrezenCapital/ActionsHolders/ToCouncil_CheckPassedActions.jbp` | `914d4385992c822488b5fb844f6a7f21`; completed objective `530a7178ade8aca419c16f06e8a851f4` or `4ee3bbed15c1c6c4fafe19f70a96d060` selects bark; otherwise teleports to the entry below. |
| `World/Areas/Mythics/TricksterCouncil/TricksterCouncil.jbp` | `28a49e115795ed44397b5a1503cef4f0` |
| `World/Areas/Mythics/TricksterCouncil/EnterPoints/TricksterCouncil_Enter.jbp` | `91c44d833734aa540ba18be8e0440cb9` |
| `World/Areas/Act_3_DemonsHerecy/DrezenCapital/EnterPoints/DrezenCapitalFromTricksterCouncil.jbp` | `9f060611800cfc24faace5caf2cffb14` |
| `World/Areas/Act_3_DemonsHerecy/DrezenCapital/EnterPoints/DrezenRestPoint.jbp` | `ab3b5c105893562488ae5bb6e7b0cba7`; P3′ quarters anchor, not a Chamber entrance. |
| `World/Etudes/Common/WrathOfTheRighteous/MythicTrickster/PlayerIsTrickster/Council/Council5_2/TricksterCouncil_Council5_2.jbp` | `9b0197e878a63bd478aded7661cf9cc2`; non-once trigger plays `8f3e5a188cd717f49c690ff4c0ce78c9`; adds Council1 mechanics `f4fa4e2cdac6d51419104a1c7466eaeb`. |
| `World/Etudes/Common/WrathOfTheRighteous/MythicTrickster/PlayerIsTrickster/Council/TricksterCouncil_CouncilFight.jbp` | `ce1d29b444c5f624dbe558ab89b78950`; non-once trigger includes party selection/combat setup. This etude is distinct from its mechanics blueprint. |
| `World/Areas/Mythics/TricksterCouncil/Addons/TricksterCouncil_NoCouncil.jbp` | `d56190770d26e1d42800369d4902570f`; mechanics, not a preset. |

Coordinates in the offline reference come from doc10b §4's scene-transform
research; this job has not independently extracted Unity transforms or tested
navmesh positions. In particular ShykaLocPlayer is about **1.459 m** from
Shyka's documented native spot, so it is excluded while that spot is occupied.
The earlier blanket claim that every candidate clears native spawners is false.

## One bounded guard contract (engine job required)

The sole doorway is the native bedroom closet entity
`36cada36-2a31-4d6c-8253-9ffc8bfcd845`. Intercept its ActionsHolder only for a
current paid-page Trickster with earned `trickster.residence.claimed`, in the
approved residence visit window. Otherwise run the original actions unchanged.
Table, bed, Ledger, Pulura and Alushinyrra acquire no residence entrance.

| Lifecycle state | Required behavior |
|---|---|
| Pre-load | Enter creates an unsaved token naming the Chamber and start time; LoadArea entry with BeforeExit. No suppression outside the Chamber. |
| In-area | Only an authorized visit token plus current eligibility plus loaded Chamber permits suppression of the two named etudes' triggers. Remove Council1 and CouncilFight mechanics (`3a6513ad79a05134d837bf302e42d5ee`); ensure NoCouncil once; preserve other mechanics. |
| Failed/interrupted load | Clear token if load fails or Chamber has not finished loading within 120 seconds. No native writes. |
| Save/reload | Clear token on every load, including loading inside the Chamber. Such a reload is a native visit; native triggers can fire. Never restore a token from story history. |
| Exit / other area / party death | Clear token; explicit Exit loads the Drezen return entry with None. Clear on non-Chamber AreaLoaded and on party death. |
| Native re-entry / uninstall | Native trigger/mechanics behavior remains intact. Only inert spawned-copy area-save residue is accepted. |

No completing Council5_2, disabling fight etudes, changing quest outcomes or
reviving Council members to clean the room. A saved ownership flag cannot be a
visit token. Live method signatures and both guard halves still need proof.

## Seats and current presence (separate seating job)

Before each selection and placement, resolve each **woman**, her RouteOpen,
qualified SeatWomen, own closure, current departure epoch, committed route and
joined/tolerated stance, and actual bodily channel for this venue/chapter.
Historical return, correspondence, projection, shell or invitation does not
grant a body. Revalidate after delayed continuation/load and before any touch.
An own-house partner stays out of the residence picker but retains Table, pair,
route, Ledger, Last Call and epilogue access. Do not close her romance.
The Guest List retains the whole roster as a record, distinguishing historical
entries from current speakers. Each eligible unselected woman's away line is
written by her route in her own voice and duties; no generic absence template.
Letters require her current reachable-by-letter channel, not merely an empty
seat. Ember and Aivu remain friendship-only and never enter intimate staging.

Use the player's picker order; accepted last-rest invitations preselect only
currently eligible residents. Never rotate or silently substitute residents.
Capacity is six for P3, four for P3′. Selected living native Chadali/Eritrice
retain their own spots and count toward capacity; never spawn duplicates.
Other native bodies reserve their occupied positions. Native hostility or
blocked paths must fail acceptance, not be erased by a household flag.

Resolve free seats in fixed index order from the reference. For each resident,
maximize the minimum distance to already seated enmity partners; tie by lowest
seat index. Use existing first-wins target and reconciliation readers, never
produce a new target. Fixed X hostility survives practical restitution; only
its declared existing overrides can remove a seating conflict. Reject the selected pairing if the resulting separation
is below eight metres; show a message without changing enmity or stance. Keep
copies at least 1.5 m from native occupied positions and residents at least
1.0 m apart. Failed resolution is atomic, with no partial spawn or flag spend.
P3′ needs its own measured quarters coordinates; Chamber coordinates are not
quarters coordinates. The four-seat test covers capacity, not live placement.

## Ownership story (separate story job)

Reserved IDs remain `trickster.residence.claim_vault` and
`trickster.residence.hub`. Append new nodes/answers; do not repurpose existing
IDs or choice indices. The buyout, attendant, notice, terms and counting-house
charter are **authored RRT additions**, justified by the collection's loan and
the crusade's authority over the Wound's ground. They change ownership only;
no resurrection, Crossroads outcome or Council survival is supplied by them.

Keep doc10's terms: charter or one owned magic item at native cost >=10,000 gp;
Diplomacy DC26 success floor 6,000 or no Mendevian tithe; failure floor 15,000
or Drezen-road toll. The clerk must be able to counter/refuse the charter,
leaving the item offer available. Refusal sets vault_refused, never claimed.
Accept the charter as consideration from the crusade's commanding authority,
not as proof that the future Crossroads already exists. No additional price.
Cobblehoof speaks only when currently alive and actually present; otherwise
the attendant alone. His gestures/“Phrr!” must not become fluent dialogue.
His native voice sample still needs reopening in the story job.

Do not enable the ownership producer until entry, guard, seats, debit and
readers exist and pass P3 acceptance. Respect doc10's existing scheduling,
with paid page/current path and current Commander survival, rather than a new
Ch6 pair-completion fallback. The charter Ledger and Last Call readers are
historical cost records; any living response needs its host's current gates.
Conditional paragraphs may appear only on epilogue pages. No new intimate
scene is authorized by residence; any later approved moment needs its own
Commander+woman or woman+woman slot/brief and current-body checks.

## Ordered acceptance / ownership

| Order | Acceptance | Owner / status |
|---|---|---|
| 1 | Closet with earned claim enters; no-page, non-Trickster, unclaimed and failed path retain canon door. P3 unavailable before approval. | Engine + live saves, pending |
| 2 | Three Council histories (against Council, Nocta allied, Council allied): 60-second settle without session replay, party selection or combat; reconciled mechanics result; no hostile/blocking survivors. | Engine + live saves, pending |
| 3 | Picker order, index ties, multiple enmity partners, exact 8 m boundary, impossible pairing, duplicate/capacity rejection, native exclusions and no duplicate Council women. | Offline tests supplied; runtime/2 m walk/render/dialog proof pending |
| 4 | Failed load, timeout, interrupted exit, party death, save/reload inside/outside, native re-entry and uninstall restore native behavior. | Engine + live saves, pending |
| 5 | Every Council outcome: appropriate speaker, charter acceptance/counter/refusal, exact one-item debit/floors, refused/unfunded ownership remains unclaimed; charter Ledger/Last Call consequences. | Story + engine tests, pending |
| 6 | All women: deliberate closure, later departure/death versus old return, independent multi-woman seats, remote-only, own-house; no unreturned sacrifice living pages. Joined and tolerated residents work; own-house pairs progress without P3. | Runtime row/rules tests, pending |
| 7 | If any P3 acceptance fails or guard is rejected, use P3′ quarters with measured four-seat placement. No closet override or Chamber residents; all pair arcs still work. | Coordinator + seating/story jobs, pending |

## Surface classification and scope

New runtime payoff/departure surfaces: **none**. Reference outputs are transient
coordinates only, not flags. Existing contracts, scene text and voice locks are
untouched; no dependent native rewrite is currently required. The later closet
override is an authored Trickster-only native change and must preserve its bark
and teleport branches elsewhere. Future claim, live hub, resident copies,
charter Ledger and Last Call additions must be individually classified in
payoff/departure inventories before shipping. New narrative desires, gates,
reconciliation conditions and optional arcs are outside this unit.

Inspected HEAD: `Presence` exposes one Position, no Seats resolver; no
ResidenceAction, ResidenceGuard or closet ownership interception was found in
src. Those files, shared Last Call/household modules, harness and story.py are
forbidden here. Escalate those dependencies; do not simulate them with unknown
JSON fields or a freely set claimed flag. No harness/game run was performed.
