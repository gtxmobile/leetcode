def removeDuplicates(A):
        head=0
        i=0
        origlen=len(A)
        while i<origlen-1:
            if A[i]!=A[i+1]:
                A[head]=A[i]
                head+=1
            i+=1
        if A[i]!=A[head]:
            A[head]=A[i]
        head+=1
        return len(A[:head])
from random import randint
A=sorted([randint(1,5) for i in range(10)])
print A
print removeDuplicates(A)
