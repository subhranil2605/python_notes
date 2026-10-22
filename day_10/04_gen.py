import tracemalloc


def amounts_as_list(n):
    result = []
    for i in range(n):
        result.append(i % 500 + 1)
    return result


def amounts_as_generator(n):
    for i in range(n):
        yield i % 500 + 1


def peak_memory(x, n=1_000_000):
    # Start the stopwatch
    tracemalloc.start()

    # Calculate the sum of the products
    total = sum(x(n))

    # Read the stopwatch
    _current, peak = tracemalloc.get_traced_memory()

    # Stop the stopwatch
    tracemalloc.stop()

    return total, peak


for func in [amounts_as_list, amounts_as_generator]:
    total, peak = peak_memory(func)

    print(f"{func.__name__} total={total:,} peak_memory={peak:,} bytes")

# print(f"{328 / 24_064_768:%}")
# 0.001%
