with open('instructions.txt') as f:
	insts = f.readlines()

with open('input.txt') as f:
	lines = f.readlines()

stacks = [[],[],[],[],[],[],[],[],[]]

for line in lines:
	for x in range(9):
		if(line[1+(x*4)] != " "):
			stacks[x].append(line[1+(x*4)])

print(stacks)

for line in insts:
	splitter = line.split(" ")

	count = int(splitter[1])
	src = int(splitter[3]) - 1
	dst = splitter[5]
	dst = int(dst.replace("\n", "")) - 1
	print(count)
	print(src)
	print(dst)
	
	print(stacks)

	for x in range(count):
		src_stack = stacks[src]
		item = src_stack[0]
		del(src_stack[0])
		stacks[src] = src_stack
		print (src_stack)
		dst_stack = stacks[dst]
		dst_stack.insert(x,item)
		stacks[dst] = dst_stack

	print(stacks)	


output = ""

for stack in stacks:
	output += str(stack[0])

print(output)