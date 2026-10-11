# Type: range

# print(range(10))

# Syntax
# range(start=0, stop=11, step=1)
# range(0, 11, 1)

# converting a range to list
print(list(range(0, 11, 1)))

print(list(range(11)))

# Bad example: step can't be a float number
# print(list(range(0, 1, 0.1)))

print(list(range(10, 0, -1)))
