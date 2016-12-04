#ben isenberg 9/10/2016

#basic string compression
def compressor(string1):
	new_str = ""

	repeated = 1

	for x in range(len(string1)-1):
		
		if (string1[x] == string1[x+1]):
			repeated = repeated + 1
		else:
			new_str = new_str + string1[x] + str(repeated)
			repeated = 1

	new_str = new_str + string1[-1] + str(repeated)

	if (len(string1) <= len(new_str)):
		print("no compression possible")
	else:
		print("%s compressed to %s" % (string1, new_str))

def main():
	compressor("aabcccccaaa")
	compressor("aabcaa")
	compressor("aabcccccaaaRRRRuuuuuYYYtttIIIaaaaZZZZZZZZ")

main()