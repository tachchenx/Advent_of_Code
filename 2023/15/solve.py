def hash (string):
    current_value = 0
    char_list = list(string)
    #print(char_list)

    for char in char_list:
        num = ord(char)
        current_value += num
        current_value *= 17
        current_value = current_value % 256
    
    return current_value


with open('input.txt') as f:
    line = f.readline().split(",")

part1 = 0

for item in line:
    myHash = hash(item)
    #print(item, myHash)
    part1 += myHash

print("Part1: ", part1)