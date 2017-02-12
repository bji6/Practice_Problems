class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sorted_list = sorted(nums)
        #print(sorted_list)
        return sorted_list[-k]
