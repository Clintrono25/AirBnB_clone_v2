#!/bin/usr/python3
""""Contains the City model"""
from multiprocessing.managers import BaseManager
from unicodedata import name
from models.base_model import BaseModel

class City(BaseManager):
    """Implements the City class"""
    state_is = ""
    name = ""
