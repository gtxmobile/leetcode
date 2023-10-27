class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sl, tl = len(s), len(t)
        if sl < tl:
            return 0
        dp = [[0] * (tl + 1) for _ in range(sl + 1)]
        dp[0][0] = 1
        for i in range(1, sl+1):
            dp[i][0] = 1
        for i in range(1,sl+1):
            for j in range(1,tl+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                dp[i][j] += dp[i-1][j]
        return dp[sl][tl]