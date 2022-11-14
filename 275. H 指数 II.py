from typing import List


class Solution274:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        l = 0
        ll  = len(citations)
        r = ll -1
        while l <= r:
            mid = (l + r) // 2
            if ll - mid <= citations[mid]:
                ans = ll - mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


print(Solution274().hIndex([0, 1, 3, 5, 6]))
print(Solution274().hIndex([1, 2, 100]))
print(Solution274().hIndex([11,15]))

