# Nocticula acquisition prose repair independent rereview

Reviewed frozen source `storylines/nocticula_trickster_acquisition.py`, SHA256 `B638B82325AE94230BF2AA640F33950167718C4C88ED7D35576696C2F0BBA9F8`.
I verified the hash, read the original independent findings and repair-development report, and followed the affected request and reply passages in the actual source.
I did not author these repairs.
Only this report was edited.

## Scoped verdict

All three reported prose defects are repaired in this source.
The changed passages pass the relevant continuity and literary criteria above 90.
This is not approval of the whole acquisition module, full-route length, native integration or runtime availability.

| Repaired dimension | Score | Finding |
| --- | --- | --- |
| Early and later refusal object and gesture continuity | 95 | Pass |
| Shared reply callback across candid and watchful seals | 95 | Pass |
| Speaker-relative brother reference | 97 | Pass |
| Local Nocticula voice and refusal agency | 94 | Pass |
| Local prose clarity and selected-path continuity | 94 | Pass |

## Refusal paths

I followed `history -> request -> decline` and `history -> request -> price -> decline` in each of `audience_missed`, `audience_rejected` and `audience_patronage`.
The six paths are actual available edges from each scene's first node.

On the early path, `request` establishes Nocticula's extended empty hand.
The new refusal lowers that hand while she waits for the Commander to finish speaking.
It neither produces wax nor makes nonexistent pieces disappear.

On the later path, `price` creates the disc, breaks it, leaves one half between her fingers and places the other on the table.
She then turns her retained half over.
Lowering that hand is compatible with this position and does not assert that it is empty or that the table half has moved.
The Commander's refusal tells her to keep both halves, so leaving their exact disposal off-page is not a contradiction.
The revised gesture works at both entry points without inserting an unperformed retrieval or requiring a second refusal node.

The refusal remains cool and dismissive rather than wounded, pleading or automatically accommodating.
Her attention returns to the audience's actual business.
The terminal choice writes only `noct.acq.closed`; it grants neither a seal nor the request flag.
That prevents the later acquisition scenes under their existing forbids without asserting that the parent relationship or native audience has been ended by this text.

## Reply paths

Both `price -> bounded` and `price -> leverage` have the same physical producer: `price` breaks the wax across its center before either choice.
Both subsequent nodes explicitly use its broken edge.
The watchful `leverage` path alone adds a shallow score across the back.

`her_hand/start` now says the new answering line traces the old break.
That callback therefore has an established object on both branches and no longer depends on the watchful score.
The following turn beneath the wax and the Commander's choice to keep their hands still do not require a newly scored edge.
Later turning the sheet follows the completed stroke and does not contradict the earlier decision to avoid lifting it while it forms.

I read the intervening narrow-success, voluntary-letter and exposed-then-letter preparation passages.
They preserve the half-seal and its break rather than repairing the physical split before the reply.
The failure passage's statement that the wax is intact describes survival of the attempted aperture, not a newly rejoined full disc.
The new callback introduces no additional prop or required handling step on those paths.

## Speaker reference

At `price`, Nocticula now says "the name my brother found amusing."
That correctly makes Socothbenoth her brother.
The Commander's nearby uses of "your brother" address Nocticula and remain correct.
Her later instruction to explain what "my brother" has been doing is consistent with the repaired line.
The repair preserves the original sardonic register without inventing Commander kinship.

## Checks and limits

I independently ran `python -m storylines.nocticula_trickster_acquisition`.
It passed six scene definitions, 37 delivered nodes, six fixture histories and 36 completed trial outcomes.
I also ran a separate focused source traversal verifying all six refusal paths, the six candid/watchful branch instances, the shared broken-edge callback and the refusal's exact closure write.
That check also verified no producer writes `noct.acq.renewed_agreement`, `noct.acq.conflict_resolved_verified` or `noct.acq.postconflict_reply_verified`.
No test result substitutes for the prose reading above.

These are Python source checks, not an executed C# or Unity audience lifecycle.
I did not independently compare the complete frozen module with the pre-repair bytes, so the author's text-only structural-delta result is not claimed as my own reproduction.
I did not recalculate selected word counts for this three-passage repair.

The opening remains unregistered.
The actual return to native audience answers after the addon book event is still unproved.
There is no certified parent-continuation join, completed acquisition romance, post-conflict response or recovery after leaving the audience without the request.
The previous review's broader incomplete-scope findings remain in force.
No artwork, export, installed mod or runtime behavior is approved by this rereview.
