class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        olist=[]
        cnt=0
        beg=0
        for i in range(len(s)):
            if s[:i] in dict:
                if i==len(s)-1:
                    return s
                else:
                    olist+=self.wordBreak(s[i::],dict)
            else:
                return False
        return olist

