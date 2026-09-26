# Konomi private future: bounded integration review

No blocking integration defect was found in the three campaign scenes and five ending variants.
The completed private future selects one ordinary ending for each reviewed outcome, with the intended reuse of existing committed transformation, ascension and Aeon endings.
This is a source/export and offline rules review, not actual Unity execution or full-route approval.

## Reviewed revisions

| File | SHA-256 |
| --- | --- |
| `storylines/konomi_future.py` | `7877AD77F2711421A30BA2449955648A503BBB633EADC2740F4ADAC8F893F57E` |
| `storylines/konomi.py` | `702855D59922B48B0C88145AE7034A4EA417CC53FBEA82F984C0BA3AE928B235` |
| `expansion.py` | `12F2099E7E7E3A1B11B4FE4C2E1AD9D6AD94049735B883FB21E12BA58C096F9D` |
| `tests/Program.cs` | `4F898E24540C5A7C14F9628B144AB1A700B7DA92A0875AD20450AD56AAE00ACF` |
| `development/Story.json` | `A8FC9B76D8C9DBE6268E74DC067F0F6AB502430E85D25BAF6A674628D8A16C95` |

The exporter imports `konomi_future` and includes its scene list once.
I also inspected the exported requirements, blockers and delays for the three new campaign scenes.

## Campaign progression

All three scenes are remote books in Drezen, chapters 3 or 5, requiring native dismissal, completed officer state and the authored private return.
They forbid ordinary officer presence, inhuman state, the original farewell and a completed private future.
Normal relationship closure remains effective.
Current Trickster status is not required after the established private return, preserving continuation after an applicable change to Legend.

`lease_offer` requires the kept reunion and waits 48 hours.
`chosen_evening` requires the recorded career decision and waits another 48 hours.
`private_future_choice` requires the completed private evening and waits 24 hours.
The preceding authored timestamp supplies each delay under the existing rules.
Completing or declining the final private future blocks these three campaign scenes even if their individual completion flags are removed.

The evening's explicit acceptance can establish `konomi.lovers` on both the intimate-night and quiet branches.
This is a courtship stage flag here, not proof that the quiet choice included sex.
Separate `private_night_chosen` and `private_quiet_chosen` flags preserve the physical choice.
Neither branch silently grants commitment.
Declining at the evening instead distinguishes a new romantic prospect from an existing lover, records closure and private parting, and does not fabricate the completed romantic evening or new lover status.

The final discussion offers a shared-life commitment, continued uncommitted courtship where no commitment exists, or separation.
An existing commitment cannot be silently downgraded through the open-courtship option, because that option is forbidden when committed.
Separation retains historical commitment flags but adds explicit closure, so ending predicates treat it as a breakup rather than continuing the commitment.
No effect restarts the native officer etude, changes selection history or grants ordinary presence.
No choice writes another relationship's state.
Ordinary scene completion also performs the existing addon timestamp and journal bookkeeping.

## Ending selection

| Private future outcome | Ordinary state | Inhuman only | Ascended, including inhuman plus ascended |
| --- | --- | --- | --- |
| Committed and not closed | New `distance` | Existing `changed` | Existing `ascended` |
| Open and not committed/closed | New `distance_open` | New `distance_changed_open` | New `distance_ascended_open` |
| Closed with private parting | New `distance_apart` | New `distance_apart` | New `distance_apart` |

Every new ending requires `konomi.private_future`.
The old public, private, apart and unfinished endings now forbid that flag.
The old changed and ascended endings deliberately retain eligibility for committed private outcomes, with ascension excluding the changed ending.
The existing Aeon ending also remains eligible for a committed, nonclosed outcome in its separate `AeonEpilogue` sequence.
An Aeon-sequence cue is not counted as a second ordinary epilogue selection.
No new Aeon ending for an uncommitted or parted relationship is supplied by this change.

I independently evaluated the exported ordinary-ending requirement/forbid predicates for 24 combinations of committed/open/parted outcome, normal/inhuman/ascended/both transformation state and old public-history presence.
Each combination selected exactly one ordinary ending.
This independent predicate check supplements source inspection; it does not emulate native epilogue sequence execution.
The exclusivity claim concerns completed, valid private outcomes, not arbitrary edited flag combinations or an unfinished campaign.

## Test assessment

`CheckKonomiFuture` walks all scene paths for both supported chapters and new, lover and committed histories.
It checks native dismissal and another commitment remain intact, early-decline history, quiet/night distinction, explicit stage progress, no downgrade of an existing commitment, postponement without flag progress and suppression after the future is resolved.
It checks each prerequisite and blocker, area and chapter limits, the initial 47/48-hour boundary, and both subsequent delay boundaries.
For every completed private outcome it requires exactly one ordinary ending across four transformation states and verifies its ID.
It separately checks the retained committed Aeon ending.
These checks directly address the changed behavior rather than relying on the aggregate assertion count.

The owner reports 159,260 passing rule assertions.
I inspected the suite and performed the separate exported ending-predicate check, but did not independently rerun the full suite.
No live Unity, native actor, portrait, save/load or ToyBox result is inferred.
No additional source correction was identified for this bounded integration.

## Early invitation-decline follow-up

The assembled-route review identified a separate earlier gap outside the completed private-future outcomes assessed above.
A declined `fate_reply` could lack an ending for a new prospect or reuse the official-correspondence breakup for an established lover despite the dismissal.
The owner reports reproducing this through an assertion in the actual post-to-reply rules walk before applying the fix.
The final helper now excludes `private_declined` from the old `apart` ending.
The new `dismissed_apart` ending requires `private_declined` and `closed`, and forbids `private_future`.
It describes declined private contact without restoring an official appointment or requiring a prior lover stage.

I independently checked the exported predicates for all 12 combinations of new/lover/committed history and normal/inhuman/ascended/both state after early decline.
Each selects exactly `konomi.ending_dismissed_apart`.
I also repeated the 24 completed private-future combinations above; each still selects exactly one ordinary ending.
The new early ending cannot overlap those late outcomes because it forbids their `private_future` milestone.
The new rules assertion walks the actual reply decline and checks exactly one correctly named ending; the independent export check additionally covers transformation overlays.
No further ending-selection defect was found in these bounded states.

Follow-up source SHA-256 for `storylines/konomi.py`: `4BC95F60FB700FF30CCFEAEE5D6AA155D9A7D3C04691365B0D58A555EA311F92`.
Follow-up test SHA-256 for `tests/Program.cs`: `78A97936BA00DECE001F45B35F300F4D479B5521D62D437BD67D4991372E4591`.
Follow-up export SHA-256 for `development/Story.json`: `9E7A287C64F0BB5727158F98A908F1EF0B047A8F5A879CEC2408662A6B868A56`.
The owner reports 143 scenes and 159,281 passing rule assertions for this revision.
This follow-up remains an offline ending/state review and does not establish live epilogue execution.
