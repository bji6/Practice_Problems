class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        my_list = S.split("-")
            
        #determine size of first group (num chars % K)
        counter = 0
        for i in my_list:
            counter += len(i)
        
        firstgroupsize = counter % K
        #print(firstgroupsize)
        #print(my_list)
    
        counter2 = 0
        my_list2 = []
        firstGroup = True
        if (firstgroupsize == 0):
            firstGroup = False
        
        for s in my_list:
            for c in s:
                if (firstGroup and counter2 == firstgroupsize):
                    my_list2.append("-")
                    firstGroup = False
                    counter2 = 0
                    #print("1st if")
                elif (counter2 > 0 and counter2 == K):
                    my_list2.append("-")
                    counter2 = 0
                    #print("2nd if")
                
                my_list2.append(c.upper())
                counter2 += 1
                #print(my_list2)
                #print(counter2)
                
        result = ''.join(my_list2)
        
        return result
