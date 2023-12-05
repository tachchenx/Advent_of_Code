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

with open('input.txt') as f:
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

#for idx in range(len(type_list)):
#	cur_type = type_list[idx].strip(":")
#	print(cur_type)
#	print(globals()[cur_type])


for seed in seeds:
	print("BEGINNING WITH SEED:" , seed, "####################")
	for type_idx in range(1,len(type_list)):
		cur_type = type_list[type_idx]
		#print(cur_type)
		#print(globals()[cur_type])

		for idx in range(0, len(globals()[cur_type])-1 ,3):
			#print("IDX:", idx)
			#print(globals()[cur_type][idx], globals()[cur_type][idx+1], globals()[cur_type][idx+2])
			dst_range = globals()[cur_type][idx]
			src_range = globals()[cur_type][idx+1]
			range_len = globals()[cur_type][idx+2]
			#print("Seed before", seed)
			if src_range <= seed <= src_range+range_len-1:
				seed += (dst_range-src_range)
				break

	print("Seed after", seed)
	print("##########")
	if(lowest_dist == None or lowest_dist > seed):
		lowest_dist = seed

print("Lowest dist is:", lowest_dist)