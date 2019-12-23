import os

from flask import Flask
from werkzeug.utils import import_string
from healthcheck import HealthCheck


# instantiate the extensions
health_live = HealthCheck()
health_ready = HealthCheck()

def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    cfg = import_string(app_settings)()
    app.config.from_object(cfg)

    # register blueprints
    from app.api.info import info_blueprint
    app.register_blueprint(info_blueprint)

    from app.api.uploads.views import upload_blueprint
    app.register_blueprint(upload_blueprint)

    # register healthchecks
    from app.api.uploads.health import demo_healthcheck
    health_live.add_check(demo_healthcheck)
    app.add_url_rule("/health/live", "healthcheck_live", view_func=lambda: health_live.run())

    from app.api.uploads.health import isready_healthcheck
    health_ready.add_check(isready_healthcheck)
    app.add_url_rule("/health/ready", "healthcheck_ready", view_func=lambda: health_ready.run())

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
