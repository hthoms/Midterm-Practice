counter = 1
def doLotsOfStuff():
	global counter
	for k in (1, 2, 3):
		counter += 1
doLotsOfStuff()
print(counter)

for k in range(2):
	print(k)
for k in range(4, 6):
	print(k)

kvps = {"user":"Chris", "password":"Becca"}
print(kvps)
print(kvps["password"])



foo = {1:"1",2:"2",3:"3"}
del foo[1]
print(foo)
foo[1] = 10
print(foo)
del foo[2]
print(len(foo))

names = ["a","b","c","d"]
print(names[-1][-1])

t = (1, "a", [1, 2, 3])
print(type(t))
print(t)