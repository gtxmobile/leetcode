from typing import List

class Solution47:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        self.len = len(nums)
        self.nums = nums
        self.dfs(0)
        return list(self.ans)

    def dfs(self,idx:int):
        if idx == self.len:
            self.ans.add(tuple(self.nums))
        for i in range(idx,self.len):
            self.nums[i],self.nums[idx] = self.nums[idx],self.nums[i]
            self.dfs(idx+1)
            self.nums[idx],self.nums[i] = self.nums[i],self.nums[idx]