from collections import Counter

input = []
stones = []
part1 = 0

with open('input.txt') as f:
    line = f.readline().strip("\n")

    while line:
        input.append(list(line))
        line = f.readline().strip("\n")

for line in input:
    print(line)

for y in range(len(input)):
    for x in range(len(input[0])):
        item = input[y][x]
        if item == "O":
            stones.append((y,x))


for stone in stones:
    print(stone)
    y, x = stone
    while True:
        if y == 0:
            break
        next = input[y-1][x]

        if next == ".":
            input[y][x] = "."
            y = y-1
            input[y][x] = "O"
        else:
            break

for line in input:
    print("".join(line))

for y in range(len(input)):
    line = input[y]
    part1 += Counter(line).get("O",0) * (len(input) - y)

print(part1)
            