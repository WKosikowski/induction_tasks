#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from Calculator import *
import unittest

class CalculatorTests(unittest.TestCase):
	def test_mode_happyPath(self):
		calculator = Calculator([1,1,1,2,3,4,5])
		self.assertEqual(calculator.mode(), 1)
	
	def test_mode_noMode(self):
		calculator = Calculator([1,2,3,4,5,6,7])
		self.assertEqual(calculator.mode(), None)
		
	def test_mode_oneElement(self):
		calculator = Calculator([1])
		self.assertEqual(calculator.mode(), 1)
		
	
if __name__ == '__main__':
	unittest.main()