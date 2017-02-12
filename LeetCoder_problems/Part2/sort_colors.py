class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        #sort reds first, then whites, then blues
        # O(3N) runtime, linear runtime
        color = 0
        last_index = 0
        while (color < 3):
            
            for i in range(last_index,len(nums),1):
                cur_color = nums[i]
                #color swap
                if (cur_color == color):
                    temp = nums[last_index]
                    nums[last_index] = cur_color
                    nums[i] = temp
                    last_index += 1
            
            color += 1
