#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

import PySimpleGUI as sg
from Colour import Colour 

colour = Colour(0, 0, 0)
hexOutput = sg.Text(colour.hex())

# All the stuff inside your window.
layout = [  [sg.Text("Enter RGB Value in decimal.")],
			[sg.Slider(range = (0,255), resolution = 1, tick_interval = 255, enable_events=True),
				sg.Slider(range = (0,255), resolution = 1, enable_events=True),
				sg.Slider(range = (0,255), resolution = 1, enable_events=True)
			],
			[sg.Button('Ok')],
			[hexOutput]]

# Create the Window
window = sg.Window('RGB to HEX', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	
	# if user closes window or clicks cancel
	if event == sg.WIN_CLOSED or event == 'Cancel':
		break
	colour.red = int(values[0])
	colour.green = int(values[1])
	colour.blue = int(values[2])
	hexOutput.update(value = colour.hex())
window.close()