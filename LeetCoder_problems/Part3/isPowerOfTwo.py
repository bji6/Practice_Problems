# leetcode 7/6/2019
# determine if a number is a power of two, using bit operations


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
    
        # check how many bits are set to 1
        bit_count = 0
        while(n > 0):
            
            if (n & 1 == True):
                bit_count += 1
            
            n = n >> 1
            
            if (bit_count > 1):
                break
        
        # powers of two have only 1 bit set to 1
        if (bit_count == 1):
            return True
        
        return False