import fasttext
from project.server.main.utils_str import normalize
from project.server.main.utils import download_file
import os

from project.server.main.logger import get_logger

logger = get_logger(__name__)

project_id = os.getenv("OS_TENANT_ID")
project_id = "32c5d10cb0fe4519b957064a111717e3"
models = {}

os.system("mkdir -p /src/models/")

def init():
    for f in ['journal_title', 'title', 'abstract', 'keywords', 'mesh_headings']:
        model_name = f"/src/models/pubmed_model_{f}.model"
        if os.path.exists(model_name) is False:
            download_file(f"https://storage.gra.cloud.ovh.net/v1/AUTH_{project_id}/models/pubmed_model_{f}.model", model_name)
        logger.debug(f"loading model {model_name}")
        models[f] = fasttext.load_model(model_name)
        logger.debug("nb labels : {}".format(models[f].get_labels()))

def bsso_classify(elems):
    for e in elems:
        fields = {"bsso_classification": detect_field(e)}
        e.update(fields)
    return elems

def dedup_sort(x):
    y = list(set([e for e in x if e]))
    y.sort()
    return y

def detect_field(elt):
    
    weights={'journal_title': 1.5, 'title': 1, 'abstract': 1, 'keywords': 1, 'mesh_headings': 1}
    
    results = []
    results_journal = {}
    res = {}
    fields_predected = {}
    
    prediction_journal_title = []
    
    for f in ['journal_title', 'title', 'abstract', 'keywords', 'mesh_headings']:
        current_words = elt.get(f) 
        if current_words is None:
            continue
        if isinstance(current_words, list):
            current_words = " ".join(current_words)

        if f == "abstract" and len(current_words.split(" ")) < 20:
                continue
        elif f == "title" and len(current_words.split(" ")) < 10:
            continue
        elif len(current_words.split(" ")) < 2:
            continue
        elif len(current_words) < 5:
            continue

        current_words = normalize(current_words).replace("\n", " ")

        current_prediction = models[f].predict(current_words,  k=-1, threshold=0.5)
        
        res[f] = current_words
        res[f"{f}_prediction"] = current_prediction

        #print(f, current_words, current_prediction)

        results.append({"labels": current_prediction[0], "scores": current_prediction[1], "model": f})
        
        
        for k, pred in enumerate(list(current_prediction[0])):
            pred = pred.replace('__label__', '').replace('_', ' ')
            if pred not in fields_predected:
                fields_predected[pred] = {"nb": 0, "models":[], "scores":[], "weighted_score": 0, "field": pred}
            fields_predected[pred]["nb"] += 1
            fields_predected[pred]["models"].append(f)
            fields_predected[pred]["scores"].append(current_prediction[1][k])
            fields_predected[pred]["weighted_score"] += weights[f] #* current_prediction[1][k]
            
            if f == "journal_title":
                prediction_journal_title.append(pred)
    
    sorted_res = sorted(fields_predected.items(), key=lambda item: item[1]["weighted_score"])
    sorted_res.reverse()
    if sorted_res:
        max_weighted = sorted_res[0][1]["weighted_score"]
        ans = {"field":[], "models":[], "weighted_score": max_weighted}
        for k in sorted_res:
            if k[1]["weighted_score"] != max_weighted:
                continue
            ans["field"].append(k[1]["field"])
            ans["models"].append(";".join(dedup_sort(k[1]["models"])))

        for f in ['journal_title', 'title', 'abstract', 'keywords', 'mesh_headings']:
            ans[f] = elt.get(f) 
            
        ans["field"] = dedup_sort(ans["field"])
        
        ans["models"] = dedup_sort(ans["models"])
        
        ans["field_journal_title"] =  prediction_journal_title
        return ans
        
    return {}

