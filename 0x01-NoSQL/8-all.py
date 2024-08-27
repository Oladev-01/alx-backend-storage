#!/usr/bin/env python3
"""this function is to read all documents in a collection"""

from typing import List, Dict
from pymongo import collection


def list_all(mongo_collection: collection) -> List[Dict]:
    """func to return list of documents"""
    list_doc = list(mongo_collection.find())
    return list_doc if list_doc else []
