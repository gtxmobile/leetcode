class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ret = 0
        for a in A:
            ret = ret ^ a
        return ret
