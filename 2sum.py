def twoSum(num, target):
        head=0
        tail=len(num)-1
        while head<tail:
            he=num[head]+num[tail]
            print he
            if he>target:
                tail-=1
            elif he==target:
                break
            else:
                head+=1

def towSum2(num,target):
    d={}
    for i in range(len(num)):
        d[num[i]]=i+1
    for i in num:
        if target-i!=i and d[target-i]:
            print "index1=%d,index2=%d"%(d[i],d[target-i])
            return

towSum2([3,2,4],6)
