class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        res = []
        wl = len(words[0])
        ll = len(words)
        tl = wl * ll
        sl = len(s)
        if sl < tl:
            return res
        d1 = {}.fromkeys(words, 0)
        for i in words:
            d1[i] += 1
        for i in range(sl - tl + 1):
            d2 = dict(d1)
            for j in range(i, i + tl, wl):
                if d2.get(s[j:j + wl]):
                    d2[s[j:j + wl]] -= 1
                else:
                    break
            if not any(d2.values()):
                res.append(i)
        return res
