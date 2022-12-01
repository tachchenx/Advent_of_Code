max = 0

with open('input.txt') as f:
	lines = f.readlines()

sum = 0
for line in lines:
	if line == "\n":
		if sum > max:
			max = sum

		sum = 0
	else:
		sum += int(line)

print(max)