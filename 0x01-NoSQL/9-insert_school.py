#!/usr/bin/env python3

"""Module for inserting a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo
            collection object where the new document will be inserted.
        **kwargs: Arbitrary keyword arguments representing the fields and
            values of the document to be inserted.

    Returns:
        bson.objectid.ObjectId: The _id of the newly inserted document.
    """
    # Insert the document into the collection
    result = mongo_collection.insert_one(kwargs)
    # Return the _id of the newly inserted document
    return result.inserted_id
