#ben isenberg 10/16/2016

#take a list of strings and group anagrams together
def anagramGroup(string_list):
	anagram_map = {}

	#organize strings that are anagrams
	for string in string_list:
		sorted_chars = ''.join(sorted(string))
		if (sorted_chars not in anagram_map):
			anagram_map[sorted_chars] = []
		anagram_map[sorted_chars].append(string)

	new_array = []

	for key in anagram_map.keys():
		for s in anagram_map[key]:
			new_array.append(s)

	return new_array


def main():
	list1 = ["insect","Anna Madrigal","Tom Marvelo Riddle","listen","I am Lord Voldemort","A man and a girl","silent"]

	print(anagramGroup(list1))

main()
