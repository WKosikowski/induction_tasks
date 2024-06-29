#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from enum import Enum

# this solution was done based on https://supunsetunga.medium.com/writing-a-parser-getting-started-44ba70bb6cc9

class TokenType(Enum):
	ALPHABETICAL = 1
	NUMERICAL = 2
	SPACE = 3
	UNRECOGNISED = 4
	

class Token:
	def __init__(self, value: str, tokenType: TokenType):
		self.value = value
		self.tokenType = tokenType
		

class Lexer:
	def __init__(self, input):
		self.input = list(input)
		self.tokenIndex = 0
		
	def nextToken(self) -> Token:
		if self.tokenIndex < len(self.input):
			character = self.input[self.tokenIndex]
#			print(character)
			self.tokenIndex += 1
#			print(self.tokenIndex)
			if character == " ":
				return Token(character, TokenType.SPACE)
			elif character.isalpha():
				return Token(character, TokenType.ALPHABETICAL)
			elif character.isnumeric():
				return Token(character, TokenType.NUMERICAL)
			else:
				return Token(character, TokenType.UNRECOGNISED)
		return None


class Parser:
	grammar = [TokenType.ALPHABETICAL, TokenType.ALPHABETICAL, TokenType.NUMERICAL, TokenType.NUMERICAL, TokenType.SPACE, TokenType.ALPHABETICAL, TokenType.ALPHABETICAL, TokenType.ALPHABETICAL]
	def parse(self, input):
		lexer = Lexer(input)
		errors = []
		
		nextToken = lexer.nextToken()
		tokenIndex = 0
		while  nextToken != None:
			if tokenIndex <  len(Parser.grammar):
				if Parser.grammar[tokenIndex] != nextToken.tokenType:
					errors.append("Wrong token detected on position {}. Got {} but expected {}".format(tokenIndex+1, nextToken.tokenType, Parser.grammar[tokenIndex]))
				
			nextToken = lexer.nextToken()
			tokenIndex += 1
			
		if tokenIndex != len(Parser.grammar):
			errors.append("incorrect input string detected. Detected {} but expected {}".format(tokenIndex,  len(Parser.grammar)))
		return errors
				
		


