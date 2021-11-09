from project.server.main.asjc_classifier import asjc_classify 
from project.server.main.sdg.sdg import test_sdg
from project.server.main.utils_str import normalize

def sdg_classify(elems):
    elems = asjc_classify(elems)
    for e in elems:
        if ('title' not in e) and ('abstract' not in e) and ('keywords' not in e):
            continue
        if 'asjc_classification' not in e:
            continue
        asjc_list = [k['code_asjc'] for k in e['asjc_classification']]
        ti = get_str(e.get('title', ''))
        abs = get_str(e.get('abstract', ''))
        kw = get_str(e.get('keywords', ''))
        ti_abs_kw = f'{ti} {abs} {kw}'
        ti_abs_kw = normalize(ti_abs_kw.strip())
        calc = test_sdg(asjc_list, ti_abs_kw)
        e.update(calc)
    return elems
