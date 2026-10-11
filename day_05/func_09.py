# Positional argument


def full_name(first_name: str, last_name: str) -> str:
    return f"{first_name.strip()} {last_name.strip()}".title()


print(full_name("rUTUJA", "      DEshmukh       "))


print(full_name(first_name="Subhranil", last_name="Sarkar"))
print(full_name(last_name="Sarkar", first_name="Subhranil"))

print(full_name("Sarkar", "Subhranil"))

# def calculate(*args, **kwargs):
#     # args -> tuple
#     # kwargs -> dict 
