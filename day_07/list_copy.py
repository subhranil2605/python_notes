import copy

numbers = [1, 2, [98, 99, [14, 6]]]
# Create the copy of the numbers
# numbers_copy = numbers[:]
numbers_copy = copy.deepcopy(numbers)

# print(f"Previous actual list: {numbers=}")
# print(f"Previous copied list: {numbers_copy=}")

# numbers_copy[0] = 5

# print(f"After actual list: {numbers=}")
# print(f"After copied list: {numbers_copy=}")

print(f"Previous actual list: {numbers=}")
print(f"Previous copied list: {numbers_copy=}")

numbers_copy[2][2][1] = 999999

print(f"After actual list: {numbers=}")
print(f"After copied list: {numbers_copy=}")



# numbers_copy[2] = [45]

# print(numbers)
# print(numbers_copy)

# Chaining of indexing
# print(numbers[2])
# print(numbers[2][2])
# print(numbers[2][2][1])