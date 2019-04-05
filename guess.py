from gameflow import clearScreen, restart
from drawhangman import drawHangMan
from randomword import randomWord, array

class Guess:

	def __init__(self, guessLeft):
		clearScreen()
		self.__guessLeft = guessLeft

	def incorrectGuess(self):

		clearScreen()

		self.__guessLeft -= 1

		if self.__guessLeft  != 0:
			print("Incorrect!")
			print(f"You have {self.__guessLeft} guesses left")

			drawHangMan(self.__guessLeft)
			print(" ".join(array))
		else:
			self.lose()

	def lose(self):
		clearScreen()

		print("You lose")
		drawHangMan(self.__guessLeft)
		print(f"The answer is: {randomWord}")
		restart()

	def win(self):
		clearScreen()

		drawHangMan(None)
		restart()
