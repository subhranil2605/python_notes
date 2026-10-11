# if condition inside a dictionary comprehension

user = {
    "id": 1001,
    "name": "Rutuja",
    "location": "Pune",
}

# Access the id of the user
print(user["id"])
# print(user["age"])

# .get() method on the dictionary
print(user.get("id"))
print(user.get("age", "INVALID_AGE"))

# .values()
print(user.values())
print(list(user.values()))

# .key()
print(user.keys())
print(list(user.keys()))

# .items()
print(user.items())
print(list(user.items()))

# .update()
inventory = {"apple": 100, "orange": 80}
# inventory["banana"] = 156
# print(inventory)

inventory.update({"banana": 156})
inventory.update(strawberry=456, mango=7)
inventory.update([("litchi", 21), ("pineapple", 45)])

print(inventory)

# Removing keys: .pop(key)
inventory.pop("apple")
print(inventory)

del inventory["orange"]
print(inventory)

# Deleting items from behind: .popitem()
inventory = {"apple": 100, "orange": 80, "banana": 78}

inventory.popitem()
print(inventory)

inventory.popitem()
print(inventory)

inventory.popitem()
print(inventory)

# How to delete everything at once: .clear()
inventory = {"apple": 100, "orange": 80, "banana": 78}

print(inventory)
inventory.clear()

print(inventory)

# Copying Dictionary
inventory = {
    "apple": 100,
    "orange": 80,
    "banana": 78,
    "vendors": ["amazon fresh", "blinkit"],
}

# shallow copy
inventory_2 = inventory.copy()
inventory_2["vendors"].append("instamart")
print(inventory_2)

print(inventory)

# .setdefault()
inventory = {"apple": 100, "orange": 80}
print(inventory.setdefault("apple"))
print(inventory.setdefault("mango"))

# inventory.setdefault("banana", 99)
# print(inventory)
