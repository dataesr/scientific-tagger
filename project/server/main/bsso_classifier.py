import fasttext
from project.server.main.utils_str import normalize
from project.server.main.utils import download_file
import os

from project.server.main.logger import get_logger

logger = get_logger(__name__)

project_id = os.getenv("OS_TENANT_ID")
project_id = "32c5d10cb0fe4519b957064a111717e3"
models = {}

os.system("mkdir -p /src/models")

def init():
    for f in ['journal_title', 'title', 'abstract', 'keywords', 'mesh_headings']:
        model_name = f"/src/models/pubmed_model_{f}.model"
        if os.path.exists(model_name) is False:
            download_file(f"https://storage.gra.cloud.ovh.net/v1/AUTH_{project_id}/models/pubmed_model_{f}.model", "/src/models/")
        logger.debug(f"loading model {model_name}", flush=True)
        models[f] = fasttext.load_model(model_name)
        logger.debug("nb labels : {}".format(models[f].get_labels()), flush=True)

def bsso_classify(elems):
    for e in elems:
        fields = {"bsso_fields": detect_field(e)}
        e.update(fields)
    return elems

def detect_field(elt):
   
    if len(models) < 5:
        init()

    results = []
    
    for f in ['journal_title', 'title', 'abstract', 'keywords', 'mesh_headings']:

        current_words = elt.get(f)
        
        if current_words is None:
            continue
        if isinstance(current_words, list):
            current_words = " ".join(current_words)
 
        if len(current_words)<10:
            continue

        current_words = normalize(current_words).replace("\n", " ")
    
        current_prediction = models[f].predict(current_words, 2)
        results.append(current_prediction)
        
    final_res = []
    for r in results:
        score1 = r[1][0]
        score2 = r[1][1]
        if (score1 + score2) > 0.95 and (score1 - score2)< 0.10:
            final_res = r[0]
            
    if len(final_res) > 0:
        final_res = [w.replace('__label__', '').replace('_', ' ') for w in final_res]
        return final_res
    
    current_max = 0
    for r in results:
        if r[1][0] > current_max:
            final_res = [r[0][0]]
            current_max = r[1][0]
    
    final_res = [w.replace('__label__', '').replace('_', ' ') for w in final_res]
    return final_res
