import random
import drawhangman
from gameflow import clearScreen, restart

def win():
    clearScreen()
    print("You Win")
    restart()

def lose():
    clearScreen()
    print("You lose")
    drawhangman.drawHangMan(totalGuess)
    print(f"The answer is: {randomWord}")
    restart()

def checkWin(totalGuess):
    if totalGuess > 0 and "".join(array) == randomWord:
        win()

def checkLose(totalGuess):
    if totalGuess == 0:
        lose()


def checkGuess(totalGuess):
    checkWin(totalGuess)

    clearScreen()
    print("Incorrect!")
    print(f"You have {totalGuess} guesses left")
    drawhangman.drawHangMan(totalGuess)
    print("".join(array))
    checkLose(totalGuess)

    running(totalGuess)

def running(totalGuess):
    checkWin(totalGuess)

    answer = input("Guess your letter: ")
    if answer.isdigit() or len(answer) > 1 or answer == "":
        print("Please enter one character and do not put numbers")
        running(totalGuess)
    else:
        for i in randomWord:
            if i.lower() == answer.lower():
                for x,y in enumerate(randomWord):
                    if(y == i):
                        array[x] = i
                print(" ".join(array))
                running(totalGuess)

        totalGuess -= 1
        checkGuess(totalGuess)

with open("sowpods.txt", 'r') as f:
    lines = f.readlines()

randomWord = random.choice(lines).strip()

array = []
totalGuess = 6

for _ in range(len(randomWord)):
    array.append("_ ")

clearScreen()
print(">>> Welcome to Hangman!")
print("".join(array))

running(totalGuess)
