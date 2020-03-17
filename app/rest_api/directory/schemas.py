from flask_restful import fields

directory_schema = dict(
    first_name=fields.String,
    last_name=fields.String,
    phone_number=fields.String,
    address=fields.String,
    district=fields.String
)
