from flask import Blueprint
from flask_restful import Api, Resource

info_blueprint = Blueprint("info", __name__)
api = Api(info_blueprint)


class Info(Resource):
    def get(self):
        return {"clani": ["ls4262"],
                "opis_projekta": "Projekt implementira platformo za podatkovno analizo.",
                "mikrostoritve": ["http://35.195.92.163:8082/v1/buckets/"],
                "github": ["https://github.com/rso-projekt-leon/data-upload", 
                           "https://github.com/rso-projekt-leon/data-storage-service",
                           "https://github.com/rso-projekt-leon/data-catalog",
                           "https://github.com/rso-projekt-leon/documentation"],
                "travis": ["https://travis-ci.org/rso-projekt-leon/data-upload",
                           "https://travis-ci.org/rso-projekt-leon/data-storage-service"],
                "dockerhub": ["https://hub.docker.com/repository/docker/leon11sj/data-storage-microservice",
                              "https://hub.docker.com/repository/docker/leon11sj/data-upload-microservice"]
                }, 200


api.add_resource(Info, "/v1/demo/info")