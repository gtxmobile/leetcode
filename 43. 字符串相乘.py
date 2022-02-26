class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        l1, l2 = len(num1), len(num2)
        ans = [0] * (l1 + l2)
        for i, n1 in enumerate(num1[::-1]):
            c = 0
            shu = int(n1)
            for j, n2 in enumerate(num2[::-1]):
                ji = shu * int(n2) + ans[i + j] + c
                c = ji // 10
                yu = ji % 10
                ans[i + j] = yu
            ans[i + l2] = c
        tmp = [str(i) for i in ans[::-1]]
        return "".join(tmp).lstrip('0')


print(Solution().multiply('123', '456'))
