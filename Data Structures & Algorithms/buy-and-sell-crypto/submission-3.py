class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for n in prices:
            min_price = min(min_price, n)
            max_profit = max(max_profit, n - min_price)
        return max_profit