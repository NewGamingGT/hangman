import random

with open("sowpods.txt", 'r') as f:
    lines = f.readlines()

randomWord = random.choice(lines).strip()
#TODO Make up a better name for this variable
array = []

for _ in range(len(randomWord)):
    array.append("_")

# Add starting characters
characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

probability = 10
for _ in range(probability):
	randomCharacters = random.choice(characters)
	for index, Value in enumerate(randomWord):
		if Value == randomCharacters:
			array[index] = Value

# Add first character as starting character
array[0] = randomWord[0]
