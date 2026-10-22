from collections.abc import Iterable, Iterator

things = {
    "list": [1, 2],
    "str": "Rutuja",
    "dict": {"a": 1},
    "range": range(3),
    "list_iterator": iter([1, 2, 3]),
}

print(f"{'object':<14} {'iterable?':<10} {'iterator?'}")
for name, obj in things.items():
    print(f"{name:<14} {isinstance(obj, Iterable)!s:<10} {isinstance(obj, Iterator)}")
