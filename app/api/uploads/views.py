import os
import requests
import json

from flask import Blueprint, request
from flask import current_app as app
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

from app.config import get_etcd_config

upload_blueprint = Blueprint("upload", __name__)
api = Api(upload_blueprint)


def allowed_file(file):
    filename = file.filename
    # We only want files with a . in the filename
    if not "." in filename:
        return False
    
    if " " in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_EXTENSIONS
    if ext.lower() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False 

def update_data_catalog_info(dataset_name, file_name, file_size, num_lines):
        # catalog microservice
        catalog_post_data = {
                    "dataset_lenght": num_lines,
                    "dataset_size": file_size,
                    "dataset_name": dataset_name,
                    "file_name": file_name,
                    }

        catalog_adderss = get_etcd_config('/data-upload/catalog-url', 'DATA_CATALOG_URL')         
        catalog_url = catalog_adderss + '/v1/datasets'
        headers = {'Content-type': 'application/json'}
        try:
            r_catalog = requests.post(catalog_url, data=json.dumps(catalog_post_data), headers=headers)
            return r_catalog.status_code
        except:
            return 400

def save_file_to_s3(file, filename, dataset_name):
    files = {'file': (filename, file.read(), dataset_name)}
    data_storage_url = get_etcd_config('/data-upload/storage-url', 'DATA_STORAGE_URL')  + '/v1/files'
    try:
        r_data_storage = requests.post(data_storage_url, files=files)
        return (r_data_storage.text, r_data_storage.status_code)
    except:
        return ('data_storage_service not aviable', 400)

class UploadFile(Resource):
    def get(self):
        response_object = {
                    "status": "success",
                    "message" : "Upload service up."
                }
        return response_object, 200

    def post(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            return {'message' : 'No file part in the request'}, 400

        file = request.files['file'] 
    
        # Ensuring the file has a name
        if file.filename == '':
            return {'message' : 'No file selected for uploading'}, 400

        # Ensuring the file type is allowed
        # Ensuring the filename is allowed
        # Ensuring the filesize is allowed
        if allowed_file(file):
            filename = secure_filename(file.filename)
            dataset_name = file.content_type

            # preveri ali ima dataset name presledke
            if " " in dataset_name:
                return {'message' : 'Error: Dataset name has spaces.'}, 400

            # preveri ali datasename že obstaja
            try:
                catalog_adderss = get_etcd_config('/data-upload/catalog-url', 'DATA_CATALOG_URL')         
                catalog_url = f'{catalog_adderss}/v1/datasets/{dataset_name}'
                dataset_status = requests.get(catalog_url)
            except:
                return {'message' : 'Error saving fail. (error connecting to data-catalog)'}, 400

            if dataset_status.status_code == 404:
                s3_message, s3_status_code = save_file_to_s3(file, filename, dataset_name)
                if s3_status_code == 201:
                    file.seek(0) # postavimo file nazaj na začetek
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    file_size = os.path.getsize(file_path)/(1024*1024)
                    num_lines = sum(1 for line in open(file_path))
                    catalog_update_status = update_data_catalog_info(dataset_name, filename, file_size, num_lines)
                    if catalog_update_status == 201:
                        return {'message' : 'File successfully uploaded'}, 201
                    else:
                        return {'message' : 'Error adding file info to database.'}, 400
                    try:
                        os.remove(file_path)
                    except:
                        print('Error deleting file.') # add to log
                else:
                    return {'message' : s3_message}, 400
            else:
                return {'message' : 'Dataset name already used.'}, 400
        else:
            return {'message' : 'Allowed file type is .csv'}, 400

api.add_resource(UploadFile, "/v1/upload")
