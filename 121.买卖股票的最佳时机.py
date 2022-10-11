# coding:utf-8
from random import randint


def maxProfi(prices):
    min_p, max_p = 99999999, 0
    for i, p in enumerate(prices):
        min_p = min(min_p, p)
        max_p = max(max_p, p - min_p)
    return max_p


prices = [randint(1, 10) for i in range(10)]
print(maxProfi(prices))
