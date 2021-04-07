import string, re
import pickle
from project.server.main.FoR import set_FoR
from project.server.main.utils import download_file, get_aggregate
from project.server.main.utils_swift import upload_object, download_object
import pandas as pd
import fasttext
from sklearn.model_selection import train_test_split
from project.server.main.utils_str import normalize
import os

PV_MOUNT = "/src/local_data/"
os.system(f"mkdir -p {PV_MOUNT}")

def calibrate_pubmed():
    try:
        issn_dict_health = pickle.load(open(f"{PV_MOUNT}issn_dict_health.pkl", "rb"))
        assert(len(issn_dict_health)>1000)
    except:
        set_FoR()
    issn_dict_health = pickle.load(open(f"{PV_MOUNT}issn_dict_health.pkl", "rb"))
    calibrate("pubmed", issn_dict_health)

def dualize_dict(input_dict):
    new_dict = {}
    for k in input_dict:
        for e in input_dict[k]:
            if e not in new_dict:
                new_dict[e] = []
            if k not in new_dict[e]:
                new_dict[e].append(k)
    return new_dict

def calibrate(collection, issn_map):
    sampling_size = 1000 # per category

    field_map = dualize_dict(issn_map)
    data_field = []
    for field in field_map:
        issns = field_map[field]
        pipeline = [
            {
            "$match": {
            "$or": [
                { "issn_electronic": { "$in": issns}},
                { "issn_print": { "$in": issns}} ]
            }
        },
        { "$sample": { "size": sampling_size } },
        {
            "$project": {
                "_id": 0, "title": 1, "abstract": 1, "keywords": 1, "issn_electronic": 1, "issn_print": 1, "mesh_headings": 1, "journal_title": 1
            }
        }
        ]

        url_data = get_aggregate(collection, pipeline, field)
        sample_data = f"{PV_MOUNT}sample_data.json"
        download_object("tmp", url_data.split('/')[-1], sample_data)
        data_field.append(pd.read_json(sample_data, orient="records", lines=True).to_dict(orient='records'))

    data = pd.concat(data_field)
    print("len data = "+str(len(data)), flush=True)
    print("len issn_map = "+str(len(issn_map)), flush=True)
    for elt in data:
        if '_id' in elt:
            del elt['_id']
        current_label_text = []
        #current_label_text_global = []
        for issn_type in ['issn_electronic', 'issn_print']:
            issn = elt[issn_type]
            if issn in issn_map:
                current_label_text += issn_map[issn][0:1]

        current_label_text = list(set(current_label_text))

        elt["labels_text"] = current_label_text

    data_with_label = [ e for e in data if len(e['labels_text'])]

    data_train, data_test = train_test_split(data_with_label, test_size = 0.1)

    for data_type in ["train", "test"]:
        print(data_type, flush=True)
        outfile = {}
        for f in ['title', 'abstract', 'keywords', 'mesh_headings', 'journal_title']:
            outfile[f] = open(f"{PV_MOUNT}{collection}_{data_type}_{f}.txt", "w")
            outfile[f].close()

        for f in ['title', 'abstract', 'keywords', 'mesh_headings', 'journal_title']:
            outfile = open(f"{PV_MOUNT}{collection}_{data_type}_{f}.txt", "a+")
            print(f, flush=True)

            if data_type == "train":
                current_data = data_train
            else:
                current_data = data_test

            for ix, elt in enumerate(current_data):
                if ix % 100000 == 0:
                    print(ix, end=',', flush=True)

                current_words = elt.get(f)
                if current_words is None:
                    continue

                if isinstance(current_words, list):
                    current_words = " ".join(current_words)

                if f == "abstract" and len(current_words.split(" ")) < 20:
                    continue
                if f == "title" and len(current_words.split(" ")) < 10:
                    continue

                current_words = normalize(current_words)

                labels = ["__label__" + label.replace(' ','_') for label in elt.get('labels_text', [])]

                tags = " ".join(labels)

                newline = current_words + " " + tags + "\n"

                outfile.write(newline)
            outfile.close()
            print(flush=True)

    for f in ['journal_title', 'title', 'abstract', 'keywords', 'mesh_headings']:
        print("training "+f, flush=True)

        model = fasttext.train_supervised(f'{PV_MOUNT}{collection}_train_{f}.txt',
                                       wordNgrams = 2,
                                       lr = 0.05,
                                       minCount = 100,
                                       dim = 10,
                                      # pretrainedVectors = "wiki-news-300d-1M.vec",
                                       epoch = 25)
        model_filename = f"{PV_MOUNT}{collection}_model_{f}.model"
        model.save_model(model_filename)
        upload_object("models", model_filename)        

        print(model.test(f'{PV_MOUNT}{collection}_test_{f}.txt'), flush=True)
        print(model.test_label(f'{PV_MOUNT}{collection}_test_{f}.txt'), flush=True)
        print(flush = True)
        print("*************", flush=True)
        print(flush=True)


