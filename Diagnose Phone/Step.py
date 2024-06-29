#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

class Step:
	
	def __init__(self, component, question, onPositiveAns = None, onNegativeAns=None):
		self.text = question
		self.onPositiveAns = onPositiveAns
		self.onNegativeAns = onNegativeAns
		self.parent = None
		self.component = component
		if onPositiveAns != None:
			self.onPositiveAns.parent = self
		if onNegativeAns != None:
			self.onNegativeAns.parent = self
			
	def isFinal(self):
		if self.onPositiveAns == None and self.onNegativeAns == None:
			return True
		else:
			return False
		
	def description(self):
		return self.text + self.parent.component