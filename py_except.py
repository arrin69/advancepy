# errors and exceptions
from MyOwnException import MyOwnException, AnotherException

# syntax error
# a = 5
# print(a))

# TypeError
# print(1 + "a")

# exception raises FileNotFoundError
# file = open("not_a_file.txt")


x: int = 5
if x < 5:
    raise Exception("number is less than 5 :(")
else:
    try:
        assert x > 6, "X is less than 6 :) "
    except AssertionError as ex:
        print("hallo", ex)

try:
    a = 5 / 0
except ZeroDivisionError as zeroError:
    print(zeroError, "Cannot divide by 0 ")
    try:
        b = 5 + "10"
    except TypeError as typerError:
        print(typerError, "There is a type error also")
    finally:
        print("this is good example of Python exception handling")


def check_value(x: int):
    if x == 3:
        raise MyOwnException("this is not correct")
    if x == 5:
        raise AnotherException("x is not a good number", 5)


try:
    print(check_value(3))
except MyOwnException as my:
    print("oh ho my own exception is thrown")
    print(my)
    try:
        check_value(5)
    except AnotherException as another:
        print("another exception")
        print(another.value, another.message)
