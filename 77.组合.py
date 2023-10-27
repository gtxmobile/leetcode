from itertools import combinations
from typing import List
class Solution77:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        cur = []
        def dfs(b,l):
            if l == k:
                ans.append(cur[:])
            for i in range(b,n):
                cur.append(i+1)
                dfs(i+1,l+1)
                cur.pop()
        dfs(0,0)
        return ans

print(Solution77().combine(4,2))
#print([list(i) for i in combinations(range(1, 10), 2)])
