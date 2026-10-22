def add(a, b):
    return a + b


def multiplication(a, b):
    return a * b


def equals(number_1, number_2, func):
    return func(number_1, number_2)


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("What operation do you want? '+' or '*': ")


if operator == "+":
    result = equals(number_1=number1, number_2=number2, func=add)
elif operator == "*":
    result = equals(number_1=number1, number_2=number2, func=multiplication)
else:
    print("Please enter valid operator!")

print(result)
