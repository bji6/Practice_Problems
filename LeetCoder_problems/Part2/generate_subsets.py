class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        return self.recursiveSets(nums, 0, [], [[]])
        
    def recursiveSets(self, nums, index, cur_combo, set_list):
        
        if (len(nums) == index):
            return set_list
            
        
        for i in range(index, len(nums), 1):
            temp = cur_combo[:]
            if (nums[i] in temp):
                continue
            temp.append(nums[i])
            set_list.append(temp)
            set_list = self.recursiveSets(nums, i, temp, set_list)
        
        return set_list
