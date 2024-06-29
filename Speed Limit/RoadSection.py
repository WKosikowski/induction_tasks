#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

import datetime

class RoadSection:
	def __init__(self, limit, distance):
		self.speedLimit = limit
		self.distance = distance
	
	def speed(self, time):
		return self.distance / time
	
	def isOverLimit(self, inTime, outTime):
		speed = self.speed((outTime - inTime).total_seconds() / (60*60))
		if inTime == outTime:
			return None
		return [speed, abs(speed) > self.speedLimit]


