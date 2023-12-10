def is_zero_lst(lst):
    return all(element == 0 for element in lst)        

with open('input.txt') as f:
	lines = f.readlines()

part1 = 0
part2 = 0

for line in lines:

    rows = []
    line  = line.strip("\n")
    line = line.split(" ")
    line = [int(char) for char in line]
    rows.append(line)

    prev_row = line
    while True:
        new_row = []
        for idx in range(0, len(prev_row)-1):
            new_row.append(prev_row[idx+1] - prev_row[idx])
        rows.append(new_row)
        if is_zero_lst(new_row):
            break
        prev_row = new_row

    first_elements = [sublist[0] for sublist in rows]
    last_elements = [sublist[-1] for sublist in rows]
    first_elements.reverse()
    last_elements.reverse()

    new_right = 0
    for idx in range(1,len(last_elements)):
        new_right = last_elements[idx] + new_right

    new_left = 0
    for idx in range(1,len(first_elements)):
        new_left = first_elements[idx] - new_left
    
    part1 += new_right
    part2 += new_left
    
print(part1)
print(part2)