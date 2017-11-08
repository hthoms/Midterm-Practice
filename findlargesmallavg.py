fhand = open("data.txt", "r")
floatlist = []
for line in fhand:
	if int(line) > 0:
		floatlist.append(int(line.rstrip()))
avg = 0
bignum = None
smallnum = None
for num in floatlist:
	if bignum == None or num > bignum:
		bignum = num
	if smallnum == None or num < smallnum:
		smallnum = num
	avg += num
avg = avg / len(floatlist)
print("Largest: ", bignum)
print("Smalles: ", smallnum)
print("Average: ", avg)
