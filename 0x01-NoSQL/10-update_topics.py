#!/usr/bin/env python3
"""updating topics"""
from pymongo import collection


def update_topics(mongo_collection: collection, name: str, topics: list[str]):
    """update topics"""
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
