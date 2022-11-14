from typing import List


class Solution274:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        ans = 0
        for i, n in enumerate(citations):
            if i + 1 <= n:
                ans +=1
        return ans


print(Solution274().hIndex([3, 0, 6, 1, 5]))
print(Solution274().hIndex([1, 3, 1]))
