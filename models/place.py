#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship("Amenity", secondary=place_amenity,
                             backref="place_amenities",
                             viewonly=False)

    @property
    def reviews(self):
        """returns the list of Review instances"""
        reviews_list = []
        all_reviews = list(models.storage.all(Review))
        for instance in all_reviews.values():
            if instance.place_id == self.id:
                reviews_list.append(instance)
        return reviews_list

    @property
    def amenities(self):
        """returns the list of Amenity instances"""
        amenities_list = []
        all_amenities = list(models.storage.all(Amenity))
        for instnce in all_amenities.values():
            if instnce.place_id == self.id:
                amenities_list.append(instnce)
        return amenities_list

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute amenities that handles append
        method for adding an Amenity.id to the attribute"""
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
