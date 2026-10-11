# Enumeration

names = ["Rutuja", "Pratiksha", "Subhranil"]

# range(5) -> range(0, 5)
# list(range(5)) -> [0, 1, 2, 3, 4]
# for i in range():

# for name in names:
#     print(name)

# for i in range(len(names)):
#     print(i)

# for i in range(len(names)):
#     print(i, names[i])

# Enumerate
# print(list(enumerate(names)))

for idx, name in enumerate(names, start=1):
    print(idx, name)