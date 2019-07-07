# 6/29/2019
# leetcode preorder binary tree traversal using DFS iteratively


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if (root is None):
            return []
        
        my_stack = []
        
        preorder = []
        
        my_stack.append(root)
        
        while (len(my_stack) > 0):
            curr_node = my_stack.pop()
            preorder.append(curr_node.val)
            
            if (curr_node.right is not None):
                my_stack.append(curr_node.right)
            
            # add left node last we because we want to traverse left side first
            if (curr_node.left is not None):
                my_stack.append(curr_node.left)
            
                
        return preorder
