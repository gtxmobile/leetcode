def countAndSay(n):
    ret=[]
    for i in range(n):
        if i==0:
            ret.append([1])
        else:
            j=0
            prv=ret[-1]
            plen=len(prv)
            tmp=[]
            cnt=1
            while j<plen-1:
                if prv[j]==prv[j+1]:
                    cnt+=1
                else:
                    tmp.append(cnt)
                    tmp.append(prv[j])
                    cnt=1
                j+=1
            tmp.append(cnt)
            if cnt==1:
                tmp.append(prv[j])
            else:
                tmp.append(prv[j-1])
            ret.append(tmp)
    #print ret
    return ''.join(map(str,ret[n-1]))

print countAndSay(30)

