import string, re
from tokenizers import normalizers
from tokenizers.normalizers import Lowercase, NFD, StripAccents, Strip, BertNormalizer

normalizer = normalizers.Sequence([BertNormalizer(), Strip()])

def delete_punct(w: str) -> str:
    """Delete all puctuation in a string."""
    return w.lower().translate(
      str.maketrans(string.punctuation, len(string.punctuation)*" "))

def normalize(x):
    y = normalizer.normalize_str(delete_punct(x))
    y = y.replace("\n", " ")
    # remove double spaces
    y = re.sub(' +', ' ', y).strip()
    return y
