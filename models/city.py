#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=True)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=True)
    else:
        state_id = ""
        name = ""
