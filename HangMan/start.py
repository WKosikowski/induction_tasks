#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from game import *
from fileReader import *
import PySimpleGUI as sg

#game and file reader is created
game = Game()
fileReader = Reader()
fileReader.openFile()

#the initial password for the game is set
game.getPassword(fileReader.getWord())
fileReader.closeFile()

#GUI text is created for the hidden password
hiddenPassword = sg.Text("".join(game.passwordHidden), font = ("Calibri", 32))
failedGuessesText = sg.Text("Failed guesses: 0\nTry not to go above 7!")

#input box, combo and text displaying previously guessed characters is created
inputBox = sg.InputText(enable_events=True)
historyText = sg.Text("used characters: " + ", ".join(game.history))
difficultyCombo = sg.Combo(["Easy", "Normal", "Hard"], default_value="Easy", enable_events=True)

#layout for the window is created
layout = [[hiddenPassword],
	[sg.Text("Enter your guess:"), inputBox],  
	[sg.Button("Enter")],
	[failedGuessesText],
	[historyText],
	[sg.Button("Restart"), difficultyCombo]]

#window is created
window = sg.Window('Hangman', layout, size=(300,230), return_keyboard_events=True)

#game is ran through a loop until the window is closed
while True:
	event, values = window.read()
	
	if (event == "Enter" or event == "Return:603979789") and len(values) > 0 and game.state == GameState.ONGOING: #when enter is pressed, there is an input and the game is ongoing
		#game checks if the letter is in the password	
		game.checkLetter(values[0])
		#the box is cleared
		inputBox.update("")
	if event == sg.WIN_CLOSED or event == 'Cancel': #when the window is closed
		break #loop breaks and the program stops
	
	#difficulty of password is decided before restart
	fileReader.decideDifficulty(values[1])	
	
	if event == "Restart": #when the restart button is pressed
		#values are reset
		fileReader.openFile() 
		game.restart() 
		newPassword = fileReader.getWord()
		game.getPassword(newPassword)
		fileReader.closeFile()
		
		
	
		
	#texts and boxes are reset
	hiddenPassword.update("".join(game.passwordHidden), text_color="white")
	historyText.update("used characters: " + ", ".join(game.history))
	
	#game checks if you won or lost
	game.checkWin()
	
	#the text is updated based on game.state
	if game.state == GameState.ONGOING:
		failedGuessesText.update("Failed guesses: {}\nTry not to go above 7!".format(game.incorrectCounter))
	elif game.state == GameState.LOST:
		failedGuessesText.update("You have failed to guess the word")
		hiddenPassword.update(game.password, text_color="red")
	elif game.state == GameState.WON:
		failedGuessesText.update("You have guessed the word correctly!")
		hiddenPassword.update(game.password, text_color="yellow")
	

		
window.close()
