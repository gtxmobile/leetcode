class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <11:
            return []
        a = s[0:10]
        m = {a:1}
        ret = set()
        for e in range(11, len(s)+1):
            new_s = s[e-10:e]
            if new_s in m:
                ret.add(new_s)
            else:
                m[new_s] = 1
        return list(ret)
