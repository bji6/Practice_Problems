#ben isenberg 10/2/2016

#recursive method to produce all permutations of n coins
#using any number of quarters, dimes, nickels, pennies
def coinsPerms(number_of_coins):
	#base case
	if (number_of_coins == 0):
		return [""]

	new_list = []
	
	#QUARTERS
	if ((number_of_coins - 25) >= 0):
		temp_list = coinsPerms(number_of_coins - 25)
		for x in temp_list:
			new_list.append("Q_" + x)
	#DIMES
	if ((number_of_coins - 10) >= 0):
		temp_list = coinsPerms(number_of_coins - 10)
		for x in temp_list:
			new_list.append("D_" + x)
	#NICKELS
	if ((number_of_coins - 5) >= 0):
		temp_list = coinsPerms(number_of_coins - 5)
		for x in temp_list:
			new_list.append("N_" + x)
	#PENNIES
	if ((number_of_coins - 1) >= 0):
		temp_list = coinsPerms(number_of_coins - 1)
		for x in temp_list:
			new_list.append("P_" + x)

	return new_list

def main():
	print(coinsPerms(25))
	print(coinsPerms(10))

main()