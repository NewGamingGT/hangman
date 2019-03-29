import random

with open("sowpods.txt", 'r') as f:
    lines = f.readlines()

randomWord = random.choice(lines).strip()

array = []

for _ in range(len(randomWord)):
    array.append("_")
