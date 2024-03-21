#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
reviews = relationship("Review", backref="user", cascade="all, delete")


class Review(BaseModel):
    """ Review classto store review information """
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
