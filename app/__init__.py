import os

from flask import Flask


ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_FOLDER = os.path.join(ROOT_FOLDER, 'frontend')
STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'frontend')

app = Flask(__name__, static_folder=STATIC_FOLDER,
            template_folder=TEMPLATE_FOLDER)

from app.rest_api import api
