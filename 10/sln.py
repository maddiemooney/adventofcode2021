from collections import deque
from statistics import median

def partone(lst):
	opens = ['(', '[', '{', '<']
	closes = [')', ']', '}', '>']
	pairs = {'(': ')', '[': ']', '{':'}', '<':'>'}
	scores = {')': 3, ']': 57, '}':1197, '>':25137}

	total = 0

	for line in lst:
		corrupt = False
		expected = deque()

		for char in line:
			if char in opens:
				expected.append(pairs[char])
			elif char in closes:
				nxt = expected.pop()
				if nxt != char and not corrupt:
					total += scores[char]
					corrupt = True
	return total 

def parttwo(lst):
	opens = ['(', '[', '{', '<']
	closes = [')', ']', '}', '>']
	pairs = {'(': ')', '[': ']', '{':'}', '<':'>'}
	scores = {')': 1, ']': 2, '}':3, '>':4}

	total = []

	for line in lst:
		corrupt = False
		expected = deque()

		for char in line:
			if char in opens:
				expected.appendleft(pairs[char])
			elif char in closes:
				nxt = expected.popleft()
				if nxt != char and not corrupt:
					corrupt = True
		if not corrupt:
			linescore = 0
			for e in expected:
				linescore = linescore * 5 + scores[e]
			total.append(linescore)

	total.sort()
	return median(total)

file1 = open('input.txt', 'r')
lst = [list(x.strip()) for x in file1.readlines()]
print(partone(lst))
print(parttwo(lst))
