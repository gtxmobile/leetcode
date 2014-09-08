
def generateParenthesis(n):
    getpair(n,n,[])
    return ret
ret=[]
def getpair(l,r,item):
    if l>r:
        return
    if l==r==0:
        ret.append(''.join(item))
    if l>0:
        getpair(l-1,r,item+['('])
    if r>0:
        getpair(l,r-1,item+[')'])

print generateParenthesis(10)
