class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #time complexity = 0(N+K) = O(N)
        #space complexity = O(K) = O(N)
        
        # O(k) space, k = unique numbers in list
        num_count = []
        majority_items = []
        
        # O(N) runtime
        for i in nums:
            if (i in num_count):
                num_count[i] += 1
            else:
                num_count[i] = 1
                
        at_least = len(nums) / 3
        
        result = []
        
        #O(k) runtime
        for k in num_count:
            if (num_count[k] > at_least):
                result.append(k)
        
        return result
