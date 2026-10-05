"""eng7-l09: ordered narration tokens and exact unmarked span diagnostics."""
import re
from tools.player_text_lint import surfaces


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


def check(story, draft=False):
    result = {"hard": [], "review": []}
    for sid, location, text, speaker, kind in surfaces(story):
        hard, review = spans(text, speaker, kind)
        for level, rows in (("hard", hard), ("review", review)):
            for code, start, end in rows:
                result[level].append(dict(scene=sid, location=location, code=code, start=start, end=end,
                                          match=text[start:end], draft=draft))
    return result
