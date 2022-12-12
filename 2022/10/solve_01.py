instructions = []

with open('input.txt') as f:
	inp = f.readlines()

for line in inp:
	line = line.replace("\n","")
	line = line.split()
	if len(line) == 2:
		temp = []
		temp.append(line[0])
		temp.append(int(line[1]))
		instructions.append(temp)
	else:
		instructions.append(line[0])

#print(instructions)

run = 1
cycle = 1
inst_no = 0
last_inst = None
x = 1
value = 0
nextThresh = 20

while run == 1:

	if cycle == nextThresh:
		nextThresh += 40
		print(cycle)
		print(x)
		print(cycle * x)
		print ("################")
		value += (cycle * x)

	inst = instructions[inst_no]

	if inst == "noop":
		cycle += 1
		inst_no += 1
		continue
	elif inst == "END":
		run = 0
		continue
	else:
		if last_inst == inst:
			cycle += 1
			inst_no +=1
			x += inst[1]
			last_inst = None
			continue
		else:
			last_inst = inst
			cycle += 1
			continue	

print(value)