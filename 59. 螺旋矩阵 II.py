class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        cnt=1
        ret=[[n*n]*n for i in range(n)]
        for i in range(n/2):
            for j in range(i,n-i-1):
                ret[i][j]=cnt
                ret[j][n-i-1]=cnt+n-i*2-1
                ret[n-i-1][n-j-1]=cnt+2*(n-i*2-1)
                ret[n-j-1][i]=cnt+3*(n-i*2-1)
                cnt+=1
            cnt+=3*(n-i*2-1)
        return ret