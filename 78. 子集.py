from typing import List


class Solution78:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.cur = []
        self.l = len(nums)
        self.nums = nums
        self.dfs(0)
        return self.ans

    def dfs(self, n):
        if n >self.l:
            return
        self.ans.append(self.cur[:])

        for i in range(n,self.l):
            self.cur.append(self.nums[i])
            self.dfs(i+1)
            self.cur.pop()

print(Solution78().subsets([1,2,3]))

