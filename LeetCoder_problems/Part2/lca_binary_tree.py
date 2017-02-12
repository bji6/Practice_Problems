from collections import deque

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
        temp = root
        p_count = self.BFSCount(p.val,0,temp)
        print(p_count)
        temp = root
        q_count = self.BFSCount(q.val,0,temp)
        print(q_count)
        temp = root
        
        p_lists = []
        for i in range(p_count):
            tupp = self.recursiveDFS([temp.val], p.val, temp, False, p_lists)
            list1 = tupp[0]
            p_lists.append(list1[:])

        q_lists = []

        for i in range(q_count):
            tupp2 = self.recursiveDFS([temp.val], q.val, temp, False, q_lists)
            list2 = tupp2[0]
            q_lists.append(list2[:])

        lca = root.val
        matches = []
        
        #remove duplicate solutions
        if(p.val == q.val):
            q_lists = []

            movethis = p_lists.pop()
            q_lists.append(movethis)

        for pl in p_lists:
            for ql in q_lists:
                if (len(pl) > len(ql)):
                    for i in range(len(ql)):
                        if (ql[i] in pl):
                            lca = ql[i]
                            matches.append((i,lca))
                else:
                    for i in range(len(pl)):
                        if (pl[i] in ql):
                            lca = pl[i]
                            matches.append((i,lca))

        sorted_matches = sorted(matches)
        lca = sorted_matches[-1][1]
        #print(sorted_matches)

        if (p.val == q.val and lca == p.val and len(sorted_matches) > 1):
            lca = sorted_matches[-2][1]

        return lca
        
    def recursiveDFS(self, mystack, tofind, curNode, end, lists):
        # base case
        # correct path
        if (curNode.val == tofind):
            #check if we already have this solution
            alreadyhave = False
            for l in lists:
                print("existing solution")
                print(l)
                print("just found solution")
                print(mystack)
                if (len(mystack) == len(l)):
                    alreadyhave = True
                    for i in range(len(l)):
                        if (l[i] != mystack[i]):
                            alreadyhave = False
                            break
                    # we already have this solution
                    if (alreadyhave == True):
                        break
            if (alreadyhave == False):
                end = True
                print("!!! found solution !!!")
                print(mystack)
                return (mystack, end)
        
        temp = curNode.left
        #print(mystack)

        if (temp is not None):
            tempstack = mystack[:]
            tempstack.append(temp.val)
            tupp = self.recursiveDFS(tempstack, tofind, temp, end, lists)
            # end recursion
            if (tupp[1] == True):
                #print(tupp)
                return tupp
        
        temp = curNode.right
        if (temp is not None):
            tempstack = mystack[:]
            tempstack.append(temp.val)
            tupp = self.recursiveDFS(tempstack, tofind, temp, end, lists)
            
            if (tupp[1] == True):
                #print(tupp)
                return tupp

        return (mystack, False)

    # function counts instances of node value in the tree
    def BFSCount(self, toFind, count, root):
        myqueue = deque()
        myqueue.append(root)

        while(len(myqueue) > 0):
            n = myqueue.popleft()
            if (n.val == toFind):
                count += 1
            if (n.left is not None):
                myqueue.append(n.left)
            if (n.right is not None):
                myqueue.append(n.right)

        return count

def main():
    """
    root = TreeNode(5)
    root.left = TreeNode(3)
    temp = root.left
    temp.left = TreeNode(2)
    temp.right = TreeNode(4)
    temp = temp.left
    temp.left = TreeNode(1)
    temp2 = temp.left
    root.right = TreeNode(6)
    temp = root.left
    """
    test = Solution()
    """
    print(test.lowestCommonAncestor(root,temp2,temp))

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    temp = root.left
    temp.left = TreeNode(6)
    temp.right = TreeNode(2)
    temp = temp.right
    temp.left = TreeNode(7)
    temp.right = TreeNode(4)
    temp2 = temp.right
    temp = root.right
    temp.left = TreeNode(0)
    temp.right = TreeNode(8)

    print(test.lowestCommonAncestor(root,root.left,root.right))

    print(test.lowestCommonAncestor(root,root.left,temp2))
    """

    root = TreeNode(37)
    root.left = TreeNode(-34)
    temp = root.left
    temp.right = TreeNode(-30)
    #q2 = temp.right
    root.right = TreeNode(-48)
    temp = root.right
    temp.left = TreeNode(-71)
    p = temp.left
    temp.right = TreeNode(48)
    temp2 = temp.left
    temp2.left = TreeNode(-54)
    temp2 = temp.right
    temp2.left = TreeNode(-71)
    q = temp2.left
    temp2.right = TreeNode(22)
    temp2 = temp2.right
    temp2.right = TreeNode(-71)
    temp2.left = TreeNode(-100)
    q2 = temp2.left

    #print(test.lowestCommonAncestor(root,p,q))

    print(test.lowestCommonAncestor(root,p,q2))

main()
