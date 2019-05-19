class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.s=candidates
        self.slen=len(candidates)
        self.ret=[]
        self.guicom(0,target,[])
        return self.ret
        #return map(list,{}.fromkeys([tuple(i) for i in self.ret]).keys())

    def guicom(self,start,target,result):
        import copy
        if target==0:
            self.ret.append(copy.copy(result))
        if target<0:
            return
        i=start
        while i<self.slen:
            if self.s[i]>target:
                return
            if i>start and self.s[i]==self.s[i-1]: i+=1;continue
            result.append(self.s[i])
            self.guicom(i+1,target-self.s[i],result)
            result.pop()
            i+=1