#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances"""
        from models import storage
      all_cities = models.storage.all(City)
        for obj, instance in all_cities.items():
            if isinstance(instance, City) and self.id == City.state_id:
                all_cities.append(obj)
        return all_cities
