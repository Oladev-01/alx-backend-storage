#!/usr/bin/env python3
"""school having a topic"""

from typing import List, Dict
from pymongo import collection


def schools_by_topic(mongo_collection: collection,
                     topic: str) -> List[Dict[str, any]]:
    """return schools offering a subject topic"""
    get_schools = mongo_collection.find({"topics": topic})
    return list(get_schools)
