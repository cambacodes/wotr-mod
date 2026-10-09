"""eng7-l09: ordered narration tokens and exact unmarked span diagnostics."""
import re
import json
from tools.player_text_lint import surfaces
from tools.player_text_lint import EXCEPTIONS


def markup_shape(text):
    return re.findall(r'\{/?n\}|["“”]|\n', text)


def spans(text, speaker="Narrator", kind="node"):
    hard, review = [], []
    depth, last = 0, 0
    openers = []
    outside = []
    for tag in re.finditer(r'\{/?n\}', text):
        if depth == 0:
            outside.append((last, tag.start()))
        if tag.group() == "{n}":
            if depth:
                hard.append(("nested-narration", tag.start(), tag.end()))
            depth += 1
            openers.append((tag.start(), tag.end()))
        elif depth == 0:
            hard.append(("orphan-narration-closer", tag.start(), tag.end()))
        else:
            depth -= 1
            openers.pop()
        last = tag.end()
    if depth:
        hard.extend(("unclosed-narration", start, end) for start, end in openers)
    else:
        outside.append((last, len(text)))
    # eng7-f2: UI labels are valid display surfaces without narration markup.
    # Markup balance is still checked; NPC text retains full prose detection.
    if kind == "ui":
        return hard, review
    # end eng7-f2
    # Mask display tokens without changing offsets. Gender tags are speech, not prose.
    mask = list(text)
    for token in re.finditer(r'\{[^{}]*\}|\[[^\]]*\]', text):
        mask[token.start():token.end()] = " " * (token.end() - token.start())
    masked = "".join(mask)
    # Quotes may span lines and narration spans (Owlcat dialogue often does).
    quote_mask = list(masked)
    # eng7-f2: Owlcat also repeats an opening quote on continuation paragraphs.
    # A quote at the start of a line while speech is open does not close it.
    opened = None
    for i, char in enumerate(masked):
        if char in {'"', '“', '”'}:
            if opened is None and char != '”':
                opened = char
            elif ((opened == '“' and char == '”') or
                  (opened == '"' and char == '"' and
                   masked[masked.rfind('\n', 0, i) + 1:i].strip())):
                opened = None
            quote_mask[i] = '\0'
        elif opened is not None:
            quote_mask[i] = '\0'
    # end eng7-f2
    # A standalone narration paragraph separates speech turns. A fresh opening
    # after it requires the previous turn to close. Inline attribution and
    # uninterrupted Owlcat continuation paragraphs remain valid.
    # --- eng8-q8c / E-Q8-04 ---
    review.extend(speech_boundaries(text))
    # end eng8-q8c
    remaining = "".join(quote_mask)
    for begin, end in outside:
        for line in re.finditer(r'[^\n\0]+', remaining[begin:end]):
            raw = line.group()
            if not re.search(r'[A-Za-z]', raw):
                continue
            if kind in {"choice", "entry"} and not re.search(r'["”]', text[begin:end]):
                continue  # intentional action/Continue answers
            start = begin + line.start() + len(raw) - len(raw.lstrip())
            finish = begin + line.end() - len(raw) + len(raw.rstrip())
            review.append(("unmarked-narration-review", start, finish))
    return hard, review


# --- eng8-q8c: quote boundaries use narration tokens, not quotes inside them ---
def speech_boundaries(text):
    rows = []
    opened, start, standalone = None, None, False
    for token in re.finditer(r'\{n\}[\s\S]*?\{/n\}|["“”]', text):
        value, i = token.group(), token.start()
        if value.startswith('{n}'):
            before = text[text.rfind('\n', 0, i) + 1:i]
            line_end = text.find('\n', token.end())
            after = text[token.end():line_end if line_end >= 0 else len(text)]
            if opened is not None and not before.strip() and not after.strip():
                standalone = True
            continue
        at_line_start = not text[text.rfind('\n', 0, i) + 1:i].strip()
        if opened is None and value != '”':
            opened, start, standalone = value, i, False
        elif value != '”' and at_line_start and opened == value:
            if standalone:
                rows.append(("speech-boundary-review", start, i))
            standalone = False
        elif (opened == '“' and value == '”') or (opened == '"' and value == '"'):
            opened, start, standalone = None, None, False
    return rows
# end eng8-q8c


def check(story, draft=False, exceptions=None):
    result = {"hard": [], "review": []}
    # eng8-q8c: reviewed continuation exceptions bind to the complete surface.
    policy = json.loads(EXCEPTIONS.read_text(encoding="utf-8")) if exceptions is None else exceptions
    for sid, location, text, speaker, kind in surfaces(story):
        hard, review = spans(text, speaker, kind)
        for level, rows in (("hard", hard), ("review", review)):
            for code, start, end in rows:
                if code == "speech-boundary-review" and any(
                    e.get("scene") == sid and e.get("location") == location and e.get("code") == code
                    and e.get("markup_shape") == markup_shape(text) and e.get("reason")
                    for e in policy.get("eng8-q8c", {}).get("speech_boundary_exceptions", [])):
                    continue
                result[level].append(dict(scene=sid, location=location, code=code, start=start, end=end,
                                          match=text[start:end], draft=draft))
    # Inline (native-cue) scenes render each node as one cue: gated paragraphs become Continue cues that override the
    # node's authored answers in game (managed NativeAudienceTests, 2026-10-08). Catch it here, before the managed run.
    for scene in story.get("Scenes", []):
        if scene.get("NativeReturnCue"):
            for node in scene.get("Nodes", []):
                if node.get("Paragraphs"):
                    result["hard"].append(dict(scene=scene["Id"], location=node["Id"], code="inline-scene-paragraphs",
                                               start=0, end=0, match="", draft=draft))
    return result
