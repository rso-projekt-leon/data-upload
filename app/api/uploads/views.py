import os
import requests
import json

from flask import Blueprint, request
from flask import current_app as app
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

upload_blueprint = Blueprint("upload", __name__)
api = Api(upload_blueprint)


def allowed_file(file):
    filename = file.filename
    # We only want files with a . in the filename
    if not "." in filename:
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
        catalog_url = app.config['DATA_CATALOG_URL'] + '/v1/datasets'
        headers = {'Content-type': 'application/json'}
        r_catalog = requests.post(catalog_url, data=json.dumps(catalog_post_data), headers=headers)
        print(r_catalog.text)
        return r_catalog.status_code

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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_size = os.path.getsize(os.path.join(app.config['UPLOAD_FOLDER'], filename))/(1024*1024)
            num_lines = sum(1 for line in open(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
            print(filename, file_size, num_lines)
            dataset_name = file.content_type
            #doadaj file na storage, če je uspelo shrani v bazo
            status = update_data_catalog_info(dataset_name, filename, file_size, num_lines)
            if status == 201:
                return {'message' : 'File successfully uploaded'}, 201
            else:
                return {'message' : 'Error adding file info to database.'}, 400
        else:
            return {'message' : 'Allowed file type is .csv'}, 400

api.add_resource(UploadFile, "/v1/upload")
