#ben isenberg 10/1/2016


#recursive method to solve towers of hanoi for N disks
# uses 3 stacks
def towersOfHanoi(num_disks,tower1,tower2,tower3):
	
	if (num_disks == 1):	#base case: move 1 disk from tower1 to tower3
		tower3.append(tower1.pop())
		return (tower1, tower2, tower3)

	if (num_disks == 2):	#base case: move 2 disks from tower 1 to tower3
		tower2.append(tower1.pop())
		tower3.append(tower1.pop())
		tower3.append(tower2.pop())
		return (tower1, tower2, tower3)

	# f(N) = f(N-1) + f(1) +f(N-1)
	# note the stack rearrangement
	tower1, tower3, tower2 = towersOfHanoi(num_disks - 1, tower1, tower3, tower2)
	tower1, tower2, tower3 = towersOfHanoi(1, tower1, tower2, tower3)
	tower2, tower1, tower3 = towersOfHanoi(num_disks - 1, tower2, tower1, tower3)

	return (tower1, tower2, tower3)


def main():
	stack1 = [10,9,8,7,6,5,4,3,2,1]
	stack2 = []
	stack3 = []

	stack1, stack2, stack3 = towersOfHanoi(len(stack1),stack1,stack2,stack3)

	print(stack1)
	print(stack2)
	print(stack3)

main()