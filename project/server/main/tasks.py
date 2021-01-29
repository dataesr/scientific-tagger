import time
import datetime
from project.server.main.pf_classifier import pf_classify
from project.server.main.bso_classifier import bso_classify

def create_task_classify(arg):
    classification = {}
    classification_type = arg.get('type', 'bso')
    publications = arg.get('publications', [])
    if classification_type == "pf":
        print("pf", flush=True)
        classification = pf_classify(publications)
    elif classification_type == "bso":
        print("bso", flush=True)
        classification = bso_classify(publications)
    print("classif", flush=True)
    print(classification, flush=True)
    return classification
