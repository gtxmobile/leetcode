class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, ob):
        m = len(ob)
        n = len(ob[0])
        table = [[1 ^ ob[0][0]] * n]
        for i in range(1, n):
            table[0][i] = (table[0][i - 1]) & (1 ^ ob[0][i])
        for i in range(1, m):
            table.append([(table[i - 1][0]) & (1 ^ ob[i][0])] * n)
        for i in range(1, m):
            for j in range(1, n):
                if ob[i][j] == 1:
                    table[i][j] = 0
                else:
                    table[i][j] = table[i - 1][j] + table[i][j - 1]
        return table[m - 1][n - 1]
