import re

FILLER_PHRASES = [
    "my name is",
    "this is",
    "i am",
    "its",
    "it's",
    "hello",
    "hi"
]

INVALID_WORDS = {
    "yes", "no", "correct", "right", "bye", "and", "return"
}

def extract_name(text: str):
    t = text.lower()

    for p in FILLER_PHRASES:
        t = t.replace(p, "")

    # remove punctuation
    t = re.sub(r"[^a-zA-Z\s]", "", t)

    words = [w for w in t.split() if w not in INVALID_WORDS]

    if not words:
        return None

    # take last 1–3 words
    name_words = words[-3:]
    name = " ".join(name_words)

    if len(name) < 2:
        return None

    return name.title()


def extract_spelled_name(text: str):
    letters = re.findall(r"[A-Za-z]", text)
    if len(letters) >= 2:
        return "".join(letters).upper()
    return None
