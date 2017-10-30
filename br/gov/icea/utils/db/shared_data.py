from pymongo import MongoClient

class shared_data(object):
    def __init__(self, database):
        self.__client = MongoClient()
        self.__db = self.__client[database]

    def update(self, key, timestamp, count):
        data = {'_id': key, 'timestamp': timestamp, 'count': count}
        self.__db.attack.update({'_id': key}, data, upsert=True)

    def findAll(self):
        return self.__db.attack.find()

    def find(self, key):
        return self.__dev.attack.find({'_id': key})