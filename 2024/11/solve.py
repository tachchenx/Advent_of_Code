#Part 1: 18:42

stone_list = []
swap_list = []
blinks = 75


with open("input.txt") as f:
    lines = f.readline()

stones = lines.split()
for stone in stones:
    #print(int(stone))
    stone_list.append(int(stone))


print(stone_list)

#stone_list = [1234]

for x in range(blinks):
    for num in stone_list:
        
        if num == 0:
            swap_list.append(1)
        elif len(str(num))%2 == 0:
            numstr = str(num)
            first, second = numstr[:len(numstr)//2], numstr[len(numstr)//2:]
            swap_list.append(int(first))
            swap_list.append(int(second))
        else:
            num = num*2024
            swap_list.append(num)

    stone_list = swap_list
    swap_list = []

print(len(stone_list))