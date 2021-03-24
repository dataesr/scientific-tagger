from project.server.main.utils import download_file
import json
import os
import re

os.system("mkdir -p /src/models")
if os.path.exists("/src/models/asjc.json") is False:
    download_file("https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/models/asjc.json", "/src/models/")
asjc_data = json.load(open('/src/models/asjc.json', 'r'))

asjc_dict = {}
for e in asjc_data:
    if e.get('issn'):
        asjc_dict[e.get('issn')] = e

def asjc_classify(elems, details = False):
    for e in elems:
        if 'issn_list' not in e:
            if 'journal_issns' in e:
                issns = e['journal_issns']
                if not isinstance(issns, str):
                    continue
                issn_list = [k.strip() for k in re.split(",|;", issns)]
                e['issn_list'] = [k for k in issn_list if len(k)>0]
            else:
                continue
        res = []
        for issn in e['issn_list']:
            if issn in asjc_dict:
                if asjc_dict[issn]['asjc'] not in res:
                    res += asjc_dict[issn]['asjc']
        calc = {'asjc_classification': res}
        e.update(calc)
    return elems
