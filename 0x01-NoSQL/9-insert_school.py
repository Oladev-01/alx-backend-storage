#!/usr/bin/env python3
"""inserting into collection"""

from typing import Dict
from pymongo import collection
from bson import ObjectId


def insert_school(mongo_collection: collection, **kwargs:
                  Dict[str, any]) -> ObjectId:
    """inserting into collection"""
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
