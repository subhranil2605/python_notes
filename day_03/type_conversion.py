# Casting
# str -> float -> int

# Implicit Casting (automatic)

x = 5  # int
y = 6.6  # float

# Python automatically casts x to 5.0 before adding
result = x + y
# print(result)

# Explicit casting
# int()
# float()
# str()
# bool()

# list()
# tuple()
# dict()
# set()

# ----

int_value = 20
float_value = 4.5
string_value = "Rutuja"
boolean_value = True

# int()

# float -> int
print(int(float_value))

# str -> int
# string is numeric (.isnumeric()) -> int
# int("45") -> 45 ✅
# int("45.5") -> ❌

# bool -> int

# -----
# float()

# int -> float
print(float(int_value))

# str -> float
print(float("45"))
print(float("45.45"))

# bool -> float
print(float(True))

# -----
# str()

# int -> str
print(str(int_value))

# float -> str
print(str(float_value))


# ----
# bool()
print(bool(0)) # falsy
print(bool(1))

# Truthy and Falsy

print(bool(-145)) # truthy
print(bool("Rutuja")) # truthy
print(bool("")) # falsy


print(bool([1, 2, 3])) # truthy
print(bool([])) # falsy


