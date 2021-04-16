import datetime
import requests
import shutil
import os
import re

from project.server.main.logger import get_logger

logger = get_logger(__name__)

def getFilename_fromCd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]

def download_file(url, destination):
    start = datetime.datetime.now()
    with requests.get(url, allow_redirects=True, stream=True) as r:
        r.raise_for_status()
        local_filename = url.split('/')[-1]
        #getFilename_fromCd(r.headers.get('content-disposition')).replace('"', '')
        logger.debug(f"start downloading {local_filename} at {start}", flush=True)
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f, length=16*1024*1024)
    os.system(f"mv {local_filename} {destination}{local_filename}")
    end = datetime.datetime.now()
    delta = end - start
    logger.debug(f"end download in {delta}", flush=True)
    return f"{destination}{local_filename}"
