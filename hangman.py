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


def incorrectGuess(totalGuess):
	clearScreen()

	if totalGuess != 0:
		print("Incorrect!")
		print(f"You have {totalGuess} guesses left")

		drawHangMan(totalGuess)
		print(" ".join(array))
	else:
		lose()

	running(totalGuess)

def checkInput():
    guessChar = input("Guess your letter: ")

    if guessChar.isdigit() or len(guessChar) > 1 or guessChar == "":
        print("Please enter one character and do not put numbers")
        running(totalGuess)
    else:
        return guessChar


def running(totalGuess):
    correct = False
    guessChar = checkInput()

    for value, char in enumerate(randomWord):
        if char.lower() == guessChar.lower():
            correct = True
            array[value] = char

    print(" ".join(array))

    if correct != True:
        totalGuess -= 1
        incorrectGuess(totalGuess)
    else:
        if "".join(array) == randomWord:
        	win()

    running(totalGuess)


totalGuess = 6

clearScreen()
print(">>> Welcome to Hangman!")
print(" ".join(array))

running(totalGuess)
