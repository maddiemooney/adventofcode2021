from functools import reduce

def partone(lst):
	total = 0
	for i in range(0,len(lst)):
		for j in range(0, len(lst[i])):
			neighbors = []
			if i != 0:
				neighbors.append(lst[i-1][j])
			if i != len(lst)-1:
				neighbors.append(lst[i+1][j])
			if j != 0:
				neighbors.append(lst[i][j-1])
			if j != len(lst[i])-1:
				neighbors.append(lst[i][j+1])

			if lst[i][j] < min(neighbors):
				total += (1+lst[i][j])
	return total

def getbasin(lst, coord, visited):
	basin = []
	x = coord[0]
	y = coord[1]
	if lst[x][y] != 9 and coord not in visited:
		basin.append(lst[x][y])
		visited.append((x,y))
		if x != 0:
			basin+=getbasin(lst, (x-1,y), visited)
		if x != len(lst)-1:
			basin+=getbasin(lst, (x+1,y), visited)
		if y != 0:
			basin+=getbasin(lst, (x,y-1), visited)
		if y != len(lst[x])-1:
			basin+=getbasin(lst, (x,y+1), visited)
		
	return basin

def parttwo(lst):
	# get start points
	low = []
	for i in range(0,len(lst)):
		for j in range(0, len(lst[i])):
			neighbors = []
			if i != 0:
				neighbors.append(lst[i-1][j])
			if i != len(lst)-1:
				neighbors.append(lst[i+1][j])
			if j != 0:
				neighbors.append(lst[i][j-1])
			if j != len(lst[i])-1:
				neighbors.append(lst[i][j+1])

			if lst[i][j] < min(neighbors):
				low.append((i,j))

	basins = []
	for coord in low:
		visited = []
		basin = getbasin(lst, coord, visited)
		basins.append(len(basin))

	basins.sort(reverse=True)
	return reduce((lambda x, y: x * y), basins[0:3])



file1 = open('input.txt', 'r')
lst = [list(map(int, x.strip())) for x in file1.readlines()]
print(partone(lst))
print(parttwo(lst))