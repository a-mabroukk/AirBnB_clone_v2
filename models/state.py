#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances"""
        all_cities = models.storage.all(City)
        for obj, instance in all_cities.items():
            if isinstance(instance, City) and City.state_id == state.id:
                all_cities.append(obj)
        return all_cities