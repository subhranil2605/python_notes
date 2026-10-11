numbers = list(range(1, 21))

# apply cube + 3 on every element and store it in a new list
# transform the list to a new one

new_numbers = list(map(lambda x: x**3 + 3, numbers))
print(new_numbers)

# new_numbers_for = []
# for x in numbers:
#     y = x**3 + 3
#     new_numbers_for.append(y)

# print(new_numbers_for)

# List comprehension
new_numbers_com = [x**3 + 3 for x in numbers]
print(new_numbers_com)
