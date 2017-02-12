class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = self.determineWinner(nums, 0, len(nums)-1, 0, True, 0, 0)
 
        return result
        
    #fuction builds game tree, determines winner    
    def determineWinner(self, nums, leftindex, rightindex, level, player1, score1, score2):
        #base case
        if (level == len(nums)):
            #player 1 won
            if (score1 >= score2):
                return True
            return False
        
        # this is player 1's turn
        if (player1):
            #left leaf
            winning1 = self.determineWinner(nums, leftindex+1, rightindex, level+1, not player1, score1+nums[leftindex], score2)
            winning2 = False

            #alpha beta pruning
            if (winning1):
                return True

            #right leaf
            if (rightindex != leftindex):
                winning2 = self.determineWinner(nums, leftindex, rightindex-1, level+1, not player1, score1+nums[rightindex], score2)

            if (winning1 or winning2):
                return True
            else:
                return False
        # this is player 2's turn
        else:
            #left leaf
            winning1 = self.determineWinner(nums, leftindex+1, rightindex, level+1, not player1, score1, score2+nums[leftindex])
            winning2 = True

            #alpha beta pruning
            if (winning1 == False):
                return False

            #right leaf
            if (rightindex != leftindex):
                winning2 = self.determineWinner(nums, leftindex, rightindex-1, level+1, not player1, score1, score2+nums[rightindex])

            if (winning1 == False or winning2 == False):
                return False
            else:
                return True
        


def main():
    test = Solution()

    print(test.PredictTheWinner([1,5,2]))

    print(test.PredictTheWinner([1,5,10,7]))

    print(test.PredictTheWinner([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))


main()