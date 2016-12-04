#ben isenberg 10/1/2016

#function that starts recursion
def multiplyInts(int1, int2):
	recursiveMultiply(int1,int2,0)

#recursive method to multiply two numbers 
#using addition operator only
def recursiveMultiply(int1,int2,result):
	
	if (int2 == 0):
		print(result)
		return

	result += int1

	recursiveMultiply(int1, int2 - 1, result)

	return


def main():
	multiplyInts(12,3)
	multiplyInts(27,23)

main()