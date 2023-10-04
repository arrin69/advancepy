from pydantic import BaseModel


# Java style library pydantic to marshal and unmarshal

class NewUser(BaseModel):
    name: str
    age: int
    happy: bool


user: NewUser = NewUser(name="pradeep", age=23, happy=True)
userJson = user.model_dump_json(indent=4)
print(userJson)

userstr = '{"name":"pradeep","age":23,"happy":true}'
userFstr = user.model_validate_json(userstr)
print(userFstr.name)
print(type(userFstr))

