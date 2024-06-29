#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from enum import Enum

class GameState(Enum):
	ONGOING = 1
	WON = 2
	LOST = 3



class Game:
	def __init__(self):
		self.incorrectCounter = 0 #counter for incorrect guesses
		self.state = GameState.ONGOING #the state of the game
		self.password = "" #the word to be guessed
		self.passwordHidden = [] #the word to be guessed in hidden format
		self.history = [] #past letters that have been guessed
		
	#set epassword and passwordHidden
	def getPassword(self, password):
		self.passwordHidden = []
		self.password = password
		print(password, self.password)
		for i in range(0, len(self.password)):
			self.passwordHidden.append("_ ")
		
	#check if given letter is in password
	def checkLetter(self, letter):
		if len(letter) != 1: #if te input is not one character long
			return
		inPassword = False
		if letter.isalpha() and letter not in self.history: #checks wether letter is alphabetical and if it was not already used
			for i in range(0, len(self.password)):
				if self.password[i].lower() == letter.lower():
					self.passwordHidden[i] = self.password[i]
					inPassword = True
			if not inPassword:
				self.incorrectCounter += 1
			self.history.append(letter)
			
	#ceck if game is won or lost
	def checkWin(self):
		if "_ " not in self.passwordHidden:
			self.state = GameState.WON
		if self.incorrectCounter >= 7:
			self.state = GameState.LOST
	
	#resets parameters for the next game
	def restart(self):
		self.incorrectCounter = 0
		self.state = GameState.ONGOING
		self.history = []
		
	
	