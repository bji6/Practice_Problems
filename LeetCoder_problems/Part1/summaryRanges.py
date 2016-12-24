# for a given sorted int array of unique ints, provide a summary of continuous ranges in the array
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        str_list = []
        range_count = 0
        
        for i in range(len(nums)-1):
            # keep counting range length
            if (nums[i+1] == (nums[i] + 1)):
                range_count += 1
            # found end of continuous range
            elif (range_count > 0):
                str_list.append("%d->%d" % (nums[i - range_count], nums[i]))
                range_count = 0
            else:
                # just one number by itself
                str_list.append("%d" % nums[i])
            
        # have to check the last index of input array
        last_index = len(nums) - 1
        
        if (range_count > 0):
            str_list.append("%d->%d" % (nums[last_index - range_count], nums[last_index]))
            range_count = 0
        elif (last_index >= 0):
            str_list.append("%d" % nums[last_index])
        
        return str_list