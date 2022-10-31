import fasttext
from collections import Counter
from project.server.main.bso_category import get_bso_category
from project.server.main.pf_classifier import get_pf_label
from project.server.main.utils import download_file
import pickle
import os

os.system("mkdir -p /src/models/")
if os.path.exists("/src/models/all_categ_revue.pkl") is False:
    download_file("https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/models/all_categ_revue.pkl", "/src/models/all_categ_revue.pkl")
all_categ_revue = pickle.load(open('/src/models/all_categ_revue.pkl', 'rb'))

def get_categ_from_source(source, top=1):
    try:
        mst_common = Counter(all_categ_revue[source]).most_common()
        mst_common_list = [e[0] for e in mst_common if (e[0] and (e[0] not in ['unknown', '']))]
        ans = ";".join([e for e in mst_common_list[0:top]]) # the most common
        if ans == "":
            ans = 'unknown'
    except:
        ans = 'unknown'
    return ans

def format_pf_tags(x):
    pf_tags_formatted = []
    for ix, tag in enumerate(x[0]):
        confidence = x[1][ix]
        pf_tags_formatted.append({'tag': tag.replace('__label__', ''), 'confidence': confidence})
    return pf_tags_formatted

def get_discipline_calc(title, journal_name, details = False):
    current_field = "unknown"
    method = ""
    pf_tags = []

    top_categ = None
    if journal_name:
        top_categ = get_categ_from_source(journal_name, 3)

    if isinstance(title, str) and len(title)>0:
        prediction_pf = get_pf_label(title)
        current_field = get_bso_category(prediction_pf)
        method = "pf_classifier_confident"
        pf_tags = prediction_pf

    if current_field == "unknown" and journal_name:
        current_field = get_categ_from_source(journal_name)
        method = "category_from_journal"

    if current_field == 'unknown' and isinstance(title, str) and len(title)>0:
        prediction_pf_2 = get_pf_label(title, nb_top = 10)
        current_field = get_bso_category(prediction_pf_2, is_strict=False)
        method = "pf_classifier_lenient"
        pf_tags = prediction_pf_2

    ans = { "bso_classification": current_field }
    if details:
        ans.update( {
            "bso_classification_method": method,
            "bso_classification_pf_tags": format_pf_tags(pf_tags),
            "bso_classification_journal_top_categ": top_categ
        } )
    return ans


def bso_classify(elems, details = False):
    for e in elems:
        if 'title' in e:
            calc = get_discipline_calc(e['title'], e.get('journal_name'), details)
            e.update(calc)
    return elems
