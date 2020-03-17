from flask_restful import Resource, marshal_with
from http import HTTPStatus

from app.core.directory.directory import create_directory, update_directory, delete_directories
from app.rest_api.directory.parsers import (
    create_directory_parser,
    delete_directory_parser,
    update_directory_query_parser,
    update_directory_parser,
)
from app.rest_api.directory.schemas import directory_schema


class DirectoryResource(Resource):

    @marshal_with(directory_schema)
    def post(self):
        args = create_directory_parser.parse_args()
        result = create_directory(args)
        if result:
            return result, HTTPStatus.CREATED
        return 'Failed to create directory', HTTPStatus.INTERNAL_SERVER_ERROR

    def put(self):
        params = update_directory_query_parser.parse_args()
        query = update_directory_parser.parse_args()
        result = update_directory(query, params)
        if result:
            return 'Updated', HTTPStatus.OK
        return 'Failed to update directories', HTTPStatus.INTERNAL_SERVER_ERROR

    def delete(self):
        query = delete_directory_parser.parse_args()
        result = delete_directories(query)
        if result:
            return 'Deleted', HTTPStatus.NO_CONTENT
        return 'Failed to delete directories', HTTPStatus.INTERNAL_SERVER_ERROR
