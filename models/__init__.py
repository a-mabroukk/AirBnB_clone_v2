#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

env_var = os.environ['HBNB_TYPE_STORAGE']
if env_var == 'db':
    storage = DBStorage()
    storage.reload()

storage = FileStorage()
storage.reload()
