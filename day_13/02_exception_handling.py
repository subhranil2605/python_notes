import sys


def linux_interaction():
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux system")

    # mocking
    print("Doing linux things")


try:
    linux_interaction()
except RuntimeError as error:
    print(error)
