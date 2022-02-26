class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.ret = 0
        self.row = len(grid)
        self.col = len(grid[0])
        self.grid = grid
        if self.col == 0:
            return ret
        self.visit = [[0] * self.col for i in range(self.row)]
        for x in range(self.row):
            for y in range(self.col):
                if not self.visit[x][y] and grid[x][y] == "1":
                    self.bfs(x, y)
                    self.ret += 1
        print(self.ret)
        return self.ret

    def bfs(self, x, y):
        if x < 0 or y < 0 or x > self.row - 1 or y > self.col - 1:
            return
        if self.visit[x][y]:
            return
        self.visit[x][y] = 1
        if self.grid[x][y] == "0":
            return
        self.bfs(x - 1, y)
        self.bfs(x + 1, y)
        self.bfs(x, y + 1)
        self.bfs(x, y - 1)


Solution().numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
