# What a `for` loop really does

# When you write `for item in orders`, Python quietly does three things:

# 1. It calls `iter(orders)` to get an iterator.
# 2. It calls `next()` on that iterator again and again, giving you each value.
# 3. When the iterator has nothing left, it raises a special exception called `StopIteration`. Then the for loop catches it and ends.

orders = ["PEN-01", "INK-02", "STAPLER"]

# for order in orders:
#     print(order)

iterator = iter(orders)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print("processing", item)
