
def twoSum2(num, target):
    head=0
    tail=len(num)-1
    while head<tail:
        he=num[head]+num[tail]
        if he>target:
            tail-=1
        elif he==target:
            return [head,tail]
        else:
            head+=1


print twoSum2([2, 7, 11, 15],9)