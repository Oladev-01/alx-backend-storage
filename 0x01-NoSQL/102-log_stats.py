#!/usr/bin/env python3
"""show logs"""
from pymongo import MongoClient


def show_logs():
    """show logs"""
    db = MongoClient()
    logs = db.logs.nginx
    print(f"{logs.count_documents({})} logs")
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:
        print(f"\tmethod {method}: {logs.count_documents({'method': method})}")
    print(logs.count_documents({'method': 'GET', 'path': '/status'}), end=' ')
    print("status check")
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    get_top_ip = list(logs.aggregate(pipeline))
    for ip in get_top_ip:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == '__main__':
    show_logs()
