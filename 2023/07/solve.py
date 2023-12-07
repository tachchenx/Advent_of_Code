with open('input.txt') as f:
	lines = f.readlines()

val_list = []

for line in lines:
	hand, bid = line.split()
	hand = hand.translate(str.maketrans('TJQKA', 'ABCDE'))
	#print(hand)
	best_list = sorted(list(set(map(hand.count, hand))), reverse = True)
	#print(best_list)
	unique_chars = len(set(hand))
	best = best_list[0]

	if(len(best_list)>1):
		if best == 2 and unique_chars == 3:
			second = 2
		elif best == 2 and unique_chars == 4:
			second = 1
		else:
			second = best_list[1]
	else:
		second = 0

	val_list.append((best, second, hand, int(bid)))
	
#print(val_list)
val_list = sorted(val_list)

#for val in val_list:
	#print(val)

part1 = 0

for x in range(len(val_list)):
	part1 += (1+x)*val_list[x][3]
	
print(part1)