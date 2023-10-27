from typing import List
class Solution123:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('inf')
        buy2 = float('-inf')
        sell1 = 0
        sell2 = 0
        for price in prices:
            buy1 = min(price, buy1)
            sell1 = max(sell1, price-buy1)
            buy2 = max(buy2,sell1-price)
            sell2 = max(sell2,price+buy2)
        return sell2

print(Solution123().maxProfit([3,3,5,0,0,3,1,4]))