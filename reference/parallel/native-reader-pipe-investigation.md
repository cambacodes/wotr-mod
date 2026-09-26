# Native reader pipe investigation

The reported managed-reader failure is retained as an unexplained transient observation.
An identical sequential full managed rerun passed, so there is currently no reproduced defect supporting a production change.
This investigation changes no managed code, reader script, shared build output or game files.

## Observed failure and successful rerun

The parent reported `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` at `json.load(sys.stdin)` in `managed-tests/read-native.py`.
The parent then failed at `Native blueprint extraction failed` in `ReadNative`, before construction could finish.
The failure occurred during a managed run alongside independent Rules and Python tasks.
That timing alone does not establish concurrency as the cause.

Both the failed invocation and successful rerun explicitly selected `C:/Users/Z/AppData/Local/Python/pythoncore-3.14-64/python.exe` through `RRT_PYTHON` and the repository's `expansion-parent-bindings.json` through `RRT_PARENT_BINDINGS`.
The default PyManager launcher was therefore not involved in the reported failure.
The parent reported that the identical sequential rerun passed 61,288 assertions over 483 scenes and 17,838 generated blueprints.
Its DLL SHA-256 was `6ADEDEE3CA9085D8C98DF8191C764BCDDD169EB18277635E5AA5D8E943925292` and Story SHA-256 was `22D9A9302DBCB80E89E68BC7A7A849F9A756115F83F06E22126BD8A4D46E1A00`.
These full-run results are parent evidence, not a second full run performed by this reviewer.

## Source inspection

`ReadNative` starts a subprocess with redirected stdin and stdout, writes the serialized distinct ID sequence, closes stdin, reads stdout to completion and then checks the process exit code.
The inspected order includes the required close before Python's `json.load(sys.stdin)` can finish reading to EOF.
Closing the .NET stream flushes its buffered text; an omitted manual flush is not an established defect here.
Even an empty serialized ID sequence would be the valid JSON array `[]`, rather than empty input.

The Python failure location precedes archive opening, GUID lookup and parent-manifest handling.
Archive content, missing blueprints and simultaneous read-only archive scans do not directly explain this particular parse failure.
Column one alone cannot distinguish zero input bytes from other input that fails at its first character.
No raw failing stdin capture is available, so describing the failure as proven empty input would overstate the evidence.

The reader's inspected SHA-256 is `E37AA72FD914C1407614AAB49EA5A1FBADD79A812C29488EB4C362E2C9D02351`.

## Bounded isolated reproduction

The isolated .NET Framework 4.8 project is `C:/Users/Z/AppData/Local/Temp/native-reader-pipe-9x06ntc6/Check.csproj`.
It uses the actual repository reader, actual game archive and the real Konomi presence etude `b5f301fbc4c44535a6309d610d5bd28a`.
Its subprocess options and Write/Close/ReadToEnd/WaitForExit order match the inspected parent operation.
It uses a fixed valid JSON ID array so the pipe behavior can be exercised without rebuilding the shared test program.
The project builds to its own temporary directory with zero warnings and errors.

The probe runs four attempts through the default `python` launcher and four through the explicit interpreter used by the parent.
All eight attempts passed with exit code zero and the requested native record present in the 3,035-character JSON response.
The default-launcher trials are comparison evidence only; they are not a reproduction of the observed parent environment.
The small request does not reproduce the complete 483-scene request size or concurrent workload.
No synthetic corruption or deliberate empty-input run would establish why the actual invocation failed.

## Decision

Do not add a speculative retry, change JSON transport or serialize all project checks on this evidence.
Keep the original failure visible alongside the successful rerun.
If the same failure recurs, the useful next observation is the exact serialized request length/hash and bytes actually received by an isolated diagnostic reader, together with executable, exit status and stderr.
That diagnostic would need explicit implementation and review; it is not present in the current production reader.
The current evidence does not identify a root cause or certify that the transient cannot recur.
