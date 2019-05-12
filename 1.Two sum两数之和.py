
def twoSum(nums,target):
    d={}
    for i in range(len(nums)):
        if d.get(nums[i],None) != None:
            if nums[i]*2 == target:
                return [d.get(nums[i]),i]
        else:
            continue
        d[nums[i]]=i
    for i in nums:
        if target-i!=i and d[target-i]:
            #print "index1=%d,index2=%d"%(d[i],d[target-i])
            return [d[i],d[target-i]]

twoSum([3,2,4],6)



