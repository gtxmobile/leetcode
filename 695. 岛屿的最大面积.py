class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        ans = 0
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                ans = max(ans, self.bfs(i, j))
        return ans

    def bfs(self, x, y):
        if x < 0 or x >= self.row or y < 0 or y >= self.col or not self.grid[x][y]:
            return 0
        self.grid[x][y] = 0
        return 1 + self.bfs(x + 1, y) + self.bfs(x, y + 1) + self.bfs(x - 1, y) + self.bfs(x, y - 1)
