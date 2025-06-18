import sqlite3 as sql
from contextlib import contextmanager


@contextmanager
def connection(db_path):
    connection = sql.connect(db_path, autocommit=True)
    cursor = connection.cursor()
    try:
        yield cursor
    except:
        connection.rollback()
    finally:
        connection.close()
