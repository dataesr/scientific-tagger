import time
import datetime
from project.server.main.pf_classifier import pf_classify
from project.server.main.bso_classifier import bso_classify
from project.server.main.asjc_classifier import asjc_classify

def create_task_classify(arg):
    classification = {}
    classification_type = arg.get('type', 'bso')
    publications = arg.get('publications', [])
    if len(publications) > 10000:
        classification['message'] = "More than 10.000 publications have been submitted. Only the first 10.000 are treated. Please split your request."
        publications = publications[0:10000]
    if classification_type == "pf":
        classification['publications'] = pf_classify(publications)
    elif classification_type == "bso":
        details = arg.get('details', False)
        classification['publications'] = bso_classify(publications, details)
    elif classification_type == "asjc":
        classification['publications'] = asjc_classify(publications)
    return classification
