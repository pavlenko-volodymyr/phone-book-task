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
        return True
    except Exception:
        return False
