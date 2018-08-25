

# Created by Sachin Dev on 14/07/18

class TimeTableException(Exception):
    def __init__(self, message):
        self.message = message


class TimeTableNotFoundException(TimeTableException):
    pass