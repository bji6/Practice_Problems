class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_array = {}
        length = len(nums)
        
        #use a hash value to make value look ups easier
        for i in range(length):
            hash_array[nums[i]] = i
        
        index1 = 0
        index2 = 0
        
        for i in range(length):
            trgt2 = target - nums[i]
            
            #we can't add together the same index so check for this
            if ((trgt2 in hash_array) and (i != hash_array[trgt2])):
                index1 = i
                index2 = hash_array[trgt2]
                break
        
        return (index1, index2)