class Node:
    def __init__(self, is_value, left_value, right_value):
        self.is_attribute = is_value
        self.left_attribute = left_value
        self.right_attribute = right_value
    
    def __str__(self):
        return f"Node(is={self.is_attribute}, left={self.left_attribute}, right={self.right_attribute})"
        
def create_node(parameters):
    return Node(*parameters)

def find_node_by_is(nodes, target_is_value):
    matching_nodes = [node for node in nodes if node.is_attribute == target_is_value]
    return matching_nodes[0] if matching_nodes else None

nodes = []
instructs = []
start = "AAA"
current_node = None
steps = 0

with open('test2.txt') as f:
	lines = f.readlines()

for line in lines[2:]:
     line = line.replace("=", "").replace("(", "").replace(")","").replace(",","").split()
     nodes.append(create_node(line))

current_node = find_node_by_is(nodes, start)
#print(current_node)

instructs = lines[0].strip("\n")


while not current_node.is_attribute == "ZZZ":
    for char in instructs:
        #print(char)
        if char == "L":
            current_node = find_node_by_is(nodes, current_node.left_attribute)
        elif char == "R":
            current_node = find_node_by_is(nodes, current_node.right_attribute)
        else:
            print("ERROR")
            break
        
        steps+=1
        if current_node.is_attribute == "ZZZ":
            break

print("Part 1:", steps)