from typing import List
class Solution37:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col = [[0]*9 for _ in range(9)]
        row = [[0]*9 for _ in range(9)]
        fang = [[[0]*9 for _a in range(3)] for _b in range(3)]
        solves = []
        for i in range(9):
            for j in range(9):
                if board[i][j]!= '.':
                    num = int(board[i][j])-1
                    row[i][num] = 1
                    col[j][num] = 1
                    fang[i//3][j//3][num] = 1
                else:
                    solves.append((i,j))

        def dfs(l):
            if l == len(solves):
                return True
            i,j = solves[l]
            for num in range(9):
                if row[i][num]>0 or col[j][num]>0 or fang[i//3][j//3][num] >0 :
                    continue
                row[i][num] = 1
                col[j][num] = 1
                fang[i//3][j//3][num] = 1
                board[i][j] = str(num)+1
                if dfs(l+1):
                    return True
                else:
                    row[i][num] = 0
                    col[j][num] = 0
                    fang[i // 3][j // 3][num] = 0
            return False
        dfs(0)



