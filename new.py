import random
import os
import sys
import time

def drawHangMan(lives):
    if lives == 5:
        print("  __")
        print(" |/")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|__")
    elif lives == 4:
        print("  _______")
        print(" |/      |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|__")
    elif lives == 3:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|__")
    elif lives == 2:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|__")
    elif lives == 1:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |")
        print(" |")
        print(" |")
        print("_|__")
    else:
        print("You lose")
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \\|/")
        print(" |       |")
        print(" |      / \\")
        print(" |")
        print(" |")
        print("_|__")

def restart():
    time.sleep(1)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

def running(totalGuess):
    if "".join(array) == randomWord:
        os.system("cls")
        print("You Win")
        restart()
        return 0

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
        if  totalGuess > 0:
            if "".join(array) == randomWord:
                return 0
            else:
                os.system("cls")
                print("Incorrect!")
                print(f"You have {totalGuess} guesses left")
                drawHangMan(totalGuess)
                running(totalGuess) 
        else:
            os.system("cls")
            drawHangMan(totalGuess)
            restart()
            return 0
            


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
