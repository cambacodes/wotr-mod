# Aranka path-acquisition correction rereview

Status: the three requested corrections are confirmed in the pinned source and report, with one remaining report-fidelity correction; no live access is verified.

Reviewed source SHA-256: `7F7CA38A934ED03AE75651F8688C2C2184A799D6A0C927EE4FEB36D94B6DE3C1`.

Reviewed development report SHA-256: `12D70148245939AE78A3FEE19E4EDC7FD270D0872F8CDC337E1997F950F4FD7B`.

## Confirmed corrections

The module replaces the unproduced `chapter.5` flag with `REQUIRED_CHAPTER = 5` and requires `invitation_entry_ready` to receive a numeric chapter value equal to five.

The report now describes numeric Chapter 5 as a proposed condition and clearly states that the integration must read current Chapter 5 state.

The predicate check is explicitly documented as synthetic and limited: it supplies its own flags and does not verify a producer, current save, Aranka identity, location, consent, or live actor.

Running the exact Python module completes its bounded self-check successfully, including Chapter 4 rejection, missing Trickster contact rejection, and conflicting active path rejection.

Counting all ten `invitation` strings with `re.findall(r"\b[^\W_]+(?:['’][^\W_]+)*\b", text)` produces 278 words, matching the revised report's stated tokenizer count.

## Remaining report mismatch and scope

The report's final source-hash line still records the superseded source hash `E171CEB7DBEF9FD897D474123490ED889E66901489DC52CA48673F79CD4DFD01`, not the reviewed source SHA-256 above.

Update that line so the report pins the source version actually reviewed.

The numeric chapter argument is a testable function parameter, not evidence that a runtime adapter reads the current game chapter correctly.

The contact proof and Azata live-actor proof still have no runtime producers, the module remains unregistered, and the synthetic self-check cannot establish that any invitation is attainable in an actual save.

The ten path entries remain design concepts, with Swarm deliberately unresolved, and this rereview grants no access or romance-route approval.
