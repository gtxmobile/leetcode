def removeDuplicates(A):
        ret=[]
        for i in range(len(A)-2):
            if not A[i]==A[i+1]==A[i+2]:
                ret.append(A[i])
        ret.extend(A[-2:])
        return ret
def removeDup(A):
        head=0
        for i in range(len(A)-2):
            if not A[i]==A[i+1]==A[i+2]:
                A[head]=A[i]
                head+=1
        if len(A)>2:
            A[head]=A[-2]
            A[head+1]=A[-1]
            return head+2
        else:
            return len(A)
        print A

A = [1]
print removeDup(A)

