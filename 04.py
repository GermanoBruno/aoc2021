import inputUtils

class Board:
	def __init__(self, size, numbers):
		self.size = size
		self.numbers = numbers
		self.marked = [[0 for column in range(0, size)] for row in range(0, size)]
		self.score = sum([sum(row) for row in self.numbers])

	def getMarked(self):
		return self.marked

	def getNumbers(self):
		return self.numbers

	def getSize(self):
		return self.size

	def getScore(self):
		return self.score

	def checkBingo(self):
		columns = [[row[i] for row in self.marked] for i in range(0, self.size)]
		bingo = [1 for i in range(0, self.size)]
		if ((bingo in columns) or (bingo in self.marked)):
			return True
		return False

	def markNum(self, num):
		for row in self.numbers:
			if(num in row):
				self.marked[self.numbers.index(row)][row.index(num)] = 1
				self.score = self.score - num
				return self.checkBingo()		
		return False
####################################################################

def getBoards(l):
	boardList = []
	numOrder = [int(i) for i in l[0].split(',')]
	boards = l[1:]
	for i in range(0, int(len(boards)/6)):
		board = [boards[(i*6) + j].split() for j in range(1,6)]
		board = [[int(i) for i in line] for line in board]
		boardList.append(Board(len(board), board))
	return numOrder, boardList


def winningBoard(l):
	numOrder, boards = getBoards(l)
	for each in numOrder:
		for board in boards:
			if(board.markNum(each)):
				return(board.getScore() * each)

def losingBoard(l):
	numOrder, boards = getBoards(l)

	for each in numOrder:
		for board in boards:
			if(board.markNum(each)):
				score = board.getScore()*each
				boards.remove(board)
				if(len(boards) == 0):
					return score
####################################################################


import inputUtils

inp = inputUtils.loadInput(4)

# Part 1
print(winningBoard(inp))
# Part 2
print(losingBoard(inp))