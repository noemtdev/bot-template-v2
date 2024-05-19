from pymongo import MongoClient

class Base:
    def __init__(self, database, collection):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[database]
        self.collection = self.db[collection]

    def find(self, query):
        return self.collection.find(query)

    def insert(self, data):
        return self.collection.insert_one(data)

    def update(self, query, data):
        return self.collection.update_one(query, data)

    def delete(self, query):
        return self.collection.delete_one(query)
