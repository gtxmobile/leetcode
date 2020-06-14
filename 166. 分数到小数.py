class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n = abs(numerator)
        d = abs(denominator)
        if numerator*denominator < 0:
            head = "-"
            fuhao = -1
        else:
            head = ""
            fuhao = 1
        sha = []
        ret = n//d
        yu = n % d
        if yu == 0:
            return str(fuhao * ret)
        tou = ret
        prefix = {yu:0}
        start = -1
        index = 1
        while yu > 0:
            yu *= 10
            s = yu // d
            yu = yu % d
            sha.append(str(s))
            if yu not in prefix:
                prefix[yu] = index
                index += 1
            else:
                start = prefix[yu]
                break

        if start == -1:
            return head+str(tou)+"."+"".join(sha)
        return head+str(tou)+"."+"".join(sha[:start])+"("+"".join(sha[start:])+")"

print(Solution().fractionToDecimal(1,17))