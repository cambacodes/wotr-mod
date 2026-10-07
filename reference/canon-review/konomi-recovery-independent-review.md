# Independent Konomi retained-body recovery review

The frozen service passes this review as an unregistered prerequisite for an explicit retained-body recovery action.
I found no blocking defect within that scope.
This is not approval of a playable recovery route or proof that resurrection works in Unity.
I did not author the reviewed source or tests and changed neither.

## Reviewed files and evidence

| File | SHA256 |
| --- | --- |
| `src/KonomiRecovery.cs` | `F476A0DAD2E3FA6164743E4F78A14AB18551791233BD927A1932B709441D5329` |
| `managed-tests/KonomiRecoveryTests.cs` | `EC3AB112077A4AF985E06B0CF6338F49911FD7508CD3A1B0D9C5A60A02DA7429` |
| Installed `Assembly-CSharp.dll` | `2CB7160B7154D4FFACC77B9C51B1EB26199E1294300F04FDFC073367B2EF8953` |

I inspected the implementation report, both frozen files, the reused `JerribethRecovery.Inspect` implementation and both current `KonomiContactObservation` paths.
I checked the recorded native `UnitDescriptor.Resurrect` and `ContextActionResurrect` bodies in `jerribeth-recovery-managed-records.json` against that record's matching installed-assembly hash.
The production operation calls the native full-restore method directly.
Native work changes death flags and health before later view, buff and event processing, so a partial failure is possible in the real runtime.

## Independent execution

I copied the author's isolated project definitions and runner into `C:/Users/Z/AppData/Local/Temp/konomi-recovery-review-8b9bceda`, changing their private build paths.
Both isolated builds succeeded with zero warnings and errors.
The original focused test file passed all 31 assertions.
I then copied that test file into the review temporary directory and added four checks for a competing spawner claiming the same actor, an unsupported attempt version, a blank request identity and an unsupported serialized proof version.
The extended temporary fixture passed all 35 assertions.
The extra checks remain in that temporary directory and do not alter the shared test file.
No shared build output, game file, save or source was changed.

The actual installed resurrection call raised `System.Security.SecurityException: ECall methods must be packaged into a system module` from `UnitDescriptor.Resurrect`.
The fixture remained dead and finally dead, retained its native spawn/death history, saved only an unconfirmed attempt and returned Pending.
This independently reproduces the stated Unity boundary.
Positive life-confirmation checks set native fields in controlled fixtures and therefore test observation handling only.
They are not successful resurrection demonstrations.

## Contract assessment

The source observer requires the exact saved spawner, retained actor identity, blueprint, scene storage and registry agreement.
It rejects competing claims and additional Konomi representations in the inspected source storage.
The runtime wrapper additionally requires loaded serializable source state, a conscious Commander, no combat, no loading/unloading, no hostile actor and no competing saved capital-area object.
Those runtime gates were inspected and compiled, not executed through live Unity.

The first request requires a retained dead actor and records the stable authored choice identity and saved actor ID before native dispatch.
Persistence failure prevents dispatch.
The checkpoint uses the existing player SettingsList save mechanism, with no claim of an immediate forced disk save.
A different request cannot adopt an existing attempt.
Malformed or unsupported records cannot grant historical-death proof.

`Poll` cannot call resurrection.
An explicit repeated request may retry an unconfirmed dead actor, while an unconscious living actor remains pending.
Confirmation requires a fresh observation of the same actor object alive and conscious.
Saving a separate confirmed object prevents a failed write from changing the pending attempt in memory.
A confirmed request cannot resurrect a subsequent observed death.
Current destruction, loss of provenance, area loss or identity mismatch cannot count as a confirmed return.
The service does not clear HasDied, clone an actor, restore office history, grant romance access or move the character manually.

## Integration requirements and limits

Both existing contact-observer paths currently reject HasDied before a recovery exception could apply.
Their integration needs separate review.
Validate original saved provenance first, then excuse only historical HasDied for that exact currently living actor with a confirmed recovery record.
Keep actual death, destruction, competing identity and office guards intact.
Apply the same restriction to the unloaded saved-state path so that leaving Drezen does not misclassify an established return.
`HasVerifiedReturn` alone does not validate source storage, registry agreement, hostility or office status.

The authored action must supply the current mythic, quest and voluntary-choice authorization.
`CanRequest` supplies retained-dead eligibility only.
It does not check a prospective request identity against an existing pending attempt, so a caller must handle a rejected request without consuming its success effects.
The action must remain reachable for verification after the actor becomes alive and grant success only after a current Confirmed result.
Neither the existence of a checkpoint nor a native method return is sufficient.

A confirmed observation establishes current life, not completion of every downstream native event or visual update after a partial exception.
Actual native resurrection, stable later-frame state, restored view/animation behavior, game save/load persistence and ToyBox coexistence still need runtime verification.
The current service has no Main registration or authored caller and does not make the route playable.
Missing, destroyed, never-spawned, hostile and other unresolved histories remain outside this prerequisite and remain unfinished work under the broader Trickster requirement.
No full-route quality score, release approval or Unity success is inferred from these checks.
