from flask_restful import reqparse
from town_phone_book import db
from town_phone_book.models import Directory


def get_arg_parser(action='post'):
    parser = reqparse.RequestParser()
    if action in ('put', 'delete'):
        parser.add_argument("id", type=int, required=True)

    if action in ('post', 'put'):
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


def update_directory(kwargs):
    directory_id = kwargs.pop('id', None)

    if not directory_id:
        return None
    else:
        try:
            new_directory = Directory.query.filter_by(id=directory_id).\
                update(kwargs)
            db.session.commit()
        except Exception as e:
            return None

    return new_directory


def delete_directory(kwargs):
    directory_id = kwargs.pop('id', None)

    if not directory_id:
        return None
    else:
        directory = Directory.query.filter_by(id=directory_id).first()
        if directory:
            try:
                db.session.delete(directory)
                db.session.commit()
            except Exception as e:
                return None
        # if directory not found, it is not present in DB
        # required result obtained =)
    return True

