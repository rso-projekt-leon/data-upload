
import sys

from flask.cli import FlaskGroup

from app import create_app, create_metrics


app = create_app()
dispatcher = create_metrics(app)
cli = FlaskGroup(create_app=create_app)


if __name__ == '__main__':
    cli()