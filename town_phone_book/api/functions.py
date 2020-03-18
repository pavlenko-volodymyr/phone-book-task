from flask_restful import Resource, reqparse
from town_phone_book import db
from town_phone_book.models import Directory


def get_arg_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("district", type=str, required=True)
    parser.add_argument("first_name", type=str, required=True)
    parser.add_argument("last_name", type=str, required=True)
    parser.add_argument("phone_number", type=str, required=True)
    parser.add_argument("address", type=str, required=True)

    return parser


def create_new_directory(kwargs):
    try:
        new_directory = Directory(**kwargs)
        db.session.add(new_directory)
        db.session.commit()
    except Exception as e:
        return None

    return new_directory
