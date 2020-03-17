import json
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


with open(os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'config/config.json', ))) as f:
    config = json.load(f)

engine = create_engine('sqlite:///home/serhii/directory.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
