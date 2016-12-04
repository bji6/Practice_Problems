#ben isenberg 9/10/2016


#check if strings match, or are 1 letter different
def check_one_away(string1, string2):
	
	len1 = len(string1)
	len2 = len(string2)

	if (abs(len2 - len1) > 1):
		print("False")
		return

	letter_count = {}

	number_mismatch = 0

	if (len1 > len2):
		x = 0
		if (string1[x] != string2[x]):  #check where to start comparison
			x = 1
			number_mismatch = number_mismatch + 1

		for c in range(x,len2):
			if (string1[c] != string2[c-number_mismatch]):
				number_mismatch = number_mismatch + 1
	elif (len1 < len2):
		x = 0
		if (string1[x] != string2[x]):  #check where to start comparison
			x = 1
			number_mismatch = number_mismatch + 1

		for c in range(x,len1):
			if (string1[c-number_mismatch] != string2[c]):
				number_mismatch = number_mismatch + 1
	else:
		for c in range(len1):
			if (string1[c] != string2[c]):
				number_mismatch = number_mismatch + 1

	if (string1[len1-1] != string2[len2-1]):	#check if last letters dont match (important for different str lengths)
		number_mismatch = number_mismatch + 1
	
	if (number_mismatch > 1):
		print("false")
		return

	print("true")


def main():
	check_one_away("pale","ple")
	check_one_away("pales","pale")
	check_one_away("pale","bale")
	check_one_away("pale","bake")
	check_one_away("ple","pale")

main()