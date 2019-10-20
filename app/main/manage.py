import os
import unittest
from flask_restful import Api

from api.upload_dataset import UploadFile

from app import create_app


app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
api = Api(app)

api.add_resource(UploadFile, '/file-upload')

# app.app_context().push()

#manager = Manager(app)

#migrate = Migrate(app, db)

#manager.add_command('db', MigrateCommand)

# @manager.command
# def run():
#     app.run()

# @manager.command
# def test():
#     """Runs the unit tests."""
#     tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1

if __name__ == '__main__':
    app.run()