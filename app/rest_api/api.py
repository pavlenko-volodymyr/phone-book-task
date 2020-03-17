from flask_restful import Api

from app import app
from app.rest_api.directory.resource import DirectoryResource

api = Api(app)

api.add_resource(DirectoryResource, '/directory')
