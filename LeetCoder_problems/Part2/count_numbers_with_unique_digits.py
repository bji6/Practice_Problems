class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        #numbers from 0 to (10 ** n) exclusive
        
        total_sum = 0
        
        if (n == 0):
            return 1
        
        #first time is n_choose 10
        n_choose = 10
        
        for i in range(1,n+1):
            temp = i
            #reset variables
            result = 1
            counter = 0
            
            while (temp > 0):
                if (counter >= 2):
                    n_choose -= 1
                result *= n_choose
                counter += 1
                temp -= 1
            
            #add to total
            total_sum += result
            
            #reset variable
            n_choose = 9
        
        return total_sum
