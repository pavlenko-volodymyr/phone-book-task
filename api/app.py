from flask import Flask
from flask import jsonify
from flask import make_response
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from flask_restful import reqparse
from flask_restful import Api


app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
api = Api(app)

db.create_all()

create_phone_book_parser = reqparse.RequestParser()
create_phone_book_parser.add_argument('first_name',
                            help='This field cannot be blank',
                            required=True)
create_phone_book_parser.add_argument('last_name',
                            help='This field cannot be blank',
                            required=True)
create_phone_book_parser.add_argument('telephone',
                            help='This field cannot be blank',
                            required=True)
create_phone_book_parser.add_argument('address',
                            help='This field cannot be blank',
                            required=True)

update_phone_book_parser = reqparse.RequestParser()
update_phone_book_parser.add_argument('first_name',
                            help='This field cannot be blank',
                            required=False)
update_phone_book_parser.add_argument('last_name',
                            help='This field cannot be blank',
                            required=False)
update_phone_book_parser.add_argument('telephone',
                            help='This field cannot be blank',
                            required=False)
update_phone_book_parser.add_argument('address',
                            help='This field cannot be blank',
                            required=False)

get_phone_book_parser = reqparse.RequestParser()
get_phone_book_parser.add_argument('district',
                            help='This field cannot be blank',
                            required=False)


class PhoneBook(db.Model):
	__tablename__ = "phone_books"

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(128), nullable=False)
	last_name = db.Column(db.String(128), nullable=False)
	telephone = db.Column(db.String(128), nullable=False)
	address = db.Column(db.String(128), nullable=False)


	def __init__(self, first_name, last_name, telephone, address):
		self.first_name = first_name
		self.last_name = last_name
		self.telephone = telephone
		self.address = address

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()


class AbstractBookResource(Resource):
	def _phone_book_to_dict(self, phone_book):
		return {
			'id': phone_book.id,
			'first_name': phone_book.first_name,
			'last_name': phone_book.last_name,
			'address': phone_book.address,
			'telephone': phone_book.telephone
		}

class PhoneBookListResource(AbstractBookResource):
	def post(self):
		data = create_phone_book_parser.parse_args()
		phone_book = PhoneBook(data.first_name, data.last_name, data.telephone, data.address)
		phone_book.save_to_db()

		return jsonify(self._phone_book_to_dict(phone_book))

	def get(self):
		data = get_phone_book_parser.parse_args()
		district = data.district

		if district:
			result_query = db.session.query(PhoneBook) \
				.filter(PhoneBook.address.like('%{}%'.format(district))).all()
		else:
			result_query = db.session.query(PhoneBook).all()

		result = []

		for phone_book in result_query:
			result.append(self._phone_book_to_dict(phone_book))

		return jsonify(result)


class PhoneBookResource(AbstractBookResource):
	def get(self, id):
		phone_book = PhoneBook.query.get(id)

		if not phone_book:
			return make_response(jsonify({
				'error': 'Model not found.'
				}), 404)

		return jsonify(self._phone_book_to_dict(phone_book))

	def delete(self, id):
		phone_book = PhoneBook.query.get(id)

		if not phone_book:
			return make_response(jsonify({
				'error': 'Model not found.'
				}), 404)

		phone_book.delete_from_db()

		return jsonify({
			'status': 'success'
			})

	def put(self, id):
		phone_book = PhoneBook.query.get(id)
		data = create_phone_book_parser.parse_args()

		if not phone_book:
			return make_response(jsonify({
				'error': 'Model not found.'
				}), 404)

		first_name = data.first_name
		last_name = data.last_name
		telephone = data.telephone
		address = data.address

		if first_name:
			phone_book.first_name = first_name

		if last_name:
			phone_book.last_name = last_name

		if telephone:
			phone_book.telephone = telephone

		if address:
			phone_book.address = address

		phone_book.save_to_db()

		return jsonify(self._phone_book_to_dict(phone_book))


api.add_resource(PhoneBookListResource, '/api/v1/directories')
api.add_resource(PhoneBookResource, '/api/v1/directories/<int:id>')


if __name__ == '__main__':
	# To run it manually
	app.run(port=5001)