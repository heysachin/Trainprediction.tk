

# Created by Sachin Dev on 14/07/18

class StationException(Exception):
    def __init__(self, message):
        self.message = message


class StationNotFoundException(StationException):
    pass