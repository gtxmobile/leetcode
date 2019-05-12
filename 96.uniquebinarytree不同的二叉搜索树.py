#coding: utf-8
class Solution(object):
    def numTrees(self,n):
        if n==1 or n==0:
            return 1
        if n==2:
            return 2
        totalsum=0
        if n&1==1:
            totalsum+=(self.numTrees(n/2))**2
            print totalsum
        for i in range(n/2):
            totalsum+=(2*self.numTrees(n-i-1)*self.numTrees(i))
        return totalsum
    print numTrees(5)



