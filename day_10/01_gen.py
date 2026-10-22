def get_squares_gen(n: int):
    for i in range(1, n + 1):
        yield i**2


my_generator = get_squares_gen(1000)

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
