#ben isenberg 10/23/2016

#returns negated int
def negate(b):
	neg_b = 0
	increment = -1

	if (b < 0):
		increment = 1

	for i in range(b):
		neg_b = neg_b + increment

	return neg_b

#subtract using only + operator
def subtract(a,b):
	b = negate(b)
	a = a + b

	return a

#multiply using only + operator
def multiply(a,b):
	new_a = 0
	for i in range(abs(b)):
		new_a = new_a + a

	if (b < 0 and a > 0):
		new_a = negate(new_a)

	return new_a

#divide using only + operator
def divide(a,b):
	count = 0
	while (a > 0):
		a = subtract(a,b)
		count = count + 1
	
	if (a < 0):
		count = count - 1

	return count

def main():
	print(subtract(10,17))
	print(multiply(30,subtract(5,3)))
	print(multiply(30,subtract(1,3)))
	print(divide(1230,17))
	print(divide(20,10))

main()