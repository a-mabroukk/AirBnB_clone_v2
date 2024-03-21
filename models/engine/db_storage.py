#!/usr/bin/python3
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}

mysql_user = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
db = getenv('HBNB_MYSQL_DB')
env = getenv('HBNB_ENV')


class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                      (mysql_user, password, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dictionary = {}
        for clas in classes:
            if cls is None:
                all_objects = self.__session.query(classes[clas]).all()
            for obj in dictionary:
                key = obj.__class__.__name__ + '.' + obj.id
                dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """ a method that add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """a method that commit all changes of the current database session"""
        self.__session.commit(obj)

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is None:
            return
        else:
            objec = obj.__class__.__name__ + '.' + obj.id
            if objec in self.__session:
                del self.__session[objec]

    def reload(self):
        """create all tables in the database"""

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)

        Session = scoped_session(session_factory)

        self.__session = Session()
