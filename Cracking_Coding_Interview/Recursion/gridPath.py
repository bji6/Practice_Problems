#ben isenberg 10/1/2016

#recursive method
#start at upper left, find path to lower right of a grid
def findPath(grid, rows, cols, path, loc_x, loc_y):
	#base case, found the goal
	if (grid[loc_y][loc_x] == "G"):
		print("Solution to maze = %s" % path)
		return
	#base case, dead end
	if (grid[loc_y][loc_x] == "X"):
		return

	if ((loc_x + 1) < cols):	#traverse right if we can
		path_right = path + "right_"
		findPath(grid, rows, cols, path_right, loc_x + 1, loc_y)
	
	if ((loc_y + 1) < rows):	#traverse down if we can
		path_down = path + "down_"
		findPath(grid, rows, cols, path_down, loc_x, loc_y + 1)

	return


def main():
	matrix = [[" ","X"," "," "," "],
			  [" "," "," ","X"," "],
			  ["X"," "," "," "," "],
			  [" "," ","X","X","G"]]

	findPath(matrix,4,5,"",0,0)

main()