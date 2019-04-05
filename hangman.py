from randomword import randomWord, array
from guess import Game


def main():
	game = Game(6)

	print(">>> Welcome to Hangman!")
	print(" ".join(array))

	while True:
		correctGuess = False
		guessCharacter = getInput()

		correctGuess = guessIsCorrect(guessCharacter, correctGuess)

		print(" ".join(array))

		if correctGuess != True:
			game.incorrectGuess()
		else:
			if AllCharacterIsCorrect():
				game.win()

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

def AllCharacterIsCorrect():
	if "".join(array) == randomWord:
		return True

if __name__ == '__main__':
    main()
