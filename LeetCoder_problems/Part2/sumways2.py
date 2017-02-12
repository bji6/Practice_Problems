import pdb
from collections import deque

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        distList = [0]
        index = 0
        
        while (index < len(nums)):
            tempList = []
            
            for n in distList:
                # add
                tempList.append(n + nums[index])
                # subtract
                tempList.append(n - nums[index])

            distList = tempList
            
            index += 1

        count = 0

        for n in distList:
            if (n == S):
                count += 1

        return count

def main():
    test = Solution()

    print(test.findTargetSumWays([1,1,1,1,1], 3))

    #print(test.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0))

main()