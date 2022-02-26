class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        prv = []
        for i in range(rowIndex + 1):
            tmp = []
            if i > 0:
                tmp.append(1)
            for j in range(len(prv) - 1):
                tmp.append(prv[j] + prv[j + 1])
            tmp.append(1)
            prv = tmp
        return prv
