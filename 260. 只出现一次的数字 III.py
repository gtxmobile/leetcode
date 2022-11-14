from typing import List


class Solution260:
    def singleNumber(self, nums: List[int]) -> List[int]:
        tmp = 0
        for n in nums:
            tmp ^= n
        i = len(bin(tmp)) - 3  # 最高位非0位是第几位

        a, b = 0, 0
        for n in nums:
            if n >> i & 1:
                a ^= n
            else:
                b ^= n
        return [a, b]
