matrix = []
visibility = []

with open('input.txt') as f:
	inp = f.readlines()

for line in inp:
	line = line.replace("\n","")
	line = list(map(int, line))
	matrix.append(line)
	zeros = []
	for x in range(len(line)):
		zeros.append(0)
	visibility.append(zeros)

rows = len(matrix)
cols = len(matrix[0])
print("matrix with", rows, " rows")
print("matrix with", cols, " columns")


#go through rows
for y in range(rows):
	blocking = -1
	#forward
	for x in range(cols):
		if matrix[y][x] > blocking:
			visibility[y][x] = 1
			blocking = matrix[y][x]
	#backward
	blocking = -1
	for x in range(cols-1, 0, -1):
		if matrix[y][x] > blocking:
			visibility[y][x] = 1
			blocking = matrix[y][x]

#go through cols
for x in range(cols):
	blocking = -1
	#forward
	for y in range(rows):
		if matrix[y][x] > blocking:
			visibility[y][x] = 1
			blocking = matrix[y][x]
	#backward
	blocking = -1
	for y in range(rows-1, 0, -1):
		if matrix[y][x] > blocking:
			visibility[y][x] = 1
			blocking = matrix[y][x]

visible = 0
for rows in visibility:
	for elem in rows:
		visible += elem


print (visible)