



n=8
pan=[-1]*n
col=[0]*n
def search(k):
    if k==n:
        #print pan
        #for i in pan:
        #    print '* '*i+'Q '+'* '*(n-i)
        print [('.'*i+'Q'+'.'*(n-i-1)) for i in pan]
        return
    for i,c in enumerate(col):
        ok=1
        if not c:
            for j in range(k):
                if abs(k-j)==abs(pan[j]-i):
                    ok=0
                    break
            if ok:
                col[i]=1
                pan[k]=i
                search(k+1)
                col[i]=0

search(0)
