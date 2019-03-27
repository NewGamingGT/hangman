import random
import os
import sys
import time
import drawhangman

def restart():
    time.sleep(1)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

def clearScreen():
    os.system("cls")

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
        print("Please enter one character")
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

array = ["","","","","","","","","","","","","","","","","","","","","","","",""]
totalGuess = 6

for i in range(0, len(randomWord)):
    array[i] = "_ "

os.system("cls")
print(">>> Welcome to Hangman!")
print("".join(array))
running(totalGuess)
