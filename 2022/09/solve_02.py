visited = [[0,0]]

nodes = []

for x in range(10):
	nodes.append([0,0])

print(nodes)
def addCoord(coord):
	global visited
	#print("------")
	#print("Visited so far:",visited)
	#print("Adding", coord)
	if coord in visited:
		#print("Duplicate")
		pass
	else:
		pair = [coord[0], coord[1]]
		visited.append(pair)
		#print("Added coord")
		#print(visited)

	#print("------")

def moveNode(nodeID):
	global nodes
	head = nodes[nodeID-1]
	tail = nodes[nodeID]

	if nodes[nodeID] == nodes[nodeID-1]:
		print("Node", nodeID, " is same as", nodeID-1)
		if nodeID == len(nodes)-1:
			addCoord(nodes[nodeID])
		return

	xoff = 0
	yoff = 0
	for x in range(-1,2,1):
		for y in range(-1,2,1):
			if tail[0]+x == head[0] and tail[1]+y == head[1]:
				xoff = x
				yoff = y
				if nodeID == len(nodes)-1:
					addCoord(nodes[nodeID])
				return


	xDiff = abs(head[0] - tail[0])
	yDiff = abs(head[1] - tail[1])

	if xDiff > 2 or yDiff > 2:
		#print("ERROR")
		pass

	if yDiff > xDiff:
		tail[0] = head[0]
		if tail[1] < head[1]:
			tail[1] = head[1] - 1
		else:
			tail[1] = head[1] + 1
	else:
		tail[1] = head[1]
		if tail[0] < head[0]:
			tail[0] = head[0] - 1
		else:
			tail[0] = head[0] + 1

	nodes[nodeID][0] = tail[0]
	nodes[nodeID][1] = tail[1]

	if nodeID == len(nodes)-1:
			addCoord(nodes[nodeID])


with open('input.txt') as f:
	inp = f.readlines()

for line in inp:
	line = line.replace("\n","")
	line = line.split()
	line[1] = int(line[1])
	print(line)
	token = line[0]
	steps = line[1]
	hor = 0
	ver = 0

	if token == "R":
		hor = 1
	if token == "L":
		hor = -1
	if token == "U":
		ver = 1
	if token == "D":
		ver = -1

	for moves in range(steps):

		print("++++++")
		nodes[0][0] += hor
		nodes[0][1] += ver
		print("Head moved:", nodes[0])
		for x in range(1,len(nodes)):
			print("Node", x, "at", nodes[x])
			moveNode(x)
			print("Node now", x, "at", nodes[x])
		print("Tail moved:", nodes[9])

		print("###############")

print("Visited: ",len(visited))