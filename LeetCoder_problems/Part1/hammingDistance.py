class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """ 		
 		# use xor to find where bits are different
        bit_string = bin(x^y)
        
        #print(bit_string)
        
        bit_count = 0
        
        #skip first 2 chars, they are not part of binary number
        for i in range(2,len(bit_string),1):
            if (bit_string[i] == '1'):
                bit_count += 1
        
        return bit_count