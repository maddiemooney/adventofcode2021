def partone(lst):
	total = 0
	lens = [2, 3, 4, 7]
	for output in lst:
		if len(output) in lens:
			total += 1 
	return total

def parttwo(inputs, outputs):
	total = 0
	for group in inputs:
		idx = inputs.index(group)
		digit = ''
		solve = {}

		# find "1", "4", "7", "8"
		# get possible "0", "6", "9"
		# get possible "2" "3", "5"
		sixlen = []
		fivelen = []
		for pattern in set(group):
			key = ''.join(sorted(pattern))
			if len(key) == 2:
				solve[1] = key
			elif len(key) == 3:
				solve[7] = key
			elif len(key) == 4:
				solve[4] = key
			elif len(key) == 5:
				fivelen.append(key)
			elif len(key) == 6:
				sixlen.append(key)
			elif len(key) == 7:
				solve[8] = key
			else:
				print("something is wrong")

		# find "0", "6", "9"
		for item in sixlen:
			if len(set(item).intersection(solve[1])) == 1:
				solve[6] = item
			elif len(set(item).intersection(solve[4])) == 4:
				solve[9] = item
			else:
				solve[0] = item

		# find "2", "3", "5"
		for item in fivelen:
			if len(set(item).intersection(solve[1])) == 2:
				solve[3] = item
			elif len(set(item).intersection(solve[6])) == 5:
				solve[5] = item
			else:
				solve[2] = item

		# i am a bad programmer
		solve2 = {v: k for k, v in solve.items()}

		for o in outputs[idx]:
			key = ''.join(sorted(o))
			digit += str(solve2[key])
		total += int(digit)

	return total


file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]
inputs = [x.split("|")[0].strip().split(" ") for x in lst]
outputs = [x.split("|")[1].strip().split(" ") for x in lst]
flat_outputs = [item for sublist in outputs for item in sublist]
print(partone(flat_outputs))
print(parttwo(inputs, outputs))

