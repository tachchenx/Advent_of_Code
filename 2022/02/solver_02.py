def getMoveVal(move):
	if move == "X" :
		return 1
	if move == "Y" :
		return 2
	if move == "Z" :
		return 3

def findMove(enemy, me):
	if enemy == "A":
		if me == "X":
			return "Z"
		if me == "Y":
			return "X"
		if me == "Z":
			return "Y"
	if enemy == "B":
		if me == "X":
			return "X"
		if me == "Y":
			return "Y"
		if me == "Z":
			return "Z"
	if enemy == "C":
		if me == "X":
			return "Y"
		if me == "Y":
			return "Z"
		if me == "Z":
			return "X"

def getFightVal(enemy, me):
	if enemy == "A":
		if me == "X":
			return 3
		if me == "Y":
			return 6
		if me == "Z":
			return 0
	if enemy == "B":
		if me == "X":
			return 0
		if me == "Y":
			return 3
		if me == "Z":
			return 6
	if enemy == "C":
		if me == "X":
			return 6
		if me == "Y":
			return 0
		if me == "Z":
			return 3

with open('input.txt') as f:
	lines = f.readlines()

points = 0

for line in lines:
	enemy = line[0]
	me = line[2]

	movePoints = getMoveVal(findMove(enemy, me))
	fightpoints = getFightVal(enemy, findMove(enemy, me))

	print (movePoints)
	print (fightpoints)
	print ("##############################")

	points += movePoints
	points += fightpoints

print (points)