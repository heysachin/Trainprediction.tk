

# Created by Sachin Dev on 14/07/18
import uuid
import models.stations.constants as StationConstants
from common.database import Database


class Station(object):
    def __init__(self, name, _id=None):
        self.name = name
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Station {}>".format(self.name)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name
         }

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(StationConstants.COLLECTION, {})]

    @classmethod
    def get_by_id(cls, id):
        return cls(**Database.find_one(StationConstants.COLLECTION, {"_id": id}))

    def save_to_mongo(self):
        Database.insert(StationConstants.COLLECTION, self.json())

    @classmethod
    def get_by_name(cls, station_name):
        return cls(**Database.find_one(StationConstants.COLLECTION, {"name" : station_name}))