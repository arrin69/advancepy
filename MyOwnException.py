class MyOwnException(Exception):
    pass


class AnotherException(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

