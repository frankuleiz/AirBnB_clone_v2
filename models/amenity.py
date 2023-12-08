#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """Amenity class"""
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)

        from models.place import place_amenity
        place_amenities = relationship(
            "Place", secondary=place_amenity,
            back_populates="amenities",
        )
    else:
        name = ""
