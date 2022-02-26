class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][-1] < target:
                continue
            for j in range(n)[::-1]:
                if matrix[i][j] == target:
                    return True
                if matrix[i][j] < target:
                    return False
        return False
