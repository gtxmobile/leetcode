def maxSubArray(A):
    MAX=-111111
    totalsum=0
    start=0
    end=0
    for i,a in enumerate(A):
            totalsum+=a
            if totalsum>MAX:
                MAX=totalsum
                end=i
            if totalsum<0:
                totalsum=0
                start=i+1
    print MAX
    return A[start:end+1]

print maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
