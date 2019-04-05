import random

with open("sowpods.txt", 'r') as f:
    lines = f.readlines()

randomWord = random.choice(lines).strip()
#TODO Make up a better name for the variable
array = []

for _ in range(len(randomWord)):
    array.append("_")

# Add starting characters
#characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#for _ in range(10):
#	for index, Value in enumerate(randomWord):
#		if Value == random.choice(characters):
#			array[index] = Value
