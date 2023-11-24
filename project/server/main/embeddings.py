import os
import spacy
from sklearn import preprocessing

from project.server.main.logger import get_logger

logger = get_logger(__name__)

nlp = spacy.load("en_core_sci_scibert")
model_multilingual = SentenceTransformer('distiluse-base-multilingual-cased-v1')

def get_embeddings(embed_type, text, normalize=True):
    if not isinstance(text, str) or text is None or len(text) == 0:
        return None
    if embed_type == 'scibert':
        return get_scibert_embeddings(text, normalize)
    elif embed_type == 'multilingual':
        return get_multilingual_embeddings(text, normalize)
    else:
        logger.debug(f'unknown {embed_type} embedding type!')

def get_scibert_embeddings(text, normalize=True):
    doc = nlp(text)
    tokvecs = doc._.trf_data.tensors[-1]
    if normalize:
        tokvecs = preprocessing.normalize(tokvecs, norm='l2')
    assert(len(tokvecs[0]) == 768)
    # converting to float for json serialization
    return { 'embeddings': [float(e) for e in tokvecs[0]] }

def get_multilingual_embeddings(text, normalize=True):
    return model_multilingual.encode(text, normalize_embeddings=normalize)
