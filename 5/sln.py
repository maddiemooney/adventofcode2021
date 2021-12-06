def partone(lst):
	visited = {}
	for pair in lst:
		coord = pair.split(" -> ")
		start = tuple(int(x.strip()) for x in coord[0].split(","))
		end = tuple(int(x.strip()) for x in coord[1].split(","))

		line = []

		if start[0] == end[0]:
			if end[1] > start[1]:
				for i in range(0, end[1]-start[1]):
					line.append((start[0], start[1]+i))
			elif end[1] < start[1]:
				for i in range(0, start[1]-end[1]):
					line.append((start[0], start[1]-i))
			line.append(end)

		elif start[1] == end[1]:
			if end[0] > start[0]:
				for i in range(0, end[0]-start[0]):
					line.append((start[0]+i, start[1]))
			elif end[0] < start[0]:
				for i in range(0, start[0]-end[0]):
					line.append((start[0]-i, start[1]))
			line.append(end)

		else:
			line = []

		for point in line:
			if point in visited:
				visited[point] += 1
			else:
				visited[point] = 1

	total = 0
	for point, count in visited.items():
		if count >= 2:
			total += 1
		
	return total

def parttwo(lst):
	visited = {}
	for pair in lst:
		coord = pair.split(" -> ")
		start = tuple(int(x.strip()) for x in coord[0].split(","))
		end = tuple(int(x.strip()) for x in coord[1].split(","))

		line = []

		if start[0] == end[0]:
			if end[1] > start[1]:
				for i in range(0, end[1]-start[1]):
					line.append((start[0], start[1]+i))
			elif end[1] < start[1]:
				for i in range(0, start[1]-end[1]):
					line.append((start[0], start[1]-i))

		elif start[1] == end[1]:
			if end[0] > start[0]:
				for i in range(0, end[0]-start[0]):
					line.append((start[0]+i, start[1]))
			elif end[0] < start[0]:
				for i in range(0, start[0]-end[0]):
					line.append((start[0]-i, start[1]))

		else:
			if end[1] > start[1] and end[0] > start[0]:
				for i in range(0, end[1]-start[1]):
					line.append((start[0]+i, start[1]+i))
			elif end[1] < start[1] and end[0] < start[0]:
				for i in range(0, start[1]-end[1]):
					line.append((start[0]-i, start[1]-i))
			elif end[1] > start[1] and end[0] < start[0]:
				for i in range(0, end[1]-start[1]):
					line.append((start[0]-i, start[1]+i))
			elif end[1] < start[1] and end[0] > start[0]:
				for i in range(0, start[1]-end[1]):
					line.append((start[0]+i, start[1]-i))
		line.append(end)
			
		for point in line:
			if point in visited:
				visited[point] += 1
			else:
				visited[point] = 1

	total = 0
	for point, count in visited.items():
		if count >= 2:
			total += 1
		
	return total


file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]
print(partone(lst))
print(parttwo(lst))



