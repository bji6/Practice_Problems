# leetcode 7/6/2019


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        result = False
    
        element_index = {}
    
        # check if there are two indexes in array nums, i & j, such that:
        # 1. nums[i] == nums[j]
        # 2. abs(i - j) <= k
        for i in range(len(nums)):

            if (nums[i] not in element_index):
                # add first found index for the element nums[i]
                element_index[nums[i]] = i
            else:
                # calculate index distance
                difff = element_index[nums[i]] - i
                if (difff < 0):
                    difff *= -1
                if (difff <= k):
                    # found a match
                    result = True
                    break
                # keep track of largest index found so far
                element_index[nums[i]] = i
        
        return result
        