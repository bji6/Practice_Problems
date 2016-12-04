#ben isenberg 10/23/2016

#a function that finds number of trailing zeros in n factorial
def factorialZeros(n):
	temp = n
	#compute n factorial
	for i in range(1,temp):
		n = n * (temp-i)

	#find number of trailing zeros
	trailingCount = 0
	divisor = 10
	#print(n)
	while (n % divisor == 0):
		trailingCount = trailingCount + 1
		divisor = divisor * 10

	return trailingCount

def main():
	print(factorialZeros(3))
	print(factorialZeros(5))
	print(factorialZeros(10))
	print(factorialZeros(14))
	print(factorialZeros(20))

main()