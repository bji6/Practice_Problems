class Solution(object):
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        length = len(nums)
        
        if (length == 0):
            return -1
        
        # use hash table to store index of each item in array
        cache = {}
        
        for i in range(length):
            cache [nums[i]] = i

        # if item is in hash table return index
        if (target in cache):
            return cache[target]
        
        return -1