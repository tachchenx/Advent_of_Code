sums = []


with open('input.txt') as f:
	lines = f.readlines()
sum = 0
for line in lines:
	if line == "\n":
		sums.append(sum)
		sum = 0
	else:
		sum += int(line)

top3 = 0
for x in range(3):
	maxval = max(sums)
	top3 += maxval
	sums.remove(maxval)

print (top3)