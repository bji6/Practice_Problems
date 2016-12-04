# Ben Isenberg 9/10/2016


def checkStringUnique(string):
	hash_table = {}

	for c in string:
		if (c not in hash_table):
			hash_table[c] = 0
		else:
			print("String does not have unique characters")
			return
	print("String has %d unique characters" % len(hash_table.keys()))

def checkStringUnique2(string):
	#use ascii codes to figure out if all chars are unique in string

	bit_vector = [1]*len(string)


	for x in range(len(string)):
		bit_vector[x] = bit_vector[x] + ord(string[x]) 
	
	for x in range(len(bit_vector)):
		for y in range(len(bit_vector)):
			if (x != y and bit_vector[x] == bit_vector[y]):
				print("String does not have unique characters")
				return
	print("String has %d unique characters" % len(string))	

def main():
	checkStringUnique("alphabet")
	checkStringUnique("piano")

	checkStringUnique2("uniqlo")
	checkStringUnique2("losers")


main()