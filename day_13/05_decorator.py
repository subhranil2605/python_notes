# In python everything is object


def greet():
    return "Hello Rutuja"


my_func = greet


print(my_func())
print(my_func is greet)
print(my_func == greet)
