#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey=('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey=('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="cities")
    reviews = relationship("Review", backref="place", cascade="all, delete")

    @property
    def reviews(self):
        """getter attribute cities that returns the list of Review instances"""
        from models import storage
        all_reviews = models.storage.all(Review)
        for obj, instance in all_reviews.items():
            if isinstance(instance, Review) and Review.place_id == Place.id:
                all_reviews.append(obj)
        return all_reviews

    place_amenity = Table('association', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
                primary_key=True), Column('amenity_id'), String(60),
                ForeignKey('amenities.id'),
        primary_key=True)

    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    @property
    def amenities(self):
        """ returns the list of Amenity instances based on the attribute"""
        from models import storage
        all_amenities = models.storage.all(Amenity)
        for obj, instance in all_amenities.items():
            if isinstance(instance, Amenity) and Place.amenity_ids == Amenity.id:
                all_amenities.append(obj)
        return all_amenities

    @amenities.setter
    def amenities(self, value):
        """ handles append method for adding an Amenity.id to the attribute"""
        from models import storage
        if isinstance(value, Amenity):
            self.amenity_ids.append(value.Amenity.id)

            #self.amenity_ids = append(Amenity.id)
