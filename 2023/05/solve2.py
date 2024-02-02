type_list = ["seeds:", "seed_to_soil", "soil_to_fertilizer", "fertilizer_to_water", "water_to_light", "light_to_temperature", "temperature_to_humidity", "humidity_to_location"]


seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

lowest_dist = None

def run_seed(seed, conv_ranges, lower):
	for rng in conv_ranges:
		for i in range(0, len(conv_ranges), 3):
			dest, source, rng = conv_ranges[i:i + 3]
			if seed < source or seed > (source + rng - 1): continue	
			if lower == -1: lower = source + rng
			seed = seed - source + dest
			break
	return seed, lower

with open('test.txt') as f:
	lines = f.readlines()

type = ""

for line_idx in range(len(lines)):
	line = lines[line_idx]
	line = line.strip("\n")
	line = line.split()
	if line:
		#print(line)

		if not line[0].isdigit():
			type = line[0].replace('-', '_')
			if not type == "seeds:":
				continue

		#print(type)
		if type == "seeds:":
			for x in range(1, len(line)):
				seeds.append(int(line[x]))

		elif type in type_list[1:]:
			for num in line:
				globals()[type].append(int(num))

seed_ranges = []

for idx in range(0, len(seeds)-1 ,2):
	lower = seeds[idx]
	upper = seeds[idx]+seeds[idx+1]-1
	seed_ranges.append((lower, upper))

seed_ranges.sort(key=lambda x: x[0])
print(seed_ranges)

for idx in range(len(seed_ranges)-1):
	upper_left = seed_ranges[idx][1]
	lower_right = seed_ranges[idx+1][0]

	if(upper_left > lower_right):
		print("ERROR")

conv_ranges = []

for type in type_list[1:]:
	conv_ranges.append(globals()[type])

conv_ranges = [element for sublist in conv_ranges for element in sublist]

print(conv_ranges)
part2 = float('inf')

for lower, higher in seed_ranges:
	while lower < higher:
		seed = lower
		seed, lower = run_seed(seed, conv_ranges, lower=-1)
		part2 = min(part2, seed)

print(part2)