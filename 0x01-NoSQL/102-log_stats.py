#!/usr/bin/env python3

"""Module for providing some stats about the Nginx logs in MongoDB"""

import sys
import pymongo


def print_nginx_logs(nginx_collection):
    '''Prints stats about Nginx request logs.'''
    print(f'{nginx_collection.count_documents({})} logs')
    print(f'Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print(f'\tmethod {method}: {req_count}')
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print(f'{status_checks_count} status check')


def top_10_ips(self):
    """Prints statistics about the top 10 HTTP IPs in a collection."""
    print(f"IPs:")
    request_logs = self.aggregate([
        {"$group": {"_id": "$ip", "totalRequests": {"$sum": 1}}},
        {"$sort": {"totalRequests": -1}},
        {"$limit": 10}
    ])
    for request_log in request_logs:
        ip = request_log["_id"]
        ip_requests_count = request_log["totalRequests"]
        print(f"\t{ip}: {ip_requests_count}")


def main():
    '''Check if pymongo is properly installed and provides some stats
       about Nginx logs stored in MongoDB.'''
    try:
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
        print_nginx_logs(client.logs.nginx)
        top_10_ips(client.logs.nginx)
    except ImportError:
        print('pymongo not found. Install it using "pip install pymongo"')


if __name__ == '__main__':
    main()
