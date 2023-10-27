class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r = len(word1)
        c = len(word2)
        dp = [[0 for i in range(c+1)] for j in range(r+1)]
        for i in range(r+1):
            for j in range(c+1):
                if i==0:
                    dp[i][j] = j
                    continue
                if j==0:
                    dp[i][j] = i
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[r][c]