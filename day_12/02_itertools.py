# numbers = [10, 20, 30, 40, 50]

# print(numbers[0:2]) # slicing

from itertools import islice


# generator is a special kind of iterator
def get_numbers():
    for n in range(10000001):
        yield n


numbers = get_numbers()
print(list(islice(numbers, 5)))
print(list(islice(numbers, 1, 10)))
print(list(islice(numbers, 1, 10, 2)))
