#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024


import unittest
from solution2 import Parser
from solution2 import Lexer
from solution2 import TokenType
class ParserTests(unittest.TestCase):
	def test_parser_valid(self):
		parser = Parser()
		self.assertEqual(parser.parse("AA11 AAA"), [])
	
	def test_parser_short(self):
		parser = Parser()
		self.assertEqual(parser.parse("AA11 "), ['incorrect input string detected. Detected 5 but expected 8'])
		
	def test_parser_long(self):
		parser = Parser()
		self.assertEqual(parser.parse("AA11 AAABBDRRYHY"), ['incorrect input string detected. Detected 16 but expected 8'])
		
	def test_parser_invalidSymbols(self):
		parser = Parser()
		self.assertEqual(parser.parse("1AA2_rf3"), ['Wrong token detected on position 1. Got TokenType.NUMERICAL but expected TokenType.ALPHABETICAL', 'Wrong token detected on position 3. Got TokenType.ALPHABETICAL but expected TokenType.NUMERICAL', 'Wrong token detected on position 5. Got TokenType.UNRECOGNISED but expected TokenType.SPACE', 'Wrong token detected on position 8. Got TokenType.NUMERICAL but expected TokenType.ALPHABETICAL'])
		
	
	

class LexerTests(unittest.TestCase):
	def test_lexer_valid(self):
		input = "abc123 e234£"
		lexer = Lexer(input)
		list = []
		for i in input:
			list.append(lexer.nextToken().tokenType)
		self.assertEqual(list,  [TokenType.ALPHABETICAL,
			TokenType.ALPHABETICAL,
			TokenType.ALPHABETICAL,
			TokenType.NUMERICAL,
			TokenType.NUMERICAL,
			TokenType.NUMERICAL,
			TokenType.SPACE,
			TokenType.ALPHABETICAL,
			TokenType.NUMERICAL,
			TokenType.NUMERICAL,
			TokenType.NUMERICAL,
			TokenType.UNRECOGNISED])
	
if __name__ == '__main__':
	unittest.main()