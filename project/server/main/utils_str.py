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

def get_str(x):
    res = ''
    if isinstance(x, dict):
        for f in x:
            if f not in ['lang']:
                res += ' ' + get_str(x[f])
    if isinstance(x, str):
        res = x.strip()
    if isinstance(x, list):
        for e in x:
            res += ' ' + get_str(e)
    return res.strip()

