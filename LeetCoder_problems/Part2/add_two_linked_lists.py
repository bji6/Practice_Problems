# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        len1 = 1
        len2 = 1
        stack1 = []
        stack2 = []
        
        # calc lengths of lists
        temp = l1
        while (temp.next != None):
            len1 += 1
            stack1.append(temp.val)
            temp = temp.next
        stack1.append(temp.val)
        
        temp = l2
        while (temp.next != None):
            len2 += 1
            stack2.append(temp.val)
            temp = temp.next
        stack2.append(temp.val)
        
        #print(stack1)
        #print(stack2)
        
        counter = len2
        l2_longer = False
        if (len1 < len2):
            counter = len1
            l2_longer = True
        
        result = []
        carry_over = 0
        while (counter > 0):
            num1 = stack1.pop()
            num2 = stack2.pop()
            sum1 = num1 + num2 + carry_over
            carry_over = sum1 / 10
            sum1 %= 10
            result.append(sum1)
            counter -= 1
        
        #print(result)
        remaining = stack1
        
        if (l2_longer):
            remaining = stack2
        
        while (len(remaining) > 0):
            num1 = remaining.pop()
            sum1 = num1 + carry_over
            carry_over = sum1 / 10
            sum1 %= 10
            result.append(sum1)
            
        if (carry_over > 0):
            result.append(carry_over)
            
        #print(result)
        
        new_list = ListNode(result.pop())
        
        temp = new_list
        
        while (len(result) > 0):
            node = ListNode(result.pop())
            temp.next = node
            temp = temp.next
        
        return new_list
