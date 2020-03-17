from app.database import session
from app.models.directory.directory import Directory
from sqlalchemy import update


def create_directory(args):
    try:
        item = Directory(**args)
        session.add(item)
        session.commit()
        return item
    except Exception:
        return False


def update_directory(query, params):
    try:
        item = update(Directory).where(**params).values(**query)
        session.execute(item)
        session.commit()
        return 'Updated'
    except Exception:
        return False


def delete_directories(query):
    try:
        directories = Directory.query.filter(**query).all()
        session.delete(directories)
        session.commit()
        return 'Deleted'
    except Exception:
        return False
