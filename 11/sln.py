def getneighbors(lst, coord):
	neighbors = []
	i = coord[0]
	j = coord[1]
	if i != 0:
		neighbors.append((i-1, j))

	if i != len(lst)-1:
		neighbors.append((i+1, j))

	if j != 0:
		neighbors.append((i, j-1))

	if j != len(lst[i])-1:
		neighbors.append((i, j+1))

	if i != 0 and j != 0:
		neighbors.append((i-1, j-1))

	if i != 0 and j != len(lst[i])-1:
		neighbors.append((i-1, j+1))

	if i != len(lst)-1 and j != 0:
		neighbors.append((i+1, j-1))

	if i != len(lst)-1 and j != len(lst[i])-1:
		neighbors.append((i+1, j+1))

	return neighbors

def get_key(my_dict, val):
	for key, value in my_dict.items():
		if val in value:
			return key
 
	return "key doesn't exist"

def partone(lst, steps):
	total = 0
	energy = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
	for i in range(0,len(lst)):
		for j in range(0, len(lst[i])):
			elevel = lst[i][j]
			energy[elevel].append((i,j))

	for step in range(0, steps):

		visited = [] #can only flash once per step

		# increases by 1
		flash = energy[9]
		energy[9] = energy[8]
		energy[8] = energy[7]
		energy[7] = energy[6]
		energy[6] = energy[5]
		energy[5] = energy[4]
		energy[4] = energy[3]
		energy[3] = energy[2]
		energy[2] = energy[1]
		energy[1] = energy[0]
		energy[0] = flash

		tovisit = flash.copy()
		visited = []

		while(len(tovisit) > 0):
			coord = tovisit.pop(0)

			if coord not in visited:
				visited.append(coord)
				neighbors = getneighbors(lst, coord)

				for neighbor in neighbors:
					if neighbor not in visited and neighbor not in tovisit:
						elevel = get_key(energy, neighbor)

						if elevel == 9:
							tovisit.append(neighbor)
							energy[9].remove(neighbor)
							energy[0].append(neighbor)
							
						elif elevel != 0:
							energy[elevel].remove(neighbor)
							energy[elevel+1].append(neighbor)
			
		total += len(visited)
	return total

def parttwo(lst):
	step = 0
	energy = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
	for i in range(0,len(lst)):
		for j in range(0, len(lst[i])):
			elevel = lst[i][j]
			energy[elevel].append((i,j))

	while len(energy[0]) != len(lst) * len(lst[i]):

		visited = [] #can only flash once per step

		# increases by 1
		flash = energy[9]
		energy[9] = energy[8]
		energy[8] = energy[7]
		energy[7] = energy[6]
		energy[6] = energy[5]
		energy[5] = energy[4]
		energy[4] = energy[3]
		energy[3] = energy[2]
		energy[2] = energy[1]
		energy[1] = energy[0]
		energy[0] = flash

		tovisit = flash.copy()
		visited = []

		while(len(tovisit) > 0):
			coord = tovisit.pop(0)

			if coord not in visited:
				visited.append(coord)
				neighbors = getneighbors(lst, coord)

				for neighbor in neighbors:
					if neighbor not in visited and neighbor not in tovisit:
						elevel = get_key(energy, neighbor)

						if elevel == 9:
							tovisit.append(neighbor)
							energy[9].remove(neighbor)
							energy[0].append(neighbor)
							
						elif elevel != 0:
							energy[elevel].remove(neighbor)
							energy[elevel+1].append(neighbor)
			
		step += 1
	return step



file1 = open('input.txt', 'r')
lst = [list(map(int, x.strip())) for x in file1.readlines()]
print(partone(lst, 100))
print(parttwo(lst))


