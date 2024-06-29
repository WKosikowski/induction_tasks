#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

import re



class Validifier:
	validFormat = format = re.compile("[A-Z]{2}[0-9]{2}[ ]{1}[A-Z]{3}") #correct format of a licence plate
	
	def isValid(self, licence):
		if Validifier.validFormat.match(licence): #if the format of the given licence plate is the same as validFormat
			return "valid"
		return "invalid"


validifier = Validifier()

print(validifier.isValid("AA22 AAA"))


