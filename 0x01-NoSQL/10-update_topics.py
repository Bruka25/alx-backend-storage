#!/usr/bin/env python3

"""Module for changing the topics of school document based on name"""

def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object
            where the documents are stored.
        name (str): The school name to update.
        topics (list of str): The list of topics to set for the school.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation.
    """
    # Perform the update operation
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
