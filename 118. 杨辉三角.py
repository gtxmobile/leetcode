class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        prv=[]
        ret=[]
        for i in range(numRows):
            tmp=[]
            if i>0:
                tmp.append(1)
            for j in range(len(prv)-1):
                tmp.append(prv[j]+prv[j+1])
            tmp.append(1)
            prv=tmp
            ret.append(prv)
        return ret