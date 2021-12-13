def partone(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.isupper():
            newpaths = partone(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths 


def check(path, node):
	if node.isupper():
		return True
	elif node == 'start' or node == 'end':
		return False
	else:
		if path.count(node) == 2:
			return False
		elif path.count(node) == 1:
			valid = True
			for p in path:
				if p.islower() and path.count(p) == 2:
					valid = False
			return valid


def parttwo(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if start not in graph:
		return []
	paths = []
	for node in graph[start]:
		if node not in path or check(path, node):
			newpaths = parttwo(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths


file1 = open('input.txt', 'r')
lst = [line.strip() for line in file1.readlines()]
nodes = {}
for line in lst:
	pair = line.split("-")
	parent = pair[0]
	child = pair[1]

	if parent not in nodes:
		nodes[parent] = [child]
	else:
		nodes[parent].append(child)
	if child not in nodes:
		nodes[child] = [parent]
	else:
		nodes[child].append(parent)


print(len(partone(nodes, 'start', 'end')))
print(len(parttwo(nodes, 'start', 'end')))
