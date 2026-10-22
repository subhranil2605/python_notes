numbers = [1, 2, 3, 4]

# Step 1: converting the list to an iterator
iterator = iter(numbers)

# Step 2: calling next() to get all the values from the iterator
while True:
    item = next(iterator, "Nothing Left in the list")

    # Step 3: To break the loop
    if item == "Nothing Left in the list":
        break
    
    print(item)
