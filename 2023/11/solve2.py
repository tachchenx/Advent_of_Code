import numpy as np
from itertools import combinations
 
with open('input.txt') as f:
    lines = f.readlines()
 
map = []
 
for line in lines:
    line = line.strip("\n")
    line = list(line)
    map.append(line)
 
galax_list = []

for y in range(len(map)):
    for x in range(len(map[0])):
        line = map[y]
        if line[x] == "#":
            galax_list.append((y, x))

#print(galax_list)

empty_rows = []
empty_cols = []

array = np.array(map)
#print(array)

rows, colls = array.shape

for col_idx in range(colls):
    if len(np.unique(array[:, col_idx])) == 1:
        empty_cols.append(col_idx)

for row_idx in range(rows):
    if len(np.unique(array[row_idx,:])) == 1:
        empty_rows.append(row_idx)

#print(empty_cols, empty_rows)

factor = 1000000

for gal_idx in range(len(galax_list)):
    galax = list(galax_list[gal_idx])
    plus_rows = len([num for num in empty_rows if num < galax[0]])
    plus_cols = len([num for num in empty_cols if num < galax[1]])
    #print(galax, plus_cols, plus_rows)
    galax[0] = galax[0] + (plus_rows * factor) - plus_rows
    galax[1] = galax[1] + (plus_cols * factor) - plus_cols
    galax_list[gal_idx] = tuple(galax)

#print(galax_list)

combinations = list(combinations(galax_list,2))
#print(combinations, len(combinations))
part1 = 0
for pair in combinations:
    one = pair[0]
    two = pair[1]
    dist = abs(one[0]-two[0]) + abs(one[1]-two[1])
    #print(pair, dist)
    part1 += dist

print("Part1:", part1)