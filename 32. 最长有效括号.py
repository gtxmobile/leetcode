class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] is '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(i - stack[-1], res)
                else:
                    stack.append(i)
        return res
