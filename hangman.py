from randomword import randomWord, array
from guess import Game


def main():
	totalGuess = 6
	game = Game(totalGuess)

	print(">>> Welcome to Hangman!")
	print(" ".join(array))

	while True:
		correctGuess = False
		guessCharacter = getInput()

		# returns true if the player guessed one of the character correctly
		isCorrectGuess = guessIsCorrect(guessCharacter, correctGuess)

		print(" ".join(array))

		if isCorrectGuess != True:
			game.incorrectGuess()
		else:
			# win the game is the function returns true
			if AllCharacterIsCorrect():
				game.win()

	return 0


def getInput():
	while True:
		guessCharacter = input("Guess your letter: ")
		# Check if the input is a number or more than one character or the input is empty
		if guessCharacter.isdigit() or len(guessCharacter) > 1 or guessCharacter == "":
			print("Please enter one character and do not put numbers")
		else:
			return guessCharacter


def guessIsCorrect(charGuess, isCorrectGuess):
	# Loop through the random word and see if the character guessed is equal to one of the character in random word
	for index, char in enumerate(randomWord):
		if char.lower() == charGuess.lower():
			isCorrectGuess = True
			array[index] = char

	return isCorrectGuess

# Returns true if the list of characters is equal to the random word generated
def AllCharacterIsCorrect():
	if "".join(array) == randomWord:
		return True

if __name__ == '__main__':
    main()
