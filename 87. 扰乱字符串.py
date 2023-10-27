from executing import cache


class Solution87:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        if (n:=len(s1)) == 1:
            return True
        for i in range(1,n):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]):
                return True
            if self.isScramble(s1[:i],s2[n-i:]) and self.isScramble(s1[i:],s2[:n-i]):
                return True
        return False

print(Solution87().isScramble("great", "rgeat"))