from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def db_add(item):
    db.session.add(item)
    if db.session.commit() is None:
        return True
    return False


def db_delete(item):
    db.session.delete(item)
    if db.session.commit() is None:
        return True
    return False
