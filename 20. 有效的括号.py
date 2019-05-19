class Solution:
    # @return a boolean
    def isValid(self, s):
        stack=[]
        dic={')':'(',']':'[','}':'{'}
        for i in s:
            if i in '([{':
                stack.append(i)
            elif stack and dic[i]==stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False