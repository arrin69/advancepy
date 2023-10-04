import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user: User = User("Max", 37)


def encode_user(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError("not a user")


userJson: str = json.dumps(user, default=encode_user)
print(userJson)


# custom encoder
class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
        return json.JSONEncoder.default(self, obj)


userJson: str = UserEncoder().encode(user)
print(userJson)
