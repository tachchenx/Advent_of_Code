sol_1 = 0
sol_2 = 0



with open('input.txt') as f:
	lines = f.readlines()

cardcount = [1] * len(lines)

for line in lines:
	line = line.strip("\n")
	line = line.split("|")
	print(line)
	first = line[0].split(":")
	num = int(first[0].strip("Card "))
	print("Num is", num, "And cardcount is", cardcount[num-1])
	first = first[1].split()
	second = line[1].split()
	first_set = set(first)
	second_set = set(second)

	ans = first_set.intersection(second_set)
	#print(len(ans))
	if len(ans) > 0:
		sol_1 += pow(2, len(ans)-1)

	wins = len(ans)

	for x in range(wins):
		print("X is", x, "Num is", num)
		cardcount[num+x] += cardcount[num-1]

print(sol_1)

for number in cardcount:
	sol_2 += number

print(sol_2)