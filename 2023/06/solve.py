with open('input.txt') as f:
	lines = f.readlines()

times = lines[0].split()
times = times[1:]
combined_time = int(''.join(map(str, times)))
print(combined_time)

dists = lines[1].split()
dists = dists[1:]
combined_dist = int(''.join(map(str, dists)))
print(combined_dist)

part1 = 1
part2 = 0

for x in range (len(times)):
	time = int(times[x])
	dist = int(dists[x])

	num_sols = 0
	for t in range(0,time+1):
		traveled = (time-t)*t
		if traveled > dist:
			num_sols += 1
	part1 *= num_sols

for t in range(0,combined_time+1):
		traveled = (combined_time-t)*t
		if traveled > combined_dist:
			part2 += 1

print("Part1:", part1)
print("Part2:", part2)
