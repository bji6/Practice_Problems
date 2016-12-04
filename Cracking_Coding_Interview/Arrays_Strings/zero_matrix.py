#ben isenberg 9/10/2016

#zero matrix
# anywhere in a give matrix where there is a zero, set entire row and col to zero

def set_zero(matrix1, cols, rows):
	cols_zeros = []
	rows_zeros = []


	for x in range(rows):
		for y in range(cols):
			if (matrix1[x][y] == 0):
				rows_zeros.append(x)
				cols_zeros.append(y)

	for item in rows_zeros:
		for y in range(cols):
			matrix1[item][y] = 0

	for item in cols_zeros:
		for x in range(rows):
			matrix1[x][item] = 0

	print(matrix1)

def main():
	matrix = [[1,3,0,5,6],[0,2,3,9,8],[2,3,0,4,2],[9,5,6,7,4]]

	print(matrix)
	
	set_zero(matrix,5,4)

main()