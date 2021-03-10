'''
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen.

Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. 
'''

import re

exp = r'(/[a-z]/)([a-z]+_?[a-z]*)'
categories_dict = {}

with open('Training_01.txt', 'r') as f:
	
	# splitlines method turns file lines into list
	lines = f.read().splitlines()

	for line in lines:
		
		exp = re.compile(exp)
		mo = re.match(exp, line)
		cat = mo.group(2)
		
		if cat not in categories_dict:
			categories_dict[cat] = 1
			
		else:
			categories_dict[cat] += 1
	
with open('SUN_categories.txt', 'w') as output:
	
	for elem in categories_dict:
		output.write('%s: %i entries\n' % (elem, categories_dict.get(elem, None)))