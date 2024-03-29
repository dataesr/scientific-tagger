import swiftclient
import json
import pandas as pd
import gzip
from io import BytesIO, TextIOWrapper
import os

from project.server.main.logger import get_logger

logger = get_logger(__name__)

user = "{}:{}".format(os.getenv("OS_TENANT_NAME"), os.getenv("OS_USERNAME"))
key = os.getenv("OS_PASSWORD")
project_id = os.getenv("OS_TENANT_ID")
project_name = os.getenv("OS_PROJECT_NAME")

#user=":"
#key=""
#project_id=""
#project_name="Alvitur"

conn = swiftclient.Connection(
    authurl='https://auth.cloud.ovh.net/v3',
    user=user,
    key=key,
    os_options={
            'user_domain_name': 'Default',
            'project_domain_name': 'Default',
            'project_id':project_id,
            'project_name': project_name,
            'region_name':'GRA'},
    auth_version='3'
    )

def upload_object(container, filename):
    object_name = filename.split('/')[-1]
    logger.debug(f"uploading {filename} in {container} as {object_name}")
    cmd = f"swift --os-auth-url https://auth.cloud.ovh.net/v3 --auth-version 3\
      --key {key} --user {user} \
      --os-user-domain-name Default \
      --os-project-domain-name Default \
      --os-project-id {project_id} \
      --os-project-name {project_name} \
      --os-region-name GRA"
    cmd = cmd + f" upload {container} {filename} --object-name {object_name}"
    cmd += " --segment-size 1048576000 --segment-threads 100"
    os.system(cmd)
    return f"https://storage.gra.cloud.ovh.net/v1/AUTH_{project_id}/{container}/{object_name}"

def download_object(container, filename, out):
    logger.debug(f"downloading {filename} from {container} to {out}")
    cmd = f"swift --os-auth-url https://auth.cloud.ovh.net/v3 --auth-version 3\
      --key {key} --user {user} \
      --os-user-domain-name Default \
      --os-project-domain-name Default \
      --os-project-id {project_id} \
      --os-project-name {project_name} \
      --os-region-name GRA"
    cmd = cmd + f" download {container} {filename} -o {out}"
    os.system(cmd)

def exists_in_storage(container, filename):
    try:
        conn.head_object(container, filename)
        return True
    except:
        return False
    
def get_objects(container, path):
    try:
        df = pd.read_json(BytesIO(conn.get_object(container, path)[1]), compression='gzip')
    except:
        df = pd.DataFrame([])
    return df.to_dict("records")
    
def set_objects(all_objects, container, path):
    logger.debug(f"setting object {container} {path}",end=':')
    if isinstance(all_objects, list):
        all_notices_content = pd.DataFrame(all_objects)
    else:
        all_notices_content = all_objects
    gz_buffer = BytesIO()
    with gzip.GzipFile(mode='w', fileobj=gz_buffer) as gz_file:
        all_notices_content.to_json(TextIOWrapper(gz_file, 'utf8'), orient='records')
    conn.put_object(container, path, contents=gz_buffer.getvalue())
    logger.debug(f"done",end=':')
    return


def delete_folder(cont_name, folder):
    cont = conn.get_container(cont_name)
    for n in [e['name'] for e in cont[1] if folder in e['name']]:
        logger.debug(n)
        conn.delete_object(cont_name, n)
