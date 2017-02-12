class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        
        for i in nums:
            if (i < min_val):
                min_val = i

        return min_val
