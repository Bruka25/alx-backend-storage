The followin scripts are for ALX 0x01-NoSQL project witrhin alx-backend-storage curriculum, inside it contains the following mongodb script
files:

* A script that lists all databases in MongoDB
* A script that creates or uses the database my_db
* A script that inserts a document in the collection school
```
  -> The document must have one attribute name with value “Holberton school”
  -> The database name will be passed as option of mongo command
```

* A script that lists all documents in the collection school
```
  -> The database name will be passed as option of mongo command
```

* A script that lists all documents with name="Holberton school" in the collection school
```
  The database name will be passed as option of mongo command
```

* A script that displays the number of documents in the collection school
```
  -> The database name will be passed as option of mongo command
```
* A script that adds a new attribute to a document in the collection school
```
  -> The script should update only document with name="Holberton school" (all of them)
  -> The update should add the attribute address with the value “972 Mission street”
  -> The database name will be passed as option of mongo command
```

* A script that deletes all documents with name="Holberton school" in the collection school
```
  -> The database name will be passed as option of mongo command
```
* A Python function that lists all documents in a collection
```
  -> Prototype: def list_all(mongo_collection):
  -> Return an empty list if no document in the collection
  -> mongo_collection will be the pymongo collection object
```
* A Python function that inserts a new document in a collection based on kwargs
```
  -> Prototype: def insert_school(mongo_collection, **kwargs):
  -> mongo_collection will be the pymongo collection object
  -> Returns the new _id
```
* A Python function that changes all topics of a school document based on the name
```
  -> Prototype: def update_topics(mongo_collection, name, topics):
  -> mongo_collection will be the pymongo collection object
  -> name (string) will be the school name to update
  -> topics (list of strings) will be the list of topics approached in the school
```
* A Python function that returns the list of school having a specific topic
```
  -> Prototype: def schools_by_topic(mongo_collection, topic):
  -> mongo_collection will be the pymongo collection object
  -> topic (string) will be topic searched
```
* A Python script that provides some stats about Nginx logs stored in MongoDB
```
  -> Database: logs
  -> Collection: nginx
  -> Display (same as the example):
         first line: x logs where x is the number of documents in this collection
         second line: Methods:
         5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below -         warning: it’s a tabulation before each line)
         one line with the number of documents with:
             method=GET
             path=/status
```

* A script that lists all documents with name starting by Holberton in the collection school
```
  -> The database name will be passed as option of mongo command
```
* A Python function that returns all students sorted by average score
```
  -> Prototype: def top_students(mongo_collection):
  -> mongo_collection will be the pymongo collection object
  -> The top must be ordered
  -> The average score must be part of each item returns with key = averageScore
```
* Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs






































































































