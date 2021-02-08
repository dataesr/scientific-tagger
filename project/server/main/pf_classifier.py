import fasttext
from collections import Counter
from project.server.main.utils_str import normalize_text
from project.server.main.utils import download_file
from os import path

if path.exists("/models/model_pf.bin") is False:
    download_file("https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/models/model_pf.bin", "/models/")
if path.exists("/models/model_pf.vec") is False:
    download_file("https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/models/model_pf.vec", "/models/")

model_pf = fasttext.load_model('/models/model_pf.bin')

def get_pf_label(title, nb_top = 10):
    if not isinstance(title, str) or title is None or len(title) == 0:
        return "unknown"
    title_norm = normalize_text(title).lower()
    print(f"get_pf_label {title} ==> {title_norm}", flush=True)
    prediction = model_pf.predict(title_norm,nb_top)
    return prediction



def pf_classify(elems, nb_top = 10):
    for e in elems:
        print(e, flush=True)
        if 'doi' in e and 'title' not in e or 'journal_name' not in e:
            print("should enrich metadata", flush=True)
            continue

        if 'title' in e:
            pf_labels = get_pf_label(e['title'], nb_top)
            print(pf_labels, flush=True)
            pf_classif = []
            scores = list(pf_labels[1])
            for ix, label in enumerate(list(pf_labels[0])):
                pf_classif.append({
                    "label": label.replace("__label__", ""),
                    "score": scores[ix]
                    })
            e['pf_classification'] = pf_classif
    return elems

