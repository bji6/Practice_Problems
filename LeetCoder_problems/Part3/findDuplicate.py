# 6/22/2019
# leetcode find duplicate number in array with small amount of memory, bit vector


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        bitvector = 0 << len(nums)
        #print("bitvector = %d" % bitvector)
        for num in nums:
            bit_loc = 1 << (num-1)
            if (bit_loc & bitvector):
                return num
            bitvector = bitvector | bit_loc
            #print("bitvector = %d" % bitvector)
