with open('input.txt') as f:
	lines = f.readlines()

sum = 0

for line in lines:
	line = line.replace("\n","")
	split = line.split(",")
	first = split[0]
	first = first.split("-")
	second = split[1]
	second = second.split("-")
	
	if int(first[0]) >= int(second[0]) and int(first[0]) <= int(second[1]):
		sum += 1
	elif int(first[1]) >= int(second[0]) and int(first[1]) <= int(second[1]):
		sum += 1
	elif int(second[0]) >= int(first[0]) and int(second[0]) <= int(first[1]):
		sum += 1
	elif int(second[1]) >= int(first[0]) and int(second[1]) <= int(first[1]):
		sum += 1

print(sum)