# This is a sample Python script.
import sys
import timeit
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
from functools import reduce
from itertools import product, permutations

## Lambda
# add10 = lambda x: x + 10
# print(add10(3))
#
# mult = lambda x, y: x * y
# print(mult(4, 5))
#
# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
# print(points2D)
# print(points2D_sorted)

# map funtion
# alist = [1, 2, 3, 4]
# blist = map(lambda x: x * 2, alist)
# print(list(alist))
# print(list(blist))

# filter function - return all elements for which condition is evaluate to true
#
# alist = [1, 2, 3, 4, 5, 6, 7, 8]
# blist = filter(lambda x: x % 2 == 0, alist)
# print(list(blist))
#
# clist = [x for x in alist if x%2==0]
# print(clist)
#
# clist = reduce(lambda x, y: x+y, alist)
# print(clist)


# reduce(func, seq) keeping appluing the func and return single value


# iterators: itertools
# product this returns cartesian product of given list
# firstList = [1,2]
# secondList = [3]
# prod = product(firstList, secondList, repeat=2)
# # prod = product(firstList, secondList)
# print(list(prod))

# permutations - give permutations of given list with order
# a = [1, 2, 3, 4, 5]
# perm = permutations(a)
# print(len(list(perm)))

# permutations with combinations


# Collections
# counter
# a:str = "aaaabbbbcccdd"
# myCounter: Counter = Counter(a)
# print(myCounter)
# print(myCounter.keys())
# print(myCounter.values())
# print(myCounter.most_common(1))
# print(list(myCounter.elements()))

## namedTuple is a way to create class and initialise it with values
# Point = namedtuple('Point', 'x,y,z')
# pt: Point = Point(3, [1, 2, 3, 4], {5: "apple", 4: "banana"})
# print(pt)
# print(pt.x, pt.y, pt.z)
# print(type(pt.x), type(pt.y), type(pt.z))

## orderedDictionary is a dictionary where order in which elements are added is retained
# order_dict: OrderedDict = OrderedDict()
# order_dict['b'] = 2
# order_dict['c'] = 3
# order_dict['d'] = 4
# order_dict['a'] = 1
# order_dict['e'] = 5
# order_dict['f'] = 6
# print(order_dict)


## defaultDict is an abstract datatype which provides
# a default value of a key when it is not found in dictionary
# and it avoids runtime error of keyError
# d = defaultdict(float)
# d["a"] = 1
# d["b"] = 2
# print(d["c"])


## deque is an abstraction over list and it provides ways to add and delete elements
# from front and back
# my_deque = deque()
# my_deque.append(1)
# my_deque.append(2)
# my_deque.append(3)
# print(my_deque)
# my_deque.appendleft(6)
# print(my_deque)
# my_deque.extendleft([5, 6, 7, 8])
# print(my_deque)
# my_deque.pop()
# print(my_deque)
# my_deque.popleft()
# print(my_deque)
# my_deque.rotate(-1)
# print(my_deque)

# Strings
# mystring = "hello world"
# char = mystring[1]
# print(char)
# print(mystring.upper())
# print(mystring[1:5])  # substring from index 1 t0 4 (last 5 -1 )
# print(mystring[::-1]) # give elements in reverse order
#
# print("Tom says " + mystring)
# # for i in mystring:
# #     print(i)
# mystring = "    pradeep   "
# print(mystring.strip().upper().endswith("P"))
# print(mystring.find("e"))
# print(mystring.count("e"))
# name = "PRadeep"
# age = 23
# mystring = f"how are you {name}"
# print(mystring)
# mystring = "how are you %s %d"
# print(mystring)
#

# mystring = mystring.split(".")
# print(".".join(mystring))

# sets unordered mutable no duplicates

# myset = {1, 2, 3, 4, 2, 4, 1}
# print(myset)
# myset = set("Hello")
# print(myset)

# emptySet = {} this is not empty set instead this is empty dictionary
# emptySet = set()  # this is empty set
# print(emptySet)
# emptySet.add(1)
# emptySet.add(2)
# emptySet.add(3)
# emptySet.add(4)
# print(emptySet)
# # emptySet.remove(6) # will raise error for not found value
# emptySet.discard(6) # do not throw error if element is not found
# print(emptySet)
# emptySet.pop() # removes first element from set
# print(emptySet)
#
#
# if "l" in myset:
#     print("i am in ")
#
# for x in myset:
#     print(x)

# unions and intersetion of sets
# odds = {1, 3, 5, 7, 9}
# evens = {2, 4, 6, 8, 10}
# primes = {2, 3, 5, 7, 11}
#
# u = odds.union(evens)
# print(u)
#
# intersection = odds.intersection(evens)
# print(intersection)
# intersection = odds.intersection(primes)
# print(intersection)
# intersection = evens.intersection(primes)
# print(intersection)


# # differences of sets
# setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 12, 1345, 67, 89}
# # print(setB.difference(setA)) # returns elements which are not present in given set
# #
# # print(setB.symmetric_difference(setA)) # returns none common elements
# #
# # setA.update(setB)
# # print(setA)
#
# # forzenset not mutable set
# a = frozenset({1, 2, 3, 4, 5})
# print(a.update(2))

## dictionaries
# mydict = {"name": "pradeep", "age": 23, "city": "Zoetermeer"}
# # print(mydict)
#
# mydict2 = dict(name="Marry", age=21, city="DenHaag")
# # print(mydict2.get("age"))
# mydict2["email"] = "abc@ss.com"
# print(mydict2)

# delete item from dictionary
# del mydict2["email"]  # keyword to delete given property from dictionary
# print(mydict2)
# mydict2.pop("age")  # removes the given key
# print(mydict2)
# mydict2.popitem()  # removes last element from dictionary
#
# if "pp" in mydict2:
#     print("I am there")
#
# try:
#     print(mydict2["pradeep"])
# except KeyError:
#     print("Error")

# iterate over items of dictionary
# for key, value in mydict2.items():
#     print(key, value)
#
#
# # mydict2_cpy = mydict2 # is not copy instead both variables are pointing tosame elements in memeory
# mydict2_cpy = dict(mydict2)
# mydict2["fruit"] = "banana"
# print(mydict2)
# print(mydict2_cpy)


# update method to merge two dictionaries
# mydict2.update(mydict)
# print(mydict2)
# print(mydict)
#


# tuple ordered immutable ordered allows duplicate

# unpacking
# myTuple = ("max", 28, "boston", "banana", "nose", "leg")
# myList = ["max", 28, "boston", "banana", "nose", "leg"]
# # name, age, city, fruit = myTuple
# # print(name, age, city, fruit)
#
# i1, *i2, i3 = myTuple
# print(i1)  # print fisrst item
# print(i2, type(i2))  # prints all elements between first and last
# print(i3)  # last element
#
# print(sys.getsizeof(myTuple), "bytes")
# print(sys.getsizeof(myList), "bytes")

# print(timeit.timeit(stmt="['max', 28, 'boston', 'banana', 'nose', 'leg']", number=1000000))
# print(timeit.timeit(stmt="('max', 28, 'boston', 'banana', 'nose', 'leg')", number=1000000))


# myTuple = ("max", 28, "boston")
# print(myTuple)
# print(type(myTuple))
#
# newTuple = tuple(["max", 28, "boston"])
# print(type(list(myTuple)))
#
# sliceD = myTuple[2:5]
# print(sliceD)

# List un ordered mutable allows duplicate
# copies
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# myList_square = [i * i for i in myList]
# print(myList)
# print(myList_square)

# myList = ["banana", "cherry", "apple"]
# copy_mylist = list(myList)
# print(copy_mylist)
# myList.append("lemon")
# print(myList)
# print(copy_mylist)

# # slices
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# a = myList[::-1]
# print(a)

#
# duplicateList = [0] * 5
# print(duplicateList)
# myList = ["banana", "cherry", "apple"]
# print(duplicateList + myList)


# myList = ["banana", "cherry", "apple"]
# print(myList)
#
# emptyList = list()
# print(emptyList)
#
# emptyList.append("pineapple")
#
# emptyList.append(5)
# emptyList.append("pineapple")
# emptyList.append("cherry")
#
# print(emptyList)
#
# for i in emptyList:
#     print(i)
#
# if "pineapple" in emptyList:
#     print(" I am in emtyList")
# if "lemon" in emptyList:
#     print("lemon is there")
# else:
#     print("lemon is Not there")
#
# emptyList.insert(3, "grapes")
# print(emptyList)
# print(emptyList)
# emptyList.remove("cherry")
# emptyList.reverse()
# print(emptyList)
#
# numberList = [4, 7, 86, 234, 786844, 1, 3]
# # numberList.sort()
# print(sorted(numberList))

#
# my_dict = {3: 9, 6: 34, 13: 34, 1: 8}
# mytuple = (3, 4)
# my_dict2 = {mytuple: "pradeep"}
# print(my_dict)
# print(my_dict2[(3, 4)])
