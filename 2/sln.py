def partone(lst):
	x = 0
	y = 0
	for cmd in lst:
		if "forward" in cmd:
			x += int(cmd[-1])
		elif "down" in cmd:
			y += int(cmd[-1])
		elif "up" in cmd:
			y -= int(cmd[-1])
	return x*y

def parttwo(lst):
	x = 0
	y = 0
	aim = 0
	for cmd in lst:
		if "forward" in cmd:
			x += int(cmd[-1])
			y += int(cmd[-1]) * aim
		elif "down" in cmd:
			aim += int(cmd[-1])
		elif "up" in cmd:
			aim -= int(cmd[-1])
	return x*y

file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))
	
