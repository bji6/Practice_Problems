# 6/23/2019
# leetcode

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        my_list = []
        
        if (len(strs) == 0):
            return ""
        
        common_prefix = strs[0]
        
        for c in common_prefix:
            my_list.append(str(c))
            
        #print my_list
            
        for x in range(1, len(strs)):
            s = strs[x]
            for i in range(len(s)):
                char = s[i]
                #print char
                if (i < len(my_list) and my_list[i] != char):
                    my_list = my_list[:i]
            
            if (len(my_list) > len(s)):
                my_list = my_list[:len(s)]
        
        #print my_list
        
        return "".join(my_list)