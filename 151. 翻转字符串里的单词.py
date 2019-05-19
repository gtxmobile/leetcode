class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        #words=s.strip().split(' ')
        #words=[w for w in words if w]
        return ' '.join([w for w in s.strip().split() if w][::-1])