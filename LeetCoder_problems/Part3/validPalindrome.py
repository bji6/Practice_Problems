# 6/22/2019
# leetcode determine if a string is a valid palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        index1 = 0
        index2 = len(s) - 1
        
        palindrome = True
        
        if (s == ""):
            return palindrome
        
        while (index1 < index2):
            char1 = s[index1].lower()  # ignore case
            
            if (not char1.isalnum()):  # only alphanumeric chars
                index1 += 1
                continue
            
            char2 = s[index2].lower()
            
            if (not char2.isalnum()):
                index2 -= 1
                continue
            
            if (char1 != char2):
                palindrome = False
                break
            
            index1 += 1
            index2 -= 1
            
        return palindrome
        
        