class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        ret = []
        dic = {}.fromkeys(S, 0)
        for i in S:
            dic[i] += 1
        path = []
        dic = dic.items()
        dic.sort()
        self.subset(path, 0, ret, dic)
        return ret

    def subset(self, path, step, result, dic):
        if step == len(dic):
            result.append(path)
            return
        for i in range(dic[step][1] + 1):
            self.subset(path + [dic[step][0]] * i, step + 1, result, dic)
