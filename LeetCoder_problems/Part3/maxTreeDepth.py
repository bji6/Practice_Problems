# 6/29/2019
# leetcode find max depth of binary tree, using iterative DFS with a stack

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS tree traversal, iteratively using a stack
        my_stack = []
        
        max_depth = 0
        
        if (root is None):
            return 0
        
        my_stack.append((root, 1))
        
        while (len(my_stack) > 0):
            curr_node, curr_depth = my_stack.pop()
            
            if (curr_depth > max_depth):
                max_depth = curr_depth
            
            if (curr_node.left is not None):
                my_stack.append((curr_node.left, curr_depth + 1))
            
            if (curr_node.right is not None):
                my_stack.append((curr_node.right, curr_depth + 1))
        
        return max_depth
