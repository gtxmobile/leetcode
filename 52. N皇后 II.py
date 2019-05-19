class Solution:
    # @return an integer

    def totalNQueens(self, n):
        self.cnt=0
        self.n=n
        self.pan=[-1]*n
        self.col=[0]*n
        self.search(0)
        return self.cnt

    def search(self,k):
        if k==self.n:
            #print pan
            #for i in pan:
            #    print '* '*i+'Q '+'* '*(n-i)
            #print
            self.cnt+=1
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