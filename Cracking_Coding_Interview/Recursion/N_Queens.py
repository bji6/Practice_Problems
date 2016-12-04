#ben isenberg 10/2/2016
#something wrong with it, doesn't get last column
import sys

#recursive method, N queens
def nQueens(grid,column,N,queen_list):
	#base case
	#print(len(queen_list))
	if (len(queen_list) == N):
		printGrid(grid,N)
		return

	#launch recursive call for every valid queen placement
	for i in range(N):
		new_placement = [i,column]  # (y,x) (row,col)
		#print("New placement %s,%s" % (column,i))

		#add queen if valid
		if (checkValid(queen_list,i,column)):
			
			grid[new_placement[1]][new_placement[0]] = "Q"
			
			printGrid(grid,N)
			
			queen_list2 = queen_list
			queen_list2.append(new_placement)

			nQueens(grid,column+1,N,queen_list2)


def checkValid(queen_list, row, col):
	#check if placement is valid	
	for q in queen_list:
		if (row == q[0]):  #check shared row, y
			return False
		if (col == q[1]):  #check shared column, x
			return False
		
		row_distance = abs(row - q[0])
		col_distance = abs(col - q[1])
		#check for diagonal
		if (col_distance == row_distance):
			return False
	return True



def printGrid(grid,N):
	print("++++++++")
	for i in range(N):
		for j in range(N):
			temp = grid[j][i]
			sys.stdout.write("%s" % temp)
		sys.stdout.write("\n")
	print("++++++++")

def main():
	# 8x8 grid
	matrix = [["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"]]

	#matrix = [["-","-","-"],
	#		  ["-","-","-"],
	#		  ["-","-","-"]]

	my_list = []
	#Need to run nQueens starting at each row, adding first queen
	for i in range(8):
		my_list.append([i,0])
		matrix[0][i] = "Q"
		#printGrid(matrix,8)
		nQueens(matrix,1,8,my_list)
		
		my_list = []
		matrix = [["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"],
			  ["-","-","-","-","-","-","-","-"]]

main()