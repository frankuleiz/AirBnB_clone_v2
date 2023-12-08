#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref=backref(
            "state", cascade="all, delete"))
    else:
        name = ""

    @property
    def cities(self):
        """
        Getter attribute that returns the list of instances
        with state.id equals the currrent state.id
        """
        from models import storage
        related_cities = []
        my_cities = storage.all(City)
        for city in my_cities.values():
            if self.id == city.state_id:
                related_cities.append(city)
        return related_cities
