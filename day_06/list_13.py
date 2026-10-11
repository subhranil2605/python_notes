languages = ["Marathi", "Bengali", "Urdu", "English"]

# rutuja_speaking = languages[0]
# subhranil_speaking = languages[1]
# buttler_speaking = languages[2]

# Multiple assignment trick
# unpacking the list
# rutuja_speaking, subhranil_speaking, buttler_speaking = languages


# rutuja_speaking, _ , _ = languages

# rutuja_speaking, *others = languages
rutuja_speaking, *others, x = languages

print(rutuja_speaking)
print(others)
print(x)


