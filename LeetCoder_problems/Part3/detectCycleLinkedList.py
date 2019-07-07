# 6/29/2019
# hackerrank detect a cycle in singly linked list


# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    # we use two ptrs, 1 moving 2 nodes at a time
    # if they meet, then we have a cycle

    curr_ptr = head
    ahead_ptr = head.next

    while (ahead_ptr is not None):
        
        if (curr_ptr == ahead_ptr):
            return 1
        
        curr_ptr = curr_ptr.next

        ahead_ptr = ahead_ptr.next

        if (ahead_ptr is not None):
            ahead_ptr = ahead_ptr.next


    return 0
