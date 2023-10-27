from typing import List
class Solution131:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        ret = []
        n = len(s)

        @cache
        def is_pal(i,j):
            if i>=j:
                return 1
            return is_pal(i+1,j-1) if s[i]==s[j] else 0
        def dfs(i:int):
            if i == n:
                return ret.append(ans[:])

            for j in range(i,n):
                if is_pal(i,j):
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()
        dfs(0)
        return ans
