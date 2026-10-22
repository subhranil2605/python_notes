def my_func():
    print("Program started")
    yield 10  # pause 1
    # resume

    print("Program is in the middle of execution")
    yield 20  # pause 2

    print("Program stopped")


gen = my_func()

# print(gen)
print(next(gen))
print(next(gen))
