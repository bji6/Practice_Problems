# 6/22/2019
# leetcode greedy algo using a stack
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''

from collections import deque

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        my_stack = deque()
        
        my_stack.append((0, nums[0])) #store index, value pair
        
        visited_nodes = {}
        
        canJump = False
        
        while(len(my_stack) > 0):
            
            index = my_stack[-1][0]
            value = my_stack[-1][1]
            
            steps_can_take = index + 1 + value
            
            if (steps_can_take >= len(nums)):
                canJump = True
                break
                
            if (index in visited_nodes):
                my_stack.pop()
            else:
                visited_nodes[index] = 0
                
                # add steps to our stack
                x = 1
                while (x <= value):
                    if ((index + x) < len(nums)):
                        my_stack.append((index + x, nums[index + x]))
                    x += 1
            
            #print my_stack
            
        
        return canJump
            