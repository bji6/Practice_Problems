# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        temp1 = head
        temp2 = head
        count = 0
        
        # O(N) runtime
        while (temp1.next != None):
            
            if (count >= n):
                temp2 = temp2.next
                
            temp1 = temp1.next
            count += 1
        
        #print(temp1.val)
        #print(temp2.val)
        
        #removing node len(list) - n
        if (count < n):
            head = head.next
        else:
            temp2.next = temp2.next.next
        
        return head
