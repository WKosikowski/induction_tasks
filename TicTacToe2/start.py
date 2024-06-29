#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

import PySimpleGUI as sg
from game import *
from fileHandler import FileHandler


def main():
	fileHandler = FileHandler
	stats = FileHandler.read()
	
	game = Game(int(stats[0]), int(stats[1]), int(stats[2]) )
	
	buttonsdGrid = []
	for i in range (0,9):
		buttonsdGrid.append(sg.Button(game.grid[i].value, size=(3,3), button_color=("white", "navyblue"), key = i))
		
	infoText = sg.Text("It's now player {} turn".format(game.state.value), auto_size_text=True)
	winHistoryText = sg.Text("Player X Wins: {}\nPlayer O Wins: {}\nDraws: {}".format(game.winHistory_X, game.winHistory_O, game.winHistory_Draw), auto_size_text=True)
	
	layout =[[buttonsdGrid[0], buttonsdGrid[1], buttonsdGrid[2]],
			[buttonsdGrid[3], buttonsdGrid[4], buttonsdGrid[5]],
			[buttonsdGrid[6], buttonsdGrid[7], buttonsdGrid[8]],
			[sg.Button("restart"), infoText ],
			[winHistoryText]]
	
	window = sg.Window('TicTacToe', layout)
	
	while True:
		event, values = window.read()
		
		if event == sg.WIN_CLOSED:
			fileHandler.save(game.winHistory_X, game.winHistory_O, game.winHistory_Draw)
			
			break
		
		if event == "restart":
			game.reset()
		elif game.state == GameState.ONGOINGX or game.state == GameState.ONGOINGO:
			game.mark(event)
			
		if game.state == GameState.ONGOINGX or game.state == GameState.ONGOINGO :
			infoText.update("It's now player {} turn".format(game.state.value))
			infoText.update(text_color="white")
		elif game.state == GameState.OWIN:
			infoText.update("O wins")
			infoText.update(text_color="red")
		elif game.state == GameState.XWIN:
			infoText.update("X wins")
			infoText.update(text_color="red")
		elif game.state == GameState.DRAW:
			infoText.update("Draw!")
			infoText.update(text_color="yellow")
		for i in range(0,9):
			buttonsdGrid[i].update(game.grid[i].value)
			if game.grid[i] == TileState.NONE:
				buttonsdGrid[i].update(button_color=("navyblue", "navyblue"))
			else:
				buttonsdGrid[i].update(button_color=("navyblue", "white"))
		
		winHistoryText.update("Player X Wins: {}\nPlayer O Wins: {}\nDraws: {}".format(game.winHistory_X, game.winHistory_O, game.winHistory_Draw))
		
	window.close()
	
	
main()