#!/usr/bin/env python3

"""Module for returning a list of schools for having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    functon for returning the list of collections

    Args:
        mongo_collection: collection where documents are stored
        topic: list of topics
    """
    select_topic = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(select_topic)]
