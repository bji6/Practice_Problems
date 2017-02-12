class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        cur_index = 0
        cur_num = 2
        result = [0,1]
        
        if (num == 0):
            return [0]
        
        # O(N) algorithm, one pass, list builds on itself
        while (len(result) <= num):
            adder = result[cur_index]
            result.append(1 + adder)
            cur_index += 1
            
            # start over, increase cur_num by power of 2
            if (cur_index == cur_num):
                cur_index = 0
                cur_num *= 2
        
        return result
