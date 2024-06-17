#!/usr/bin/env python3

"""Module for providing some stats about the Nginx logs in MongoDB"""

import sys
import pymongo


def print_nginx_logs(nginx_collection):
    '''Prints stats about Nginx request logs.'''
    print(f'{nginx_collection.count_documents({})} logs')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(nginx_collection.find({'method': method})))
        print(f'\tmethod {method}: {req_count}')
    status_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print(f'{status_checks_count} status check')


def main():
    '''Check if pymongo is properly installed and provides some stats
       about Nginx logs stored in MongoDB.'''
    try:
        client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
        print_nginx_logs(client.logs.nginx)
    except ImportError:
        print('pymongo not found. Install it using "pip install pymongo"')


if __name__ == '__main__':
    main()
