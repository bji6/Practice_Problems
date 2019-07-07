# 6/29/2019
# leetcode reverse a singly linked list


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        prev_node = None
        
        curr_node = head
        
        while (curr_node is not None):
            next_node = curr_node.next
            curr_node.next = prev_node
            
            prev_node = curr_node
            curr_node = next_node
            
        return prev_node