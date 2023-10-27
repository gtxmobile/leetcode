class Solution50:
    def myPow(self, x: float, n: int) -> float:
        if n>0:
            return self.help(x,n)
        if n<0:
            return 1.0/self.help(x,-n)
        return 1.0

    def help(self,x, n):
        if n==0:
            return 1.0
        ret = self.help(x, n//2)
        ret *= ret
        if(n%2 ==1):
            ret *=x
        return ret


