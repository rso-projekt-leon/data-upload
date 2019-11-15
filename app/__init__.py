import os

from flask import Flask


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # register blueprints
    from app.api.info import info_blueprint
    app.register_blueprint(info_blueprint)

    from app.api.uploads.views import upload_blueprint
    app.register_blueprint(upload_blueprint)

 
    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
