# 6/29/2019
# leetcode, level by level traversal of binary tree using BFS


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if (root is None):
            return []
        
        # BFS iterative traversal of binary tree
        my_queue = []
        
        # return a list of lists, each list has all node values at a tree level
        return_list = []
        level = 0
        
        my_queue.append((root, level))
        
        while (len(my_queue) > 0):
            curr_node, level = my_queue.pop(0)
            
            if (len(return_list) == level):  # check if we are at a new tree level
                return_list.append([])
            
            return_list[level].append(curr_node.val)
            
            if (curr_node.left is not None):
                my_queue.append((curr_node.left, level + 1))
                
            if (curr_node.right is not None):
                my_queue.append((curr_node.right, level + 1))
        
        return return_list
