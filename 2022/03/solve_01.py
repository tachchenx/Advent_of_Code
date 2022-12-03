import string

def getCharVal(char):
	if char.isupper():
		return (string.ascii_uppercase.index(char)) + 27
	else:
		return (string.ascii_lowercase.index(char)) + 1

def findDuplicate(first, second):
	for char in first:
		if char in second:
			return getCharVal(char)

with open('input.txt') as f:
	lines = f.readlines()

sum = 0

for line in lines:
	line = line.replace("\n","")
	length = len(line)
	split = int(length/2)
	first = []
	second = []
	for x in range(0 , split):
		first.append(line[x])
		second.append(line[x+split])

	sum += findDuplicate(first, second)

print (sum)