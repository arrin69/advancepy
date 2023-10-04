import random

# a float number between 0 to 1
print(random.random())

# a float between given range including upper bound not included i.e. 3
print(random.randrange(1, 3))

# an int between a range including upper bound i.e. 4
print(random.randint(1, 4))

# number from a normal distribution with a mean of 0 and standard deviation
print(random.normalvariate(0, 1))

mylist: list = list("PRADEEP")
# print(random.choice(mylist))
# print(random.sample(mylist, 3))
random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
random.seed(3)
print(random.random())
print(random.randint(1, 10))
random.seed(4)
print(random.random())
print(random.randint(1, 10))
