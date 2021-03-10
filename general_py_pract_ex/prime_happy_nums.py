# ex 23
'''Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.'''

# strategy
# find shortest text file and turn it into a list
# compare that list to lines from the other text file
# output list to CLI

f_prime = 'primenumbers.txt'
f_happy = 'happynumbers.txt'

def compare(f_prime, f_happy):
	
	dupes = []
	
	with open(f_prime, 'r') as f1:
		
		prime_lines = f1.read().splitlines()
	
	with open(f_happy, 'r') as f2:
		
		happy_lines = f2.read().splitlines()
		
	for elem in happy_lines:
		
		if elem in prime_lines:
			
			dupes.append(elem)
	
	print('There are %i numbers 1-1000 that are happy and prime' % len(dupes))
	print('These are:')
	print(dupes)
	
compare(f_prime, f_happy)
