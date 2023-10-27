from typing import List
class Solution188:
    def maxProfit(self,k:int, prices: List[int]) -> int:
        buy = [float('-inf')]*(k+1)
        sell = [0]*(k+1)
        for price in prices:
            for i in range(1,k+1):
                buy[i] = max(buy[i],sell[i-1]-price)
                sell[i] = max(sell[i],price+buy[i])
        return sell[-1]

print(Solution188().maxProfit([3,3,5,0,0,3,1,4]))