def sortColors(A):
    alen=len(A)
    head=0
    cur=0
    tail=alen-1
    while cur<alen and cur<=tail:
        if A[cur]==0:
            A[head],A[cur]=A[cur],A[head]
            head+=1
            cur+=1
        elif A[cur]==2:
            if A[tail]!=2:
                A[cur],A[tail]=A[tail],A[cur]
            tail-=1
        else:
            cur+=1
    return A

from random import randint
A=[randint(0,2) for i in range(50)]
print A

print sortColors(A)
