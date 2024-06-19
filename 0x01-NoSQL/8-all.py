#!/usr/bin/env python3

"""Python module for listing all documents"""


def list_all(mongo_collection):
    """
    Retrieve all documents from the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): A pymongo collection
            object representing the MongoDB collection from which documents
            are to be retrieved.

    Returns:
        list: A list containing all documents from the collection
              Each document is represented as a dictionary.

        If no documents are found, an empty list is returned.
    """
    cursor = mongo_collection.find({})
    # Initialize an empty list to store the documents
    all_documents = []
    # Iterate over the cursor and append each document to the list
    for document in cursor:
        all_documents.append(document)
    return all_documents
