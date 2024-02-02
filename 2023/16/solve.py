up = (-1, 0)
down = (1, 0)
left = (0, -1)
right = (0, 1)

def move(position, direction):
    return(position[0] + direction[0], position[1] + direction[1])

class Beam:
    def __init__(self, position, direction):
        self.x = position[1]
        self.y = position[0]
        self.direction = direction
        self.visited = set()
    
    def getPos(self):
        return (self.y, self.x)
    
    def getDir(self):
        return self.direction
    
    def setPos(self, position):
        self.x = position[1]
        self.y = position[0]
    
    def addVisited(self, position):
        if self.direction == up or self.direction == down:
            self.visited.add((position, "vert"))
        else:
            self.visited.add((position, "hor"))

visited = set()
start = (0,0)
beams = [Beam(start, right)]
map = []
visu = []


with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip("\n")
    line = list(line)
    map.append(line)

for y in range(len(map)):
    dots = []
    for x in range(len(map[0])):
        dots.append(".")
    visu.append(dots)

for beam in beams:
    print(len(beams))
    while True:
        visited.add(beam.getPos())
        size = len(beam.visited)
        beam.addVisited((beam.getPos()))
        if size == len(beam.visited):
            break
        nextPos = move(beam.getPos(), beam.getDir())
        if 0 > nextPos[0] or nextPos[0] >= len(map):
            #print("YO")
            break
        if 0 > nextPos[1] or nextPos[1] >= len(map[0]):
            #print("YE")
            break
        beam.setPos(nextPos)
        #print(nextPos)
        nextItem = map[nextPos[0]][nextPos[1]]

        if nextItem == ".":
            continue
        elif nextItem == "+":
            if beam.direction == left or beam.direction == right:
                break
        elif nextItem == "#":
            if beam.direction == up or beam.direction == down:
                break
        elif nextItem == "/":
            if beam.direction == left:
                beam.direction = down
            elif beam.direction == right:
                beam.direction = up
            elif beam.direction == up:
                beam.direction = right
            elif beam.direction == down:
                beam.direction = left
            else:
                continue
        elif nextItem == "\\":
            if beam.direction == left:
                beam.direction = up
            elif beam.direction == right:
                beam.direction = down
            elif beam.direction == up:
                beam.direction = left
            elif beam.direction == down:
                beam.direction = down
            else:
                continue
        elif nextItem == "|":
            if beam.direction == up or beam.direction == down:
                continue
            elif beam.direction == left or beam.direction == right:
                beams.append(Beam(beam.getPos(), up))
                beams.append(Beam(beam.getPos(), down))
                map[nextPos[0]][nextPos[1]] = "+"
                break
            else:
                print("ERROR")
                break
        elif nextItem == "-":
            if beam.direction == left or beam.direction == right:
                continue
            elif beam.direction == up or beam.direction == down:
                beams.append(Beam(beam.getPos(), left))
                beams.append(Beam(beam.getPos(), right))
                map[nextPos[0]][nextPos[1]] = "#"
                break
            else:
                print("ERROR")
                break
        else:
            print("ERROR")
            break


for coord in visited:
    visu[coord[0]][coord[1]] = "#"

#for line in visu:
#    print("".join(line))

print("Part1:", len(visited))