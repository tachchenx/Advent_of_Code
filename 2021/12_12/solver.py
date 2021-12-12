input = [line.split('-') for line in open('testinput.txt').read().splitlines()]

#print(f'Input: {input}')

def makeGraph(ways):
    graph = {}
    for c1, c2 in ways:
        if c1 not in graph:
            graph[c1] = set()
        if c2 not in graph:
            graph[c2] = set()
        graph[c1].add(c2)
        graph[c2].add(c1)
    return graph

graph = makeGraph(input)
print(f'{graph}')

def countWays(graph, position, visited, visited_2nd = False):
	if position == "end":
		return 1
	
	counter = 0
	for adj in graph[position]:
		#print ("Adj:", adj)
		if adj != "start":
			if adj.isupper() or adj not in visited:
				counter += countWays(graph, adj, visited + [adj], visit_2nd, True)
			elif visit_2nd == False:
				counter += countWays(graph, adj, visited, True)

	return counter


visited_default = ['start']
graph = makeGraph(input)
part1 = countWays(graph, 'start', visited_default, True)
part2 = countWays(graph, 'start', visited_default, False)

print ("Part1:", part1)
print ("Part2:", part2)