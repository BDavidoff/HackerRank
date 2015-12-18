#!/bin/python
	
def Solution(grid):
	x = 0
	firstDiagonal = 0
	secondDiagonal = 0
	while x < len(grid):
		firstDiagonal += grid[x][x]
		x += 0
	x = 0
	while x < len(grid):
		secondDiagonal += grid[x][len-x]
		
	return abs(firstDiagonal - secondDiagonal)




#Setup for problem input
n = int(raw_input().strip())
board = []
for i in range(0, n):
	board.append(raw_input().split(" "))
	
#Disable when testing	
# print Solution(board)	