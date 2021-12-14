import collections

def partone(polymer, rules, steps):
	for i in range(0, steps):
		newpoly = ''
		for c in range(0, len(polymer)-1):
			group = polymer[c:c+2]
			if group in rules:
				if len(newpoly) > 0:
					if newpoly[-1] == group[0]:
						newpoly += rules[group] + group[1]
				else:
					newpoly += group[0] + rules[group] + group[1]
			else:
				newpoly += group
		polymer = newpoly

	tally = collections.Counter(polymer).most_common()
	return tally[0][1] - tally[-1][1]

def parttwo(polymer, rules, steps):

	counter1 = collections.Counter()
	for i in range(0, len(polymer)-1):
	    counter1[polymer[i:i+2]] += 1

	for i in range(0, steps):
	    counter2 = counter1
	    counter1 = collections.Counter()
	    for group in counter2.keys():
	        counter1[group[0] + rules[group]] += counter2[group]
	        counter1[rules[group] + group[1]] += counter2[group]

	counter3 = collections.Counter()
	counter3[polymer[0]] = 1
	for group, num in counter1.items():
	    counter3[group[1]] += num

	tally = counter3.most_common()
	return(tally[0][1] - tally[-1][1])


file1 = open('input.txt', 'r')
rules = {}
polymer = ''


for line in file1.readlines():
	if "->" in line:
		pair = line.split(" -> ")
		rules[pair[0].strip()] = pair[1].strip()
	elif any(c.isalpha() for c in line):
		polymer = line.strip()

print(partone(polymer, rules, 10))
print(parttwo(polymer, rules, 40))
