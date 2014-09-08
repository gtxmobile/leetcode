#coding: utf-8

import random

MID=32111
MAX=64222
def candy(ratings):
    cds=[1]*len(ratings)
    prv=-1
    for i,r in enumerate(ratings):
        if i==0:
            pass
        else:
            if r>prv:
                cds[i]+=1
        prv=r
    rlen=len(ratings)-2
    prv=ratings[-1]
    for i in range(len(ratings)-1):
        print cds[rlen-i],cds[rlen-i+1]
        if ratings[rlen-i]>prv and cds[rlen-i]<=cds[rlen-i+1]:
                cds[rlen-i]=cds[rlen-i+1]+1
        prv=ratings[rlen-i]
        print cds
    print sum(cds)
ratings=[random.randint(0,10000) for i in range(100000)]
ratings=[1,0,2]
candy(ratings)

