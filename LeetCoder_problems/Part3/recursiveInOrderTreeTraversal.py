# 6/29/2019
# leetcode recursive in-order traversal of tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        my_list = []
        inorder_recursive(root, my_list)
        
        return my_list
        

def inorder_recursive(node, listt):
    # base case
    if (node is None):
        return
    
    # recursive cases
    inorder_recursive(node.left, listt)
    
    listt.append(node.val)
    
    inorder_recursive(node.right, listt)
