class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        bj={}
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    bj[i,j]=1
        for r,c in bj.iterkeys():
            for i in range(n):
                matrix[r][i]=0
            for j in range(m):
                matrix[j][c]=0
        return matrix