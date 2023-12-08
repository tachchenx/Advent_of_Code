from math import lcm

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

with open('input.txt') as f:
	lines = f.readlines()

for line in lines[2:]:
     line = line.replace("=", "").replace("(", "").replace(")","").replace(",","").split()
     nodes.append(create_node(line))

current_node = find_node_by_is(nodes, start)
#print(current_node)

instructs = lines[0].strip("\n")

nodes_list = []

for node in nodes:
    is_val = node.is_attribute
    if str(is_val).endswith("A"):
        nodes_list.append(node)
        #print(str(node))
print(len(nodes_list))
end = False
step_list = []

for x in range(len(nodes_list)):
    #print("Runde", x)
    while True:
        end = False
        for char in instructs:
            #print("From:", str(nodes_list[x]))
            if char == "L":
                nodes_list[x] = find_node_by_is(nodes, nodes_list[x].left_attribute)
            elif char == "R":
                nodes_list[x] = find_node_by_is(nodes, nodes_list[x].right_attribute)
            else:
                print("ERROR")
                break
            #print("To:", str(nodes_list[x]))
            steps+=1
            
            is_val = nodes_list[x].is_attribute
            if str(is_val).endswith("Z"):
                #print("ENDE")
                end = True
                break
            
        if end:
            break
    step_list.append(steps)
    steps = 0

#print(step_list)

print("Part2:", lcm(*step_list))