#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from tile import TileState
from enum import Enum

class GameState(Enum):
	ONGOINGO = 1
	ONGOINGX = 2
	DRAW = 3
	XWIN = 4
	OWIN = 5
	

class Game:
	def __init__(self, winHistory_X, winHistory_O, winHistory_Draw):
		self.state = None
		self.grid = []		
		self.reset()
		self.winHistory_X = winHistory_X
		self.winHistory_O = winHistory_O
		self.winHistory_Draw = winHistory_Draw
		
		
	def reset(self):
		self.state = GameState.ONGOINGO
		self.grid = [TileState.NONE, TileState.NONE, TileState.NONE, TileState.NONE, TileState.NONE, TileState.NONE, TileState.NONE, TileState.NONE, TileState.NONE]
		
		
	def mark(self, index):
		if index > -1 and index < 9:
			if self.state == GameState.ONGOINGX and self.grid[index] == TileState.NONE:
				print("was", self.state)
				self.grid[index] = TileState.X
				self.state = GameState.ONGOINGO
				print("is", self.state)
			elif self.state == GameState.ONGOINGO and self.grid[index] == TileState.NONE:
				print("was", self.state)
				self.grid[index] = TileState.O
				self.state = GameState.ONGOINGX
				print("is", self.state)
		self.checkWin()	
			
	def checkWin(self):
		self.singleCheckWin(0, 4, 8)
		self.singleCheckWin(2, 4, 6)
		
		self.singleCheckWin(0, 1, 2)
		self.singleCheckWin(3, 4, 5)
		self.singleCheckWin(6, 7, 8)
		
		self.singleCheckWin(0, 3, 6)
		self.singleCheckWin(1, 4, 7)
		self.singleCheckWin(2, 5, 8)
		
		
		if TileState.NONE not in self.grid and (self.state == GameState.ONGOINGO or self.state == GameState.ONGOINGX):
			self.state = GameState.DRAW
			self.winHistory_Draw += 1
		
	def singleCheckWin(self, tile1, tile2, tile3):
		if self.grid[tile1] == self.grid[tile2] and self.grid[tile1] == self.grid[tile3]:
			if self.grid[tile1] == TileState.X:
				self.state = GameState.XWIN
				self.winHistory_X += 1
			elif self.grid[tile2] == TileState.O:
				self.state = GameState.OWIN
				self.winHistory_O += 1
	
	