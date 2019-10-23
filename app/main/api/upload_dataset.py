import os
from flask import request
from flask import current_app as app
from werkzeug.utils import secure_filename
from flask_restful import Resource

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

class UploadFile(Resource):
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
            return {'message' : 'File successfully uploaded'}, 201
        else:
            return {'message' : 'Allowed file type is .csv'}, 400
