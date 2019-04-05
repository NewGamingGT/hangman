from randomword import randomWord, array
from guess import Guess


def main():
	guessLeft = Guess(6)

	print(">>> Welcome to Hangman!")
	print(" ".join(array))

	while True:
		correctGuess = False
		guessCharacter = getInput()

		correctGuess = guessIsCorrect(guessCharacter, correctGuess)

		print(" ".join(array))

		if correctGuess != True:
			guessLeft.incorrectGuess()
		else:
			if "".join(array) == randomWord:
				guessLeft.win()

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

if __name__ == '__main__':
    main()
