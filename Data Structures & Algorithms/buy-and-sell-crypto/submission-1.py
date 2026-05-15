class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        profit = 0

        for n in prices:
            profit = max(profit, n - min_value)
            min_value = min(min_value, n)
        return profit