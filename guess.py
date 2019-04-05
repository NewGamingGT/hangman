from gamemanager import clearScreen, restart
from drawhangman import drawHangMan
from randomword import randomWord, array

class Guess:

	def __init__(self, guessLeft):
		clearScreen()
		self.__guessLeft = guessLeft

	def getGuessLeft(self):
		return self.__guessLeft

	def incorrectGuess(self):

		clearScreen()

		self.__guessLeft -= 1

		if self.__guessLeft  != 0:
			print("Incorrect!")
			print(f"You have {self.__guessLeft} guesses left")

			drawHangMan(self.__guessLeft)
			print(" ".join(array))
		else:
			Game.lose(self)

class Game(Guess):

	def lose(self):
		clearScreen()

		print("You lose")
		drawHangMan(Guess.getGuessLeft(self))
		print(f"The answer is: {randomWord}")
		restart()

	def win(self):
		clearScreen()

		drawHangMan(Guess.getGuessLeft(self))
		restart()
