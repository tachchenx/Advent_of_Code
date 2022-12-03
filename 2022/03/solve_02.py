import string

def getCharVal(char):
	if char.isupper():
		return (string.ascii_uppercase.index(char)) + 27
	else:
		return (string.ascii_lowercase.index(char)) + 1

def findDuplicate(first, second, third):
	for char in first:
		if char in second and char in third:
			return getCharVal(char)

with open('input.txt') as f:
	lines = f.readlines()

sum = 0

for x in range(0, len(lines), 3):
	one = lines[x].replace("\n", "")
	two = lines[x+1].replace("\n", "")
	three = lines[x+2].replace("\n", "")

	sum += findDuplicate(one, two, three)

print (sum)