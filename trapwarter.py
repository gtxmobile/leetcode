def trap(A):
    rs=A[:]
    lmax=0
    rmax=0
    ret=0
    rs[-1]=rmax
    for i in range(len(A)-1)[::-1]:
        rs[i]=max(A[i+1],rmax)
        rmax=rs[i]
    for i in range(1,len(A)):
        lmax=max(A[i-1],lmax)
        if min(lmax,rs[i])-A[i]>0:
            ret+=(min(lmax,rs[i])-A[i])*1
    return ret

print trap([0,1,0,2,1,0,1,3,2,1,2,1])

import sys
a=sys.stdin.readline().split()[1:]
b=sys.stdin.readline().split()[1:]
a=zip(a[::2],a[1::2])
b=zip(b[::2],b[1::2])
dic={}
for k,v in a:
  dic[k]=float(v)
for k,v in b:
  if dic.get(k):
    dic[k]+=float(v)
  else:
    dic[k]=float(v)
print len(dic),
for k,v in sorted(dic.items())[::-1]:
  print k,v,
