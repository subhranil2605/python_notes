def get_squares_gen():
    # yield 1**2
    # yield 2**2
    # yield 3**2
    # yield 4**2
    # yield 5**2
    # yield 6**2
    
    for i in range(1, 7):
        yield i**2


gen = get_squares_gen()

print(next(gen))
print(next(gen))
