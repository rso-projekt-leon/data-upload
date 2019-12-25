import os
import logging

from flask import Flask
from werkzeug.utils import import_string
from healthcheck import HealthCheck
from prometheus_client import make_wsgi_app
from flask_prometheus_metrics import register_metrics
from werkzeug.middleware.dispatcher import DispatcherMiddleware

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

    #logging
    if __name__ != '__main__':
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

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


def create_metrics(app):
    app_mode = os.getenv("FLASK_ENV")
    register_metrics(app, app_version="v1.4.151", app_config=app_mode)
    dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})
    return dispatcher
