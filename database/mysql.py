# database/mysql.py
from contextlib import contextmanager
import pymysql
import sqlalchemy as sa
from config.settings import MySQLSettings

_mysql = MySQLSettings()

@contextmanager
def get_connection():
    u = sa.engine.url.make_url(_mysql.uri)
    conn = pymysql.connect(
       host=u.host, port=u.port or 3306,
       user=u.username, password=u.password,
       db=u.database,
       cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conn
    finally:
        conn.close()
