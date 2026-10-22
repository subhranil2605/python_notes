# def get_values(n):
#     start = 0
#     while start < n:
#         yield start
#         start += 1


# my_gen = get_values(10)

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

values = [10, 20, 30]
iterator = iter(values)

while True:
    # try:
    #     value = next(iterator)
    # except StopIteration:
    #     break
    value = next(iterator)

    print(value)
