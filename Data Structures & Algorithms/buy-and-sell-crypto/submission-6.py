class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_total = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_total = max(max_total, price - min_price)
        return max_total
