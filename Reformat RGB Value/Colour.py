#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024


class Colour:
	hexFormat = '#{:02X}{:02X}{:02X}'
	def __init__(self, red, green, blue):
		self.red = Colour.adjustToRGBRange(red)
		self.green = Colour.adjustToRGBRange(green)
		self.blue = Colour.adjustToRGBRange(blue)
		
	def hex(self):
		return Colour.hexFormat.format(self.red, self.green, self.blue) 
	
	def adjustToRGBRange(value):
		return max(min(value, 255), 0)

