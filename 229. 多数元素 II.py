from typing import List


def majorityElement(nums: List[int]) -> List[int]:
    a1 = -10 ** 10
    a2 = -10 ** 10
    cnt1 = 0
    cnt2 = 0
    for n in nums:
        if n != a1 and n != a2:
            if cnt1 == 0:
                a1 = n
                cnt1 += 1
            elif cnt2 == 0:
                a2 = n
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        elif n == a1:
            cnt1 += 1
            a1 = n
        else:
            cnt2 += 1
            a2 = n
    n1, n2 = 0, 0
    for n in nums:
        if cnt1 > 0 and n == a1:
            n1 += 1
        if cnt2 > 0 and n == a2:
            n2 += 1
    ans = []
    if n1 > len(nums) / 3:
        ans.append(a1)
    if n2 > len(nums) / 3:
        ans.append(a2)
    return ans


print(majorityElement([3, 2, 3]))
print(majorityElement([1, 2]))
print(majorityElement([1]))

