def partone(boards, boardtotals, nums):
	
	for num in nums:
		for board in boards:
		
			idx = boards.index(board)
			
			for row in board:
				if num in row:
					col = row.index(num)
					boardtotals[idx] -= row[col]
					row[col] = 'x'
					if row == ['x', 'x', 'x', 'x', 'x']:
						return boardtotals[idx] * num
					elif board[0][col] == 'x' and\
						board[1][col] == 'x' and\
						board[2][col] == 'x' and\
						board[3][col] == 'x' and\
						board[4][col] == 'x':
						return boardtotals[idx] * num		

def parttwo(boards, boardtotals, nums):
	
	for num in nums:
		for board in list(boards):

			idx = boards.index(board)
			for row in board:
				if num in row:
					col = row.index(num)
					
					boardtotals[idx] -= row[col]
					row[col] = 'x'
					if row == ['x', 'x', 'x', 'x', 'x']:
						if len(boards) > 1:
							boards.remove(board)
							del boardtotals[idx]
						else:
							return boardtotals[idx] * num
					elif board[0][col] == 'x' and\
						board[1][col] == 'x' and\
						board[2][col] == 'x' and\
						board[3][col] == 'x' and\
						board[4][col] == 'x':
						if len(boards) > 1:
							boards.remove(board)
							del boardtotals[idx]
						else:
							return boardtotals[idx] * num

#main stuff
file1 = open('input.txt', 'r')
lines = file1.readlines()
nums = [int(x.strip()) for x in lines[0].split(",")]

boards = []
boardtotals = []
counter = 0   

# initialize
board = []
total = 0

for line in lines[2:]:
	#print(str(counter)+": "+line)
	if counter <= 4:
		row = []
		for char in line.split(" "):
			if char != '' and char != '\n':
				row.append(int(char.strip()))
				total += int(char.strip()) 

		if row:
			board.append(row)
			counter += 1
	else:
		boards.append(board)
		boardtotals.append(total)

		board = []
		total = 0
		counter = 0

print(partone(boards, boardtotals, nums))
print(parttwo(boards, boardtotals, nums))

