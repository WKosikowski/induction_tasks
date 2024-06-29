#!/usr/bin/env python3
import random
# Wojciech Kosikowski (c) 2024

class Game:
	def __init__(self):
		self.number = random.randint(1, 9)
		self.guess = None
		self.answersCorrect = 0
		self.guesses = 0

		
	def randomiseNum(self, min, max):
		self.number = random.randint(min, max)

	def start(self):
		while self.guess != "exit":
			print("please guess a number between 0 and 9")
			self.guess = input()
			if self.guess != "exit":
				self.guesses += 1
				if int(self.guess) == self.number:
					print("correct answer in", self.guesses, "guesses", "\n")
					self.guesses = 0
					self.answersCorrect +=1
					self.randomiseNum(1, 9)
				elif int(self.guess) > self.number:
					print("too high\n")
				elif int(self.guess) < self.number:
					print("too low\n")
		print("correct answers:", self.answersCorrect)
					

game = Game()
game.start()