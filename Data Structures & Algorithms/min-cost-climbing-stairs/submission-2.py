class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 = 0, cost[0]
        for i in range(1, len(cost)):
            prev1, prev2 = prev2, min(prev1, prev2) + cost[i]
        return min(prev1, prev2)