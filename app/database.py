"""Module that provides a db service for toher parts of application to use"""
from flask import current_app, g
from pymongo import MongoClient


def get_db():
    """
    obtains the db
    """
    if 'db' not in g:
        client = MongoClient(current_app.config['MONGO_URI'])
        g.db = client.get_default_database()
    return g.db


def close_db(e):
    """
    disconnects the current db
    """
    db = g.pop('db', None)
    if db is not None:
        db.client.close()
