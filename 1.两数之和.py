def twoSum(nums, target):
    d = {}
    for i, v in enumerate(nums):
        if (target - v) in d:
            return [d[target - v], i]
        d[v] = i
    return []


print(twoSum([2, 2, 4], 6))
