#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

import random
from enum import Enum


class Difficulty(Enum):
	EASY = 1
	NORMAL = 2
	HARD = 3

class Reader:
	def __init__(self):
		self.file = None
		self.difficulty = Difficulty.EASY
		
	def openFile(self):
		self.file = open("words.txt", "r")
		
	def closeFile(self):
		self.file.close()
	
	def decideDifficulty(self, difficulty):
		if difficulty == "Easy":
			self.difficulty = Difficulty.EASY
		if difficulty == "Normal":
			self.difficulty = Difficulty.NORMAL
		if difficulty == "Hard":
			self.difficulty = Difficulty.HARD
	
	#returns a random word based on set difficulty
	def getWord(self):
		words = self.file.read().split("\n")
		wordsSplit = []
		for i in words:
			if i.split(" ")[0] == "e:" and self.difficulty == Difficulty.EASY:
				wordsSplit.append(i.split(" ")[1])
			if i.split(" ")[0] == "n:" and self.difficulty == Difficulty.NORMAL:
				wordsSplit.append(i.split(" ")[1])
			if i.split(" ")[0] == "h:" and self.difficulty == Difficulty.HARD:
				wordsSplit.append(i.split(" ")[1])
			
		return wordsSplit[random.randint(0, len(wordsSplit) - 1)]

	