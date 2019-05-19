class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one=two=three=0
        for i in A:
            two |= (one & i)
            one ^= i
            three = one & two
            one &= ~three
            two &=  ~three
        return one
            