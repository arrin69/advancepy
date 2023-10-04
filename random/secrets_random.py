import random
import secrets

import numpy

print(secrets.randbelow(10))
print(secrets.randbits(4))  # generates number from 0 10 15

mylist: list = list("PRADEEP")
print(secrets.choice(mylist))

# with numpy
a = numpy.random.randint(0, 10, (3, 4))
# print(a)

arr = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
random.shuffle(arr)
print(arr)

numpy.random.seed(1)
print(numpy.random.rand(3, 3))
numpy.random.seed(1)
print(numpy.random.rand(3, 3))
