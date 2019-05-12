class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        ls=len(s)
        if ls==0:
            return False
        bj=[False]*(ls+1)
        bj[0]=True
        for i in range(1,ls+1):
            for j in range(i)[::-1]:
                if bj[j] and s[j:i] in dict:
                    bj[i]=True
                    break
        return bj[ls]

