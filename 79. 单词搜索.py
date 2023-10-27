from typing import List
class Solution79:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        wl = len(word)
        visit = [[0]*c for _ in range(r)]
        def dfs(m,n,idx):
            if idx == wl:
                return True
            if m>=r or m<0 or m>=c or m<0 or board[m][n] != word[idx] or visit[m][n]:
                return False
            visit[m][n] = 1
            if dfs(m+1,n,idx+1):
                return True
            if dfs(m,n+1,idx+1):
                return True
            if dfs(m-1,n,idx+1):
                return True
            if dfs(m,n-1,idx+1):
                return True
            visit[m][n] = 0
            return False

        for i in range(r):
            for j in range(c):
                if dfs(i,j,0):
                    return True
        return False