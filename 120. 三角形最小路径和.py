from typing import List


class Solution120:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if (l := len(triangle)) == 0:
            return 0
        for i in range(1, l):
            up = triangle[i - 1]
            cur = triangle[i]
            cur[0] += up[0]
            for j in range(1, i):
                cur[j] += min(up[j - 1], up[j])
            cur[i] += up[i - 1]
        return min(triangle[-1])

#print(Solution120().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))