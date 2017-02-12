# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        if (len(lists) == 0):
            return None
        
        new_list = None
        end_loop = False
        
        lists = [x for x in lists if x != None]
       # print(len(lists))
        
        while (True):
            min_index = 0
            min_val = 2147483647
            # find node with smallest value
            min_indexes = []
            for i in range(len(lists)):
                node = lists[i]
                if (node.val <= min_val):
                   # print("found min value, index %d" % i)
                    min_val = node.val
            
            # we will process all repeats at once
            for i in range(len(lists)):
                node = lists[i]
                if (node.val == min_val):
                    min_indexes.append(i)
            
            if (len(lists) == 0):
                break
            
            if (new_list is None):
                #print("chainging list")
                new_list = ListNode(min_val)
                temp = new_list
                
                for i in range(len(min_indexes)-1):
                    temp.next = ListNode(min_val)
                    temp = temp.next
                    lists[min_indexes[i]] = lists[min_indexes[i]].next
                    
                lists[min_indexes[len(min_indexes)-1]] = lists[min_indexes[len(min_indexes)-1]].next
                
            else:
                for i in range(len(min_indexes)):
                    temp.next = ListNode(min_val)
                    temp = temp.next
                    lists[min_indexes[i]] = lists[min_indexes[i]].next
                    #print(temp)
            
           # print(min_index)
            
            lists = [x for x in lists if x != None]
        
        #print(new_list.next)
        
        return new_list