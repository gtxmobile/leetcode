class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        als=[]
        sdic={}
        for i,s in enumerate(strs):
            ks=''.join(sorted(s))
            if not sdic.get(ks):
                sdic[ks]=[i]
            else:
                sdic[ks].append(i)
        for v in sdic.itervalues():
            if len(v)>1:
                for i in v:
                    als.append(strs[i])
        return als
        