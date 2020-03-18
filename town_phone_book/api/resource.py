from flask_restful import Resource

from .functions import get_arg_parser, create_new_directory, update_directory, delete_directory


class DirectoryResource(Resource):
    def get(self):
        return 404

    def post(self):
        parser = get_arg_parser(action='post')
        params = parser.parse_args()

        new_directory = create_new_directory(params)

        if new_directory:
            return '', 201
        else:
            return '', 500

    def put(self):
        parser = get_arg_parser(action='put')
        params = parser.parse_args()

        new_directory = update_directory(params)

        if new_directory:
            return '', 201
        else:
            return '', 500

    def delete(self):
        parser = get_arg_parser(action='delete')
        params = parser.parse_args()

        result = delete_directory(params)
        if result:
            return '', 201
        else:
            return '', 500


