import pdb
from collections import deque

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        result = self.recursiveSum(nums, S, 0, 0, 0)
        
        return result
        
    def recursiveSum(self, nums, S, distance, count, index):
        
        if (distance == S and len(nums) == index):
            return count + 1
        if (len(nums) == index):
            return count
        
        
        # add
        tempDis = distance + nums[index]
        #pdb.set_trace()
        tempcount = self.recursiveSum(nums, S, tempDis, count, index+1)
        if (tempcount > count):
            count = tempcount
        # subtract
        tempDis = distance - nums[index]
        tempcount = self.recursiveSum(nums, S, tempDis, count, index+1)
        if (tempcount > count):
            count = tempcount
        #pdb.set_trace()

        return count

def main():
    test = Solution()

    print(test.findTargetSumWays([1,1,1,1,1], 3))

    print(test.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0))

main()