class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join([w for w in s.strip().split() if w][::-1])
