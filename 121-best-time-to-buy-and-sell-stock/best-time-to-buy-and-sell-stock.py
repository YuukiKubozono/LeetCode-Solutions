class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        cost=float('inf')
        for x in prices:
            if x<cost:
                cost=x
            elif x-cost>profit:
                profit=x-cost
        return profit