import numpy as np

def butOne (left, right):
    count = 0
    for idx in range(len(left)):
        if not left[idx] == right[idx]:
            count += 1
    if(count <= 1):
        return True
    
    return False
    

part1 = 0

patternlist = []
pattern = []

with open('test.txt') as f:
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
    butOne_Counter_col = 0
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

            if butOne(l_col, r_col):
                butOne_Counter_col +=1
            else:
                break

            if butOne_Counter_col > 1:
                break

        if coll_found:
            break
    #print("NO COLL")
    if coll_found:
        print("Übersprngen")
        continue
    row_found = False
    butOne_Counter_row = 0
    for y in range(y_dim-1):
        for count in range (y_dim):
            top = y - count
            bot = y + count + 1

            if top == -1 or bot == y_dim:
                part1 += (y+1)*100
                row_found = True
                #print("Found matching row at:", y+1)
                break

            t_row = arr[top]
            b_row = arr[bot]

            if np.array_equal(t_row, b_row):
                continue

            if butOne(t_row, b_row):
                butOne_Counter_row +=1
            else:
                break

            if butOne_Counter_row > 1:
                break

        if row_found:
            break

print("Part1: ", part1)