class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag_str = ""
        length = len(s)
        
        if (numRows <= 1 or numRows == length):
            return s
        
        for i in range(1, numRows+1):
            new_index = i
            new_index2 = i
           
           # print(zigzag_str)
           
            if (len(zigzag_str) == length):
                return zigzag_str
           
            zigzag_str += s[i-1]
            
            new_index += (numRows - 1) * 2      #build first row and last row, 2 * (numRows - 1) is only index formula
            new_index2 += (numRows - i) * 2
                
            while (True):
                #print("looped")
                #print(new_index)
                #print(new_index2)
                #build middle rows, alternate formulas 2 * (numRows - i), 2 * (numRows - 1)
                if ((i > 1) and (i < numRows) and (new_index2 <= length)):    
                    zigzag_str += s[new_index2-1]
                
                if (new_index <= length):
                    zigzag_str += s[new_index-1]
                
                new_index2 = new_index + ((numRows - i) * 2)
                new_index += (numRows - 1) * 2
                
                if (new_index > length):
                    break
                
            if ((i > 1) and (i < numRows) and (new_index2 <= length)):    
                    zigzag_str += s[new_index2-1]
        
        return zigzag_str