from typing import List


class Solution16:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        diff = 1 << 32
        ans = 0
        nums.sort()
        for i in range(n - 2):
            t2 = target - nums[i]
            k = n - 1
            for j in range(i + 1, n-1):
                while j < k:
                    t3 = nums[j] + nums[k] - t2
                    if t3 == 0:
                        return target
                    if abs(t3) < diff:
                        diff = abs(t3)
                        ans = target + t3
                    if nums[j] + nums[k] > t2:
                        k -= 1
                    else:
                        break
        return ans

print(Solution16().threeSumClosest([-1,2,1,-4],1))