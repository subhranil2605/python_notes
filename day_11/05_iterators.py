# print(iter([1, 2, 3]))

# print(iter(42))

numbers = iter([1, 2, 3])
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers, "nothing left"))
