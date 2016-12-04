#ben isenberg 9/10/2016

# every palidrome if even number of chars, has an even number
# of every character.  if odd string length, there is only
# one character that has an odd count in the string
def checkIfPalindrome(string1):
	letter_count = {}
	string_length = 0

	for c in string1:
		if (c.isalpha()):
			lower_c = c.lower()
			if (lower_c not in letter_count):
				letter_count[lower_c] = 1
			else:
				letter_count[lower_c] = letter_count[lower_c] + 1
			string_length = string_length + 1

	if (string_length == 0):
		print("Empty string")
		return

	max_number_of_odd_letters = 0

	if ((string_length % 2) == 1):
		max_number_of_odd_letters = 1

	number_odd = 0

	for k in letter_count:
		count = letter_count[k]
		if ((count % 2) == 1):
			number_odd = number_odd + 1
		if (number_odd > max_number_of_odd_letters):
			print("%s is NOT a palindrome permutation" % string1)
			return

	print("True: %s is a permutation of a palindrome" % string1)


def main():
	checkIfPalindrome("tacocat")
	checkIfPalindrome("banana")
	checkIfPalindrome("accotat")
	checkIfPalindrome("Never odd or even")
	checkIfPalindrome("A man, a plan, a canal - Panama!")
	checkIfPalindrome("A man, a plan, a canal - Panamar!")


main()
