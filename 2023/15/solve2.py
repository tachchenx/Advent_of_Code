import re

pattern = re.compile(r'(\w+)([-=])([+-]|\d*)')
boxes = [[] for _ in range(256)]

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

ans_part2 = 0

for item in line:

    label, op, focal = (re.match(pattern, item).groups())
    label_hash = hash(label)
    print(label, label_hash)
    if op == "-":
        box = boxes[label_hash]
        for idx in range(len(box)):
            lens = box[idx]
            if lens[0] == label:
                box.pop(idx)
                boxes[label_hash] = box
                break

    elif op == "=":
        box = boxes[label_hash]
        lense_idx = 0
        found = False
        for idx in range(len(box)):
            lens = box[idx]
            if lens[0] == label:
                lense_idx = idx
                box.pop(idx)
                found = True
                break
        
        if found:
            box.insert(lense_idx, (label, focal))
        else:
            box.append((label, focal))

        boxes[label_hash] = box
    else:
        print("ERROR")

for index in range(len(boxes)):
    print("Box:", index)
    box = boxes[index]
    for lense_index in range(len(box)):
        print(box[lense_index])
        lense = box[lense_index]
        ans_part2 += (index+1)*(lense_index+1)*int(lense[1])

print("Part2: ", ans_part2)