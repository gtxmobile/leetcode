class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        max_pos = 0
        for i,n in enumerate(nums):
            if max_pos>=i:
                max_pos = max(max_pos,i+n)
                if max_pos >=l-1:
                    return True
        return False
