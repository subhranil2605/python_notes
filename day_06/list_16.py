import random

names = ["Rutuja", "Pratiksha", "Subhranil"]

winner = random.choice(names)
print(winner)

random.shuffle(names)
print(names)
