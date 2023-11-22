#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, strings
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if getenv("HBNB_TYPE_STORAGE") == "DB":
        email = Column(string(128), nullable=False)
        password = Column(string(128), nullable=False)
        first_name = Column(string(128), nullable=False)
        last_name = Column(string(128), nullable=False)

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
