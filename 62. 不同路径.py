class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        table = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i - 1][j] + table[i][j - 1]
        return table[m - 1][n - 1]
