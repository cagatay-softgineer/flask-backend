# database/mongodb.py
from contextlib import contextmanager
from pymongo import MongoClient
from config.settings import MongoSettings

_mongo = MongoSettings()

@contextmanager
def get_connection():
    uri = _mongo.uri
    if not uri:
        raise RuntimeError("Set MONGODB_URI to use MongoDB backend")
    client = MongoClient(uri)
    try:
        yield client.get_default_database()
    finally:
        client.close()
