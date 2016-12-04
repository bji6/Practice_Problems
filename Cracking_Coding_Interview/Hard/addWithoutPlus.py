#ben isenberg 11/05/2016

#function to add two positive numbers without using arithmetic operators
def addNoPlus(num1, num2):
	#convert numbers to binary strings
	binary1 = bin(num1)[2:]
	binary2 = bin(num2)[2:]
	print(binary1)
	print(binary2)

	carry_bit = 0
	sum_bit = 0
	binary_sum = ""
		
	if (len(binary2) > len(binary1)):
		for i in range(len(binary2)):
			bit2 = int(binary2[i])
			
			if (i < len(binary1)):
				bit1 = int(binary1[i])
				
				sum_bit = (bit1 ^ bit2) ^ carry_bit
				carry_bit = (bit1 & carry_bit) | (bit2 & carry_bit) | (bit1 & bit2)
			else:	
				sum_bit = bit2 ^ carry_bit
				carry_bit = bit2 & carry_bit

			binary_sum = str(sum_bit) + binary_sum
	else:
		for i in range(len(binary1)):
			bit1 = int(binary1[i])

			if (i < len(binary2)):
				bit2 = int(binary2[i])
				
				sum_bit = (bit1 ^ bit2) ^ carry_bit
				carry_bit = (bit1 & carry_bit) | (bit2 & carry_bit) | (bit1 & bit2)
			else:
				sum_bit = bit1 ^ carry_bit
				carry_bit = bit1 & carry_bit

			binary_sum = str(sum_bit) + binary_sum	

	if (carry_bit == 1):
		binary_sum = str(carry_bit) + binary_sum

	print(binary_sum)


def main():
	addNoPlus(5,3)
	addNoPlus(15,27)

main()
