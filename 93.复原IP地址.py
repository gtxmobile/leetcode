class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.l = len(s)
        self.segments = []
        self.ans = []
        self.s = s
        if self.l > 12:
            return self.ans
        self.dfs(-1, 3)
        return self.ans

    def check(self, s):
        return len(s) == 1 if s[0] == '0' else int(s) < 256

    def push_output(self, cur):
        tmps = self.s[cur:]
        if self.check(tmps):
            self.segments.append(tmps)
            self.ans.append(".".join(self.segments))
            self.segments.pop()

    def dfs(self, pre, cnt):
        if cnt == 0:
            self.push_output(pre + 1)
        for i in range(pre + 1, min(pre + 4, self.l - 1)):
            tmp_s = self.s[pre + 1:i + 1]
            if self.check(tmp_s):
                self.segments.append(tmp_s)
                self.dfs(i, cnt - 1)
                self.segments.pop()


print(Solution().restoreIpAddresses("010010"))
