import numpy as np

part1 = 0

patternlist = []
pattern = []

with open('input.txt') as f:
    while True:
        line = f.readline()
        
        if not line:
            patternlist.append(pattern)
            break

        line = line.strip("\n")

        if line == "":
            patternlist.append(pattern)
            pattern = []
        else:
            pattern.append(list(line))

for pattern in patternlist:
    arr = np.array(pattern)
    #print(arr)
    y_dim, x_dim = arr.shape

    #check collumn mirroring
    coll_found = False
    for x in range(x_dim-1):
        for count in range (x_dim):
            left = x - count
            right = x + count + 1

            if left == -1 or right == x_dim:
                part1 += x+1
                coll_found = True
                #print("Found matching collumn at:", x+1)
                break

            l_col = arr[:, left]
            r_col = arr[:, right]

            if not np.array_equal(l_col, r_col):
                break
        if coll_found:
            break
    
    row_found = False
    for y in range(y_dim-1):
        for count in range (y_dim):
            top = y - count
            bot = y + count + 1

            if top == -1 or bot == y_dim:
                part1 += (y+1)*100
                row_found = True
                #print("Found matching row at:", y+1)
                break

            t_col = arr[top]
            b_col = arr[bot]

            if not np.array_equal(t_col, b_col):
                break
        if row_found:
            break

print("Part1: ", part1)