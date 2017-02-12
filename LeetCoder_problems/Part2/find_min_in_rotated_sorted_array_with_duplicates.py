class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for i in nums:
            mydict[i] = i
            
        min_val = mydict[nums[0]]
        
        for i in mydict:
            if (i < min_val):
                min_val = i

        return min_val

