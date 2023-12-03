with open('input.txt') as f:
	lines = f.readlines()

redmax = 12
greenmax = 13
bluemax = 14

ans = 0


for line in lines:
	line = line.replace(":", ";")
	tokens = line.split(";")

	#print(line)

	redcount = 0
	greencount = 0
	bluecount = 0
	idx = 0

	for token in tokens:
		#print("TOKEN")
		#print(token)
		if "Game " in token:
			idx = token.replace("Game ","")

		else:

			token = token.split(",")
			#print(token)

			for item in token:

				if " red" in item:
					count = item.replace(" red", "")
					count = int(count)
					##print(count)
					if redcount < count:
						redcount = count;
				if " green" in item:
					count = item.replace(" green", "")
					count = int(count)
					##print(count)
					if greencount < count:
						greencount = count
				if " blue" in item:
					count = item.replace(" blue", "")
					count = int(count)
					##print(count)
					if bluecount < count:
						bluecount = count
	#print(redcount)
	#print(greencount)
	#print(bluecount)

	subsum = redcount*bluecount*greencount
	ans+= subsum

print(ans)