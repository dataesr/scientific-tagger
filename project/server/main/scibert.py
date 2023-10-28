import os
import spacy

from project.server.main.logger import get_logger

logger = get_logger(__name__)

nlp = spacy.load("en_core_sci_scibert")

def get_scibert_embeddings(text):
    if not isinstance(text, str) or text is None or len(text) == 0:
        return None
    doc = nlp(text)
    tokvecs = doc._.trf_data.tensors[-1][0]
    assert(len(tokvecs) == 768)
    # converting to float for json serialization
    return { 'embeddings': [float(e) for e in tokvecs] }
