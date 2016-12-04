#ben isenberg 10/24/2016

#given list of ppl with birth and death year find year with most
#ppl alive
def mostAliveYear(list1):
	year_map = {}

	for person in list1:
		birth = person[0]
		death = person[1]
		
		for i in range(birth,death+1):
			if (i not in year_map):
				year_map[i] = 0
			year_map[i] = year_map[i] + 1

	#find max year
	max_alive = 0
	max_year = 0

	for yr in year_map.keys():
		if (year_map[yr] > max_alive):
			max_alive = year_map[yr]
			max_year = yr

	return max_year


def main():
	list1 = [[1932,1997],[1954,2000],[1912,1974],[1991,2000],[1982,1997]]
	
	print(mostAliveYear(list1))

main()