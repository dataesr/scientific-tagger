import pandas as pd
import pickle
from project.server.main.utils import download_file
import os

PV_MOUNT = "/src/local_data/"
os.system(f"mkdir -p {PV_MOUNT}")

for_code_health = [
 '1103',
 '1117',
 '0601',
 '1109',
 '1115',
 '1112',
 '1102',
 '1114',
 '0605',
 'MD',
 '03',
 '02',
 '17',
 '09',
 '07']

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
        if len(for_code) not in [2, 4]:
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
            elif for_code[0:2] in for_code_health:
                fors_health.append(for_dict[for_code[0:2]])
            elif for_code[0:2] in ["06", "11"]:
                fors_health.append("Other "+ for_dict[for_code[0:2]])

        for issn in issns:
            issn_dict[issn] = fors

            if len(fors_health)>0:
                issn_dict_health[issn] = fors_health

    pickle.dump(issn_dict_health, open(f"{PV_MOUNT}issn_dict_health.pkl", "wb"))
    pickle.dump(issn_dict, open(f"{PV_MOUNT}issn_dict.pkl", "wb"))
