#!/usr/bin/python

# pseudofortune.py: is a fortune program clone.
# 	It's built just for fun, so don't expect the same efficient as original fortune.
#	Why? pseudofortune reads fortune cookies not from binary file, that's the reason why is less 
#	efficient. input file (txt) uses the same original fortune files where each quote
#	is separated by a '%' character.
#	As can be seen, number of fortune cookies (quotes) in file is hardcoded, being 3515 for this
#	example.

from __future__ import print_function
import re
import random
import os
import platform

fortNum = random.randint(0,3515)
enOutput = False
fortPos = 0

cwd = os.path.dirname(os.path.realpath(__file__))
sep = '/'
if os.name != "posix":
	sep = '\\'
filePath = cwd + sep + 'fortune.txt'

with open(filePath, 'r') as f:
	for line in f:
		if re.search('^%', line):
			fortPos += 1
			#print("Debug fortPos=" + str(fortPos))
			enOutput = not enOutput
			continue
		
				
		if fortPos == fortNum:
			print(line, end='')		

