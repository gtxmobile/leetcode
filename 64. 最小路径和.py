class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        MIN=9999999999
        table=[[grid[0][0]]*n]
        for i in range(1,m):
            table.append([table[i-1][0]+grid[i][0]]*n)
        for j in range(1,n):
            table[0][j]=table[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                table[i][j]=min(table[i-1][j],table[i][j-1])+grid[i][j]
        return table[m-1][n-1]