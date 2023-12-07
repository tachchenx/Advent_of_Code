def type(hand):
    return sorted(map(hand.count, hand), reverse=True)

with open('input.txt') as f:
	lines = f.readlines()

val_list = []

for line in lines:
	hand, bid = line.split()
	hand = hand.translate(str.maketrans('TJQKA', 'A0CDE'))

	real_best = 0
	fit_second = 0
	for r in '23456789ABCDE':
		mod_hand = hand.replace('0', r)
		best_list = sorted(list(set(map(mod_hand.count, mod_hand))), reverse = True)
		unique_chars = len(set(mod_hand))
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

		if(best > real_best):
			real_best = best
			fit_second = second

	val_list.append((real_best, fit_second, hand, int(bid)))
	
val_list = sorted(val_list)
part2 = 0

for x in range(len(val_list)):
	part2 += (1+x)*val_list[x][3]
	
print(part2)