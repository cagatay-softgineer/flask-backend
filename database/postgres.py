# database/postgres.py

import psycopg2
from contextlib import contextmanager
from config.settings import PostgresSettings

_pg = PostgresSettings()   # only now reads POSTGRES_* if you import this module

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        host=_pg.host,
        port=_pg.port,
        dbname=_pg.dbname,
        user=_pg.user,
        password=_pg.password
    )
    try:
        yield conn
    finally:
        conn.close()

@contextmanager
def get_connection_by_url():
    conn = psycopg2.connect(_pg.url)
    try:
        yield conn
    finally:
        conn.close()