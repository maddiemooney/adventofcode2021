import time

def partone(lst, time):
	for i in range(0, time):
		#print(lst)
		for idx, fish in enumerate(lst):
			lst[idx] = fish - 1
			if fish == 0:
				lst[idx] = 6
				lst.append(9)
	return len(lst)

def parttwo(lst, time):
	ages = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	for fish in lst:
		ages[fish] += 1

	for i in range(0,time):
		spawn = ages[0]
		ages[0] = ages[1]
		ages[1] = ages[2]
		ages[2] = ages[3]
		ages[3] = ages[4]
		ages[4] = ages[5]
		ages[5] = ages[6]
		ages[6] = ages[7] + spawn
		ages[7] = ages[8]
		ages[8] = spawn
	return sum(ages.values())


file1 = open('input.txt', 'r')
lst = [int(x.strip()) for x in file1.readline().split(",")]
start_time = time.time()
partone(lst, 80)
print("--- Part 1: %s seconds ---" % (time.time() - start_time))
start_time = time.time()
parttwo(lst,256)
print("--- Part 2: %s seconds ---" % (time.time() - start_time))