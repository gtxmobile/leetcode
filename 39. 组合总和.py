class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.s = candidates
        self.slen = len(candidates)
        self.ret = []
        self.guicom(0, target, [])
        return self.ret

    def guicom(self, start, target, result):
        import copy
        if target == 0:
            self.ret.append(copy.copy(result))
        while start < self.slen:
            if self.s[start] > target:
                return
            result.append(self.s[start])
            self.guicom(start, target - self.s[start], result)
            result.pop()
            start += 1
