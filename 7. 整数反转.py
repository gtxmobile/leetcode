class Solution7:
    # @return an integer
    def reverse(self, x):
        neg = False
        if x < 0:
            neg = True
            x = -x
        x = int(str(x)[::-1])
        if neg:
            return -x
        else:
            return x
