names = ["Rutuja", "Pratiksha", "Subhranil"]

# append
names.append("Raj")
print(names)

# insert
names.insert(1, "John")
print(names)

# extend
other_names = ["Jos", "Joe"]

names.extend(other_names)
print(names)

# remove
names.remove("John")
print(names)

# index
print(names.index("Rutuja"))

# reverse
names.reverse()
print(names)

names.sort()
print(names)

# use for loop to sort this list using the element length
# for name in names:
#     length = len(name)

names.sort(key=lambda x: -len(x))
print(names)

# map, lambda, comprehension, 