from flask_restful.reqparse import RequestParser


create_directory_parser = RequestParser()
create_directory_parser.add_argument('first_name', type=str, required=True)
create_directory_parser.add_argument('last_name', type=str, required=True)
create_directory_parser.add_argument('phone_number', type=str, required=True)
create_directory_parser.add_argument('address', type=str, required=True)
create_directory_parser.add_argument('district', type=str, required=True)

update_directory_query_parser = RequestParser()
update_directory_query_parser.add_argument('first_name', type=str, required=False, location='args')
update_directory_query_parser.add_argument('last_name', type=str, required=False, location='args')
update_directory_query_parser.add_argument('phone_number', type=str, required=False, location='args')
update_directory_query_parser.add_argument('address', type=str, required=False, location='args')
update_directory_query_parser.add_argument('district', type=str, required=False, location='args')

update_directory_parser = RequestParser()
update_directory_parser.add_argument('first_name', type=str, required=False)
update_directory_parser.add_argument('last_name', type=str, required=False)
update_directory_parser.add_argument('phone_number', type=str, required=False)
update_directory_parser.add_argument('address', type=str, required=False)
update_directory_parser.add_argument('district', type=str, required=False)
