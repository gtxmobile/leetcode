class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        ans = 0
        for i, c in enumerate(s):
            if c in seen and seen[c] >= start:
                start = seen[c]+1
            else:
                ans = max(ans, i - start+1)
            seen[c] = i
        return ans
