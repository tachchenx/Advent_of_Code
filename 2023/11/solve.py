import numpy as np
from itertools import combinations
 
with open('input.txt') as f:
    lines = f.readlines()
 
map = []
 
for line in lines:
    line = line.strip("\n")
    line = list(line)
    map.append(line)
 
strech = []
 
for line in map:
    strech.append(line)
    if len(set(line)) == 1:
        strech.append(line)
   
strech = np.array(strech)
strech = np.transpose(strech)
strech = strech.tolist()
 
final = []
for line in strech:
    final.append(line)
    if len(set(line)) == 1:
        final.append(line)
 
final = np.array(final)
final = np.transpose(final)
final = final.tolist()
 
galax_list = []

for y in range(len(final)):
    for x in range(len(final[0])):
        line = final[y]
        if line[x] == "#":
            galax_list.append((x, y))

print(galax_list)

combinations = list(combinations(galax_list,2))
print(combinations, len(combinations))
part1 = 0
for pair in combinations:
    one = pair[0]
    two = pair[1]
    dist = abs(one[0]-two[0]) + abs(one[1]-two[1])
    print(pair, dist)
    part1 += dist

print("Part1:", part1)