# 6/29/2019
# leetcode, find max sub array sum value in linear time, 2 different methods


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum_array = [0] * len(nums)
        max_sum = 0
        
        if (nums[0] > 0):
            sum_array[0] = nums[0]
            max_sum = nums[0]
        
        for i in range(1, len(nums)):
            
            if (sum_array[i-1] + nums[i] > 0): # only continue sum sequence it we are still above 0, otherwise reset
                sum_array[i] = sum_array[i-1] + nums[i]
            
            if (sum_array[i] > max_sum): # check if we found a new sum
                max_sum = sum_array[i]
        
        if (max_sum == 0):  # potentially no value above 0 in nums, just return max of negative values
            return max(nums)
        
        return max_sum
        
        
        
        
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp_sum = 0
        max_sum = nums[0]
        
        for i in range(len(nums)):
            temp_sum += nums[i]
            temp_sum = max(0, temp_sum) # dont include nums[i] in our current sum if it gets us below 0
            max_sum = max(max_sum, temp_sum)
            
        if (max_sum == 0): # no sequence was found, return largest individual value
            return max(nums)
            
        return max_sum
