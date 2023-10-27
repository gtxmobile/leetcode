from typing import List

class Solution46:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.len = len(nums)
        self.nums = nums
        self.dfs(0)
        return self.ans

    def dfs(self,idx:int):
        if idx == self.len:
            self.ans.append(self.nums[:])
        for i in range(idx,self.len):
            self.nums[i],self.nums[idx] = self.nums[idx],self.nums[i]
            self.dfs(idx+1)
            self.nums[idx],self.nums[i] = self.nums[i],self.nums[idx]

