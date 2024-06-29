#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

import random
			
			
class Question:
	def __init__(self, text, answer):
		self.text = text
		self.answer = answer


class QuestionGenerator:
	def generateQuestions(self, noOfQuestions):
		return []

class GeoQuestionGenerator(QuestionGenerator):
	database = [Question("Which place is further south. London or York?", "London"),
				Question("What colour is used to show a lake on a map?", "Blue"),
				Question("What river flows through London?", "Thames")]
	
	
	def generateQuestions(self, noOfQuestions):
		return random.sample(GeoQuestionGenerator.database, min(len(GeoQuestionGenerator.database), noOfQuestions))


class MathQuestionGenerator(QuestionGenerator):
	def generateQuestion(self):
		num1 = random.randint(0, 10)
		num2 = random.randint(0, 10)
		operation = random.randint(0, 2)
		text = ""
		answer = 0
		if operation == 0:
			text = "what is " + str(num1) + " + " + str(num2)
			answer = num1 + num2
		if operation == 1:
			text = "what is " + str(num1) + " - " + str(num2)
			answer = num1 - num2
		if operation == 2:
			text = "what is " + str(num1) + " * " + str(num2)
			answer = num1 * num2
		return Question(text, answer)
	
	def generateQuestions(self, noOfQuestions):
		quiz = []
		for i in range(0,int(noOfQuestions)):
			quiz.append(self.generateQuestion())
		return quiz


class GeneralQuizGenerator(QuestionGenerator):
	def __init__(self):
		self.generators = [MathQuestionGenerator(), GeoQuestionGenerator()]
#		print(self.generators)
		
	def generateQuestions(self, noOfQuestions):
		questions = []
		for gen in self.generators:
			questions += gen.generateQuestions(noOfQuestions/len(self.generators))
		return questions
			
class Quiz:
	def __init__(self, questions):
		self.questions = questions
		self.name = ""
		self.score = 0
		
	def start(self):
		self.name = input("what is your name?\n")
		for question in self.questions:
			answer = input(question.text + "\n")
			if answer.lower() == str(question.answer).lower():
				print("correct\n")
				self.score += 1
			else:
				print("incorrect, it's " + str(question.answer))
		print("\n\tYou have answered " + str(self.score) + " questions correctly.")
		

