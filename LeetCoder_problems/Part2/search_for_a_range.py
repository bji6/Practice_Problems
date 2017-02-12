class Solution(object):
    
    # iterative binary search
    def binary_search(self, list1, num1):
        
        new_list = []
        
        if (len(list1) == 0):
            return [-1,-1]

        if (len(list1) == 1):
            if (list1[0] == num1):
                return [0,0]
            else:
                return [-1,-1]                
        
        left = 0
        right = len(list1) - 1
        
        while (True):
            middle = (left + right) / 2
            
            if (list1[middle] == num1):
                #print("found middle = %d" % middle)
                # check the total range
                #left side
                new_index = middle - 1
                count = 0
                while (new_index >= 0 and list1[new_index] == num1):
                    new_index -= 1
                    count += 1
                    
                if (count > 0):
                    new_list.append(new_index+1)
                else:
                    new_list.append(middle)
                #right side
                new_index = middle + 1
                count = 0
                while (new_index < len(list1) and list1[new_index] == num1):
                    new_index += 1
                    count += 1
                
                if (count > 0):
                    new_list.append(new_index-1)
                else:
                    new_list.append(middle)
                
                return new_list
                
            if (right - 1 == left):
                if (list1[left] == num1):
                    #check the range
                    new_list.append(left)
                    if (list1[right] == num1):
                        new_list.append(right)
                        return new_list
                    else:
                        new_list.append(left)
                        return new_list

                elif (list1[right] == num1):
                    new_list.append(right)
                    new_list.append(right)
                    return new_list
                else:
                    return [-1,-1]
            
            if (list1[middle] > num1):
                right = middle
            elif (list1[middle] < num1):
                left = middle
    
    
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        return self.binary_search(nums, target)