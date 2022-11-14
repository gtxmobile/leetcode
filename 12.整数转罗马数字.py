# coding:utf-8
class Solution12:
    def intToRoman(self, num):
        table = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
                 ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]
        returnint = []
        for roma, dec in table:
            while num - dec >= 0:
                returnint.append(roma)
                num -= dec
        return "".join(returnint)
