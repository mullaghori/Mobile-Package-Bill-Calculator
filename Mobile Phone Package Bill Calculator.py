

#Mobile Phone Package Bill Calculator

bold = '\33[1m'
end = '\33[0m'
red = '\33[31m'
yellow = '\33[33m'
green = '\33[32m'
white = '\33[37m'
whitebg = '\33[47m'
blackbg = '\33[40m'

def Package_1(minutes_used):
	pkg_bill = 40
	pkg_minutes = 450
	add_min_cost = 0.45
	if minutes_used > pkg_minutes:
		add_minutes = minutes_used - pkg_minutes
		total_bill = pkg_bill + (add_minutes * add_min_cost)
		print(f"\nI hope that you would have enjoyed our Package_1.\nYour due bill for the current month is " + bold + f"RM{total_bill}/-" + end + "! Be happy 😊.")
	else:
		total_bill = pkg_bill
		print(f"\nI hope that you would have enjoyed our Package_1.\nYour due bill for the current month is " + bold + f"RM{total_bill}/-" + end + "! Be happy 😊.")
	
	
def Package_2(minutes_used):
	pkg_bill = 60
	pkg_minutes = 900
	add_min_cost = 0.40
	if minutes_used > pkg_minutes:
		add_minutes = minutes_used - pkg_minutes
		total_bill = pkg_bill + (add_minutes * add_min_cost)
		print(f"\nI hope that you would have enjoyed our Package_2.\nYour due bill for the current month is " + bold + f"RM{total_bill}/-" + end + "! Be happy 😊.")
	else:
		total_bill = pkg_bill
		print(f"\nI hope that you would have enjoyed our Package_2.\nYour due bill for the current month is " + bold + f"RM{total_bill}/-" + end + "! Be happy 😊.")
		
	
def Package_3(minutes_used):
	pkg_bill = 70
	total_bill = pkg_bill
	print(f"\nI hope that you would have enjoyed our Package_3.\nYour due bill for the current month is " + bold + f"RM{total_bill}/-" + end + "! Be happy 😊.")
	

print("Enter either 1, 2 or 3 as your package!\n")
try:
	Package = int(input('Which Package, you had purchased?\n'))

	if Package != 1 and Package != 2 and Package != 3:
		print('\n' + yellow + bold + 'You have entered a wrong package name!' + end + white + ' Please try again.')
		print("Enter either 1, 2 or 3 as your package!\n")	
		Package = int(input('Which Package, you had purchased?\n'))

		if Package != 1 and Package != 2 and Package != 3:
			print('\n')
			print(whitebg + red + bold + 'You again entered a wrong package name!.')
			print(blackbg, white)
			print(green + 'Run the program again!' + white + end)
		
		else:
			used_minutes = int(input('How many minutes you have used?\n'))

			if Package == 1:
				Package_1(used_minutes)
			elif Package == 2:
				Package_2(used_minutes)
			else:
				Package_3(used_minutes)
		
	else:
		used_minutes = int(input('How many minutes you have used?\n'))

		if Package == 1:
			Package_1(used_minutes)
		elif Package == 2:
			Package_2(used_minutes)
		else:
			Package_3(used_minutes)
			
except:
	print(red + bold + '\nYou should have entered an integer value!\n\n' + white + green + 'Run the program again!.' + end + white)
