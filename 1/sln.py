def partone(lst):
	total = 0
	for i in range(1,len(lst)):
		if lst[i] > lst[i-1]:
			total += 1
	return total	

def parttwo(lst):
	total = 0
	for i in range(2, len(lst)-1):
		if (lst[i+1] + lst[i] + lst[i-1]) > (lst[i] + lst[i-1] + lst[i-2]):
			total += 1
	return total

file1 = open('input.txt', 'r')
lst = [int(line.strip()) for line in file1.readlines()]

print(partone(lst))
print(parttwo(lst))
