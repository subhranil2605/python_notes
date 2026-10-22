# Mental model

# Book - bookmark
# red, blue, green, yellow

# Book -> iterable
# bookmarks -> iterator

# Any object in python, on which we can use for loop, is an "Iterable"


# red <- next(bookmark)
# blue <- next(bookmark)
# yellow <- next(bookmark)
# green <- next(bookmark)
# "Invalid" <- next(bookmark) # StopIteration

# from collections.abc import Iterable, Iterator

orders = ["PEN-01", "INK-02", "STAPLER"]
bookmark = iter(orders)

# print(type(orders), type(bookmark))

# print(isinstance(orders, Iterable))
# print(isinstance(orders, Iterator))
# print(isinstance(bookmark, Iterator))


# def squaring_list(numbers):
#     if isinstance(numbers, list):
#         return [num * 2 for num in numbers]
#     else:
#         return []


# print(squaring_list([1, 2, 3]))
# print(squaring_list("subhranil"))
