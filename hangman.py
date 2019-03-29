from drawhangman import drawHangMan
from gameflow import clearScreen, restart
from randomword import randomWord, array


def win():
    clearScreen()
    print("You Win")
    restart()


def lose():
    clearScreen()
    print("You lose")
    drawHangMan(totalGuess)
    print(f"The answer is: {randomWord}")
    restart()


def checkWin(totalGuess):
    if "".join(array) == randomWord:
        win()


def checkLose(totalGuess):
    if totalGuess == 0:
        lose()


def joinArray(array):
    print(" ".join(array))


def checkGuess(totalGuess):
    checkWin(totalGuess)

    clearScreen()
    
    print("Incorrect!")
    print(f"You have {totalGuess} guesses left")

    drawHangMan(totalGuess)
    joinArray(array)
    checkLose(totalGuess)

    running(totalGuess)


def checkInput():
    guessChar = input("Guess your letter: ")

    if guessChar.isdigit() or len(guessChar) > 1 or guessChar == "":
        print("Please enter one character and do not put numbers")
        running(totalGuess)
    else:
        return guessChar


def running(totalGuess):

    checkWin(totalGuess)

    guessChar = checkInput()

    for i in randomWord:
        if i.lower() == guessChar.lower():
            for x, y in enumerate(randomWord):
                if(y == i): array[x] = i

            joinArray(array)
            running(totalGuess)

    totalGuess -= 1
    checkGuess(totalGuess)

totalGuess = 6

clearScreen()
print(">>> Welcome to Hangman!")
joinArray(array)

running(totalGuess)
