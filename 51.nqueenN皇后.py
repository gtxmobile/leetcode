


class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.ret=[]
        self.n=n
        self.pan=[-1]*n
        self.col=[0]*n
        self.search(0)
        return self.ret

    def search(self,k):
        if k==self.n:
            self.ret.append([('.'*i+'Q'+'.'*(self.n-i-1)) for i in self.pan])
            return
        for i,c in enumerate(self.col):
            ok=1
            if not c:
                for j in range(k):
                    if abs(k-j)==abs(self.pan[j]-i):
                        ok=0
                        break
                if ok:
                    self.col[i]=1
                    self.pan[k]=i
                    self.search(k+1)
                    self.col[i]=0

