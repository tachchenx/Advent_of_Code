buf = []

def shiftIn (char):
	if len(buf) == 4:
		buf.append(char)
		del buf[0]
	else:
		buf.append(char)

def isUnique():
	seen = set()
	uniq = []
	for char in buf:
		if char not in seen:
			uniq.append(char)
			seen.add(char)
	if len(uniq) == 4:
		return 1
	else:
		return 0

with open('input.txt') as f:
	inp = f.readlines()

line = inp[0]

for x in range(len(line)):
	shiftIn(line[x])
	if len(buf) == 4:
		if isUnique() == 1:
			print(x+1)
			break