

# Created by Sachin Dev on 14/07/18

class TrainException(Exception):
    def __init__(self, message):
        self.message = message


class TrainNotFoundException(TrainException):
    pass