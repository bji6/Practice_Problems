#ben isenberg 11/05/2016
import random

#randomly shuffle a deck of cards
def randomShuffle(deck):
	for i in range(len(deck)):
		index1 = random.randrange(0,len(deck))
		index2 = random.randrange(0,len(deck))
		temp = deck[index1]
		deck[index1] = deck[index2]
		deck[index2] = temp

	return deck

def main():
	deck = []
	deck.append("Apple")
	deck.append("Bannana")
	deck.append("Cherry")
	deck.append("Dragon Fruit")
	deck.append("Honey Dew")
	deck.append("Pineapple")
	deck.append("Kiwi")
	deck.append("Strawberry")
	deck.append("Pear")
	deck.append("Plum")

	#print(deck)
	print(randomShuffle(deck))
	print(randomShuffle(deck))
	print(randomShuffle(deck))

main()
	
