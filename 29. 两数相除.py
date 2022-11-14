class Solution29:
    def divide(self, dividend: int, divisor: int) -> int:
        ret = 0
        sign = -1
        if (dividend<0 and divisor<0) or (dividend>0 and divisor>0):
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        for i in range(32,-1,-1):
            #print(i)
            if dividend >= (divisor<<i):
                dividend -= divisor<<i
                ret += 1<< i
        if sign<0:
            return -ret
        if ret > 1<<32 -1:
            return 1<<32-1
        return ret
