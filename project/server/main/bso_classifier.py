import fasttext
from collections import Counter
from project.server.main.utils_str import normalize_text
from project.server.main.bso_category import get_bso_category
from project.server.main.pf_classifier import get_pf_label
from project.server.main.utils import download_file
import pickle
from os import path

if path.exists("/models/all_categ_revue.pkl") is False:
    download_file("https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/models/all_categ_revue.pkl", "/models/")
all_categ_revue = pickle.load(open('/models/all_categ_revue.pkl', 'rb'))

def get_categ_from_source(source):
    try:
        mst_common = Counter(all_categ_revue[source]).most_common()
        if mst_common[0][0] == 'unknown':
            ans = mst_common[1][0] # the 2nd most common
        else:
            ans = mst_common[0][0] # the most common

    except:
        ans = 'unknown'
    return ans

def get_discipline_calc(title, journal_name):
    current_field = "unknown"
    if isinstance(title, str) and len(title)>0:
        prediction_pf = get_pf_label(title)
        current_field = get_bso_category(prediction_pf)

    if current_field == "unknown":
        current_field = get_categ_from_source(journal_name)
    if current_field == 'unknown' and isinstance(title, str) and len(title)>0:
        prediction_pf_2 = get_pf_label(title, nb_top = 10)
        current_field = get_bso_category(prediction_pf_2, is_strict=False)
    return current_field


def bso_classify(elems):
    for e in elems:
        if 'doi' in e and 'title' not in e or 'journal_name' not in e:
            #e = enrich_metadata(e)
            continue

        if 'title' in e and 'journal_name' in e:
            bso_field = get_discipline_calc(e['title'], e['journal_name'])
            e['bso_classification'] = bso_field
    return elems
