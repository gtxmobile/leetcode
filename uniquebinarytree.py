#coding: utf-8

def numTrees(n):
    if n==1 or n==0:
        return 1
    if n==2:
        return 2
    totalsum=0
    if n&1==1:
        totalsum+=(numTrees(n/2))**2
        print totalsum
    for i in range(n/2):
        totalsum+=(2*numTrees(n-i-1)*numTrees(i))
    return totalsum
print numTrees(5)

def generateTrees(n):
     if n==1:


