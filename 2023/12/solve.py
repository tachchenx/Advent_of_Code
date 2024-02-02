from itertools import product
import re

def generate_strings(length):
    characters = ['#', '.']
    all_combinations = product(characters, repeat=length)
    result = [list(combination) for combination in all_combinations]
    return result

with open('input.txt') as f:
    lines = f.readlines()

part1 = 0

for line in lines:
    line = line.strip("\n")
    line, nums = line.split(" ")
    line = list(line)
    nums = nums.split(",")
    #print(line, nums)

    quest, empt, hash = 0,0,0
    for char in line:
        if char == "?":
            quest+=1
        elif char == ".":
            empt+=1
        if char == "#":
            hash+=1

    combs = generate_strings(quest)

    regex = "\.*"
    for x in range(len(nums)-1):
        num = nums[x]
        regex += "#{" + num + "}\.+"    
    regex += "#{" + nums[-1] + "}\.*"
    
    for comb in combs:
        replaced_list = [comb.pop(0) if item == '?' else item for item in line]
        res = re.fullmatch(regex, "".join(replaced_list))
        if res:
            part1 += 1


print("Part 1:", part1)