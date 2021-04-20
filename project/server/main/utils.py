import datetime
import requests
import shutil
import os
import re
import time

PV_MOUNT = "/src/local_data/"
os.system(f"mkdir -p {PV_MOUNT}")

def get_aggregate(collection, pipeline, output):
    url_upw = "http://unpaywall-web"
    r = requests.post(f"{url_upw}/aggregate_mongo", 
                      json={"pipeline": pipeline, "collection": collection, "output": output})
    task_id = r.json()["data"]["task_id"]
    print(f"task_id {task_id}", flush=True)
    for i in range(1, 50000):
        r_task = requests.get(f"{url_upw}/tasks/{task_id}").json()
        status = r_task.get('data', {}).get('task_status')
        if status not in ["finished", "failed"]:
            time.sleep(1)
        elif status == "finished":
            results = r_task.get('data', {}).get('task_result', [])
            return results
        elif status == "failed":
            return None
    return None

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
    os.system(f"mkdir -p {PV_MOUNT}")
    start = datetime.datetime.now()
    with requests.get(url, allow_redirects=True, stream=True) as r:
        r.raise_for_status()
        try:
            local_filename = getFilename_fromCd(r.headers.get('content-disposition')).replace('"', '')
        except:
            local_filename = url.split('/')[-1]
        print(f"start downloading {local_filename} at {start}", flush=True)
        #local_filename = f"{PV_MOUNT}{local_filename}"
        local_filename = destination
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f, length=16*1024*1024)
    end = datetime.datetime.now()
    delta = end - start
    print(f"end download in {delta}", flush=True)
    return f"{local_filename}"
