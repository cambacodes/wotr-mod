# Native reader encoding fix: independent review

The byte-input fix is accepted for the reproduced encoding failure.
This is a review of the reader transport correction, not game-runtime verification.
The reviewed `managed-tests/read-native.py` SHA256 is `334311F7E3E412987E917AB619C6267A43A03994BE6F21FB62629D3DBE46E965`.
Its final functional change is `json.load(sys.stdin)` to `json.load(sys.stdin.buffer)`, with one explanatory comment.
The temporary trace code has been removed from that file.

## Independently reproduced failure

The isolated .NET Framework 4.8 probe is `C:/Users/Z/AppData/Local/Temp/native-reader-encoding-jqvxyzyl/Check.csproj`.
Its final two trials use the ordinary Process.StandardInput writer and Write/Close order, without changing Console.InputEncoding or replacing the writer.
The local encoding loop is diagnostic labeling only; it does not configure those final trials.
Both trials reported the actual default writer as UTF-8 with preamble `EF-BB-BF` and Console.InputEncoding UTF-8.
The explicit installed Python 3.14 interpreter reported stdin encoding cp1252.
Its first decoded code points were `0xef`, `0xbb`, `0xbf`, `0x5b`, `0x22`, followed by the requested GUID.
Both failed with the exact `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` message.
The child diagnostic reads stdin as text and passes it to json.loads, matching json.load's relevant decoding behavior.
No archive contents or missing blueprint caused this failure.

An earlier experimental attempt to set ProcessStartInfo.StandardInputEncoding failed to compile because that property is absent from the target .NET Framework API.
An exploratory wrapper writer also retained an already emitted default preamble.
Neither attempt is part of the final fix or evidence of a successful alternative.
The previous eight successful isolated reader calls therefore did not disprove an encoding-dependent failure.

## Parent's full-run evidence

Root separately observed actual failing-request child PID 11640 with a UTF-8 writer, preamble `EF-BB-BF`, UTF-8 console encoding and 5,566 serialized request characters.
The Python child received 5,569 bytes, beginning `efbbbf5b223333393630633766376166`, while reporting cp1252 text input.
Decoding those exact bytes through the former text path reproduced the column-one failure.
Decoding them as byte JSON allowed the full managed run to pass 64,527 assertions.
These full-run figures and captured bytes are root's evidence, not a full managed run performed by this reviewer.
Together with the isolated witness, they identify the observed failure as an encoding/preamble mismatch rather than an unexplained empty pipe.
They do not by themselves prove which other process changed a shared console code page.
Concurrent scheduling is no longer needed as a speculative explanation for why the parser rejected the captured request.

## Fix and independent validation

Python's JSON decoder accepts byte input and detects JSON wire encoding, including the UTF-8 preamble.
Reading sys.stdin.buffer prevents locale text decoding from turning that preamble into three ordinary cp1252 characters.
It retains the existing EOF protocol and error behavior for malformed JSON.
No retry, manual prefix stripping, global console mutation or serialization of unrelated tests is required.
The GUID request remains the same JSON payload.

I inspected and independently ran `managed-tests/native-reader-encoding-test.py` against the actual installed blueprints.zip using the explicit Python 3.14 executable.
It forces cp1252 stdin decoding for child processes, reproduces the old parser failure with BOM-prefixed UTF-8, then invokes the actual fixed archive reader with both plain UTF-8 and BOM-prefixed UTF-8.
Both fixed-reader cases returned exactly the requested Konomi presence-etude record and exited successfully.
The regression passed.
This checks the actual script and archive rather than only a standalone JSON expression.
The test's input is intentionally constructed to reproduce the diagnosed wire condition; it does not manufacture the full-run evidence, which was independently captured above.

No mandatory defect was found in the final reader correction or this focused regression.
The older `native-reader-pipe-investigation.md` remains a historical record of the then-unreproduced symptom; this review supersedes its unknown-cause conclusion.
