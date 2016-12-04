#ben isenberg 10/25/2016

#mastermind game
def masterMind(guess, solution):

	num_hits = 0
	num_pseudo_hits = 0
	temp = ""
	temp2 = set()

	for i in range(4):
		if (guess[i] == solution[i]):
			num_hits = num_hits + 1
		else:
			temp = temp + solution[i]
			temp2.add(guess[i])

	temp2 = list(temp2)
	for i in range(len(temp2)):
		if (temp2[i] in temp):
			num_pseudo_hits = num_pseudo_hits + 1

	print("Hits = %d, Pseudo Hits = %d" % (num_hits,num_pseudo_hits))

def main():
	
	masterMind("GGRR","RGBY")
	masterMind("BBYB","RGBY")
	masterMind("RGBY","RGBY")

main()