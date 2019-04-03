from drawhangman import drawHangMan
from gameflow import clearScreen, restart
from randomword import randomWord, array

guessLeft = 6

def main():
	clearScreen()
	print(">>> Welcome to Hangman!")
	print(" ".join(array))

	while True:
		correctGuess = False
		guessCharacter = getInput()

		correctGuess = guessIsCorrect(guessCharacter, correctGuess)

		print(" ".join(array))

		if correctGuess != True:
			incorrectGuess()
		else:
			if "".join(array) == randomWord:
				win()

	return 0


def getInput():
	while True:
		guessCharacter = input("Guess your letter: ")

		if guessCharacter.isdigit() or len(guessCharacter) > 1 or guessCharacter == "":
			print("Please enter one character and do not put numbers")
		else:
			return guessCharacter


def guessIsCorrect(charGuess, correctGuess):
    for index, char in enumerate(randomWord):
        if char.lower() == charGuess.lower():
            correctGuess = True
            array[index] = char
    return correctGuess


def win():
	clearScreen()

	drawHangMan(None)
	restart()


def incorrectGuess():
	global guessLeft

	clearScreen()

	guessLeft -= 1

	if guessLeft != 0:
		print("Incorrect!")
		print(f"You have {guessLeft} guesses left")

		drawHangMan(guessLeft)
		print(" ".join(array))
	else:
		lose()


def lose():
	clearScreen()

	print("You lose")
	drawHangMan(guessLeft)
	print(f"The answer is: {randomWord}")
	restart()

main()