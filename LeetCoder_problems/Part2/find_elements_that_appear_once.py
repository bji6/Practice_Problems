class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        num_dict = {}
        
        for i in nums:
            if (i in num_dict):
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        
        result = []
        
        for x in num_dict:
            if (num_dict[x] == 1):
                result.append(x)
        
        return result
