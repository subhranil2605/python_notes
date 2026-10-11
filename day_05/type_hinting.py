# x = 5

# Annotation
# Type Hinting

# explicitly telling the type of variables
x: int = 5
y: float = 3.14
name: str = "Rutuja"


def add(x: float | str, y: float | str) -> float | str:
    if isinstance(x, str) and isinstance(y, str):
        return x + y
    if isinstance(x, float) and isinstance(y, float):
        return x + y
    else:
        return "Not possible"


add(5, 8)
add(5.6, 8.5)
print(add("Rutuja", "Deshmukh"))
print(add("Rutuja", 5.5))
