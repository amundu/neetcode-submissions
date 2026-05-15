class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]

        for price in prices:
            lowest_price = min(lowest_price, price)
            max_profit = max(max_profit, price - lowest_price)
        return max_profit