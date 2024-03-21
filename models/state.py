#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances"""
        from models import storage
        all_cities = models.storage.all(City)
        for obj, instance in all_cities.items():
            if isinstance(instance, City) and City.state_id == State.id:
                all_cities.append(obj)
        return all_cities
