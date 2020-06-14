class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1 or n == 0:
            return 1
        p1 = 1
        p2 = 1
        for i in range(n - 1):
            tmp = p2
            p2 = p1 + p2
            p1 = tmp
        return p2
