#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from Calculator import *

class Program:
	def start(self):
		print("enter numbers in series seperated by spaces\n")
		enteredData = input()
		enteredData = enteredData.split()
		
		
		numbers = [int(i) for i in enteredData]
		
		print(numbers)
		calculator = Calculator(numbers)
		print("mean: ", calculator.mean())
		print("median: ", calculator.median())
		print("mode: ", calculator.mode())
		
Program().start()
