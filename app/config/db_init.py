from pymongo import MongoClient

from app.config.config import DB_NAME, MONGO_URI


class MongoDBConnection:
    _client = None
    _db = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = MongoClient(MONGO_URI)
        return cls._client

    @classmethod
    def get_db(cls):
        if cls._db is None:
            cls._db = cls.get_client()[DB_NAME]
        return cls._db


mongo_db = MongoDBConnection.get_db()
