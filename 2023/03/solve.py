class Gear:
    def __init__(self, value, x, y, count):
        self.value = value
        self.x = x
        self.y = y
        self.count = count

    def display(self):
        return f"Gear with value {self.value}, position (x={self.x}, y={self.y}), and count {self.count}"

def is_valid(array, ypos, xpos):
    return 0 <= ypos < len(array) and 0 <= xpos < len(array[0])

def gear_exists(gears_list, target_x, target_y):
    for index, gear in enumerate(gears_list):
        if gear.x == target_x and gear.y == target_y:
            return index
    return -1

with open('input.txt') as f:
	lines = f.readlines()

letterarr = []
gearlist = []
ans = 0

for line in lines:
	line = line.strip("\n")
	letters = [char for char in line]
	letterarr.append(letters)

num = 0
s = ""
valid = False
adjgears = []

for ypos in range(len(letterarr)):	
	for xpos in range(len(letterarr[ypos])):
		char = letterarr[ypos][xpos]

		if char.isdigit():
			#print("Went IF")
			s+=char

			for ycheck in range(ypos-1, ypos+2):
				for xcheck in range(xpos-1, xpos+2):
					if is_valid(letterarr, ycheck, xcheck):
						testchar = letterarr[ycheck][xcheck]
						if not testchar.isdigit() and not testchar == ".":
							valid = True
							
							if testchar == "*":
								print("Found gear at ", xcheck, ycheck)
								idx = gear_exists(gearlist, xcheck, ycheck)
								print("IDX is:", idx)
								if idx == -1:
									print("ADD")
									gearlist.append(Gear(value=1, x=xcheck, y=ycheck, count=0))
									newidx = gear_exists(gearlist, xcheck, ycheck)
									print("NEW IDX:", newidx)
									adjgears.append(newidx)
									for x in range(len(gearlist)):
										print(gearlist[x].display())
								else:
									adjgears.append(idx)
		else:
			#print("Went ELSE")
			if not s == "":
				num = int(s)
				if valid:
					ans += num
					unique = list(set(adjgears))
					print(unique)

					for gear_idx in unique:
						gearlist[gear_idx].value *= num
						gearlist[gear_idx].count += 1

			num = 0
			s = ""
			valid = False
			adjgears = []

print("########## ENDE ##########")

#print(gearlist)

secondans = 0

for x in range(len(gearlist)):
	print(gearlist[x].display())
	if gearlist[x].count == 2:
		secondans += gearlist[x].value


print(ans)
print(secondans)