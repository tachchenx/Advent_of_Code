from collections import Counter
import numpy as np
import os, time

input = []
stones = []
part2 = 0
rot = 0

with open('test.txt') as f:
    line = f.readline().strip("\n")

    while line:
        input.append(list(line))
        line = f.readline().strip("\n")


input = np.array(input)
input = np.rot90(input, k=-1)

#for line in input:
#    print(line)

#print("\n")

st = time.time()

substep = 0
subframe = np.copy(input)

for run in range(1000000000):
    #if not run % 10000:
    #    print(run)
    for y in range(len(input)):
        line = "".join(input[y])
        #print(line)
        while "O." in line:
            line = line.replace("O.", ".O")
            #print(list(line))
        input[y] = list(line)
    input = np.rot90(input, k=-1)
    substep +=1

    if substep == 4:
        substep = 0
        if np.array_equal(subframe, input):
            print("LOOOOOOOP", run)
            substep = 10
            #run = (1000000000-run)%4
            #print(subframe)
            #print(input)
    if substep == 10:
        break
        

et = time.time()

input = np.rot90(input, k=1)
for line in input:
    print("".join(line))

for y in range(len(input)):
    line = input[y]
    part2 += Counter(line).get("O",0) * (len(input) - y)

print(part2)
print("Elapsed = ", et-st)
            