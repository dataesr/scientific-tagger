import os
import spacy
from sklearn import preprocessing

from project.server.main.logger import get_logger

logger = get_logger(__name__)

nlp = spacy.load("en_core_sci_scibert")

def get_scibert_embeddings(text, normalize=True):
    if not isinstance(text, str) or text is None or len(text) == 0:
        return None
    doc = nlp(text)
    tokvecs = doc._.trf_data.tensors[-1]
    if normalize:
        tokvecs = preprocessing.normalize(tokvecs, norm='l2')
    assert(len(tokvecs[0]) == 768)
    # converting to float for json serialization
    return { 'embeddings': [float(e) for e in tokvecs[0]] }
