from flask_restful import Api
from town_phone_book import app
from town_phone_book.api.resource import DirectoryResource


api = Api(app)

api.add_resource(DirectoryResource, '/directory')
