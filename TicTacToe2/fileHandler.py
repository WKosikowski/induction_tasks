#!/usr/bin/env python3
# Wojciech Kosikowski (c) 2024

class FileHandler:
	def save(xwins, owins, draws):
		file = open("statistics.txt", "w")
		file.write("X: {}\nO: {}\nD: {}".format(xwins, owins, draws))
	def read():
		file = open("statistics.txt", "r")
		stats = file.read()
		statsCleaned = [int(stats.split()[1]) for i in stats.split("\n")]
		file.close()
		return statsCleaned