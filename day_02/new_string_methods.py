# translate

table = str.maketrans(
    {
        "a": "x",
        "b": "y",
        "c": None,  # delete c
    }
)

result = "abc123".translate(table)
print(result)

