

# Created by Sachin Dev on 14/07/18
import uuid
import models.trains.constants as TrainConstants
from common.database import Database


class Train(object):
    def __init__(self, name, source, destination, _id=None):
        self.name = name
        self.source = source
        self.destination = destination
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Train {} Name {} Source {} Destination>".format(self._id,self.name,self.source,self.destination)

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "source": self.source,
            "destination": self.destination
         }

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(TrainConstants.COLLECTION, {})]

    @classmethod
    def get_by_id(cls, _id):
        return cls(**Database.find_one(TrainConstants.COLLECTION, {"_id": _id}))

    def save_to_mongo(self):
        Database.insert(TrainConstants.COLLECTION, self.json())

    @classmethod
    def get_by_name(cls, station_name):
        return cls(**Database.find_one(TrainConstants.COLLECTION, {"name": station_name}))

    @classmethod
    def get_by_source(cls, source):
        return [cls(**elem) for elem in Database.find(TrainConstants.COLLECTION, {"source": source})]

    @classmethod
    def get_by_destination(cls, destination):
        return [cls(**elem) for elem in Database.find(TrainConstants.COLLECTION, {"destination": destination})]