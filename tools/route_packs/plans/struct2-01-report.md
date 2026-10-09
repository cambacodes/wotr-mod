## CHANGES

Three structural findings fixed: timed courier departure/return, optional master chronology, and prepared coffin payment. Existing prose, scene/node/choice IDs, old choice targets and choice positions remain; new paths append. The prepared path reuses the approved sibling stone-filling prose. Seven courier placeholders and a collateral voice request are registered for Claude.

## CLASS SWEEP

Compared bundle-path source bytes and hashes with the pinned base; the six character modules, departure contracts and ownership inputs match. Reviewed every requested scene and the coffin, courier-answer, ending, presence and chapter-transition siblings. Current master timing already reads courier answers, but its existing two ANDed groups wrongly require the optional courier; the single OR group fixes this. The requested four-singleton-group recommendation is rejected with engine evidence (`src/Story.cs:890,918`).

The slot-host test used a partial fixture against a whole-project prose registry. It now validates registrations belonging to that fixture while retaining exact hashes and the missing-registration mutation. New compatibility histories are exposed through the selected save-compatibility test module.

## GATE

Runner-owned receipts are intentionally empty below. Final own checks: `python expansion.py` exited 0 (4,082 scenes); `python /work/Writer/tools/id_guard.py /work/wt/RRT-struct2-01 --baseline /tmp/struct2-01-base-Story.json` exited 0; `python -m unittest tests.test_savecompat_baseline tests.test_utf8_io` exited 0 (22 tests, with `RRT_TEST_STORY` pointing to the freshly generated export); `python tools/prose_pending_lint.py --integration --story development/Story.json` exited 0; `python tools/claude_work_queue_lint.py` exited 0; `python tools/departure_lint.py --strict --story development/Story.json` exited 0 (43 women, zero hard failures). An additional independent comparison against the declared base export preserved all 2,634 Elyanka/Camellia/Eliandra choice identities, positions, Next targets, checks and native successors. `git diff --check` exited 0. These are finding evidence, not sealed runner receipts. The tested export is retained at `/tmp/struct2-01-Story.json`; generated development bytes were restored to the pinned version so delivery changes stay within allow_paths. The wrapper must regenerate and seal the delivered source/export, profile/environment digests and complete coverage; no inherited baseline claim is made. Earlier supplementary unittest commands were rejected by the command guard (exit 137; selection outside the pinned Python modules). The first required test run failed on the partial-fixture registry check. A subsequent stale-export check failed on the newly added chapter-transition case and an incorrect test assumption that the unfinished-test ending had a grave paragraph; the latter test now checks the existing blood/name price readers instead. Neither failed attempt is claimed as a pass.

```json
{
  "job_id": "struct2-01",
  "subject": {
    "kind": "tooling",
    "id": "struct2-01"
  },
  "base_sha": "78f9b714dd8b5ea35e58c0a37609d6a9defdbd36",
  "input_manifest_digest": "63f895c018d1ce2f3c020fba6ee8d20f4aaa06ec413dd0c5bcd603912e13b2cf",
  "scenes_reviewed": [
    "elyanka.trickster.beat.courier",
    "elyanka.trickster.beat.master",
    "elyanka.trickster.door.hearse",
    "elyanka.trickster.straight.offer",
    "elyanka.trickster.beat.hunt",
    "elyanka.trickster.beat.anatomy",
    "elyanka.trickster.beat.writ",
    "elyanka.trickster.beat.whisper",
    "elyanka.trickster.beat.night",
    "elyanka.trickster.ch6.collateral",
    "elyanka.trickster.beat.table",
    "elyanka.trickster.beat.sisters",
    "elyanka.trickster.test.the_dead",
    "camellia.trickster.killed.late_curtain_prepared",
    "camellia.trickster.bond.witness_alive",
    "eliandra.trickster.ch5.burial",
    "eliandra.trickster.ch5.regnard",
    "eliandra.trickster.ch5.healer",
    "elyanka.trickster.beat.courier_return",
    "camellia.trickster.killed.late_curtain",
    "camellia.trickster.killed.third_night"
  ],
  "expected_scene_ids": [],
  "applicability": "narrative",
  "findings": [
    {
      "id": "ELY-A4-02",
      "disposition": "fixed",
      "files": [
        "storylines/elyanka_hearse.py",
        "tools/departure_contracts.json"
      ],
      "evidence": [
        "Dispatch answers append at message2 indices 3–5; old targets retained and gated. Separate courier_return waits 96h, records earned return, and survives chapter 6. Seven exact Claude placeholders registered."
      ],
      "siblings_checked": [
        "beat.anatomy",
        "beat.writ",
        "beat.hunt",
        "beat.master",
        "ch6.collateral",
        "all three courier answers"
      ]
    },
    {
      "id": "trickster_villain-c5-p21-001",
      "disposition": "fixed",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current base already anchors to answers but requires the optional courier. One OR group preserves optionality and the latest-held-flag 120h anchor; four singleton groups would require mutually exclusive answers (src/Story.cs:890,918)."
      ],
      "siblings_checked": [
        "courier hungry",
        "courier ripening",
        "courier silent",
        "no courier history"
      ]
    },
    {
      "id": "CAM-A4-02",
      "disposition": "fixed",
      "files": [
        "storylines/camellia_round2.py"
      ],
      "evidence": [
        "Prepared price legacy terminal answers require grave_filled; appended copies deliver approved r2.stones and its grave_filled terminal receipt. Original IDs, targets and indices retained."
      ],
      "siblings_checked": [
        "killed.late_curtain",
        "killed.third_night",
        "epilogue.kept",
        "epilogue.commit"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.door.hearse",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_trickster.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.straight.offer",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_trickster.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.beat.hunt",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.beat.anatomy",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.beat.writ",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.beat.master",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.beat.whisper",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.beat.night",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.ch6.collateral",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py",
        "tools/route_packs/plans/claude-work-queue.json"
      ],
      "evidence": [
        "Claude owns physical-to-remote rewrite. Existing inspection, tent contact and explicit slot require coordinator reconciliation; work-queue entry registered."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.beat.table",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.beat.sisters",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_hearse.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT elyanka.trickster.test.the_dead",
      "disposition": "blocked",
      "files": [
        "storylines/elyanka_trickster.py"
      ],
      "evidence": [
        "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery."
      ],
      "siblings_checked": [
        "all twelve requested Elyanka conversions"
      ]
    },
    {
      "id": "CONVERT camellia.trickster.bond.witness_alive",
      "disposition": "blocked",
      "files": [
        "storylines/camellia_masks.py",
        "storylines/camellia_round2.py"
      ],
      "evidence": [
        "Current generated scene is already in-person: ContactUnit 397b090721c41044ea3220445300e1b8, native AnswerLists 589d83230bbbfd04bb1220ee4fef1ce1, Drezen Areas; no Remote or Kind. The river steps remain dialogue staging, with no separate verified river encounter binding."
      ],
      "siblings_checked": [
        "witness",
        "witness_camp",
        "witness_alive"
      ]
    },
    {
      "id": "CONVERT eliandra.trickster.ch5.burial",
      "disposition": "blocked",
      "files": [
        "storylines/eliandra_trickster.py",
        "storylines/eliandra_stars.py"
      ],
      "evidence": [
        "Current source is in-person on shrine AnswerLists 6073e28cab0691542b85a24436ed919c with ReturnToList. No separate chiefs-ground encounter or wounded-camp host is bound. Capital presence twins do not establish either requested location."
      ],
      "siblings_checked": [
        "ch5.burial",
        "ch5.regnard",
        "ch5.healer",
        "Drezen presence twins"
      ]
    },
    {
      "id": "CONVERT eliandra.trickster.ch5.regnard",
      "disposition": "blocked",
      "files": [
        "storylines/eliandra_trickster.py",
        "storylines/eliandra_stars.py"
      ],
      "evidence": [
        "Current source is in-person on shrine AnswerLists 6073e28cab0691542b85a24436ed919c with ReturnToList. No separate chiefs-ground encounter or wounded-camp host is bound. Capital presence twins do not establish either requested location."
      ],
      "siblings_checked": [
        "ch5.burial",
        "ch5.regnard",
        "ch5.healer",
        "Drezen presence twins"
      ]
    },
    {
      "id": "CONVERT eliandra.trickster.ch5.healer",
      "disposition": "blocked",
      "files": [
        "storylines/eliandra_trickster.py",
        "storylines/eliandra_stars.py"
      ],
      "evidence": [
        "Current source is in-person on shrine AnswerLists 6073e28cab0691542b85a24436ed919c with ReturnToList. No separate chiefs-ground encounter or wounded-camp host is bound. Capital presence twins do not establish either requested location."
      ],
      "siblings_checked": [
        "ch5.burial",
        "ch5.regnard",
        "ch5.healer",
        "Drezen presence twins"
      ]
    }
  ],
  "gates": [],
  "escalations": [
    {
      "id": "CONVERT elyanka.trickster.door.hearse",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.straight.offer",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.beat.hunt",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.beat.anatomy",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.beat.writ",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.beat.master",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.beat.whisper",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.beat.night",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.ch6.collateral",
      "owner": "Coordinator and Claude",
      "evidence": "Claude owns physical-to-remote rewrite. Existing inspection, tent contact and explicit slot require coordinator reconciliation; work-queue entry registered.",
      "recommendation": "Resolve remote inspection versus approved physical explicit slot, then let Claude revise the affected nodes."
    },
    {
      "id": "CONVERT elyanka.trickster.beat.table",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.beat.sisters",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT elyanka.trickster.test.the_dead",
      "owner": "Coordinator: location bindings and live placement",
      "evidence": "Current source remains Remote with Kind and no playable location host. No Elyanka placement is registered in tools/presence_placement_manifest.json; src/Story.cs EntryTargets requires an actual answer-list or valid presence hub for physical delivery.",
      "recommendation": "Approve and verify the south-gate/dead-house physical host; supply separate woods and camp hosting for hunt/night. Keep the same IDs, remove Kind on in-person scenes, and retire the remote delivery."
    },
    {
      "id": "CONVERT camellia.trickster.bond.witness_alive",
      "owner": "Coordinator: location and transition bindings",
      "evidence": "Current generated scene is already in-person: ContactUnit 397b090721c41044ea3220445300e1b8, native AnswerLists 589d83230bbbfd04bb1220ee4fef1ce1, Drezen Areas; no Remote or Kind. The river steps remain dialogue staging, with no separate verified river encounter binding.",
      "recommendation": "Keep the native entry; approve a river-steps host and transition before relocating the murder."
    },
    {
      "id": "CONVERT eliandra.trickster.ch5.burial",
      "owner": "Coordinator: location and transition bindings",
      "evidence": "Current source is in-person on shrine AnswerLists 6073e28cab0691542b85a24436ed919c with ReturnToList. No separate chiefs-ground encounter or wounded-camp host is bound. Capital presence twins do not establish either requested location.",
      "recommendation": "Approve chiefs-ground burial/sword bindings and a wounded-camp host; preserve native IDs and answers, with Claude supplying changed connecting prose."
    },
    {
      "id": "CONVERT eliandra.trickster.ch5.regnard",
      "owner": "Coordinator: location and transition bindings",
      "evidence": "Current source is in-person on shrine AnswerLists 6073e28cab0691542b85a24436ed919c with ReturnToList. No separate chiefs-ground encounter or wounded-camp host is bound. Capital presence twins do not establish either requested location.",
      "recommendation": "Approve chiefs-ground burial/sword bindings and a wounded-camp host; preserve native IDs and answers, with Claude supplying changed connecting prose."
    },
    {
      "id": "CONVERT eliandra.trickster.ch5.healer",
      "owner": "Coordinator: location and transition bindings",
      "evidence": "Current source is in-person on shrine AnswerLists 6073e28cab0691542b85a24436ed919c with ReturnToList. No separate chiefs-ground encounter or wounded-camp host is bound. Capital presence twins do not establish either requested location.",
      "recommendation": "Approve chiefs-ground burial/sword bindings and a wounded-camp host; preserve native IDs and answers, with Claude supplying changed connecting prose."
    }
  ],
  "proposals": [],
  "risks": [
    "Seven courier connecting-text placeholders require Claude.",
    "Sixteen requested hosting/voice items remain escalated; no live placement proof or independent INT/HOW/COX >=91 judging.",
    "Runner must seal fresh required receipts for delivered source/export; gates intentionally empty."
  ],
  "completion": "blocked"
}
```

## ESCALATE

Sixteen CONVERT items remain blocked on coordinator location/transition decisions or Claude voice. Each item, owner, current-source evidence and recommendation is recorded above. No host GUID or placement was guessed. The bundled manifest has no audits and an operational scene-map marker, so external judging/playthrough claims are not treated as pinned verification.

## PROPOSE

None.

## RISKS

Structural wiring does not certify prose or rubric scores. Read the seven courier placeholders before playtesting. Physical conversions need verified placements and same-ID retirement of their remote deliveries. No commit, staging, push or integration merge performed; these belong to the runner.
