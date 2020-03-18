from flask_restful import Resource

from .functions import get_arg_parser, create_new_directory, update_directory


class DirectoryResource(Resource):
    def get(self):
        return 404

    def post(self):
        parser = get_arg_parser()
        params = parser.parse_args()

        new_directory = create_new_directory(params)

        if new_directory:
            return '', 201
        else:
            return '', 500

    def put(self):
        parser = get_arg_parser()
        params = parser.parse_args()

        new_directory = update_directory(params)

        if new_directory:
            return '', 201
        else:
            return '', 500
