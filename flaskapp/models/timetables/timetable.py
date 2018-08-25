
# Created by Sachin Dev on 14/07/18
import uuid
import models.timetables.constants as TimetableConstants
from common.database import Database


#Train No	Train Name	SEQ	Station Code	Station Name	Arrival time	Departure Time	Distance
# Source Station	Source Station Name	Destination Station	Destination Station Name


class TimeTable(object):
    def __init__(self, train_no, train_name, sequence, station_code, station_name, arrival_time, departure_time, distance, source_code, source_name, dest_code, dest_name,  _id=None):
        self.train_no = train_no
        self.train_name = train_name
        self.sequence = sequence
        self.station_code = station_code
        self.station_name = station_name
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.distance = distance
        self.source_code = source_code
        self.source_name = source_name
        self.dest_code = dest_code
        self.dest_name = dest_name
        self.reach_time = None
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            "_id": self._id,
            "train_no": self.train_no,
            "train_name": self.train_name,
            "sequence": self.sequence,
            "station_code": self.station_code,
            "station_name": self.station_name,
            "arrival_time": self.arrival_time,
            "departure_time": self.departure_time,
            "distance": self.distance,
            "source_code": self.source_code,
            "source_name": self.source_name,
            "dest_code": self.dest_code,
            "dest_name": self.dest_name
         }

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(TimetableConstants.COLLECTION, {})]

    def save_to_mongo(self):
        Database.insert(TimetableConstants.COLLECTION, self.json())

    @staticmethod
    def get_trains_by_station(station_name):
        return [train["train_no"] for train in Database.find(TimetableConstants.COLLECTION, {"station_code": station_name})]

    @classmethod
    def get_train_class(cls,train_no, station_code):
        return cls(**Database.find_one(TimetableConstants.COLLECTION, {"train_no": train_no,"station_code":station_code}))

    @staticmethod
    def get_train_sequence(train_no,station_name):
        seq = Database.find_one(TimetableConstants.COLLECTION, {"station_code": station_name,"train_no":train_no})
        return int(seq["sequence"])

    @classmethod
    def get_stations_by_train(cls,train_no):
        return [cls(**train) for train in Database.find(TimetableConstants.COLLECTION, {"train_no": train_no})]

    @staticmethod
    def get_time(train_no, destination):
        dest_class = Database.find_one(
            TimetableConstants.COLLECTION, {"train_no": train_no,
                                            "station_code": destination})
        return dest_class["arrival_time"]

    @staticmethod
    def trains_btw_stations(src, dest):
        train_src = set(TimeTable.get_trains_by_station(src))
        train_dest = set(TimeTable.get_trains_by_station(dest))
        train_intersection = train_src & train_dest
        train_to_return = []
        for train in train_intersection:
            if TimeTable.get_train_sequence(train, src) < TimeTable.get_train_sequence(train, dest):
                source_class = TimeTable.get_train_class(train, src)
                print(source_class)
                source_class.reach_time = TimeTable.get_time(train,dest)
                train_to_return.append(source_class)
        return train_to_return

        # train_src_seq = TimeTable.get_trains_sequences(src)
        # train_dest_seq = TimeTable.get_trains_sequences(dest)
        # btw_station = train_src & train_dest
        # train_src_seq = dict(zip(train_src,train_src_seq))
        # train_dest_seq = dict(zip(train_dest,train_dest_seq))
        # for train in btw_station:
        #     if (train_src_seq[train] > train_dest_seq[train]:
        #         to_return[]=
