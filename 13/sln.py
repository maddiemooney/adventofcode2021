import sys
import re

def transpose(points):
    return set((y, x) for x, y in points)


def fold(points, axis, num):
	if axis == 'x':
		return transpose(fold_y(transpose(points), num))
	elif axis == 'y':
		return fold_y(points, num)

def fold_y(points, num):
    top = set(p for p in points if p[1] < num)
    bottom = set(p for p in points if p[1] > num)

    for x, y in bottom:
        point = (x, num - (y - num))
        top.add(point)

    return top


def parttwo(points):
    width = max(p[0] for p in points) + 1
    height = max(p[1] for p in points) + 1

    for y in range(0, height):
        print("".join("#" if (x, y) in points else " " for x in range(0, width)))

folds = []
points = []
file1 = open('input.txt', 'r')
for line in file1.readlines():
	if "fold" in line:
		pair = line.split('=')
		folds.append((pair[0][-1], int(pair[1].strip())))
	else:
		pair = line.strip().split(',')
		if pair[0] != '':
			points.append((int(pair[0]), int(pair[1])))

for i, (axis, num) in enumerate(folds):
    points = fold(points, axis, num)
    if i == 0:
        print(len(points))
parttwo(points)