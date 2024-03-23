#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from os import getenv
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """Class(New engine) definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Public instance methods"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, password, hos, database))
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects
        depending of the class name"""
        queries = {}
        if not cls:
            for clas in classes:
                objects = self.__session.query(classes[clas]).all()
                for objec in objects:
                    key = objec.__class__.__name__ + '.' + objec.id
                    queries[key] = objec
        else:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = objec.__class__.__name__ + '.' + objec.id
                queries[key] = objec
        return queries

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ommit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is None:
            self.__session.commit.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bing=self.__session,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.remove()
