# 6/22/2019
# leetcode generate rows of Pascal's triangle


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        rows = []
        
        for i in range(numRows):
            rows.append([])
        
        for i in range(numRows):
            row = rows[i]
            # build first 2 rows
            if (i == 0):
                row.append(1)
                continue
            if (i == 1):
                row.append(1)
                row.append(1)
                continue
            
            for x in range(i+1): # fill in the rows
                #print("x = %d, i = %d" % (x, i))
                if (x == 0 or x == i): # the ends of each row are value 1
                    row.append(1)
                else:
                    #print rows[i - 1][x - 1]
                    #print rows[i - 1][x]
                    row.append(rows[i - 1][x - 1] + rows[i - 1][x])
                
                #print rows
                
        
        return rows
