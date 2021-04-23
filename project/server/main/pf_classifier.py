import fasttext
from collections import Counter
from project.server.main.utils_str import normalize
from project.server.main.utils import download_file
import os


from project.server.main.logger import get_logger

logger = get_logger(__name__)

os.system("mkdir -p /src/models")


project_id = os.getenv("OS_TENANT_ID")
project_id = "32c5d10cb0fe4519b957064a111717e3"

model={}

def init():

    if os.path.exists("/src/models/model_pf.bin") is False:
        download_file("https://storage.gra.cloud.ovh.net/v1/AUTH_{project_id}/models/model_pf.bin", "/src/models/model_pf.bin")
    if os.path.exists("/src/models/model_pf.vec") is False:
        download_file("https://storage.gra.cloud.ovh.net/v1/AUTH_{project_id}/models/model_pf.vec", "/src/models/model_pf.vec")

    model_pf = fasttext.load_model('/src/models/model_pf.bin')
    model["pf"] = model_pf

def get_pf_label(title, nb_top = 10):

    if len(model)<1:
        init()

    if not isinstance(title, str) or title is None or len(title) == 0:
        return "unknown"
    title_norm = normalize(title) #lower
    logger.debug(f"get_pf_label {title} ==> {title_norm}")
    prediction = model["pf"].predict(title_norm,nb_top)
    return prediction



def pf_classify(elems, nb_top = 10):
    for e in elems:
        logger.debug(e)
        if 'doi' in e and 'title' not in e or 'journal_name' not in e:
            logger.debug("should enrich metadata")
            continue

        if 'title' in e:
            pf_labels = get_pf_label(e['title'], nb_top)
            logger.debug(pf_labels)
            pf_classif = []
            scores = list(pf_labels[1])
            for ix, label in enumerate(list(pf_labels[0])):
                pf_classif.append({
                    "label": label.replace("__label__", ""),
                    "score": scores[ix]
                    })
            e['pf_classification'] = pf_classif
    return elems

