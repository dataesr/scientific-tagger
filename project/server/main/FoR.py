import pandas as pd
import pickle
from project.server.main.utils import download_file
import os

PV_MOUNT = "/src/local_data/"
os.system(f"mkdir -p {PV_MOUNT}")

for_code_health = ['0304',
 '0601',
 '0604',
 '0605',
 '0606',
 '0903',
 '1003',
 '1004',
 '1101',
 '1102',
 '1103',
 '1104',
 '1105',
 '1106',
 '1107',
 '1108',
 '1109',
 '1110',
 '1111',
 '1112',
 '1113',
 '1114',
 '1115',
 '1116',
 '1117',
 '1701',
 'MD']

def set_FoR():

    #curl https://www.arc.gov.au/file/10549/download?token=Sbfb2a9n #-O FoR.xlsx
    FoR_file = download_file("https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/models/FoR.xlsx", f"{PV_MOUNT}FoR.xlsx")

    xl = pd.ExcelFile(FoR_file)

    df_issn = xl.parse("ERA 2018 Journal List")
    df_for = xl.parse("FoR Codes")
    for_dict = {}
    for i, row in df_for.iterrows():
        for_code = str(row['FoR Code']).strip()
        if len(for_code) == 1:
            for_code = "0"+for_code
        if len(for_code) == 3:
            for_code = "0"+for_code
        if len(for_code) != 4:
            continue
        for_dict[for_code] = row['FoR Description'].strip()

    for_dict['MD'] = "Multidisciplinary"

    issn_dict = {}
    issn_dict_health = {}

    for i, row in df_issn.iterrows():
        issns = []
        for x in range(1,8):
            issn = row['ISSN {}'.format(x)]
            if not pd.isnull(issn):
                issns.append(issn)

        fors = []
        fors_health = []
        for x in range(1,4):
            for_code = row['FoR {}'.format(x)]
            if pd.isnull(for_code):
                continue
            for_code = str(for_code).replace('.0', '')

            if len(for_code) == 1:
                for_code = "0"+for_code
            if len(for_code) == 3:
                for_code = "0"+for_code

            if for_code not in for_dict:
                continue
            fors.append(for_dict[for_code])

            if for_code in for_code_health:
                fors_health.append(for_dict[for_code])

        for issn in issns:
            issn_dict[issn] = fors

            if len(fors_health)>0:
                issn_dict_health[issn] = fors_health

    pickle.dump(issn_dict_health, open(f"{PV_MOUNT}issn_dict_health.pkl", "wb"))
    pickle.dump(issn_dict, open(f"{PV_MOUNT}issn_dict.pkl", "wb"))
