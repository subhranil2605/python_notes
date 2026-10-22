name = input("What is your name? ")
age = input("What is your age? ")

# print(name, age)

# Create the file in writing mode and get the file object
f_obj = open("person.txt", "w", encoding="utf-8")

# We will write values inside the txt file
f_obj.write(f"Name: {name}\n")
f_obj.write(f"Age: {age}\n")

# we have to close
f_obj.close()
