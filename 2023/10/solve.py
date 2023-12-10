import os
import time

def find_item_coordinates(matrix, item):
    coordinates = next(((i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == item), None)
    return coordinates

north = (0,-1)
east = (1,0)
south = (0,1)
west = (-1,0)

def direction (char, prev):
    if char == "|" or char == "-":
        return prev
    if char == "L":
        if prev == south:
            return east
        elif prev == west:
            return north
    if char == "J":
        if prev == south:
            return west
        elif prev == east:
            return north
    if char == "7":
        if prev == north:
            return west
        elif prev == east:
            return south
    if char == "F":
        if prev == north:
            return east
        elif prev == west:
            return south
    
    return (0,0)

def move (curr, dir):
    return (curr[0] + dir[0], curr[1] + dir[1])

     

with open('input.txt') as f:
	lines = f.readlines()

part1 = 0
part2 = 0

map = []

for line in lines:

    line = line.strip("\n")
    line = list(line)
    map.append(line)

start_pos = find_item_coordinates(map, 'S')
start_pos = (start_pos[1], start_pos[0])
curr_pos = start_pos
start_dir = None
#print(start_pos)
#print(map[start_pos[1]][start_pos[0]])

check = [north, south, east, west]
#print(check)

for dir in check:
    pos = move(start_pos, dir)
    char = map[pos[1]][pos[0]]
    if not direction(char, dir) == (0,0):
        #print("Found with direction:", dir, direction(char, dir))
        start_dir = dir
        break

curr_dir = start_dir

#for line in map:
#    print(line)

while True:
    part1 += 1
    map[curr_pos[1]][curr_pos[0]] = "X"
    curr_pos = move(curr_pos, curr_dir)
    char = map[curr_pos[1]][curr_pos[0]]
    curr_dir = direction(char, curr_dir)
    #os.system('cls')
    #print(char, curr_pos, curr_dir)
    #for line in map:
    #    print("".join(line))
    #time.sleep(0.25)

    if map[curr_pos[1]][curr_pos[0]] == "X":
        #print("ENDE", int(part1/2))
        break

print("Part1:", int(part1/2))
#for line in map:
#    print("".join(line))