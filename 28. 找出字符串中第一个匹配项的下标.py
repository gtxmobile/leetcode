class Solution28:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        n = len(haystack)
        m = len(needle)
        ss = " " + haystack
        pp = " " + needle
        jump = [0] * len(pp)
        j = 0
        for i in range(2, m + 1):
            while j > 0 and pp[i] != pp[j + 1]:
                j = jump[j]
            if pp[i] == pp[j + 1]:
                j += 1
            jump[i] = j
        j = 0
        for i in range(1, n + 1):
            while j > 0 and ss[i] != pp[j + 1]:
                j = jump[j]
            if ss[i] == pp[j + 1]:
                j += 1
            if j == m:
                return i - m
        return -1


print(Solution28().strStr("aabaaabaaac", "aabaaac"))
