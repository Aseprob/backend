"""Module that provides a db service for toher parts of application to use"""
from flask import current_app, g
from pymongo import MongoClient


def get_db():
    """
    obtains the db
    """
    if 'db' not in g:
        client = MongoClient(current_app.config.get('MONGO_URI'))
        db_name = current_app.config.get('MONGO_DBNAME', 'db')
        g.db = client[db_name]
    return g.db


def close_db(context):
    """
    disconnects the current db
    """
    print(context)
    db = g.pop('db', None)
    if db is not None:
        db.client.close()
