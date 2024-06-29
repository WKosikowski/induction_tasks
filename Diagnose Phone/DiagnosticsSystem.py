#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from Step import Step

class DiagnosticsSystem():
	def start(self):
		outcome2 = Step(None, "Looks like your phone is in working condition")
		outcome1 = Step(None, "Looks like your phone has damaged ")
		q5 = Step("Battery", "Is the phone fully charged?", outcome1, outcome2)
		q4 = Step("", "Is the phone turned on?", q5, outcome1)
		q3 = Step("Screen", "Does the screen work?", outcome1, q4)
		q2 = Step("Electronics", "Has the phone been dropped?", outcome1, q3)
		q1 = Step("Electronics", "Has the phone got wet?", outcome1, q2)	
		
		currentStep = q1
		
		print("This is a phone troubleshooting system, please answer the following questions.")
		
		while not currentStep.isFinal():
			if input(currentStep.text + "\n") == "yes":
				currentStep = currentStep.onPositiveAns
			else:
				currentStep = currentStep.onNegativeAns
		
		print(currentStep.description())
		print("\n\tThank you for using our system.")
		
		
