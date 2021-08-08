
def check(board):
	diag1 = []
	diag2 = []	
	for i in range(n):
		for j in range(n):
			if board[i][j] == 1:
				r_index = i
				c_index = j
				# check row (to the right only)
				for k in range(n-j-1):
					if board[i][j+k+1] == 1:
						print('Not a solution')
						return False
				# check col (below only)
				for z in range(n-i-1):
					if board[i+z+1][j] == 1:
						print('Not a solution')
						return False
				# check diag
				diag1.append(i + j)
				diag2.append(i - j)

	if len(diag1) != len(set(diag1)):
		print('Not a solution')
		return False
	if len(diag2) != len(set(diag2)):
		print('Not a solution')
		return False
	print('Valid solution')

n = 4

board = [[0 for x in range(n)] for y in range(n)]

d1 = []
d2 = []
r = []

def output(board):
	for i in board:
		print((" {} "*n).format(*[x for x in i]))

def solve(board, col):
	
	if col >= n:
		return True
		
	for row in range(n):
		if d1.count(row + col) <= 1 & d2.count(row - col) <= 1 & r.count(row) < 1:
			# safe, add queen
			board[row][col] = 1
			r.append(row)
			d1.append(row + col)
			d2.append(row - col)
			
			# check to see if next column has a solution
			if solve(board,col + 1):
				return True
				
			# if not, remove queen and try next row
			board[row][col] = 0
			r.pop(-1)
			d1.pop(-1)
			d2.pop(-1)
	
	# no solution 
	return False	
	
solve(board, 0)
output(board)
check(board)