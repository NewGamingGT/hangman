from gamemanager import clearScreen, restart
from drawASCII import drawHangMan, drawWin
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
			# lose the game is the guess left is equal to zero
			Game.lose(self)

class Game(Guess):


	def lose(self):
		clearScreen()

		print("You lose")
		drawHangMan(Guess.getGuessLeft)
		print(f"The answer is: {randomWord}")
		restart()


	def win(self):
		drawWin()
		restart()
