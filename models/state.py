#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class definition"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instances"""
        cities_list = []
        all_cities = models.storage.all(City)
        for instance in all_cities.items():
            if instance.state_id == self.id:
                cities_list.append(instance)
        return cities_list
