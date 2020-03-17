from app.database import session
from app.models.directory.directory import Directory


def create_directory(args):
    try:
        item = Directory(**args)
        session.add(item)
        session.commit()
        return item
    except Exception:
        return None
