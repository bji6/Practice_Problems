class Solution(object):
    # sort characters in s by frequency
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        length = len(s)
        
        hash_table = {}
        # build map of char and count
        for i in range(length):
            letter = s[i]
            if (letter not in hash_table):
                hash_table[letter] = 0
            hash_table[letter] += 1
        
        tuple_list = []
        # build a list to sort chars by count
        for i in hash_table.keys():
            # place count before char in tuple since sort function sorts based on first item in tuple
            tuple_list.append((hash_table[i],i))
        
        tuple_list.sort()
        
        output = ""
        str_list = []
        
        while (len(tuple_list) > 0):
            temp = tuple_list.pop()
            # place pieces of final string into a list, then join() them at the end, this is much faster than doing many concats on the same string
            # since strings in python are immutable, so many copies would end up getting created
            # doing many string concats in a loop is O(N^2) in python, building a list and using join() is O(N)
            str_list.append(temp[1] * temp[0])
        
        output = ''.join(str_list)
        
        return output