import string
import unicodedata

def strip_accents(w: str) -> str:
    """Normalize accents and stuff in string."""
    w2 = w.replace("’", " ")
    return "".join(
        c for c in unicodedata.normalize("NFD", w2)
        if unicodedata.category(c) != "Mn")


def delete_punct(w: str) -> str:
    """Delete all puctuation in a string."""
    return w.lower().translate(
        str.maketrans(string.punctuation, len(string.punctuation)*" "))

def normalize_text(text: str) -> str:
    """Normalize string. Delete puctuation and accents."""
    if isinstance(text, str):
        text = delete_punct(text)
        text = strip_accents(text)
        text = text.replace('\xa0', ' ')
        text = " ".join(text.split())
    return text or ""
