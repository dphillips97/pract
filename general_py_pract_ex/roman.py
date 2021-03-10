roman_dict = {
	'M': 1000,
	'CM': 900,
	'D': 500,
	'CD': 400,
	'C': 100,
	'XC': 90,
	'L': 50,
	'XL': 40,
	'X': 10,
	'IX': 9,
	'V': 5,
	'IV': 4,
	'I': 1
			}

# main loop			
while True:	
	
	# must stay in loop to 'reset' each calculation
	roman_numerals = []
	
	num = int(input('Enter a number, CTRL-C to quit: '))
	
	# while there are still numbers to convert...
	while num > 0:
		
		# for each entry in the dict
		for val in roman_dict:
			
			# if the number is higher than the highest dict value
			if num >= roman_dict[val] :
				
				# add this value to the output list
				roman_numerals.append(val)
				
				# subtract the value of the roman numeral you just created
				num = num - roman_dict[val]
				
				break
				
	output = ''.join(roman_numerals)

	print(output)


	