# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    # runtime is O(2N) which simplifies to O(N)
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if (k == 0):
            return head
            
        if (head is None):
            return head
        
        #get list length to adjust k values that are beyond length of list
        temp = head
        length = 0
        
        # O(N) runtime
        while (temp != None):
            temp = temp.next
            length += 1
        
        k = k % length
        #print(length)
        #print(k)
        
        # list will not be changed    
        if (k == 0):
            #print("test")
            return head
        
        p1 = head
        counter = 0
        p2 = head
        foundOffset = False
        
        # O(N) runtime
        while (p1.next != None):
            
            if (counter == k):
                foundOffset = True
            
            if (foundOffset):
                p2 = p2.next
            
            p1 = p1.next
            counter += 1
        
        newHead = p2.next
        
        p1.next = head
        
        p2.next = None
        
        return newHead
 