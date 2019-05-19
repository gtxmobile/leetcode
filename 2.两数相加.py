# coding:utf-8

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        matrix = []
        for i in range(numRows):
            matrix.append([])
        cur_row = 0
        down = -1
        for a in s:
            matrix[cur_row].append(a)
            if cur_row == 0 or cur_row == numRows-1:
                down = -down
            cur_row +=down
        ret = ""
        for ss in matrix:
            ret +="".join(ss)
        return ret