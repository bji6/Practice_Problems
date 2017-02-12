# Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        past_nodes = []
        level = 0
        temp = root
        
        #find node p in BST, keep track of nodes we passed
        while (temp.val != p.val):
            past_nodes.append(temp.val)
            level += 1
            
            if (temp.val > p.val):
                temp = temp.left
            elif (temp.val < p.val):
                temp = temp.right
        
        # add p as an ancestor
        past_nodes.append(temp.val)
        #print(past_nodes)
        temp = root
        #print(temp.val)
        level = 0
        lca = temp.val
        while (temp.val != q.val and level < len(past_nodes)):
            #print(temp.val)
            if (temp.val == past_nodes[level]):
                lca = temp.val
            level += 1
            
            if (temp.val > q.val):
                temp = temp.left
            elif (temp.val < q.val):
                temp = temp.right
        
        if (level < len(past_nodes) and temp.val == past_nodes[level]):
                lca = temp.val
        
        return lca
