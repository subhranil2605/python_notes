# def add(a, b, c, d):
#     return a + b + c + d


# print(add(5, 6, 8, 6))

"""
Syntax
------

def function_name(*args):
    ...
"""


def add(*args):
    # args -> tuple
    return sum(args)


print(add(5, 6, 6, 7))
print(add(5))
