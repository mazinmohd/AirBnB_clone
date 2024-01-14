#!/usr/bin/python3
""" review Model """
from models.base_model import BaseModel


class Review(BaseModel):
    """ review Class """

    place_id = ""
    user_id = ""
    text = ""
