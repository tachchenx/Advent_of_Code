class dir:
	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.subdirs = []
		self.files = []
		self.size = 0
		self.active = 0

class file:
	def __init__(self, name, size):
		self.name = name
		self.size = size

def printTree(directory, depth):
	space = ""
	suffix = ""

	if directory.active == 1:
		suffix = "(dir) <----"
	else:
		suffix = "(dir)"

	for x in range(depth):
		space += "  "
	print(space, directory.name, suffix)

	for subdir in directory.subdirs:
		printTree(subdir, depth+1)

	for files in directory.files:
		print(space + "  ", files.name, files.size)

def addSize(directory, size):
	
	directory.size += size

	if directory != baseDir:
		addSize(directory.parent, size)

def findSizes(directory):
	global sizeSum
	if directory.size <= 100000:
		sizeSum += int(directory.size)
	for subdir in directory.subdirs:
		findSizes(subdir)

def findBestDir(directory, need):
	global lowestSoFar

	if directory.size >= need and directory.size<= lowestSoFar:
		lowestSoFar = directory.size
		
	for subdir in directory.subdirs:
		findBestDir(subdir, need)


baseDir = dir("/", None)
baseDir.active = 1
currentDir = None
token = ""
sizeSum = 0
lowestSoFar = 70000000

with open('input.txt') as f:
	inp = f.readlines()

for line in inp:
	line = line.replace("\n","")
	line = line.split()

	# Command found
	if line[0] == "$":
		
		token = line[1]

		if token == "cd":
			arg = line[2]
			if arg == "..":
				currentDir.active = 0
				currentDir.parent.active = 1
				currentDir = currentDir.parent
			elif arg == "/":
				if currentDir != None:
					currentDir.active = 0
				baseDir.active = 1
				currentDir = baseDir
			else:
				for subdir in currentDir.subdirs:
					if subdir.name == arg:
						currentDir.active = 0
						subdir.active = 1
						currentDir = subdir
						break
		elif token != "ls":
			print ("ERROR")

	#console output found
	else:
		identifier = line[0]
		if identifier == "dir":
			#found new dir
			name = line[1]
			currentDir.subdirs.append(dir(name, currentDir))
		else:
			#found file
			name = line[1]
			size = int(line[0])
			currentDir.files.append(file(name, size))
			addSize(currentDir, size)

printTree(baseDir,0)
findSizes(baseDir)

currentSpace = 70000000 - baseDir.size
neededSpace = 30000000 - currentSpace

findBestDir(baseDir, neededSpace)

print(sizeSum)
print(lowestSoFar)


