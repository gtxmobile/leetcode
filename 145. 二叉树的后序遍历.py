# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        queue=[]
        ret=[]
        if not root:
            return ret
        queue.append([root,False])
        while len(queue)>0:
            node,visited=queue.pop()
            if not node:
                continue
            if visited:
                ret.append(node.val)
            else:
                queue.append([node,True])
                queue.append([node.right,False])

                queue.append([node.left,False])
        return ret
