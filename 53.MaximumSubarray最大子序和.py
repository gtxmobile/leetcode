def maxSubArray(nums):
    ret = nums[0]
    sum = 0
    for i,k in enumerate(nums):
        if sum > 0:
            sum += k
        else:
            sum = k
        ret = max(ret,sum)
    return ret

print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
