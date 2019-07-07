# 6/22/2019
# leetcode generate permutations


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        temp = [0] * len(nums)
        #print temp
        
        perm_list = []
        num_inserts = 0
        total_size = len(nums)
        generate_perms(nums, temp, perm_list, num_inserts, total_size)
        
        return perm_list
        
# can do this recursively
def generate_perms(nums, temp, perms, num_inserts, total_size):
            
    # base case
    if (num_inserts == total_size):
        perms.append(temp)
        return

    # recursive case
    for i in range(len(nums)):
        temp_cpy = temp[:]
        temp_cpy[num_inserts] = nums[i]
        #print temp_cpy
        new_nums = nums[:]
        new_nums.pop(i)
        generate_perms(new_nums, temp_cpy, perms, num_inserts+1, total_size)
