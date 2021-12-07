import statistics

def partone(lst):
	totalfuel = 99999999999999999999999
	for mode in list(set(lst)):
		tmpfuel = 0
		for crab in lst:
			tmpfuel += abs(crab-mode)
		if tmpfuel < totalfuel:
			totalfuel = tmpfuel
	return totalfuel

def parttwo(lst):
	totalfuel = 99999999999999999999999

	for i in range(min(lst), max(lst)):
		tmpfuel = 0
		for crab in lst:
			steps = abs(crab-i)
			for j in range(1,steps+1):
				tmpfuel+=j
		if tmpfuel < totalfuel:
			totalfuel = tmpfuel
	return totalfuel


file1 = open('input.txt', 'r')
lst = [int(x.strip()) for x in file1.readline().split(",")]
lst.sort()
print(partone(lst))
print(parttwo(lst))