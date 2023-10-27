from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            self.bfs(i, 0, True)
            self.bfs(i, self.n - 1, True)
        for j in range(self.n):
            self.bfs(0, j, True)
            self.bfs(self.m - 1, j, True)

        for i in range(1, self.m - 1):
            for j in range(1, self.n - 1):
                self.bfs(i, j, False)

        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] =="#":
                    self.board[i][j] = 'O'


    def bfs(self, r, c, edge):
        if r >= self.m or r < 0 or c >= self.n or c < 0:
            return
        if self.board[r][c] != "O":
            return
        if edge:
            self.board[r][c] = '#'
        else:
            self.board[r][c] = 'X'
        self.bfs(r + 1, c, edge)
        self.bfs(r - 1, c, edge)
        self.bfs(r, c + 1, edge)
        self.bfs(r, c - 1, edge)
