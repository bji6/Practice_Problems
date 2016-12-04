#ben isenberg 11/05/2016

#count number of 2 digits that appear in number list
def countTwo(number):
	count = 0
	temp = number

	while (number >= 0):
		if (temp % 10 == 2):
			count = count + 1
		temp = temp / 10

		if (temp == 0):
			number = number - 1
			temp = number

	return count

def main():
	print(countTwo(25))
	print(countTwo(34596))

main()