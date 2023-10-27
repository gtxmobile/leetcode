class Solution125:
    def isPalindrome(self, s: str) -> bool:
        tmp = [c.lower() for c in s.strip() if c.isdigit() or c.isalpha()]
        return tmp == tmp[::-1]
