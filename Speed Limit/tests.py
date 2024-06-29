#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

from RoadSection import *
import unittest

class SpeedLimitTests(unittest.TestCase):
	def test_speed_isOverLimit(self):
		road = RoadSection(50, 2)
		self.assertEqual(road.isOverLimit(datetime.datetime(2024, 7, 23, 3, 20, 0), datetime.datetime(2024, 7, 23, 3, 22, 0)), [60.0, True])
	
	def test_speed_isOverLimit2(self):
		road = RoadSection(50, 2)
		self.assertEqual(road.isOverLimit(datetime.datetime(2024, 7, 23, 3, 22, 0), datetime.datetime(2024, 7, 23, 3, 20, 0)), [-60.0, True])
		
	def test_speed_isNotOverLimit(self):
		road = RoadSection(50, 2)
		self.assertEqual(road.isOverLimit(datetime.datetime(2024, 7, 23, 3, 25, 0), datetime.datetime(2024, 7, 23, 3, 28, 0)), [40.0, False])
		
	def test_speed_isNotOverLimit(self):
		road = RoadSection(50, 2)
		self.assertEqual(road.isOverLimit(datetime.datetime(2024, 7, 23, 3, 28, 0), datetime.datetime(2024, 7, 23, 3, 25, 0)), [-40.0, False])
		
	def test_speed_isInvalid(self):
		road = RoadSection(50, 2)
		self.assertEqual(road.isOverLimit(datetime.datetime(2024, 7, 23, 3, 28, 0), datetime.datetime(2024, 7, 23, 3, 28, 0)), None)
		
if __name__ == '__main__':
	unittest.main()