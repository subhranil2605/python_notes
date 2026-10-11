numbers = [1, 2, 234, 5, 3, -5]

# Create slice from the list
slice_1 = numbers[1:3]

# When we create a slice of a list, it will create a copy of that.
# Not reference of the actual list

print(slice_1)

slice_1[0] = 999
print(slice_1)

print(numbers)
