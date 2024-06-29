#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

import PySimpleGUI as sg
from Button import Button
from player import Player


LUbutton = sg.Button("", key = "LU", enable_events=True)
LCbutton = sg.Button("", key = "LC", enable_events=True)
LDbutton = sg.Button("", key = "LD", enable_events=True)

CUbutton = sg.Button("", key = "CU", enable_events=True)
CCbutton = sg.Button("", key = "CC", enable_events=True)
CDbutton = sg.Button("", key = "CD", enable_events=True)

RUbutton = sg.Button("", key = "RU", enable_events=True)
RCbutton = sg.Button("", key = "RC", enable_events=True)
RDbutton = sg.Button("", key = "RD", enable_events=True)

gameStateText = sg.Text("game is ongoing")

layout = [[LUbutton, CUbutton, RUbutton],
		  [LCbutton, CCbutton, RCbutton],
		  [LDbutton, CDbutton, RDbutton],
		  [sg.Button("restart")],
		  [gameStateText]]


window = sg.Window('Hello Example', layout)

player = Player()
gameEnd = False

while True:
	event, values = window.read()
	

	if event == "LU" and not gameEnd:
		player.toggleTurn(LUbutton.GetText(), gameEnd)
		LUbutton.update(player.turn, )
	if event == "LC" and not gameEnd:
		player.toggleTurn(LCbutton.GetText(), gameEnd)
		LCbutton.update(player.turn)
		
	if event == "LD" and not gameEnd:
		player.toggleTurn(LDbutton.GetText(), gameEnd)
		LDbutton.update(player.turn)
		
	
	if event == "RU" and not gameEnd:
		player.toggleTurn(RUbutton.GetText(), gameEnd)
		RUbutton.update(player.turn)
	if event == "RC" and not gameEnd:
		player.toggleTurn(RCbutton.GetText(), gameEnd)
		RCbutton.update(player.turn)
	if event == "RD" and not gameEnd:
		player.toggleTurn(RDbutton.GetText(), gameEnd)
		RDbutton.update(player.turn)
		
		
	if event == "CU" and not gameEnd:
		player.toggleTurn(CUbutton.GetText(), gameEnd)
		CUbutton.update(player.turn)
	if event == "CC" and not gameEnd:
		player.toggleTurn(CCbutton.GetText(), gameEnd)
		CCbutton.update(player.turn)
	if event == "CD" and not gameEnd:
		player.toggleTurn(CDbutton.GetText(), gameEnd)
		CDbutton.update(player.turn)
		
		
		
	if event == "restart":
		LUbutton.update("")
		LCbutton.update("")
		LDbutton.update("")
		
		CUbutton.update("")
		CCbutton.update("")
		CDbutton.update("")
		
		RUbutton.update("")
		RCbutton.update("")
		RDbutton.update("")
		
		gameEnd = False
		
		gameStateText.update("game is ongoing")
	
	
	if LUbutton.GetText() != "" and LCbutton.GetText() != "" and LDbutton.GetText() != "" and CUbutton.GetText() != "" and CCbutton.GetText() != "" and CDbutton.GetText() != "" and RUbutton.GetText() != "" and RCbutton.GetText() != "" and RDbutton.GetText() != "":
		gameEnd = True
		gameStateText.update("game ended in a draw")
		print("game ended")
	
	
	if LUbutton.GetText() == "X" and CCbutton.GetText() == "X" and RDbutton.GetText() == "X" or LUbutton.GetText() == "X" and LUbutton.GetText() == "X" and LUbutton.GetText() == "X":
		
	
	print(event)
	
window.close()