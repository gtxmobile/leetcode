
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        ret = []
        if root == None:
            return ret
        queue = [root]
        while queue:
            lq = len(queue)
            tmp = []
            for i in range(lq):
                n = queue.pop(0)
                tmp.append(n.val)
                if n.left: queue.append(n.left)
                if n.right: queue.append(n.right)
            ret.append(tmp)
        return ret
