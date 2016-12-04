#ben isenberg 10/1/2016

#recursive method
# taking only 1, 2, or 3 steps, count number of ways to get to total steps
def countPermutations(total, num_of_steps):
	#base case
	if (num_of_steps == total):
		return 1
	#base case
	if (num_of_steps > total):
		return 0

	sum1 = countPermutations(total, num_of_steps + 1)
	sum2 = countPermutations(total, num_of_steps + 2)
	sum3 = countPermutations(total, num_of_steps + 3)

	return sum1 + sum2 + sum3


def main():
	print("Number of paths to %d = %d" % \
		(3,countPermutations(3,0)))
	print("Number of paths to %d = %d" % \
		(10,countPermutations(10,0)))
	print("Number of paths to %d = %d" % \
		(25,countPermutations(25,0)))

main()