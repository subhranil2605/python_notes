# list comprehension

# doubling 1 - 10 list
numbers = list(range(1, 11))
print(numbers)
numbers_double = [num * 2 for num in numbers]
print(numbers_double)

# Tuple -> ()


# def get_squares(numbers):
#     for num in numbers:
#         yield num * 2

# generator expression
numbers_gen = (num * 2 for num in numbers)
print(numbers_gen)
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))
print(next(numbers_gen))

print(sum(numbers_gen))
print(sum(numbers_gen))
