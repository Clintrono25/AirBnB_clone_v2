#!/usr/bin/python3
"""Implements the user's model"""
import email
from models.base_model import BaseModel

class User(BaseModel):
    """
    Inherits from the BaseModel class and add user's funstionalties
    Args:
        email (str): the email of the user
        password (str): the password of tge user
        first_name (str): the first name of the user
        last_name (str): the last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""