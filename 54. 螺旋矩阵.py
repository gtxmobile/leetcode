class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m < 1:
            return matrix
        n = len(matrix[0])
        cnt = 0
        ret = []
        while cnt * 2 < m and cnt * 2 < n:
            ret += matrix[cnt][cnt:n - cnt]
            ret += [matrix[i][n - cnt - 1] for i in range(cnt + 1, m - cnt - 1)]
            if cnt * 2 + 1 < m:
                ret += matrix[m - cnt - 1][cnt:n - cnt][::-1]
            if cnt * 2 + 1 < n:
                ret += [matrix[i][cnt] for i in range(cnt + 1, m - cnt - 1)[::-1]]
            cnt += 1
        return ret
