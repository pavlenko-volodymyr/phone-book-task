from flask_restful import abort
from http import HTTPStatus


def response_wrapper(error_message, success_code):
    def base(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            if result:
                return result, success_code
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=error_message)
        return wrap
    return base
