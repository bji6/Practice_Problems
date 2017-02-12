class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        
        firstMissing = 1
        
        for i in range(len(nums)):
            if (nums[i] == firstMissing):
               # print("entering while loop")
                while (firstMissing in hash_table):
                    firstMissing += 1
                break  # we now have first missing positive int
        
        return firstMissing