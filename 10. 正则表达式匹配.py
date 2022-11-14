class Solution10:
    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.ls = len(s)
        self.lp = len(p)
        dp = [[False] * (self.lp + 1) for i in range(self.ls + 1)]
        dp[0][0] = True
        for i in range(self.ls + 1):
            for j in range(1, self.lp + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if self.match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                elif self.match(i, j):
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[self.ls][self.lp]

    def match(self, i, j):
        if i == 0:
            return False
        if self.p[j - 1] == '.':
            return True
        return self.s[i - 1] == self.p[j - 1]

print(Solution10().isMatch("aa","a"))