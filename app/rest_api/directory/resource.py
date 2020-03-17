from flask_restful import Resource, marshal_with
from http import HTTPStatus

from app.core.directory.directory import create_directory
from app.rest_api.directory.parsers import create_directory_parser
from app.rest_api.directory.schemas import directory_schema


class DirectoryResource(Resource):

    @marshal_with(directory_schema)
    def post(self):
        args = create_directory_parser.parse_args()
        result = create_directory(args)
        if result:
            return result, HTTPStatus.CREATED
        return 'Failed to create directory', HTTPStatus.INTERNAL_SERVER_ERROR
