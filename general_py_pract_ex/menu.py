
#https://www.reddit.com/r/beginnerprojects/comments/1bytu5/projectmenu_calculator/

'''GOAL

Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items, you assign each one to a number, as shown below.

Chicken Strips - $3.50
French Fries - $2.50
Hamburger - $4.00
Hotdog - $3.50
Large Drink - $1.75
Medium Drink - $1.50
Milk Shake - $2.25
Salad - $3.75
Small Drink - $1.25
To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.

SUBGOALS

If you decide to, print out the items and prices every time before the user types in an order.
Once the user has entered an order, print out how many of each item have been ordered, as well as the total price. If an item was not ordered at all, then it should not show up.'''

menu = {
			1: ['Chicken Strips', 3.5],
			2: ['French Fries', 2.5],
			3: ['Hamburger', 4],
			4: ['Hotdog', 3.5],
			5: ['Large Drink', 1.75],
			6: ['Medium Drink', 1.5],
			7: ['Milk Shake', 2.25],
			8: ['Salad', 3.75],
			9: ['Small Drink', 1.25]
			}

def validator():			
	
	# entry starts off as not valid
	valid = False
	
	# while loop to repeat when entry is not valid
	while valid == False:
	
		# print menu with borders
		print('*' * 20)
		for key in menu:
			# print dict key, name, cost (formatted)
			print('%i. %s - $%.2f' % (key, menu[key][0], menu[key][1]))
		print('*' * 20)
		
		# input as string to avoid immediate error (if declared as int)
		order_digits = input('Enter your order, \'q\' to quit > ')
		
		# break on 'Q' or 'q' (pass to another fnc)
		# or pass valid quit command 
		if order_digits == 'q' or order_digits.isdigit():
			
			return order_digits
			
		# else continue loop	
		else:
			print('\nPlease enter digits only!\n')
			
def main(order_digits):
	
	# for each order generate receipt
	receipt = []
	
	# set total price to zero
	total_price = 0				

	# change order entry to list
	order_list = list(order_digits)
	
	# loop thru order list and compare against menu dict
	for item in order_list:
		
		# get total price and set to float 
		# item is string, must set to int
		total_price += (menu[int(item)][1])
		
		# add item to receipt (list of items)
		receipt.append(menu[int(item)][0])
	
	
	print('\nORDER SUMMARY: ')
	
	# find dupes in receipt 
	for item in receipt:
		count = receipt.count(item)
		print('%i %s' % (count, item))

	
	# print total price as 2 digit float
	print('\nTotal is: $%.2f\n' % total_price)

	
	
	
def looper():
	
	while True:
		
		order = validator()
		
		if str(order) == 'q':
			print('Bye!')
			break
		
		else:
			main(order)

			
looper()
	
	
