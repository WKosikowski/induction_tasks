#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

class Calculator:
	def __init__(self, numbers):
		self.numbers = numbers
		self.numbers.sort()
		
	
	def mean(self):
		print(self.numbers)
		return sum(self.numbers) / len(self.numbers)
	
	def median(self):
		medianPos = len(self.numbers) // 2
		if len(self.numbers) % 2 == 1:
			return self.numbers[medianPos]
		if len(self.numbers) % 2 == 0:
			return ( self.numbers[medianPos] + self.numbers[medianPos - 1] ) / 2
	
	def mode(self):
		mode = 0
		modeOccourence = 0
		for num in self.numbers:
			counter = 0
			for checkNum in self.numbers:
				if checkNum == num:
					counter += 1
			if counter > modeOccourence:
				mode = num
				modeOccourence = counter
		if modeOccourence == 1:
			return None
		return mode

