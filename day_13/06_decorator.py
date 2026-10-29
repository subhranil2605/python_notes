def greet_extender(func):
    def greet():
        print("Very Good evening")

        result = func()
        print(result)

        print("Bye, will meet you soon")
        return result

    return greet


def greet_rutuja():
    return "Hello Rutuja"

def greet_subhranil():
    return "Hello Subhranil"

greet_rutuja = greet_extender(greet_rutuja)
greet_subhranil = greet_extender(greet_subhranil)

greet_rutuja()
greet_subhranil()
