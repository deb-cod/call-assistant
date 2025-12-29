import re

FILLER_PHRASES = [
    "my name is", "this is", "i am", "it's", "hello", "hi"
]

def extract_name_deterministic(text: str):
    t = text.lower()

    for p in FILLER_PHRASES:
        t = t.replace(p, "")

    # remove punctuation
    t = re.sub(r"[^a-zA-Z\s]", "", t)

    words = t.split()

    if not words:
        return None

    # take last 1–3 words (names usually at end)
    name_words = words[-3:]

    name = " ".join(name_words).strip()

    # sanity check
    if len(name) < 2:
        return None

    return name.title()
