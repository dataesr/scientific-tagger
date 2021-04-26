import string, re
import pickle
from project.server.main.FoR import set_FoR
from project.server.main.utils import download_file, get_aggregate
from project.server.main.utils_swift import conn, upload_object, download_object
import pandas as pd
import fasttext
from sklearn.model_selection import train_test_split
from project.server.main.utils_str import normalize
import os
from project.server.main.logger import get_logger

logger = get_logger(__name__)

PV_MOUNT = "/src/local_data/"
os.system(f"mkdir -p {PV_MOUNT}")

def calibrate_pubmed(is_stratified, sample_data_file):
    try:
        issn_dict_health = pickle.load(open(f"{PV_MOUNT}issn_dict_health.pkl", "rb"))
        assert(len(issn_dict_health)>1000)
    except:
        logger.debug("getting FoR")
        set_FoR()
    issn_dict_health = pickle.load(open(f"{PV_MOUNT}issn_dict_health.pkl", "rb"))

    calibrate("pubmed", issn_dict_health, is_stratified, sample_data_file = sample_data_file)

def dualize_dict(input_dict, is_global):
    new_dict = {}
    for k in input_dict:
        for e in input_dict[k]:
            current_key = e
            if is_global:
                current_key = 'global'
            if current_key not in new_dict:
                new_dict[current_key] = []
            if k not in new_dict[current_key]:
                new_dict[current_key].append(k)
    return new_dict

def sample(collection, issn_map, is_stratified):
    if is_stratified:
        sampling_size = 50000 # per category
        field_map = dualize_dict(issn_map, is_global = False)
    else:
        sampling_size = 1000000
        field_map = dualize_dict(issn_map, is_global = True)
    data_field = []
    tmp_file_to_del = []
    sample_data = f"{PV_MOUNT}sample_data_{collection}_strat{is_stratified}_{sampling_size}.json"
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
        url_data = get_aggregate(collection, pipeline, field.replace(' ',''))
        tmp_file_to_del.append(url_data.split('/')[-1])
        layer_data = f"{PV_MOUNT}layer_data.json"
        download_object("tmp", url_data.split('/')[-1], layer_data)
        os.system(f"cat {layer_data} >> {sample_data}")
        os.system(f"rm -rf {layer_data}")
        #data_field.append(pd.read_json(sample_data, orient="records", lines=True).to_dict(orient='records'))
    #data = pd.concat(data_field)
    upload_object("sampling", sample_data)        


    for f in tmp_file_to_del:
        conn.delete_object("tmp", f)

    return sample_data


def calibrate(collection, issn_map, is_stratified, sample_data_file = None):
    if sample_data_file is None:
        sample_data = sample(collection, issn_map, is_stratified)
    else:
        sample_data = f"{PV_MOUNT}{sample_data_file}"
        download_object("sampling", sample_data_file, sample_data)
    data = pd.read_json(sample_data, orient="records", lines=True).to_dict(orient='records')
    #download_object("tmp", sample_data.split('/')[-1], sample_data)
    logger.debug("len data = "+str(len(data)))
    logger.debug("len issn_map = "+str(len(issn_map)))
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
        logger.debug(data_type)
        outfile = {}
        for f in ['title', 'abstract', 'keywords', 'mesh_headings', 'journal_title']:
            outfile[f] = open(f"{PV_MOUNT}{collection}_{data_type}_{f}.txt", "w")
            outfile[f].close()

        for f in ['title', 'abstract', 'keywords', 'mesh_headings', 'journal_title']:
            outfile[f] = open(f"{PV_MOUNT}{collection}_{data_type}_{f}.txt", "a+")
            logger.debug(f)

            if data_type == "train":
                current_data = data_train
            else:
                current_data = data_test

            for ix, elt in enumerate(current_data):
                if ix % 100000 == 0:
                    logger.debug(ix)

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

                current_words = normalize(current_words)

                labels = ["__label__" + label.replace(' ','_') for label in elt.get('labels_text', [])]

                tags = " ".join(labels)

                newline = current_words + " " + tags + "\n"

                outfile[f].write(newline)
            outfile[f].close()

    for f in ['journal_title', 'title', 'abstract', 'keywords', 'mesh_headings']:
        logger.debug("training "+f)

        model = fasttext.train_supervised(f'{PV_MOUNT}{collection}_train_{f}.txt',
                                       wordNgrams = 2,
                                       minCount = 20,
                                       loss='ova',
                                      # pretrainedVectors = "wiki-news-300d-1M.vec",
                                       epoch = 50)
        model_filename = f"{PV_MOUNT}{collection}_model_{f}_strat{is_stratified}.model"
        model.save_model(model_filename)
        upload_object("models", model_filename)        

        test = model.test(f'{PV_MOUNT}{collection}_test_{f}.txt', k=-1, threshold=0.5)
        precision = test[1]
        recall = test[2]
        f1 = 2*(recall * precision) / (recall + precision)
        logger.debug(f"precision: {precision}, recall: {recall}, f1: {f1}")


