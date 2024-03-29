class Solution69:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        r = x
        while r> x//r:
            r = (r+x//r)//2
        return r