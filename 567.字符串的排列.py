class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        check = {}
        for s in s1:
            v = check.setdefault(s, 0)
            check[s] = v + 1
        l = 0
        r = 0
        len1 = len(s1)
        print(check)
        for s in s2:
            v = check.setdefault(s, 0)
            check[s] = v - 1
            r += 1
            while l < r and check[s] < 0:
                check[s2[l]] += 1
                l += 1
            if r - l == len1:
                return True
        return False

    def checkInclusion2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        check = [0] * 26
        for s in s1:
            check[ord(s) - 97] += 1
        l = 0
        r = 0
        len1 = len(s1)
        for s in s2:
            check[ord(s) - 97] += 1
            r += 1
            while l < r and check[ord(s) - 97] < 0:
                check[ord(s2[l])] += 1
                l += 1
            if r - l == len1:
                return True
        return False


print(Solution().checkInclusion2("abcdxabcde", "abcdeabcdx"))
