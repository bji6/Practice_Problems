#ben isenberg 10/30/2016

#calculator function, expression has no parens
def calculator(expression):
	#order of operations, PEMDAS
	expression = evaluateExpression(expression, "*")
	expression = evaluateExpression(expression, "/")
	expression = evaluateExpression(expression, "+")
	expression = evaluateExpression(expression, "-")

	return expression

def evaluateExpression(expression, operator):
	list1 = expression.split(operator)
	#nothing to do here
	if (len(list1) == 1):
		print("no operator")
		return expression

	#if no more operators, apply operator to all that remains
	no_more = True
	for i in range(len(list1)):
		if ("*" in list1[i] or "/" in list1[i] or "+" in list1[i] or "-" in list1[i]):
			no_more = False
			break
	
	if (no_more):
		result = 0
		for i in range(len(list1)):
			if (operator == "*"):
				result = result * float(list1[i])
			elif (operator == "/"):
				result = result / float(list1[i])
			elif (operator == "+"):
				result = result + float(list1[i])
			elif (operator == "-"):
				result = result - float(list1[i])
		print(result)
		return str(result)

	# loop length - 1 times
	for i in range(len(list1)-1):
		index_x = 0
		#find where the numbers are in the string
		for j in range(len(list1[i])):
			if (list1[i][j] == "*" or list1[i][j] == "/" or list1[i][j] == "+" or list1[i][j] == "-"):
				index_x = j + 1
		#print(list1[i][index_x:])
		x = float(list1[i][index_x:])
		#find where the numbers are in the string
		index_y = len(list1[i+1])
		for j in range(len(list1[i+1])):
			if (list1[i+1][j] == "*" or list1[i+1][j] == "/" or list1[i+1][j] == "+" or list1[i+1][j] == "-"):
				index_y = j
				break
		#print(list1[i+1][0:index_y])
		y = float(list1[i+1][0:index_y])
		#print(x)
		#print(y)
		if (operator == "*"):
			x = x * y
		elif (operator == "/"):
			x = x / y
		elif (operator == "+"):
			x = x + y
		elif (operator == "-"):
			x = x - y
		# add new value to expression, remove x and y
		list1[i] = list1[i][:index_x] + str(x)
		list1[i+1] = list1[i+1][index_y:]

	#build new expression
	new_expression = ""
	for i in range(len(list1)):
		new_expression = new_expression + list1[i]

	print(new_expression)
	return new_expression


def main():
	#evaluateExpression("2*3+5/6*3+15","*")
	print("result = " + calculator("2*3+5/6*3+15"))

main()