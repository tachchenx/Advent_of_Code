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

maxScenic = 0

for x in range(cols):
	for y in range(rows):
	
		height = matrix[y][x]

		distUp = 0
		distDown = 0
		distRight = 0
		distLeft = 0

		for lookUp in range(y,0,-1):
			lookUp -= 1
			distUp += 1
			if matrix[lookUp][x] < height:
				continue
			else:
				break

		for lookDown in range(y+1,rows,1):
			distDown += 1
			if matrix[lookDown][x] < height:
				continue
			else:
				break


		for lookRight in range(x+1,cols,1):
			distRight += 1
			if matrix[y][lookRight] < height:
				continue
			else:
				#print("BREAK")
				break
		#print(distRight)

		for lookLeft in range(x,0,-1):
			lookLeft-=1
			distLeft += 1
			if matrix[y][lookLeft] < height:
				continue
			else:
				break

		scenic = distUp*distDown*distLeft*distRight
		if scenic > maxScenic:
			maxScenic = scenic

print(maxScenic)