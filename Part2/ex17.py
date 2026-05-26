import random

name = input("What is your name?\n")

animals=('Otter', 'Lion', 'Rabbit', 'Turtle', 'Bear', 'Whooper')
adjectives=('Brave ', 'Curious ', 'Generous ', 'Honest ', 'Creative ', 'Energetic ')

codename = (random.choice(adjectives)+random.choice(animals))

number = (random.randint(1,99))

print(f"{name }, your codename is : {codename }")
print(f"Your lucky number is : {number}")