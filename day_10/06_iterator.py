# Iterable
# An iterable is an object you can loop over.

my_list = [1, 2, 3]
my_name = "Subhranil"  # collection of characters
rgb_value = (244, 0, 234)
my_set = {1, 2, 3}
my_dict = {"name": "rutuja", "age": 26}

# Iterator
# An iterator is an object that produces the next item when requested

values = [23, 56, 7, 8]
values_iterator = iter(values)

# print(values_iterator)
# print(next(values_iterator))
# print(next(values_iterator))
# print(next(values_iterator))
# print(next(values_iterator))
# print(next(values_iterator))


while True:
    try:
        print(next(values_iterator))
    except StopIteration:
        break
