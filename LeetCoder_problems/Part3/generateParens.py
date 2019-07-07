# 6/29/2019
# leetcode generate all valid strings with n pairs of parentheses


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        string_list = []
        
        recursive_string_generator([], 0, 0, n * 2, string_list)
        
        result_list = []
        
        for l in string_list:
            result_list.append("".join(l))
        
        return result_list
        
    
    
def recursive_string_generator(strr, numleft, numright, size, string_list):

    # base case
    if (len(strr) == size):
        string_list.append(strr)
        return

    # recursive cases

    # add left parens 
    # (RULE: you can only add a left parens if you havent already added size/2 of them)
    if (numleft < size/2):
        temp_str = strr[:]
        temp_str.append("(")
        recursive_string_generator(temp_str, numleft + 1, numright, size, string_list)

    # add right parens
    # (RULE: you can only add a right parens if you have added more left parens to the string already)
    if (numleft > numright):
        temp_str = strr[:]
        temp_str.append(")")
        recursive_string_generator(temp_str, numleft, numright + 1, size, string_list)
        
    return
