class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ret = []
        self.getpair(n, n, [])
        return self.ret

    def getpair(self, l, r, item):
        if l > r:
            return
        if l == r == 0:
            self.ret.append(''.join(item))
        if l > 0:
            self.getpair(l - 1, r, item + ['('])
        if r > 0:
            self.getpair(l, r - 1, item + [')'])


print
Solution().generateParenthesis(10)
