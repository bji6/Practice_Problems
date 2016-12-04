#ben isenberg 10/23/2016

#a function that swaps numbers without using a temp variable
def numberSwap(a, b):
	a = a - b
	b = b + a
	a = b - a

	return (a, b)

def main():
	a = 74
	b = 3026
	(a,b) = numberSwap(a,b)
	print("a = %d, b = %d\n" % (a,b))

	a = -5
	b = 63
	(a,b) = numberSwap(a,b)
	print("a = %d, b = %d\n" % (a,b))

	a = 10
	b = 0
	(a,b) = numberSwap(a,b)
	print("a = %d, b = %d\n" % (a,b))		

main()