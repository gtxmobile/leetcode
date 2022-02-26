class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        ss = s.strip()
        if not ss:
            return 0
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1
        sign = 1
        if ss[0] == "-":
            sign = -1
            ss = ss[1::]
        elif ss[0] == "+":
            sign = 1
            ss = ss[1::]
        num = ["0"]
        for a in ss:
            if a.isdigit():
                num.append(a)
            else:
                break
        ret = sign * int("".join(num))
        if ret < MIN:
            return MIN
        if ret > MAX:
            return MAX
        return ret
