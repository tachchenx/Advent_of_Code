def getMoveVal(move):
	if move == "X" :
		return 1
	if move == "Y" :
		return 2
	if move == "Z" :
		return 3

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

with open('test_input.txt') as f:
	lines = f.readlines()

points = 0

for line in lines:
	enemy = line[0]
	me = line[2]

	movePoints = getMoveVal(me)
	fightpoints = getFightVal(enemy, me)

	points += movePoints
	points += fightpoints

print (points)