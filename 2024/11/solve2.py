from collections import Counter

stone_list = []
swap_list = []
blinks = 750


with open("input.txt") as f:
    lines = f.readline()

stones = lines.split()
for stone in stones:
    stone_list.append(int(stone))


print(stone_list)

occurrences = Counter(stone_list)

numbers_dict = dict(occurrences)
swap_dict = {}
print(numbers_dict)

for x in range(blinks):
    for idx in range(len(numbers_dict)):
        key = list(numbers_dict)[idx]
        value = numbers_dict[key]

        if key == 0:
            old = swap_dict.get(1)
            if old == None:
                old = 0
            swap_dict[1] = old + value

        elif len(str(key))%2 == 0:
            numstr = str(key)
            first, second = int(numstr[:len(numstr)//2]), int(numstr[len(numstr)//2:])
            old = swap_dict.get(first)
            if old == None:
                old = 0
            swap_dict[first] = old + value
            old = swap_dict.get(second)
            if old == None:
                old = 0
            swap_dict[second] = old + value

        else:
            new = key*2024
            old = swap_dict.get(new)
            if old == None:
                old = 0
            swap_dict[new] = old + value

    numbers_dict = swap_dict
    swap_dict = {}


print(sum(numbers_dict.values()))