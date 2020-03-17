from flask_restful import Resource, marshal_with
from http import HTTPStatus

from app.core.directory.directory import create_directory, update_directory, delete_directories
from app.decorators import response_wrapper
from app.rest_api.directory.parsers import (
    create_directory_parser,
    delete_directory_parser,
    update_directory_query_parser,
    update_directory_parser,
)
from app.rest_api.directory.schemas import directory_schema


class DirectoryResource(Resource):

    @marshal_with(directory_schema)
    @response_wrapper('Failed to create directory', HTTPStatus.CREATED)
    def post(self):
        args = create_directory_parser.parse_args()
        result = create_directory(args)
        return result

    @response_wrapper('Failed to update directory', HTTPStatus.OK)
    def put(self):
        params = update_directory_query_parser.parse_args()
        query = update_directory_parser.parse_args()
        result = update_directory(query, params)
        return result

    @response_wrapper('Failed to delete directory', HTTPStatus.NO_CONTENT)
    def delete(self):
        query = delete_directory_parser.parse_args()
        result = delete_directories(query)
        return result
