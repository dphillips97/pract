# exercise 20
'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
'''

# make list
# 11 char long
a = [-100, -12, -1, 0, 1, 3, 5, 30, 42, 43, 500]

search_num = int(input('Enter number to search for > '))
print('Is %i in the list?' % search_num)

def binary_search(search_num, a):
		
	# 2 characters seems like a good search length 
	while len(a) > 2:
		
		# Mid_index changes with each iteration, durrrr
		mid_index = int(len(a)/2)
		
		if search_num == mid_index:
			print('%i is in the list' % search_num)
			break
		
		elif search_num > mid_index:
			a = a[mid_index:]
			print(a)
			
		elif search_num < mid_index:
			a = a[:mid_index]
			print(a)
		
	if search_num in a:
		print('%i is in the list' % search_num)
	
	else:
		print('%i is NOT in the list' % search_num)
		
	
	
	
	
	
	
	
	
	
	
binary_search(search_num, a)