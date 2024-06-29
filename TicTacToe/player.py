#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

class Player:
	def __init__(self):
		self.turn = "O"
	
	def toggleTurn(self, currentOccupation, gameEnd):
		if self.turn == "X" and currentOccupation == "" and not gameEnd:
			self.turn = "O"
		elif self.turn == "O" and currentOccupation == "" and not gameEnd:
			self.turn = "X"