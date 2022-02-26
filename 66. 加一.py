class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        dlen = len(digits)
        c = 0
        digits[-1] += 1
        for i in range(1, dlen + 1):
            yu = (c + digits[-i]) % 10
            c = (c + digits[-i]) / 10
            digits[-i] = yu
        if c == 1:
            digits.insert(0, 1)
        return digits
