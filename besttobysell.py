#coding:utf-8
from random import randint
def maxProfi(prices):
    rp=prices[::-1]
    end=rp[0]
    totalsum=0
    for i in range(1,len(rp)):
        if end>rp[i]:
            totalsum+=end-rp[i]
        end=rp[i]
    return totalsum

prices=[randint(1,10) for i in range(10)]
maxProfi(prices)
