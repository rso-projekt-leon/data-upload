from flask import Blueprint
from flask_restful import Api, Resource
from app.log_app import info_log
from flask import current_app as app

info_blueprint = Blueprint("info", __name__)
api = Api(info_blueprint)

class Info(Resource):
    def get(self):
        info_log(app, 'Info get', 'ENTRY ', 'method call')
        info_log(app, 'Info get', 'EXIT ', 'method call')
        return {"clani": ["ls4262"],
                "opis_projekta": "Projekt implementira platformo za podatkovno analizo.",
                "mikrostoritve": ["https://35.195.92.163/data-storage/v1/buckets/", 
                                  "https://35.195.92.163/data-upload/v1/upload"],
                "github": ["https://github.com/rso-projekt-leon/data-upload", 
                           "https://github.com/rso-projekt-leon/data-storage-service",
                           "https://github.com/rso-projekt-leon/data-catalog",
                           "https://github.com/rso-projekt-leon/documentation",
                           "https://github.com/rso-projekt-leon/rso-k8s"],
                "travis": ["https://travis-ci.org/rso-projekt-leon/data-upload",
                           "https://travis-ci.org/rso-projekt-leon/data-storage-service"],
                "dockerhub": ["https://hub.docker.com/repository/docker/leon11sj/data-storage-microservice",
                              "https://hub.docker.com/repository/docker/leon11sj/data-upload-microservice"]
                }, 200


api.add_resource(Info, "/v1/demo/info")