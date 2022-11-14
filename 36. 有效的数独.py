from typing import List


class Solution36:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(10)]
        col = [{} for i in range(10)]
        fang = [[{} for j in range(3)] for i in range(3)]
        print(fang)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if row[i].get(num, 0) > 0 or col[j].get(num, 0) > 0 or fang[i // 3][j // 3].get(num, 0) > 0:
                        print(num, row, col)
                        return False
                    row[i][num] = 1
                    col[j][num] = 1
                    fang[i // 3][j // 3][num] = 1
        return True


print(Solution36().isValidSudoku(
    [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
