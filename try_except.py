try:
	hours = input('Enter hours: ')
	rate = input('Enter rate: ')
	print('pay is: ', (int(hours) * int(rate)))

except:
	print('please enter numeric input')