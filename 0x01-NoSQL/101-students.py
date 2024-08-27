#!/usr/bin/env python3
"""aggregate sorting"""


def top_students(mongo_collection):
    """return aggregate"""
    pipeline = [
        {"$project": {
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return mongo_collection.aggregate(pipeline)
