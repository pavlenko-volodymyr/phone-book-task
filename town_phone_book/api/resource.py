from flask_restful import Resource, reqparse
from town_phone_book import db
from town_phone_book.models import Directory


class DirectoryResource(Resource):
    def get(self):
        return 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("district", type=str, required=True)
        parser.add_argument("first_name", type=str, required=True)
        parser.add_argument("last_name", type=str, required=True)
        parser.add_argument("phone_number", type=str, required=True)
        parser.add_argument("address", type=str, required=True)

        params = parser.parse_args()
        try:
            new_directory = Directory(**params)
            db.session.add(new_directory)
            db.session.commit()
        except Exception as e:
            return None, 500

        return '', 201

