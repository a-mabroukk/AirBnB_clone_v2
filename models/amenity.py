#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel, Base):
    """Amenity class that inherits from BaseModel and Base"""
    name = ""
