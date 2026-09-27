# Yaniel opening timing revision - development record

Source: storylines/yaniel_route_opening.py.
Current source SHA-256: B779AB772F5E548E5C6D6DB225FDE21FC0DA81ADB4BD3759FAFC68BB9FB39C6F.

Earlier scoped reviews examined different source snapshots and do not score or approve this timing revision.
The current source changes the opening scene delay from 24 hours to four hours after the native rescue-state requirements are met.
This adjustment is intended to place the authored opening inside Yaniel's brief stay in Drezen, before her established choice to travel into the Abyss with Targona.
The precise rescue-to-contact interval and contact producer remain unverified.
This does not claim that the letter, actor, location, or current-state flags exist at runtime.

The follow-up scene is scheduled twelve hours after the opening.
Its source-level assertion checks the combined sixteen-hour interval against the cited one-day Drezen period.
This arithmetic is only a design constraint, not proof that the game scheduler or campaign chronology satisfies it.

`python -m py_compile storylines/yaniel_route_opening.py` passes.
The follow-up module imports the opening's scene record and asserts the four-hour and twelve-hour delays.
A fresh independent review must assess chronology, identity gating and scene availability on the exact current source.
No route readiness, integration, all-path access, art, save/load, ToyBox compatibility, or in-game behavior is claimed.

