class dir:
	def __init__(self, name):
		self.name = name
		self.subdirs = []

base = dir("base")
node1 = dir("derived1")
node2 = dir("derived2")
node3 = dir("derived3")
base.subdirs.append(node1)
base.subdirs.append(node2)
base.subdirs.append(node3)


print(base.name)
for entrys in base.subdirs:
	print(entrys.name)