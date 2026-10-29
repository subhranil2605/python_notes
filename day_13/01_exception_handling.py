def calculate_value(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Can't be divided by 0")


# You have to know the edge cases where your code can fail
# Then you handle those edge cases using try ... except block

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))

result = calculate_value(number_1, number_2)
print(result)

print("Rutuja loves Python")
