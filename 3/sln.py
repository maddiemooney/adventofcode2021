def partone(lst):
	gamma = ''
	epsilon = ''
	for i in range(0, len(lst[0])):
		zeros = 0
		ones = 0
		for number in lst:
			if number[i] == '0':
				zeros += 1
			elif number[i] == '1':
				ones += 1
		if zeros > ones:
			gamma += '0'
			epsilon += '1'
		elif ones > zeros:
			gamma += '1'
			epsilon += '0'
	return(int(gamma,2) * int(epsilon,2))
		
def parttwo(lst):
	oxygen = lst.copy()
	co2scrubber = lst.copy()

	while(len(oxygen) > 2):
		
		for i in range(0, len(oxygen[0])):
			zeros = []
			ones = []
			for j in range(0, len(oxygen)):
				if oxygen[j][i] == '0':
					zeros.append(oxygen[j])
				elif oxygen[j][i] == '1':
					ones.append(oxygen[j])
			if len(oxygen) > 1:
				if len(zeros) > len(ones):
					for idx in ones:
						oxygen.remove(idx)
				if len(ones) >= len(zeros):
					for idx in zeros:
						oxygen.remove(idx)

	while(len(co2scrubber) > 2):
		for i in range(0, len(co2scrubber[0])):
			zeros = []
			ones = []
			for j in range(0, len(co2scrubber)):
				if co2scrubber[j][i] == '0':
					zeros.append(co2scrubber[j])
				elif co2scrubber[j][i] == '1':
					ones.append(co2scrubber[j])
			if len(co2scrubber) > 1:
				if len(zeros) > len(ones):
					for idx in zeros:
						co2scrubber.remove(idx)
				if len(ones) >= len(zeros):
					for idx in ones:
						co2scrubber.remove(idx)
	return(int(oxygen[0],2) * int(co2scrubber[0],2))

file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))

