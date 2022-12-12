import math

class monkey:
	def __init__(self, number, items, operation, devisor, true, false):
		self.number = number
		self.items = items
		self.operation = operation
		self.devisor = devisor
		self.true = true
		self.false = false
		self.inspects = 0
	def __str__(self):
		return "Me is monkey " + self.number + " with op " + self.operation

def doOperation(val, op):
	old = val
	return eval(op)

monkeys = []

with open('input.txt') as f:
	inp = f.readlines()

for line in inp:
	line = line.replace("\n","")
	line = line.split()
	#print(line)

for x in range(0,len(inp),7):
	line = inp[x].split()
	number = line[1].replace(":","")
	
	line = inp[x+1].split()
	items = []

	for count in range(2, len(line), 1):
		items.append(int(line[count].replace(",","")))
	

	operation = inp[x+2].replace("Operation: ", "")
	operation = operation.replace("new = ", "")
	operation = operation.replace(" ", "")
	operation = operation.replace("\n", "")

	line = inp[x+3].split()
	devisor = int(line[3])

	line = inp[x+4].split()
	true = int(line[5])
	line = inp[x+5].split()
	false = int(line[5])

	ape = monkey(number, items, operation, devisor, true, false)
	monkeys.append(ape)

for _ in range(20):

	for monkey in monkeys:
		#print (monkey)
		op = monkey.operation
		devisor = monkey.devisor
		true = monkey.true
		false = monkey.false

		for item in monkey.items:
			monkey.inspects += 1
			ans = doOperation(item, op)
			ans = ans/3
			ans = int(math.floor(ans))
			#print(ans)

			if ans%devisor == 0:
				monkeys[true].items.append(ans)
				#print("Throw ", ans, " to ", true)
			else:
				monkeys[false].items.append(ans)
				#print("Throw ", ans, " to ", false)

		monkey.items = []

inspections = []
for monkey in monkeys:
	#print(monkey.inspects)
	inspections.append(monkey.inspects)

result = max(inspections)
inspections.remove(result)
result *= max(inspections)
print("Monkey business is: ", result)