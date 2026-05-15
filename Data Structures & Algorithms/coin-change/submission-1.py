class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remainder):
            if remainder == 0:
                return 0
            if remainder in memo: return memo[remainder]
            res = float('inf')
            for coin in coins:
                if remainder - coin >= 0:
                    res = min(res, 1 + dfs(remainder-coin))
            memo[remainder] = res
            return res
        min_coins = dfs(amount)
        return min_coins if min_coins != float('inf') else -1
            
                