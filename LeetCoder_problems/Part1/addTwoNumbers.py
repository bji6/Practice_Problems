# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # read numbers from linked lists
        value1 = 0
        value2 = 0
        multiplier = 1
   
        temp1 = l1
        temp2 = l2
        while(temp1 != None or temp2 != None):
            if (temp1 != None):
                value1 += (temp1.val * multiplier)
                temp1 = temp1.next
            
            if (temp2 != None):
                value2 += (temp2.val * multiplier)
                temp2 = temp2.next
            
            multiplier *= 10
        
        # get sum
        sum1 = value1 + value2
        #print(sum1)
        
        #build new linked list
        remainder = sum1 % 10
        sum1 /= 10
        l3 = ListNode(remainder)
        temp = l3
        
        while (sum1):
            remainder = sum1 % 10
            sum1 /= 10
            temp.next = ListNode(remainder)
            temp = temp.next
            
        return l3